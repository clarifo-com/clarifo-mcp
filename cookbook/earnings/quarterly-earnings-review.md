---
title: "How to review a company's quarterly report with AI and citations"
description: "Use Clarifo MCP to compare a quarter with the same quarter last year, read guidance changes and cite every figure to the report page."
slug: quarterly-earnings-review
category: earnings
audience: [investor, analyst]
markets: [us, nordic]
tools: [search_filings, get_company_financials, search_filing_content]
clients: [claude, chatgpt, claude-code, cursor, sdk]
updated: 2026-11-26
---

# How do I review a company's quarterly report with AI and citations?

**Short answer:** Ask the assistant to pull the company's last eight
quarters with `get_company_financials`, compare the latest quarter with the
same quarter a year earlier, and read the outlook section of the report with
`search_filing_content`. Clarifo returns every figure with a link to the
page of the report it came from, so each number in the review can be
checked.

## Prompt

> Review Kone's latest interim report with Clarifo. Compare revenue,
> operating income, operating margin and operating cash flow with the same
> quarter last year, say whether guidance changed, and list one-off items.
> Cite every figure.

## What happens

| Step | Tool | Why |
|---|---|---|
| 1 | `search_filings` | Finds the latest interim report or 10-Q and its `period_end`. |
| 2 | `get_company_financials` (`period_type="quarterly"`, `quarters=8`) | Quarterly series with `yoy` change against the same quarter last year. |
| 3 | `search_filing_content` (outlook) | The guidance paragraph from the same report. |
| 4 | `search_filing_content` (one-offs) | Impairments, restructuring and disposals. |

## What you get

A one-page review: a headline sentence, a table of the quarter against the
same quarter last year, the drivers with citations, the guidance with a
quote, one-off items, and two things to watch next quarter.

## Variations

- US company: "Review NVIDIA's latest 10-Q the same way." US fourth quarters
  are derived from the annual report and flagged as such.
- Several companies: "Do this for Kone, Wärtsilä and Metso and put the
  results in one table."
- In Claude Code, the [`earnings-review` skill](../../plugins/clarifo/skills/earnings-review/SKILL.md)
  runs this recipe with a fixed output template.

## Pitfalls

- **Fiscal quarters.** Apple's fiscal Q2 ends in March. The review states
  `period_end` so quarters are not mixed up.
- **Adjusted figures.** Companies headline adjusted EBIT. The recipe quotes
  reported figures and labels any adjusted measure.

## Related

- [Compare peers like for like](../comparison/compare-peers-like-for-like.md)
- [Weekly watchlist digest](../monitoring/weekly-watchlist-digest.md)
- Tool pages: [`get_company_financials`](../../docs/tools/get_company_financials.md),
  [`search_filing_content`](../../docs/tools/search_filing_content.md)
