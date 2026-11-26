"""Run a Clarifo research agent with the Claude Agent SDK.

    pip install -r requirements.txt
    export ANTHROPIC_API_KEY=... CLARIFO_API_KEY=...
    python agent.py --agent investment-analyst "Write an investment brief on Kone"

The agent instructions are the same files the Claude Code plugin uses
(plugins/clarifo/agents/*.md), so there is one copy to maintain.
"""
import argparse
import asyncio
import os
from pathlib import Path

from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, ResultMessage, TextBlock, query

AGENTS_DIR = Path(__file__).resolve().parents[2] / "plugins" / "clarifo" / "agents"

# Workspace write tools. Blocked here as well as by the server-side opt-in,
# so an unattended agent never changes the user's Clarifo account.
WRITE_TOOLS = [
    "save_to_workspace", "save_note", "preview_document_update", "apply_document_update",
    "create_automation_draft", "activate_automation", "update_automation",
    "move_to_trash", "restore_from_trash",
]


def load_agent_prompt(name: str) -> str:
    text = (AGENTS_DIR / f"{name}.md").read_text()
    return text.split("---", 2)[2].strip() if text.startswith("---") else text


async def main(agent: str, prompt: str) -> None:
    options = ClaudeAgentOptions(
        model=os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5"),
        system_prompt=load_agent_prompt(agent),
        mcp_servers={
            "clarifo": {
                "type": "http",
                "url": os.environ.get("CLARIFO_MCP_URL", "https://mcp.clarifo.com/mcp"),
                "headers": {"Authorization": f"Bearer {os.environ['CLARIFO_API_KEY']}"},
            }
        },
        tools=[],  # no file, shell or web tools: Clarifo only
        allowed_tools=["mcp__clarifo"],
        disallowed_tools=[f"mcp__clarifo__{t}" for t in WRITE_TOOLS],
        max_turns=30,
    )
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text, end="", flush=True)
        elif isinstance(message, ResultMessage) and message.is_error:
            raise SystemExit(f"Agent failed: {message.result}")
    print()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent", default="investment-analyst",
                    choices=sorted(p.stem for p in AGENTS_DIR.glob("*.md")))
    ap.add_argument("prompt")
    a = ap.parse_args()
    asyncio.run(main(a.agent, a.prompt))
