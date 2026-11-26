---
title: "How to run a pre-due-diligence red-flag scan on a listed company"
description: "Check cash conversion, audit and going-concern evidence, covenants, governance and CSRD coverage from public filings with Clarifo MCP before full due diligence."
slug: pre-dd-red-flag-scan
category: due-diligence
audience: [corporate-finance, analyst, investor]
markets: [us, nordic]
tools: [dd_quickscan, search_filing_content, governance, insider_activity]
clients: [claude, chatgpt, claude-code, cursor, sdk]
updated: 2026-11-26
---

# How do I scan a listed company for red flags before due diligence?

**Short answer:** `dd_quickscan` builds an evidence pack from public
filings in one call: financial trends and cash conversion, valuation on
reported earnings, and filing passages on audit, governance, covenants,
outlook and earnings quality, plus CSRD disclosure coverage for EU
companies. The assistant applies Clarifo's rubric and writes a red-flag
memo with citations. It is a first look, not due diligence.

## Prompt

> Run a pre-DD scan on YIT with Clarifo. Rate the red flags high,
> medium or low with citations, list the gaps in the evidence, and end with
> questions for management.

## What happens

| Step | Tool | Why |
|---|---|---|
| 1 | `dd_quickscan` | Trends, period view, valuation, materiality evidence, CSRD coverage. |
| 2 | `search_filing_content` | Depth on a flagged topic. |
| 3 | `governance`, `insider_activity` | US only: proxy and Form 4 context. |

## What you get

A memo: scope and gaps, rated red flags, financial trend, valuation (with
price date and earnings period), governance and audit, CSRD coverage, and
five to eight questions for management.

## Pitfalls

- **Missing evidence is not a clean bill.** If the auditor's report was not
  found in the indexed text, the memo says to check it in the filing.
- **No annualising.** A one-quarter effect stays a one-quarter effect.

## Related

- [`pre-dd-scan` skill](../../plugins/clarifo/skills/pre-dd-scan/SKILL.md)
