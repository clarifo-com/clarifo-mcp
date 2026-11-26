# Changelog

All notable changes to the Clarifo MCP service and to this repository are
documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the service version matches `version` in [`server.json`](server.json).

Changes to the tool surface (tools added, removed or with changed parameters)
are detected automatically by the weekly
[tools reference job](.github/workflows/tools-reference.yml) and listed in
[`docs/tools/CHANGES.md`](docs/tools/CHANGES.md); the entries below summarise
them for people.

## [Unreleased]

### Added
- Clarifo Developer Hub: cookbook, agent templates, a Claude Code plugin and
  integration templates for the Claude Agent SDK, OpenAI Agents SDK, Cursor,
  LangGraph, n8n and the Vercel AI SDK.
- Tools reference generated from the production server's MCP schema.
- Licensing: MIT for code, CC BY 4.0 for documentation; see `NOTICE` for what
  is excluded.

## [1.2.1]

### Changed
- Registry listing moved to the `clarifo-com` organisation (`com.clarifo/clarifo`).

## [1.2.0]

### Added
- In-chat views in ChatGPT and Claude: charts, Visual Story cards, cited source
  page, document preview and the Clarifo panel.
- Opt-in workspace writes: saving documents and notes, editing and publishing
  documents, Automate and portfolio positions (off until enabled under
  Settings > Integrations).

[Unreleased]: https://github.com/clarifo-com/clarifo-mcp/compare/v1.2.1...HEAD
[1.2.1]: https://github.com/clarifo-com/clarifo-mcp/releases/tag/v1.2.1
[1.2.0]: https://www.clarifo.com/docs/mcp
