# Catalog maintenance

This repository lists MCP servers, command-line tools (CLIs), and client libraries or SDKs that expose Google Trends data. Keep the catalog concise and in plain English.

## Inclusion rules

- Require a publicly accessible implementation that retrieves Google Trends data through its endpoints, RSS feed, a Google Trends provider API, or Google's Trends dataset in BigQuery.
- Include tools covering multiple services only when their Google Trends integration is implemented and accessible through an MCP tool, CLI command, or reusable client library.
- Exclude standalone web services, dashboards, batch pipelines, news-only tools, empty scaffolds, and generic SEO tools without an implemented Google Trends integration.
- List each project once under its primary interface: MCP, CLI, or SDKs and client libraries. Mention additional interfaces in its description and comparison row.
- Keep archived clients when they remain useful as references, and mark them **Archived**. Do not imply that an unarchived project is actively maintained or works against current upstream endpoints.
- Resolve redirects to the canonical repository. Exclude duplicate forks or wrappers without substantive standalone utility. First-party connectors to hosted Google Trends MCP services qualify; label the hosted service and required credentials explicitly.

## Verify every entry

1. Inspect the project's README and source code. Confirm the Google Trends data source, implemented interface, and each feature included in the description.
2. Link to the canonical repository or the specific tool directory in a larger repository. Check archive status through GitHub.
3. Use concise, verb-first descriptions of one or two sentences. Describe concrete behavior; omit unsupported speed, quota, uptime, anti-bot immunity, pricing, and quality claims.
4. Keep the README limited to its title, scope, official links, counted contents, comparison table, and the three tool sections. Retain supporting repository policies separately.
5. Update counts, comparison rows, and internal anchors together. Every comparison row must correspond to exactly one catalog entry.

## Before committing

- Run `npx --yes markdownlint-cli2@latest "**/*.md"` with zero issues, matching CI.
- Verify internal anchors, relative file links, project links, counts, and unique entries.
- Review the complete diff for unsupported claims and material outside the inclusion rules.
- Use `docs(awesome-list): <summary>` as the commit format.
