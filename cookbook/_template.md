---
# Front matter is required. clarifo.com renders recipes from this repository
# (one source, no copy to maintain); it builds the page URL from `slug`.
title: "How to <do the task> with Clarifo MCP"   # the question a user would type, <= 65 chars
description: "<One sentence answer, <= 155 chars, used as meta description and by AI search.>"
slug: <kebab-case, unique, never changed after publishing>
category: <earnings | comparison | risk | accounting | due-diligence | monitoring | screening | valuation>
audience: [<investor | analyst | auditor | corporate-finance | developer>]
markets: [<us | nordic>]
tools: [<tool_name>, ...]                      # tools the recipe calls, checked by CI
clients: [claude, chatgpt, claude-code, cursor, sdk]
updated: YYYY-MM-DD
---

# <Title as a question or task>

**Short answer:** <Two or three sentences that fully answer the title. AI
search engines quote this paragraph; it must make sense on its own.>

## Prompt

> <A prompt the reader can paste as-is into Claude or ChatGPT.>

## What happens

| Step | Tool | Why |
|---|---|---|
| 1 | `tool_name` | ... |

## What you get

<Describe the shape of the answer: sections, table columns, citations. Do
not paste real responses with figures; see docs/tools/examples/README.md.>

## Variations

- <Prompt variation for another market, period or audience.>

## Pitfalls

- <What goes wrong and how the recipe avoids it.>

## Related

- <Links to related recipes, agents, skills and tool pages.>
