# Clarifo with the LangGraph

A research agent that answers from Clarifo's filings database with
citations. The instructions come from the shared agent templates in
[`plugins/clarifo/agents`](../../plugins/clarifo/agents/).

## Run

```bash
pip install -r requirements.txt
export CLARIFO_API_KEY=... ANTHROPIC_API_KEY=...
python agent.py --agent investment-analyst "Write an investment brief on Kone"
```

## What the template does

- Connects to `https://mcp.clarifo.com/mcp` over Streamable HTTP with the
  API key as a bearer token.
- Leaves out the workspace write tools, so the agent cannot change the
  Clarifo account it runs as.
- Uses one of the four agent templates as the system prompt:
  `investment-analyst`, `financial-analyst`, `competitor-analyst`,
  `market-monitor`.
