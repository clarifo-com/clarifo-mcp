# Clarifo with the Vercel AI SDK

A research agent that answers from Clarifo's filings database with
citations. The instructions come from the shared agent templates in
[`plugins/clarifo/agents`](../../plugins/clarifo/agents/).

## Run

```bash
npm install
export CLARIFO_API_KEY=... ANTHROPIC_API_KEY=...
node agent.mjs investment-analyst "Write an investment brief on Kone"
```

## What the template does

- Connects to `https://mcp.clarifo.com/mcp` over Streamable HTTP with the
  API key as a bearer token.
- Leaves out the workspace write tools, so the agent cannot change the
  Clarifo account it runs as.
- Uses one of the four agent templates as the system prompt:
  `investment-analyst`, `financial-analyst`, `competitor-analyst`,
  `market-monitor`.

## In a Next.js app

`clarifo.mjs` exports `getClarifoTools()` and `loadAgentPrompt()`. Call them
in a route handler or server action, pass `tools` to `streamText`, and close
the client in `onFinish`. Never import it into client components: the API
key must stay on the server.
