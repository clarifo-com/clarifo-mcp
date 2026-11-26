---
title: "How to screen for quality growth companies in the Nordics and US"
description: "Find listed companies with double-digit revenue growth, improving operating margins and positive cash flow using Clarifo MCP screening tools."
slug: quality-growers
category: screening
audience: [investor, analyst]
markets: [us, nordic]
tools: [screen_quality_growers, screen_companies_multi, compare_companies, search_filing_content]
clients: [claude, chatgpt, claude-code, cursor, sdk]
updated: 2026-11-26
---

# How do I find quality growth companies?

**Short answer:** `screen_quality_growers` returns every company whose
revenue CAGR over the look-back period meets your floor, with EBIT positive
and its margin improving, and operating cash flow positive. It screens
operating companies only and covers the US, Finland and Sweden, or all
Nordic markets with `country="Nordic"` in one call. Compare the shortlist
with `compare_companies`.

## Prompt

> Using Clarifo, find Nordic companies with revenue CAGR of at least 10 %
> over five years, positive and improving EBIT margin and positive operating
> cash flow. Shortlist the top ten and compare the top five.

## What happens

| Step | Tool | Why |
|---|---|---|
| 1 | `screen_quality_growers` (`country="Nordic"`, `min_revenue_cagr=10`, `compare_years=5`, `top_n=10`) | The quality-growth screen. |
| 2 | `screen_companies_multi` | Optional extra AND filters, such as a size floor. |
| 3 | `compare_companies` | Side-by-side view of the top five. |

## What you get

A shortlist with each company's revenue CAGR, EBIT margins and operating
cash flow and the fiscal year each was screened on, then a comparison table
of the top five, with sources.

## Variations

- Turnarounds instead of growers: `pattern="turnaround"` finds companies
  with losses or falling margins in the previous years and improvement in
  the latest one. Confirm each with `search_filing_content` for
  restructuring language.
- US only: `country="US"`.

## Pitfalls

- A screen is a starting point, not a recommendation. Each company is
  screened on its newest complete fiscal year: check `coverage.freshness`.
- If the compare year is missing, `margin_check` says "unverified".
- Follow up each name with an
  [earnings review](../earnings/quarterly-earnings-review.md).
