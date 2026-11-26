# Clarifo plugin for Claude Code

Installs the Clarifo MCP server together with research agents and skills.

```text
/plugin install clarifo --marketplace clarifo-com/clarifo-mcp
```

Then run `/mcp`, choose **clarifo** and sign in with your Clarifo account.

## Agents

| Agent | Use it for |
|---|---|
| [`investment-analyst`](agents/investment-analyst.md) | A cited investment brief on one company: trend, valuation, bull and bear case, what to watch. |
| [`financial-analyst`](agents/financial-analyst.md) | Statements, segments, accounting policies and earnings quality. |
| [`competitor-analyst`](agents/competitor-analyst.md) | Like-for-like peer benchmarks with the narrative behind the gaps. |
| [`market-monitor`](agents/market-monitor.md) | What changed for a watchlist, portfolio or market: reports, events, insiders, calendar. |

The same agent files are the system prompts of the
[SDK integration templates](../../integrations/), so they stay in sync.

## Skills

| Skill | Use it for |
|---|---|
| [`earnings-review`](skills/earnings-review/SKILL.md) | One-page review of the latest quarter. |
| [`peer-comparison`](skills/peer-comparison/SKILL.md) | Two to five companies side by side, period and currency aligned. |
| [`pre-dd-scan`](skills/pre-dd-scan/SKILL.md) | Red-flag memo from public filings before due diligence. |

The agents and skills only read data. Workspace writes stay off until you
enable them in Clarifo under Settings > Integrations.
