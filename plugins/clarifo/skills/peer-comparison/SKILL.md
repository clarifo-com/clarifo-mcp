---
name: peer-comparison
description: Compare two to five listed companies side by side with Clarifo - growth, margins, returns and cash flow on a like-for-like period and currency - with citations. Use when the user asks to compare companies, benchmark against peers, or "how does X compare with Y".
---

# Peer comparison

## Steps

1. Resolve the names in one call with `resolve_entities`. If any is
   ambiguous, ask before continuing.
2. Choose the period:
   - same fiscal year-end for all: `compare_companies` with
     `period_type="annual"`, `years=3`;
   - different fiscal year-ends: `period_type="ltm"`;
   - one quarter: `period_type="quarterly"` (calendar-aligned by default).
3. If the companies report in different currencies, pass `currency`
   (for example `"EUR"` or `"USD"`) so amounts are converted at ECB rates,
   or compare ratios only.
4. For more than five companies or a longer series of one metric, use
   `screen_metric_trend`.
5. Optional narrative: `search_filing_content` with
   `response_mode="concise"` on the same topic for each company.

## Output

- One table, one row per company, with period and currency columns.
- Three findings that explain the biggest gaps.
- Warnings the tools returned (`fiscal_calendar_warning`,
  `mixed_currency_comparison`, `data_quality_warnings`), stated plainly.
- Numbered sources.

## Rules

- Quote `changes` from the tool (yoy_pct, cagr_pct, yoy_pp); do not compute.
- Reported figures only.
