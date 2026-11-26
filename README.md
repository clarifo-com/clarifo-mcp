# Clarifo MCP server: SEC filings and Nordic financial data for Claude, ChatGPT and Cursor

[![M8ven Score](https://m8ven.ai/badge/mcp/chasingnordics-clarifo-mcp-eisiss?v=cc402ccaf28b9c43a8761f64d2659822)](https://m8ven.ai/mcp/chasingnordics-clarifo-mcp-eisiss?s=readme)

Clarifo is a financial research platform for US and Nordic listed companies.
Its hosted MCP server lets AI assistants search company filings, pull
financial statements, compare and screen companies, and cite every figure
back to the page of the report it came from. With your permission, the
assistant can also keep the work in your Clarifo account.

- **Data:** SEC filings (10-K, 10-Q, 8-K) and Nordic annual and interim
  reports (ESEF), with financial statements and key figures over multiple
  years.
- **Citations:** every read tool returns page ids that resolve to the source
  page (a rendered report page for Nordic filings, an SEC EDGAR link for US
  filings).
- **In the chat:** in ChatGPT and Claude, results come as views: charts,
  Visual Story cards, the cited source page, a document preview and the
  Clarifo panel (your portfolios and documents).
- **Your workspace, opt-in:** company and filing data is read-only. Writing
  to your own account (saving documents and notes, editing or publishing a
  document, Automate, portfolio positions) is off until you turn it on in
  Clarifo under Settings > Integrations, and happens only when you ask.
  Edits, publishing and new automations need your approval in the chat, and
  nothing is deleted for good.

## Developer Hub

| | |
|---|---|
| [**Cookbook**](cookbook/) | Recipes with prompts, tool flows and pitfalls: earnings reviews, peer comparisons, risk-factor changes, IFRS policies, pre-DD scans, monitoring, screening. |
| [**Tools reference**](docs/tools/) | Every tool with parameters and behaviour, generated weekly from the production MCP schema. [Client differences](docs/tools/clients.md). |
| [**Claude Code plugin**](plugins/clarifo/) | The MCP connection plus investment, financial-analysis, competitor and market-monitoring agents and three skills, in one install. |
| [**Integrations**](integrations/) | Templates for the Claude Agent SDK, OpenAI Agents SDK, LangGraph, Vercel AI SDK, Cursor and n8n. |
| [**Changelog**](CHANGELOG.md) | Service and repository versions. |

Questions and ideas go to [Discussions](https://github.com/clarifo-com/clarifo-mcp/discussions).

## Endpoint

```text
https://mcp.clarifo.com/mcp
```

Streamable HTTP. Authentication is OAuth 2.1: on first connection your client
opens a browser and you sign in with your Clarifo account (a 7-day free trial
is available on the sign-in screen). Headless integrations can send a Clarifo
Data API key as a bearer token instead; see the documentation.

## Connect

### Claude (web, Claude Desktop, mobile)

1. Open the Clarifo listing in the
   [Claude Connectors Directory](https://claude.ai/directory/connectors/clarifo)
   and click **Connect**.
2. Sign in with your Clarifo account when the OAuth window opens.

The connector is stored on your Claude account, so it works the same in
Claude Desktop (macOS, Windows), on the web and on mobile.

If the directory is turned off for your workspace, add it as a custom
connector: in Claude go to **Customize > Connectors**, click **+ Add >
Add custom connector**, name it `Clarifo` and paste
`https://mcp.clarifo.com/mcp`. On Team and Enterprise plans an owner adds it
under **Organization settings > Connectors**, and members then click
**Connect**.

### Claude Code

Install the plugin to get the connection, agents and skills together:

```text
/plugin install clarifo --marketplace clarifo-com/clarifo-mcp
```

Or add only the MCP server:

```bash
claude mcp add --transport http --scope user clarifo https://mcp.clarifo.com/mcp
```

Then run `/mcp` inside Claude Code and choose Clarifo to sign in.

### ChatGPT

Add the Clarifo app from the
[ChatGPT apps directory](https://chatgpt.com/plugins/plugin_asdk_app_6a620fee8fb081918a53bd0341a34664).

### Cursor

Add to `~/.cursor/mcp.json` (or `.cursor/mcp.json` in a project):

```json
{
  "mcpServers": {
    "clarifo": {
      "url": "https://mcp.clarifo.com/mcp"
    }
  }
}
```

### Claude Desktop config file (optional)

`claude_desktop_config.json` only starts local servers, so the connector
above is the recommended way. If you manage Claude Desktop through the config
file, the [`mcp-remote`](https://github.com/geelen/mcp-remote) bridge
(Node.js 18+) connects it to the hosted server:

```json
{
  "mcpServers": {
    "clarifo": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.clarifo.com/mcp"]
    }
  }
}
```

The file is at `~/Library/Application Support/Claude/claude_desktop_config.json`
on macOS and `%APPDATA%\Claude\claude_desktop_config.json` on Windows. Restart
Claude Desktop after editing it; the first request opens the OAuth sign-in in
your browser.

## Example prompts

- "Compare NVIDIA and AMD data-center segment revenue and gross margin across the last four quarters."
- "Get Nokia Q1 2026 revenue and compare it to Ericsson for the same quarter."
- "Summarize the AI risk factors in Microsoft's latest 10-K and compare them to Alphabet's."
- "How do Nordic industrial companies apply IFRS 16 to leases in their latest annual reports?"

## Support and security

- Questions, ideas and show-and-tell: [Discussions](https://github.com/clarifo-com/clarifo-mcp/discussions).
- Bugs in the examples or templates in this repository: [Issues](https://github.com/clarifo-com/clarifo-mcp/issues/new/choose).
- Data, account and service problems: [support@clarifo.com](mailto:support@clarifo.com).
- Security reports: see [SECURITY.md](SECURITY.md); never in a public issue.

## License

Code in this repository is MIT-licensed ([LICENSE](LICENSE)) and
documentation is CC BY 4.0 ([LICENSE-docs](LICENSE-docs)). The hosted Clarifo
service, the server source code (not published here), financial data
returned by the service and the Clarifo brand are not covered by either
license; see [NOTICE](NOTICE).

## Links

- Full documentation, plans and limits: https://www.clarifo.com/docs/mcp
- Product: https://www.clarifo.com/product/features
- MCP documentation: https://www.clarifo.com/docs/mcp
- Pricing: https://www.clarifo.com/pricing
