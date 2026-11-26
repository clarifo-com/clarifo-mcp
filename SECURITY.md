# Security policy

Report vulnerabilities in the Clarifo MCP service, the Clarifo Data API or
the code in this repository privately to **support@clarifo.com** with the
subject line `SECURITY`. Do not open a public issue or discussion.

Please include the affected endpoint or file, steps to reproduce and the
impact you observed.

## Using the examples safely

- Never commit a Clarifo API key. Every example reads it from the
  `CLARIFO_API_KEY` environment variable; `.env` files are git-ignored.
- Where your plan allows several keys, use a separate key per integration
  so you can revoke one without affecting the others.
- Workspace writes (documents, notes, portfolios, automations) are off by
  default for every connection. Leave them off for automated agents unless
  the agent needs them.
- The tools return text from public company filings. Treat it as untrusted
  input in your own agents: do not let filing text trigger actions such as
  sending email or executing code without a human check.
