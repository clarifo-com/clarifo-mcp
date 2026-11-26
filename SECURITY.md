# Security policy

Report vulnerabilities in the Clarifo MCP service, the Clarifo Data API or
the code in this repository privately to **support@clarifo.com** with the
subject line `SECURITY`. Do not open a public issue or discussion.

Please include the affected endpoint or file, steps to reproduce and the
impact you observed.

## Using the examples safely

- Never commit a Clarifo API key. Every example reads it from the
  `CLARIFO_API_KEY` environment variable; `.env` files are git-ignored.
- Use a separate key per integration (Settings > API keys allows up to five
  active keys) so you can revoke one without affecting the others. Use a
  `clf_test_` key while developing: it has its own monthly cap.
- A key only writes to your workspace if both the key allows writing and
  writes are turned on under Settings > Integrations. Create keys for
  agents without write permission.
- Workspace writes (documents, notes, portfolios, automations) are off by
  default for every connection. Leave them off for automated agents unless
  the agent needs them.
- The tools return text from public company filings. Treat it as untrusted
  input in your own agents: do not let filing text trigger actions such as
  sending email or executing code without a human check.
