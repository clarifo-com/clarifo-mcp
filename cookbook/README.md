# Clarifo MCP Cookbook

Recipes for financial research with the Clarifo MCP server in Claude,
ChatGPT, Claude Code, Cursor and agent SDKs. Each recipe answers one
question, gives a prompt you can paste, shows which tools run and why, and
lists the pitfalls.

| Recipe | Markets | Category |
|---|---|---|
| [How do I review a company's quarterly report with AI and citations?](earnings/quarterly-earnings-review.md) | US, Nordic | Earnings |
| [How do I compare listed companies like for like?](comparison/compare-peers-like-for-like.md) | US, Nordic | Comparison |
| [What changed in a company's 10-K risk factors?](risk/10-k-risk-factor-changes.md) | US | Risk |
| [How do Nordic companies apply IFRS 16 to leases?](accounting/ifrs-16-leases-nordic.md) | Nordic | Accounting |
| [How do I scan a listed company for red flags before due diligence?](due-diligence/pre-dd-red-flag-scan.md) | US, Nordic | Due diligence |
| [How do I get a weekly digest of what happened to my watchlist?](monitoring/weekly-watchlist-digest.md) | US, Nordic | Monitoring |
| [How do I find quality growth companies?](screening/quality-growers.md) | US, Nordic | Screening |

## Write a recipe

Copy [`_template.md`](_template.md). The front matter is checked in CI and
is what clarifo.com uses to publish the recipe, so fill in every field. Run
the prompt against the live service before opening a pull request, and do
not paste real responses with figures (see the
[example rules](../docs/tools/examples/README.md)).

Licensed under CC BY 4.0; code blocks under MIT. See [NOTICE](../NOTICE).
