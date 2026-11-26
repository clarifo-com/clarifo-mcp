# Integrations

Templates for connecting the Clarifo MCP server to agent frameworks and
tools. Each folder runs on its own; copy it into your project.

| Folder | Framework | Language | Auth |
|---|---|---|---|
| [`claude-agent-sdk`](claude-agent-sdk/) | Claude Agent SDK | Python | API key |
| [`openai-agents-sdk`](openai-agents-sdk/) | OpenAI Agents SDK | Python | API key |
| [`langgraph`](langgraph/) | LangGraph (via LangChain `create_agent`) | Python | API key |
| [`vercel-ai-sdk`](vercel-ai-sdk/) | Vercel AI SDK | JavaScript | API key |
| [`cursor`](cursor/) | Cursor | Config | OAuth |
| [`n8n`](n8n/) | n8n | No code | API key |
| [Claude Code plugin](../plugins/clarifo/) | Claude Code | Plugin | OAuth |

## Shared design

- **One copy of the agent instructions.** The SDK templates read the system
  prompt from [`plugins/clarifo/agents/`](../plugins/clarifo/agents/), the
  same files the Claude Code plugin uses. Improve an agent once and every
  framework gets it. If you copy a folder out of this repository, copy the
  agent file with it.
- **Read-only by default.** Every template leaves out the workspace write
  tools, on top of the server-side opt-in.
- **Key from the environment.** Each folder has a `.env.example`; the key is
  read from `CLARIFO_API_KEY` and never written to disk by the code.

## Run a Python template

```bash
cd integrations/openai-agents-sdk
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
export CLARIFO_API_KEY=... OPENAI_API_KEY=...
python agent.py --agent competitor-analyst "Compare Nokia and Ericsson on operating margin over three years"
```

Agents available: `investment-analyst`, `financial-analyst`,
`competitor-analyst`, `market-monitor`.
