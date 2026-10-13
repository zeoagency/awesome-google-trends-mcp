# Contributing

Suggest MCP servers, CLIs, and SDKs or client libraries with an implemented Google Trends integration. Read [AGENTS.md](AGENTS.md) for the inclusion rules, verification process, and entry format.

## Pull request checklist

- [ ] The project has a publicly accessible implementation and an MCP, CLI, or reusable client interface for Google Trends data.
- [ ] I checked its README and source code, including the Google Trends data source and each described feature.
- [ ] The entry appears once under its primary interface, uses a canonical project link, and marks archived repositories.
- [ ] The entry uses `| [**owner/repo**](url) | <verb-first description> |` with one or two concise, factual sentences.
- [ ] The comparison row and section counts match the entry; internal anchors and project links resolve.
- [ ] `npx --yes markdownlint-cli2@latest "**/*.md"` passes with zero issues.
