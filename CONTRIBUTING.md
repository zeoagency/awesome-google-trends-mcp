# Contributing

Suggest MCP tools with implemented Google Trends access, or relevant CLIs and client libraries. Read [AGENTS.md](AGENTS.md) for the scope and verification rules.

## MCP updates

- Inspect the actual tool registrations and handlers; provide commit-pinned sources or a dated hosted tools/list capture.
- Add or update the provider's complete record in data/mcp/, preserving exact names, registered descriptions, and full input schemas. Mark non-Trends tools, separate server surfaces, and document implementation limits.
- Update data/catalog.json with a capability group, a concise behavior summary, and useful tool links derived from the implementation.
- Run `python3 maintenance/build_catalog.py` to rebuild the provider pages, catalog, and complete name index.

## Checks

- [ ] Google Trends functionality is implemented and reachable through the documented interface; artifact-only outputs are identified.
- [ ] The complete configured tool set is recorded, including schema constraints and additional server surfaces, without inferred parameters.
- [ ] Grouping and descriptions follow tool behavior; unsupported tools and unrelated gateway tools are not featured.
- [ ] `python3 maintenance/build_catalog.py --check` passes.
- [ ] `npx --yes markdownlint-cli2@latest "**/*.md"` passes with zero issues.

For standalone CLIs and SDKs, update [docs/clients.md](docs/clients.md) with a canonical link and one or two factual sentences, marking archived projects.
