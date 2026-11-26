# Clarifo in Cursor

Copy the `.cursor` folder into your project (or merge it with yours):

- `.cursor/mcp.json` connects the Clarifo MCP server. Cursor opens the
  Clarifo sign-in in your browser on first use. For a user-wide setup put
  the same `mcpServers` block in `~/.cursor/mcp.json` instead.
- `.cursor/rules/clarifo.mdc` is a project rule that tells the agent how to
  use Clarifo data: cite figures, keep periods and currencies, keep the key
  out of code and keep licensed data out of fixtures.

## Load fewer tools

Clarifo has around 55 tools. If your project uses only a few, turn the rest
off in **Cursor Settings > MCP** to keep the agent focused.

## Try it

- "Pull Kone's quarterly revenue and operating margin for the last eight
  quarters and write a pandas notebook that charts them, with the source
  links in the markdown cells."
- "Write a typed client for our dashboard that calls our backend, and
  document which Clarifo tool each panel's data comes from."
