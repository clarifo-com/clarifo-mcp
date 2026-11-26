---
name: earnings-review
description: Review a company's latest quarterly or interim report with Clarifo - results versus the same quarter last year, margin and cash-flow changes, guidance and what management said - with citations to the report. Use when the user asks how a company's quarter went, for an earnings recap, or to summarise a Q-report or 10-Q.
---

# Earnings review

Produce a one-page review of a company's latest reported quarter from its
filing, using the Clarifo MCP tools.

## Steps

1. Find the report: `search_filings` with the company and
   `document_type="interim_report"` (Nordic) or `"10-Q"` / `"8-K"` (US).
   Note `period_end` and `fiscal_year` / quarter.
2. Figures: `get_company_financials` with `period_type="quarterly"` and
   `quarters=8`. Use `by_quarter[].yoy` for the year-on-year change and the
   series for the trend.
3. Narrative, one topic per call to `search_filing_content`, filtered to the
   same year and quarter:
   - outlook and guidance (did it change?),
   - drivers of revenue and margin,
   - anything one-off (impairments, restructuring, disposals).
4. If the user holds a view or a portfolio position, compare against it;
   otherwise skip.

## Output template

```
## <Company> - <period> (<period_end>)

**In one line:** <the quarter in one sentence>

| | <quarter> | <same quarter last year> | Change |
|---|---|---|---|
| Revenue | | | |
| Operating income (EBIT) | | | |
| Operating margin | | | pp |
| Operating cash flow | | | |
| EPS | | | |

**What drove it** - 2-4 bullets with citations
**Guidance** - unchanged / raised / lowered / withdrawn, with the quote
**One-offs** - or "none disclosed"
**Watch next quarter** - 2 bullets

Sources: numbered links
```

## Rules

- Fiscal quarters are the company's own; check `period_end`.
- US Q4 is derived (full year minus Q1-Q3) and flagged `derived: true`.
- Reported figures only; label any adjusted figure the company highlights.
