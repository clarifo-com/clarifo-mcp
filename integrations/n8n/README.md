# Clarifo in n8n

n8n connects to Clarifo with its **MCP Client Tool** node, which gives an
**AI Agent** node access to Clarifo's tools. The steps below were written
for n8n 1.x; node and field names can differ slightly between versions.

## 1. Credential

1. In n8n go to **Credentials > Add credential > Bearer Auth** (some
   versions call it Header Auth; then use the header name `Authorization`
   and the value `Bearer <key>`).
2. Paste a Clarifo API key (`clf_live_…`), created in Clarifo under
   **Settings > API keys** (Pro, Team or Enterprise plan). Use a key
   dedicated to n8n, without write permission.

## 2. Workflow

1. **Trigger**: Schedule Trigger (for example weekdays 07:30) or Chat Trigger.
2. **AI Agent** node with a chat model of your choice.
   Paste the instructions of one of the agent templates as the system
   message, for example
   [`market-monitor.md`](../../plugins/clarifo/agents/market-monitor.md)
   (everything below the `---` front matter).
3. Attach an **MCP Client Tool** node to the agent's Tool input:
   - Endpoint: `https://mcp.clarifo.com/mcp`
   - Server transport: HTTP Streamable
   - Authentication: the credential from step 1
   - Tools to include: **Selected**, and pick only what the workflow needs.
     For a weekly monitor: `search_filings`, `company_events`,
     `insider_activity`, `get_company_financials`.
4. Send the agent's output to Slack, email or Teams.

## Example: weekly watchlist digest

Prompt for the AI Agent node:

> Watchlist: Kone, Wärtsilä, Metso, Sandvik, Atlas Copco. Using Clarifo,
> list everything that happened in the last 7 days: reports published,
> profit warnings or guidance changes, management changes and report dates
> in the next 14 days. Keep the source link for every item.

## Keep it safe

- Never include workspace write tools (`save_note`, `save_to_workspace`,
  `apply_document_update`, automations, trash) in an unattended workflow.
- Filing text is third-party content. Do not route it into nodes that act
  (send money, change records) without a human approval step.
