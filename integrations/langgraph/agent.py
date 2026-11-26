"""Run a Clarifo research agent on LangGraph.

Uses langchain-mcp-adapters to load Clarifo's tools and LangChain's
create_agent, which builds a LangGraph graph you can extend with your own
nodes, checkpointer or human-in-the-loop interrupts.

    pip install -r requirements.txt
    export ANTHROPIC_API_KEY=... CLARIFO_API_KEY=...
    python agent.py --agent market-monitor "What did Nordic industrials report this week?"
"""
import argparse
import asyncio
import os
from pathlib import Path

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

AGENTS_DIR = Path(__file__).resolve().parents[2] / "plugins" / "clarifo" / "agents"

# Workspace write tools. Left out here as well as by the server-side opt-in.
WRITE_TOOLS = {
    "save_to_workspace", "save_note", "preview_document_update", "apply_document_update",
    "create_automation_draft", "activate_automation", "update_automation",
    "move_to_trash", "restore_from_trash",
}


def load_agent_prompt(name: str) -> str:
    text = (AGENTS_DIR / f"{name}.md").read_text()
    return text.split("---", 2)[2].strip() if text.startswith("---") else text


async def main(agent_name: str, prompt: str) -> None:
    client = MultiServerMCPClient({
        "clarifo": {
            "transport": "streamable_http",
            "url": os.environ.get("CLARIFO_MCP_URL", "https://mcp.clarifo.com/mcp"),
            "headers": {"Authorization": f"Bearer {os.environ['CLARIFO_API_KEY']}"},
            "timeout": 60,
            "sse_read_timeout": 300,
        }
    })
    tools = [t for t in await client.get_tools() if t.name not in WRITE_TOOLS]
    graph = create_agent(
        model=os.environ.get("LANGCHAIN_MODEL", "anthropic:claude-sonnet-5-5"),
        tools=tools,
        system_prompt=load_agent_prompt(agent_name),
    )
    result = await graph.ainvoke({"messages": [{"role": "user", "content": prompt}]},
                                 {"recursion_limit": 60})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent", default="investment-analyst",
                    choices=sorted(p.stem for p in AGENTS_DIR.glob("*.md")))
    ap.add_argument("prompt")
    a = ap.parse_args()
    asyncio.run(main(a.agent, a.prompt))
