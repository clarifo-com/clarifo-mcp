---
title: "How Nordic companies apply IFRS 16 to leases: compare with AI"
description: "Find and compare the IFRS 16 lease accounting policies of Nordic listed companies in their annual reports, with page citations, using Clarifo MCP."
slug: ifrs-16-leases-nordic
category: accounting
audience: [auditor, analyst, corporate-finance]
markets: [nordic]
tools: [search_filing_content, answer_reporting_standards, get_filing_snapshot]
clients: [claude, chatgpt, claude-code, cursor, sdk]
updated: 2026-11-26
---

# How do Nordic companies apply IFRS 16 to leases?

**Short answer:** Clarifo tags the pages of Nordic annual reports with the
IFRS standards they discuss. `search_filing_content` with
`ifrs_tags=["IFRS 16"]` returns the lease policy passages from each company
with page citations, and `answer_reporting_standards` gives the standard's
own paragraphs to compare them against.

## Prompt

> Using Clarifo, compare how Kesko, Tokmanni and Axfood apply IFRS 16 in
> their latest annual reports: short-term and low-value exemptions,
> discount rate, and lease term judgements. Cite the pages and the IFRS 16
> paragraphs.

## What happens

| Step | Tool | Why |
|---|---|---|
| 1 | `search_filing_content` (`ifrs_tags=["IFRS 16"]`, per company) | The policy note passages, with page citations. |
| 2 | `answer_reporting_standards` | The IFRS 16 paragraphs on exemptions, discount rate and lease term. |
| 3 | `get_filing_snapshot` | The full page where a policy spans more than a passage. |

## What you get

A comparison table (policy choice by company) with a citation in every
cell, and the standard's paragraph references.

## Variations

- Another standard: IFRS 15 revenue, IAS 36 impairment, IFRS 18 readiness
  (the `intelligence` tool has an IFRS 18 exposure view).
- Swedish or Danish companies: add local-language terms to the query.

## Pitfalls

- One topic per search. "Leases and impairment" in one query returns
  passages about neither.

## Related

- [`financial-analyst` agent](../../plugins/clarifo/agents/financial-analyst.md)
