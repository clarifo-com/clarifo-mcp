---
title: "How to see what changed in a company's 10-K risk factors"
description: "List risk factors added, removed and edited between two 10-K filings, with the changed sentences, using Clarifo MCP."
slug: 10-k-risk-factor-changes
category: risk
audience: [investor, analyst]
markets: [us]
tools: [search_filings, search_filing_content]
clients: [claude, chatgpt, claude-code, cursor, sdk]
updated: 2026-11-26
---

# What changed in a company's 10-K risk factors?

**Short answer:** Clarifo splits the Risk Factors section of a 10-K into
individual risk factors and compares two filings. `search_filings` with
`mode="risk_changes"` returns the factors added, removed and modified, with
the sentences that changed, so you read the differences instead of two
40-page sections.

## Prompt

> Using Clarifo, what changed in Microsoft's risk factors between its latest
> 10-K and the previous one? Group the changes by theme and quote the new
> sentences.

## What happens

| Step | Tool | Why |
|---|---|---|
| 1 | `search_filings` (`mode="risk_changes"`) | Added, removed and modified factors between the latest and previous 10-K. |
| 2 | `search_filings` (`mode="risk_factors"`, `query=...`) | Full text of a factor that needs context. |
| 3 | `search_filing_content` | Optional: the same theme in a peer's filing. |

## What you get

The changes grouped by theme (for example AI, regulation, supply chain),
each with the added or edited sentence and a link to the filing.

## Variations

- Compare with a peer: "…and compare the AI-related risk factors with
  Alphabet's latest 10-K."
- IPO filings: works on S-1 and F-1 versions too (`docid` / `compare_to`).

## Pitfalls

- A moved paragraph is not a new risk. The modified list shows edited
  sentences; read them before calling a risk new.

## Related

- [`investment-analyst` agent](../../plugins/clarifo/agents/investment-analyst.md)
