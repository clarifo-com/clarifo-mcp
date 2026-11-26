# Client differences

The Clarifo MCP server exposes the same tools to every client. What differs
is how a client signs in, how it shows results and how many tools it loads.

| Client | Sign-in | Rich views | Notes |
|---|---|---|---|
| Claude (web, Desktop, mobile) | OAuth via Connectors | Yes (MCP Apps views: charts, cards, source pages) | Workspace writes ask for approval in the chat. |
| ChatGPT | OAuth via the apps directory | Yes (Apps SDK views) | `render_chart` returns Python for ChatGPT's code tool on some tools. |
| Claude Code | OAuth via `/mcp` | No, text and JSON | Install the [plugin](../../plugins/clarifo/) for agents and skills. |
| Cursor | OAuth on first call | No | See [integrations/cursor](../../integrations/cursor/). |
| SDKs (Claude Agent SDK, OpenAI Agents SDK, LangGraph, Vercel AI SDK) | `clf_` API key as bearer token (Pro, Team, Enterprise) | No | Your code receives the JSON result. |
| n8n | `clf_` API key as bearer token (Pro, Team, Enterprise) | No | See [integrations/n8n](../../integrations/n8n/). |

## Things to plan for

- **Tool count.** Clarifo has around 55 tools. Some clients and models work
  better with fewer tools loaded: every integration template in this
  repository shows how to load only the tools an agent needs.
- **Views are optional.** Tools that render a view in Claude or ChatGPT also
  return the same data as structured content, so headless clients lose
  nothing but the visual.
- **Citations.** Every figure comes with a `citation_markdown` link. Keep it
  in your agent's output: it is what makes the answer checkable.
- **Workspace writes** (saving notes and documents, portfolios, automations)
  are off for every connection until the user turns them on in Clarifo under
  Settings > Integrations; with an API key, the key must also allow writing.
  Headless agents should normally leave them off.
- **Plans and limits.** OAuth clients work on every plan with MCP access; API
  keys need Pro, Team or Enterprise. Four AI-narrated tools are Pro-only, and
  every plan has a fair-use cap and a burst cap of 120 calls per minute. See
  "Plans & limits" in the [MCP documentation](https://www.clarifo.com/docs/mcp).
- **Filing text is untrusted input.** Passages from filings are written by
  third parties. Do not let them trigger actions in your agent without a
  human check.
