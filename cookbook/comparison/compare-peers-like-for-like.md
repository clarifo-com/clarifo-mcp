---
title: "How to compare listed companies like for like with AI"
description: "Compare two to five US or Nordic companies on growth, margins and returns over the same period and currency, with citations, using Clarifo MCP."
slug: compare-peers-like-for-like
category: comparison
audience: [investor, analyst, corporate-finance]
markets: [us, nordic]
tools: [resolve_entities, compare_companies, screen_metric_trend, search_filing_content]
clients: [claude, chatgpt, claude-code, cursor, sdk]
updated: 2026-11-26
---

# How do I compare listed companies like for like?

**Short answer:** Use `compare_companies` with up to five companies. When
their fiscal years end in different months, use the trailing-twelve-month
view (`period_type="ltm"`); when they report in different currencies, pass
`currency` to convert at ECB rates. Clarifo flags both mismatches so the
comparison is not quietly wrong.

## Prompt

> Compare Nokia and Ericsson with Clarifo on revenue growth, gross margin,
> operating margin and return on equity over the last three years. Convert
> to EUR and cite the sources.

## What happens

| Step | Tool | Why |
|---|---|---|
| 1 | `resolve_entities` | Confirms both companies in one call. |
| 2 | `compare_companies` (`years=3`, `currency="EUR"`) | Side-by-side figures with `changes` (yoy, cagr) and computed ratios. |
| 3 | `search_filing_content` (`response_mode="concise"`) | How each company explains its margin, on the same topic. |

## What you get

One table with a row per company and the period and currency stated, three
findings that explain the gaps, and any warnings Clarifo returned
(`fiscal_calendar_warning`, `mixed_currency_comparison`).

## Variations

- Mixed markets: "Compare Kone with Otis" (a Nordic and a US company in
  one call; pass `currency` to convert).
- More than five companies or a longer series: ask for
  `screen_metric_trend` on one metric.
- Latest quarter only: "Compare their latest quarter, calendar-aligned."

## Pitfalls

- **Different year-ends** distort annual comparisons: use LTM.
- **Reported vs company-defined ratios.** Each ratio has a `basis`; the
  recipe does not mix them.

## Related

- [`competitor-analyst` agent](../../plugins/clarifo/agents/competitor-analyst.md)
- [`peer-comparison` skill](../../plugins/clarifo/skills/peer-comparison/SKILL.md)
