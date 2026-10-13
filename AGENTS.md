# Catalog maintenance

This repository documents MCP tools with Google Trends integrations, plus a separate CLI and SDK list. Keep navigation concise and descriptions factual, in plain English.

## Inclusion and grouping

- Require implemented Google Trends access through endpoints, RSS, a provider API, or Google's public BigQuery dataset. Research tools may deliver data as local artifacts; describe that output explicitly.
- Include broader servers only when their actual tool handlers integrate Google Trends. Exclude news-only servers, empty scaffolds, and generic SEO tools without that integration.
- Group MCPs by registered tool names, parameters, and implementation behavior. Use one primary capability group per provider; choose useful tool links rather than ratings or project marketing.
- Preserve distinct local, hosted, and conditional server surfaces. Record unsupported registrations in the full reference, but do not feature them as useful capabilities.
- Hosted tools/list verifies a registration, not proprietary implementation or successful execution. State missing evidence; never infer an MCP schema from a similar REST API.
- Keep unrelated tools from qualifying servers in their detail pages and the name index, with their scope marked. Use only Google Trends functionality to justify main-page inclusion.
- Keep standalone CLIs and client libraries in docs/clients.md. Resolve canonical repository redirects, avoid duplicate forks, and mark archived repositories.

## Source of truth and verification

- data/mcp/*.json holds complete registered names, descriptions, input schemas, scope, source citations, and extraction limitations. Pin public sources to full commit SHAs and date hosted schema captures.
- Inspect registration and handlers independently. Prefer local tools/list or isolated registration introspection; keep descriptive examples separate from schema constraints and runtime validation. Exclude injected context from caller parameters.
- Enumerate the whole configured tool set. Preserve nullability, required fields, defaults, enums, bounds, array items, nested objects, definitions/references, and additionalProperties when declared. Do not invent missing descriptions or schemas.
- data/catalog.json controls primary groups, concise behavior summaries, selected tool links, and material implementation notes. Summaries must describe what callers can obtain, including local-history coverage and known ignored parameters.
- Generate README.md, docs/tools.md, and docs/mcp/*.md with `python3 maintenance/build_catalog.py`. Edit the JSON source rather than generated pages. Every registered tool name must link from the index to its full definition.

## Before committing

1. Independently review extracted data against source or tools/list evidence, including registration completeness and source limitations.
2. Run `python3 maintenance/build_catalog.py --check` and `npx --yes markdownlint-cli2@latest "**/*.md"` with zero issues.
3. Review the diff for misleading capabilities, stale counts, broken links, and research artifacts. Keep temporary source checkouts and extraction notes outside the catalog.
4. Use `docs(awesome-list): <summary>` as the commit format.
