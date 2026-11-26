---
name: pre-dd-scan
description: Run a pre-due-diligence scan of a listed company with Clarifo - financial trends, cash conversion, valuation on reported earnings, audit and going-concern evidence, governance, covenants and CSRD disclosure coverage - and write a red-flag memo with citations. Use for target screening, credit pre-checks, M&A first looks or "any red flags in X".
---

# Pre-DD scan

A first look from public filings. It does not replace due diligence and the
memo must say so.

## Steps

1. `dd_quickscan` with the company. Pass `market="US"` for US companies (it
   skips the CSRD branch). Use `language="fi"` if the user writes Finnish.
2. Read `coverage` first and list every branch that is `no_data` or
   `failed`. `no_data` for materiality means the text was not retrieved,
   never that there are no risks.
3. Apply the rubric in `materiality_evidence.instructions` to the chunks and
   cite each finding's `source_id`.
4. If `coverage.audit_report.found` is false, the memo says the auditor's
   report must be checked in the filing.
5. Optional depth: `search_filing_content` on a flagged topic,
   `governance` (US proxy) and `insider_activity` (US Form 4).

## Memo template

```
# Pre-DD scan: <Company> (<reporting period>)

Scope and gaps: <coverage summary, missing branches>

## Red flags        (rated high / medium / low, each with citation)
## Financial trend  (revenue, EBIT, margin, OCF, cash conversion)
## Valuation        (P/E, EV/EBIT, FCF yield - with price date and earnings period)
## Governance and audit
## CSRD disclosure coverage (EU only; coverage, not compliance)
## Questions for management (5-8)

This scan is based on public filings and does not replace due diligence.
```

## Rules

- Reported basis only; never show an adjusted multiple.
- Never annualise a single-quarter effect.
