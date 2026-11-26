---
title: "How to build a weekly watchlist digest of reports and company events"
description: "Automate a weekly summary of new reports, profit warnings, guidance changes, insider trades and upcoming report dates for a watchlist with Clarifo MCP."
slug: weekly-watchlist-digest
category: monitoring
audience: [investor, analyst]
markets: [us, nordic]
tools: [search_filings, company_events, insider_activity, portfolios]
clients: [claude, chatgpt, claude-code, sdk]
updated: 2026-11-26
---

# How do I get a weekly digest of what happened to my watchlist?

**Short answer:** Ask for the reports published (`search_filings`,
`mode="reported"`), material events (`company_events`,
`scope="cross_company"`) and next report dates (`company_events`,
`scope="calendar"`) for your companies over the last seven days. Run it by
hand, or on a schedule with an SDK template or n8n.

## Prompt

> With Clarifo: for Kone, Wärtsilä, Metso, Sandvik and Atlas Copco, what
> happened in the last 7 days? Reports published, profit warnings or
> guidance changes, management changes, and report dates in the next 14
> days. Keep a source link for every item.

## What happens

| Step | Tool | Why |
|---|---|---|
| 1 | `portfolios` | Optional: use a saved portfolio instead of a typed list. |
| 2 | `search_filings` (`mode="reported"`) | Who reported, with growth figures. |
| 3 | `company_events` (`scope="cross_company"`) | Inside information, profit warnings, M&A, management changes. |
| 4 | `insider_activity` | US: Form 4 insider trades. |
| 5 | `company_events` (`scope="calendar"`) | Upcoming report dates, never guessed. |

## What you get

A headline, a table of reports, events grouped by type with source links,
and the coming report dates.

## Run it every week

- [n8n](../../integrations/n8n/) with a Schedule Trigger and a Slack node.
- Any SDK template with `--agent market-monitor`, run from cron or GitHub
  Actions.

## Pitfalls

- Nordic profit warnings arrive as inside information releases: read the
  titles, not only the event type.

## Related

- [`market-monitor` agent](../../plugins/clarifo/agents/market-monitor.md)
