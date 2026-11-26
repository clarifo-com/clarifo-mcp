"""Run a Clarifo research agent with the OpenAI Agents SDK.

    pip install -r requirements.txt
    export OPENAI_API_KEY=... CLARIFO_API_KEY=...
    python agent.py --agent competitor-analyst "Compare Nokia and Ericsson on margins"

The agent instructions are the same files the Claude Code plugin uses
(plugins/clarifo/agents/*.md), so there is one copy to maintain.
"""
import argparse
import asyncio
import os
from pathlib import Path

from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp, create_static_tool_filter

AGENTS_DIR = Path(__file__).resolve().parents[2] / "plugins" / "clarifo" / "agents"

# Workspace write tools. Blocked here as well as by the server-side opt-in.
WRITE_TOOLS = [
    "save_to_workspace", "save_note", "preview_document_update", "apply_document_update",
    "create_automation_draft", "activate_automation", "update_automation",
    "move_to_trash", "restore_from_trash",
]


def load_agent_prompt(name: str) -> str:
    text = (AGENTS_DIR / f"{name}.md").read_text()
    return text.split("---", 2)[2].strip() if text.startswith("---") else text


async def main(agent_name: str, prompt: str) -> None:
    async with MCPServerStreamableHttp(
        name="clarifo",
        params={
            "url": os.environ.get("CLARIFO_MCP_URL", "https://mcp.clarifo.com/mcp"),
            "headers": {"Authorization": f"Bearer {os.environ['CLARIFO_API_KEY']}"},
            "timeout": 60,
        },
        cache_tools_list=True,
        client_session_timeout_seconds=120,  # filing searches can take a while
        tool_filter=create_static_tool_filter(blocked_tool_names=WRITE_TOOLS),
        use_structured_content=True,
    ) as clarifo:
        agent = Agent(
            name=agent_name,
            instructions=load_agent_prompt(agent_name),
            mcp_servers=[clarifo],
            **({"model": os.environ["OPENAI_MODEL"]} if os.environ.get("OPENAI_MODEL") else {}),
        )
        result = await Runner.run(agent, prompt, max_turns=30)
        print(result.final_output)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent", default="investment-analyst",
                    choices=sorted(p.stem for p in AGENTS_DIR.glob("*.md")))
    ap.add_argument("prompt")
    a = ap.parse_args()
    asyncio.run(main(a.agent, a.prompt))
