# mvanhorn/printing-press-library

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/mvanhorn/printing-press-library) · [JSON definitions](../../data/mcp/mvanhorn-google-trends.json)

Reviewed 2026-10-13 at commit [`985f5d7cc305`](https://github.com/mvanhorn/printing-press-library/tree/985f5d7cc305b38b501c1e6302ac731a38eac503).

Query live interest, regions, and related terms; inspect cached changes, seasonality, and historical trending snapshots.

**27 tool definitions; 19 marked Google Trends.**

- The server exposes 27 registrations, including generated command mirrors; req inputs on low-level endpoints are JSON-encoded strings.
- import always errors. workflow_archive archives zero records, and default sync has no resources. Parent trends/trends_history/workflow tools provide guidance rather than data.
- Local-history tools require retained observations; trends_trending_at does not retrieve arbitrary historical dates from Google.

## Tools

| Tool | Scope |
|---|---|
| [`context`](#tool-context) | server-management |
| [`import`](#tool-import) | other |
| [`search`](#tool-search) | other |
| [`sql`](#tool-sql) | other |
| [`sync`](#tool-sync) | other |
| [`trends`](#tool-trends) | google-trends |
| [`trends_changes`](#tool-trends-changes) | google-trends |
| [`trends_explore`](#tool-trends-explore) | google-trends |
| [`trends_geo_gap`](#tool-trends-geo-gap) | google-trends |
| [`trends_history`](#tool-trends-history) | google-trends |
| [`trends_history_search`](#tool-trends-history-search) | google-trends |
| [`trends_interest`](#tool-trends-interest) | google-trends |
| [`trends_opportunities`](#tool-trends-opportunities) | google-trends |
| [`trends_pickers_category`](#tool-trends-pickers-category) | google-trends |
| [`trends_pickers_geo`](#tool-trends-pickers-geo) | google-trends |
| [`trends_region`](#tool-trends-region) | google-trends |
| [`trends_related`](#tool-trends-related) | google-trends |
| [`trends_seasonality`](#tool-trends-seasonality) | google-trends |
| [`trends_stale`](#tool-trends-stale) | google-trends |
| [`trends_trending`](#tool-trends-trending) | google-trends |
| [`trends_trending_at`](#tool-trends-trending-at) | google-trends |
| [`trends_widget_comparedgeo`](#tool-trends-widget-comparedgeo) | google-trends |
| [`trends_widget_multiline`](#tool-trends-widget-multiline) | google-trends |
| [`trends_widget_relatedsearches`](#tool-trends-widget-relatedsearches) | google-trends |
| [`workflow`](#tool-workflow) | other |
| [`workflow_archive`](#tool-workflow-archive) | other |
| [`workflow_status`](#tool-workflow-status) | other |

<a id="tool-context"></a>

### `context`

Get API domain context: resource taxonomy, auth requirements, query tips, and unique capabilities. Call this first.

No caller parameters.

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {},
  "required": [],
  "type": "object"
}
```

</details>

Sources: [library/marketing/google-trends/internal/mcp/tools.go:33](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go) · [library/marketing/google-trends/internal/mcp/tools.go:212](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go)

<a id="tool-import"></a>

### `import`

Implementation status: **unsupported**. Registered but unsupported: always returns a usage error because this API has no importable resources.

Registered but unsupported: always returns a usage error because this API has no importable resources.

<details>
<summary>Full registered description</summary>

```text
google-trends has no create/upsert endpoints to import into — every
endpoint in this API is read-only. This command always returns a usage error.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `resource` | string | Yes | — | Positional argument <resource> | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "resource": {
      "description": "Positional argument <resource>",
      "type": "string"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [
    "resource"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Cobra requires exactly one resource argument; every resource is rejected.
- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/import.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/import.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-search"></a>

### `search`

Full-text search across all synced data. Faster than paginating list endpoints. Requires sync first.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `limit` | number | No | — | Max results (default 25) | — |
| `query` | string | Yes | — | Search query (supports FTS5 syntax: AND, OR, NOT, quotes for phrases) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "limit": {
      "description": "Max results (default 25)",
      "type": "number"
    },
    "query": {
      "description": "Search query (supports FTS5 syntax: AND, OR, NOT, quotes for phrases)",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation requires nonempty string query. Limit defaults to 25 when missing or nonpositive; positive numeric value is truncated to int. Schema has no default or bounds.

Sources: [library/marketing/google-trends/internal/mcp/tools.go:33](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go) · [library/marketing/google-trends/internal/mcp/tools.go:212](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go)

<a id="tool-sql"></a>

### `sql`

Run read-only SQL against local database. Use for ad-hoc analysis, aggregations, and joins across synced resources. Requires sync first.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `query` | string | Yes | — | SQL query (SELECT or WITH...SELECT). Synced records live in resources(resource\_type, id, data); filter by resource\_type and use json\_extract on data, e.g. SELECT json\_extract(data,'$.name') FROM resources WHERE resource\_type='trends'. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "query": {
      "description": "SQL query (SELECT or WITH...SELECT). Synced records live in resources(resource_type, id, data); filter by resource_type and use json_extract on data, e.g. SELECT json_extract(data,'$.name') FROM resources WHERE resource_type='trends'.",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation requires nonempty query and rejects multiple statements and leading keywords other than SELECT/WITH; SQLite store is opened read-only.

Sources: [library/marketing/google-trends/internal/mcp/tools.go:33](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go) · [library/marketing/google-trends/internal/mcp/tools.go:212](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go)

<a id="tool-sync"></a>

### `sync`

Implementation status: **requires-explicit-resources**. Generic API-to-SQLite sync. Default sync resource list is empty, so default invocation emits no_bulk_list_endpoints warning and syncs zero resources; explicit resources take generated sync path. Explicit trends target uses GET /trends/api/widgetdata/relatedsearches and needs caller-supplied widget token/request parameters; generic sync is not keyword orchestration.

Generic API-to-SQLite sync. Default sync resource list is empty, so default invocation emits no\_bulk\_list\_endpoints warning and syncs zero resources; explicit resources take generated sync path. Explicit trends target uses GET /trends/api/widgetdata/relatedsearches and needs caller-supplied widget token/request parameters; generic sync is not keyword orchestration.

<details>
<summary>Full registered description</summary>

```text
Sync data from the API into a local SQLite database. This API does
not declare temporal sync filters, so sync performs full pagination unless an
explicit resource declares its own incremental filter.
Once synced, use the 'search' command for instant full-text search.

Exit codes & warnings:
  Resources the API denies access to (HTTP 403, or HTTP 400 with an
  access-policy body) are reported as warnings rather than failing the
  run. In --json mode each is emitted as a {"event":"sync_warning",...}
  line carrying status, reason, and message fields, and a final
  {"event":"sync_summary",...} aggregates the run.

  Exit 0 when at least one resource synced and no resource flagged in
  the spec as critical (x-critical: true) failed; non-critical failures
  emit {"event":"sync_warning","reason":"exit_policy_default_changed",
  ...} so callers can detect that a partial failure was tolerated. Pass
  --strict to exit non-zero on any per-resource failure. Exit is always
  non-zero when every selected resource failed, regardless of --strict.

Resource scoping:
  --resources runs the named top-level resources, plus any parent-keyed
  dependent whose own name is listed OR whose parent table is listed.
  Naming a parent therefore cascades to its dependents (so "sync this
  parent and its children" works without listing every nested resource
  by hand). There is no flag today to suppress the cascade for a named
  parent. To run a dependent without re-syncing its parent, list only
  the dependent by name; the parent table must already be populated
  from a prior sync.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `concurrency` | number | No | — | Number of parallel sync workers (default: 4) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `db` | string | No | — | SQLite database file path (default: resolved data directory data.db) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `full` | boolean | No | — | Full resync (ignore previous checkpoint) (default: false) | — |
| `global-param` | string | No | — | Extra query param to inject into every sync request including dependent path-scoped calls (repeatable, key=value). Use when an API requires a scope on every call regardless of path nesting. | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `latest-only` | boolean | No | — | Refresh head of each resource only; clears resume cursor and caps pages at 1. Mutually exclusive with --since (--since wins). (default: false) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `max-pages` | number | No | — | Maximum pages to fetch per resource (0 = unlimited; cap-hit emits a sync\_warning event) (default: 0) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `no-prune` | boolean | No | — | Disable deletion reconciliation on --full (by default a full sync prunes local rows the API no longer returns for a fully-enumerated parent partition) (default: false) | — |
| `param` | string | No | — | Extra query param to inject into flat-list sync requests (repeatable, key=value). Skipped on path-scoped dependent requests so a top-level scope like workspace=<id> does not double up on /parents/<id>/children calls. Use --global-param to inject everywhere. Avoid pagination keys (limit/since/cursor) — overriding them corrupts resume state. | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `resource-param` | string | No | — | Per-resource extra query param (repeatable, resource:key=value). Wins over --param and --global-param when keys conflict. | — |
| `resources` | string | No | — | Comma-separated resource types to sync. Naming a parent also runs its parent-keyed dependents (see Long help for scoping). | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `since` | string | No | — | Incremental sync duration (e.g. 7d, 24h, 1w, 30m) | — |
| `strict` | boolean | No | — | Exit non-zero on any per-resource failure (default: only critical failures or all-resource failure exit non-zero). (default: false) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "concurrency": {
      "description": "Number of parallel sync workers (default: 4)",
      "type": "number"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "db": {
      "description": "SQLite database file path (default: resolved data directory data.db)",
      "type": "string"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "full": {
      "description": "Full resync (ignore previous checkpoint) (default: false)",
      "type": "boolean"
    },
    "global-param": {
      "description": "Extra query param to inject into every sync request including dependent path-scoped calls (repeatable, key=value). Use when an API requires a scope on every call regardless of path nesting.",
      "type": "string"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "latest-only": {
      "description": "Refresh head of each resource only; clears resume cursor and caps pages at 1. Mutually exclusive with --since (--since wins). (default: false)",
      "type": "boolean"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "max-pages": {
      "description": "Maximum pages to fetch per resource (0 = unlimited; cap-hit emits a sync_warning event) (default: 0)",
      "type": "number"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "no-prune": {
      "description": "Disable deletion reconciliation on --full (by default a full sync prunes local rows the API no longer returns for a fully-enumerated parent partition) (default: false)",
      "type": "boolean"
    },
    "param": {
      "description": "Extra query param to inject into flat-list sync requests (repeatable, key=value). Skipped on path-scoped dependent requests so a top-level scope like workspace=<id> does not double up on /parents/<id>/children calls. Use --global-param to inject everywhere. Avoid pagination keys (limit/since/cursor) — overriding them corrupts resume state.",
      "type": "string"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "resource-param": {
      "description": "Per-resource extra query param (repeatable, resource:key=value). Wins over --param and --global-param when keys conflict.",
      "type": "string"
    },
    "resources": {
      "description": "Comma-separated resource types to sync. Naming a parent also runs its parent-keyed dependents (see Long help for scoping).",
      "type": "string"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "since": {
      "description": "Incremental sync duration (e.g. 7d, 24h, 1w, 30m)",
      "type": "string"
    },
    "strict": {
      "description": "Exit non-zero on any per-resource failure (default: only critical failures or all-resource failure exit non-zero). (default: false)",
      "type": "boolean"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

</details>

Implementation notes:

- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/sync.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/sync.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-trends"></a>

### `trends`

Implementation status: **guidance-only**. Parent command returns subcommand guidance, no Trends query.

Core Google Trends explore/widget flow.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

</details>

Implementation notes:

- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-trends-changes"></a>

### `trends_changes`

See exactly what changed for a keyword's related terms and interest score since your last sync.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `keyword` | string | Yes | — | Positional argument <keyword> | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `since` | string | No | — | Compare against the most recent sync at least this long ago (e.g. 7d, 24h); default 7d | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "keyword": {
      "description": "Positional argument <keyword>",
      "type": "string"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "since": {
      "description": "Compare against the most recent sync at least this long ago (e.g. 7d, 24h); default 7d",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [
    "keyword"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- since is parsed by ParseDurationLoose; empty defaults to 7d.
- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_changes.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_changes.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-trends-explore"></a>

### `trends_explore`

Requests per-widget tokens for a comparison of up to 5 keywords. Response's ['widgets'] array yields {id, token, request} for TIMESERIES, GEO\_MAP, and RELATED\_QUERIES/TOPICS widgets. Required: hl, tz, req. Returns the new explore.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `hl` | string | Yes | — | UI/response language, e.g. en-US | — |
| `req` | string | Yes | — | JSON-encoded object: {'comparisonItem':[{'keyword':str,'geo':str,'time':str}, ... | — |
| `tz` | number | Yes | — | Timezone offset in minutes (e.g. 420 for PDT) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "hl": {
      "description": "UI/response language, e.g. en-US",
      "type": "string"
    },
    "req": {
      "description": "JSON-encoded object: {'comparisonItem':[{'keyword':str,'geo':str,'time':str}, ...",
      "type": "string"
    },
    "tz": {
      "description": "Timezone offset in minutes (e.g. 420 for PDT)",
      "type": "number"
    }
  },
  "required": [
    "hl",
    "tz",
    "req"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- req, where present, is a JSON-encoded string: MCP schema does not expose nested comparison/widget schema or validate JSON locally; generic handler forwards values. Required fields are schema requirements, handler itself skips missing bindings. Extra arguments are forwarded despite no additionalProperties constraint.

Sources: [library/marketing/google-trends/internal/mcp/tools.go:33](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go) · [library/marketing/google-trends/internal/mcp/tools.go:212](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go)

<a id="tool-trends-geo-gap"></a>

### `trends_geo_gap`

Ranks the regions where two keywords' interest diverges most

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `category` | number | No | — | Google Trends category ID (default: 0) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `geo` | string | No | — | Restrict comparison to this geo (default: worldwide) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `keywordA` | string | Yes | — | Positional argument <keywordA> | — |
| `keywordB` | string | Yes | — | Positional argument <keywordB> | — |
| `limit` | number | No | — | Maximum number of regions to return (default: 15) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `resolution` | string | No | — | Geo resolution: COUNTRY, REGION, DMA, or CITY (best-effort — patches the widget's own request if present) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeframe` | string | No | — | Time range, e.g. 'today 12-m' (default: today 12-m) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "category": {
      "description": "Google Trends category ID (default: 0)",
      "type": "number"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "geo": {
      "description": "Restrict comparison to this geo (default: worldwide)",
      "type": "string"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "keywordA": {
      "description": "Positional argument <keywordA>",
      "type": "string"
    },
    "keywordB": {
      "description": "Positional argument <keywordB>",
      "type": "string"
    },
    "limit": {
      "description": "Maximum number of regions to return (default: 15)",
      "type": "number"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "resolution": {
      "description": "Geo resolution: COUNTRY, REGION, DMA, or CITY (best-effort — patches the widget's own request if present)",
      "type": "string"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeframe": {
      "description": "Time range, e.g. 'today 12-m' (default: today 12-m)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [
    "keywordA",
    "keywordB"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Requires two keyword positionals. Resolution override is best-effort only; positive limit truncates output, nonpositive limit leaves all regions.
- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_geo\_gap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_geo_gap.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go) · [library/marketing/google-trends/internal/gtrends/explore.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/gtrends/explore.go)

<a id="tool-trends-history"></a>

### `trends_history`

Implementation status: **guidance-only**. Parent command returns subcommand guidance, no history query.

history subcommands: search

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

</details>

Implementation notes:

- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_history.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_history.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-trends-history-search"></a>

### `trends_history_search`

Full-text search across every related-term and trending-topic result you've ever synced, offline.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `limit` | number | No | — | Maximum results to return (default: 20) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `query` | string | Yes | — | Positional argument <query> | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `table` | string | No | — | Restrict search to one table: related, trending (default: both) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "limit": {
      "description": "Maximum results to return (default: 20)",
      "type": "number"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "query": {
      "description": "Positional argument <query>",
      "type": "string"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "table": {
      "description": "Restrict search to one table: related, trending (default: both)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.
- table implementation accepts empty, all, related, trending; JSON Schema has no enum.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_history\_search.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_history_search.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-trends-interest"></a>

### `trends_interest`

Interest-over-time for a keyword, optionally compared against up to 4 others.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `category` | number | No | — | Google Trends category ID (default: 0) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `compare` | string | No | — | Comma-separated additional keywords to compare (up to 4 more, 5 total) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `geo` | string | No | — | Geo code (e.g. US); default: worldwide | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `keyword` | string | Yes | — | Positional argument <keyword> | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `property` | string | No | — | Search property: '' (web), images, news, youtube, froogle | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeframe` | string | No | — | Time range, e.g. 'today 12-m', 'now 7-d' (default: today 12-m) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "category": {
      "description": "Google Trends category ID (default: 0)",
      "type": "number"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "compare": {
      "description": "Comma-separated additional keywords to compare (up to 4 more, 5 total)",
      "type": "string"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "geo": {
      "description": "Geo code (e.g. US); default: worldwide",
      "type": "string"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "keyword": {
      "description": "Positional argument <keyword>",
      "type": "string"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "property": {
      "description": "Search property: '' (web), images, news, youtube, froogle",
      "type": "string"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeframe": {
      "description": "Time range, e.g. 'today 12-m', 'now 7-d' (default: today 12-m)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [
    "keyword"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation splits compare string on commas and rejects more than 5 total keywords; schema has no maxItems or bound.
- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_interest.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_interest.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go) · [library/marketing/google-trends/internal/gtrends/explore.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/gtrends/explore.go)

<a id="tool-trends-opportunities"></a>

### `trends_opportunities`

Ranks a keyword's related/rising terms by rising-momentum times parent-topic growth

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `keyword` | string | Yes | — | Positional argument <keyword> | — |
| `limit` | number | No | — | Maximum number of opportunities to return (default: 10) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "keyword": {
      "description": "Positional argument <keyword>",
      "type": "string"
    },
    "limit": {
      "description": "Maximum number of opportunities to return (default: 10)",
      "type": "number"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [
    "keyword"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_opportunities.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_opportunities.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-trends-pickers-category"></a>

### `trends_pickers_category`

Full category id-to-name lookup tree. Openly accessible, no clearance cookie required. Required: hl, tz. Returns the category. (public)

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `hl` | string | Yes | — | UI language, e.g. en-US | — |
| `tz` | number | Yes | — | Timezone offset in minutes | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "hl": {
      "description": "UI language, e.g. en-US",
      "type": "string"
    },
    "tz": {
      "description": "Timezone offset in minutes",
      "type": "number"
    }
  },
  "required": [
    "hl",
    "tz"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- req, where present, is a JSON-encoded string: MCP schema does not expose nested comparison/widget schema or validate JSON locally; generic handler forwards values. Required fields are schema requirements, handler itself skips missing bindings. Extra arguments are forwarded despite no additionalProperties constraint.

Sources: [library/marketing/google-trends/internal/mcp/tools.go:33](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go) · [library/marketing/google-trends/internal/mcp/tools.go:212](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go)

<a id="tool-trends-pickers-geo"></a>

### `trends_pickers_geo`

Full geo code-to-name lookup tree (country/region/DMA/city). Openly accessible, no clearance cookie required. Required: hl, tz. Returns the geo. (public)

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `hl` | string | Yes | — | UI language, e.g. en-US | — |
| `tz` | number | Yes | — | Timezone offset in minutes | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "hl": {
      "description": "UI language, e.g. en-US",
      "type": "string"
    },
    "tz": {
      "description": "Timezone offset in minutes",
      "type": "number"
    }
  },
  "required": [
    "hl",
    "tz"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- req, where present, is a JSON-encoded string: MCP schema does not expose nested comparison/widget schema or validate JSON locally; generic handler forwards values. Required fields are schema requirements, handler itself skips missing bindings. Extra arguments are forwarded despite no additionalProperties constraint.

Sources: [library/marketing/google-trends/internal/mcp/tools.go:33](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go) · [library/marketing/google-trends/internal/mcp/tools.go:212](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go)

<a id="tool-trends-region"></a>

### `trends_region`

Interest-by-region for a keyword.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `category` | number | No | — | Google Trends category ID (default: 0) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `geo` | string | No | — | Geo code to scope the comparison (e.g. US); default: worldwide | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `keyword` | string | Yes | — | Positional argument <keyword> | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `resolution` | string | No | — | Geo resolution: COUNTRY, REGION, DMA, or CITY (best-effort) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeframe` | string | No | — | Time range, e.g. 'today 12-m' (default: today 12-m) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "category": {
      "description": "Google Trends category ID (default: 0)",
      "type": "number"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "geo": {
      "description": "Geo code to scope the comparison (e.g. US); default: worldwide",
      "type": "string"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "keyword": {
      "description": "Positional argument <keyword>",
      "type": "string"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "resolution": {
      "description": "Geo resolution: COUNTRY, REGION, DMA, or CITY (best-effort)",
      "type": "string"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeframe": {
      "description": "Time range, e.g. 'today 12-m' (default: today 12-m)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [
    "keyword"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Resolution is a best-effort override only when widget request already contains resolution; no schema enum or implementation allowlist.
- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_region.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_region.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go) · [library/marketing/google-trends/internal/gtrends/explore.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/gtrends/explore.go)

<a id="tool-trends-related"></a>

### `trends_related`

Related queries and/or topics for a keyword (top + rising).

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `category` | number | No | — | Google Trends category ID (default: 0) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `facet` | string | No | — | Which related data to fetch: queries, topics, or both (default: both) | — |
| `geo` | string | No | — | Geo code (e.g. US); default: worldwide | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `keyword` | string | Yes | — | Positional argument <keyword> | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeframe` | string | No | — | Time range, e.g. 'today 12-m' (default: today 12-m) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "category": {
      "description": "Google Trends category ID (default: 0)",
      "type": "number"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "facet": {
      "description": "Which related data to fetch: queries, topics, or both (default: both)",
      "type": "string"
    },
    "geo": {
      "description": "Geo code (e.g. US); default: worldwide",
      "type": "string"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "keyword": {
      "description": "Positional argument <keyword>",
      "type": "string"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeframe": {
      "description": "Time range, e.g. 'today 12-m' (default: today 12-m)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [
    "keyword"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation accepts facet queries, topics, both; empty facet becomes both. Schema has no enum.
- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_related.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_related.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go) · [library/marketing/google-trends/internal/gtrends/explore.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/gtrends/explore.go)

<a id="tool-trends-seasonality"></a>

### `trends_seasonality`

Computes monthly averages, peak month, and a seasonality strength score for a keyword from cached history.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `geo` | string | No | — | Geo code to scope the seasonality calculation (e.g. US); default: all cached geos | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `keyword` | string | Yes | — | Positional argument <keyword> | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "geo": {
      "description": "Geo code to scope the seasonality calculation (e.g. US); default: all cached geos",
      "type": "string"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "keyword": {
      "description": "Positional argument <keyword>",
      "type": "string"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [
    "keyword"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_seasonality.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_seasonality.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-trends-stale"></a>

### `trends_stale`

Lists tracked keywords whose local data hasn't been refreshed recently

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `older-than` | string | No | — | Consider keywords stale if not synced within this window (e.g. 7d, 24h); default 7d | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "older-than": {
      "description": "Consider keywords stale if not synced within this window (e.g. 7d, 24h); default 7d",
      "type": "string"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

</details>

Implementation notes:

- older-than is parsed by ParseDurationLoose; empty defaults to 7d.
- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_stale.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_stale.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-trends-trending"></a>

### `trends_trending`

Current trending search topics (optionally filtered by geo). See also: trending at.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `geo` | string | No | — | Geo code to scope trending topics (e.g. US); default: worldwide | — |
| `hl` | string | No | — | UI/response language (default: en-US) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "geo": {
      "description": "Geo code to scope trending topics (e.g. US); default: worldwide",
      "type": "string"
    },
    "hl": {
      "description": "UI/response language (default: en-US)",
      "type": "string"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

</details>

Implementation notes:

- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_trending.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_trending.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go) · [library/marketing/google-trends/internal/gtrends/trending.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/gtrends/trending.go)

<a id="tool-trends-trending-at"></a>

### `trends_trending_at`

See what was trending on a specific past date and geo — a question Google Trends' own live UI cannot answer.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `date` | string | No | — | Date to look up (YYYY-MM-DD), required | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `geo` | string | No | — | Filter by geo code (e.g. US) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "date": {
      "description": "Date to look up (YYYY-MM-DD), required",
      "type": "string"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "geo": {
      "description": "Filter by geo code (e.g. US)",
      "type": "string"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation requires nonempty date although schema does not mark date required; YYYY-MM-DD is documented but not parsed/validated before equality lookup.
- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/trends\_trending\_at.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/trends_trending_at.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-trends-widget-comparedgeo"></a>

### `trends_widget_comparedgeo`

Interest-by-region data for the GEO\_MAP widget. req and token must come from a prior explore call's matching widget entry. Required: hl, tz, req, token. Returns the comparedgeo.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `hl` | string | Yes | — | UI/response language, e.g. en-US | — |
| `req` | string | Yes | — | JSON-encoded widget.request object copied verbatim from the matching explore() widget entry | — |
| `token` | string | Yes | — | Widget token copied verbatim from the matching explore() widget entry | — |
| `tz` | number | Yes | — | Timezone offset in minutes | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "hl": {
      "description": "UI/response language, e.g. en-US",
      "type": "string"
    },
    "req": {
      "description": "JSON-encoded widget.request object copied verbatim from the matching explore() widget entry",
      "type": "string"
    },
    "token": {
      "description": "Widget token copied verbatim from the matching explore() widget entry",
      "type": "string"
    },
    "tz": {
      "description": "Timezone offset in minutes",
      "type": "number"
    }
  },
  "required": [
    "hl",
    "tz",
    "req",
    "token"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- req, where present, is a JSON-encoded string: MCP schema does not expose nested comparison/widget schema or validate JSON locally; generic handler forwards values. Required fields are schema requirements, handler itself skips missing bindings. Extra arguments are forwarded despite no additionalProperties constraint.

Sources: [library/marketing/google-trends/internal/mcp/tools.go:33](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go) · [library/marketing/google-trends/internal/mcp/tools.go:212](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go)

<a id="tool-trends-widget-multiline"></a>

### `trends_widget_multiline`

Interest-over-time data for the TIMESERIES widget. req and token must come from a prior explore call's matching widget entry. Required: hl, tz, req, token. Returns the multiline.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `hl` | string | Yes | — | UI/response language, e.g. en-US | — |
| `req` | string | Yes | — | JSON-encoded widget.request object copied verbatim from the matching explore() widget entry | — |
| `token` | string | Yes | — | Widget token copied verbatim from the matching explore() widget entry | — |
| `tz` | number | Yes | — | Timezone offset in minutes | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "hl": {
      "description": "UI/response language, e.g. en-US",
      "type": "string"
    },
    "req": {
      "description": "JSON-encoded widget.request object copied verbatim from the matching explore() widget entry",
      "type": "string"
    },
    "token": {
      "description": "Widget token copied verbatim from the matching explore() widget entry",
      "type": "string"
    },
    "tz": {
      "description": "Timezone offset in minutes",
      "type": "number"
    }
  },
  "required": [
    "hl",
    "tz",
    "req",
    "token"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- req, where present, is a JSON-encoded string: MCP schema does not expose nested comparison/widget schema or validate JSON locally; generic handler forwards values. Required fields are schema requirements, handler itself skips missing bindings. Extra arguments are forwarded despite no additionalProperties constraint.

Sources: [library/marketing/google-trends/internal/mcp/tools.go:33](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go) · [library/marketing/google-trends/internal/mcp/tools.go:212](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go)

<a id="tool-trends-widget-relatedsearches"></a>

### `trends_widget_relatedsearches`

Related queries and related topics (both top and rising) for the RELATED\_QUERIES/RELATED\_TOPICS widgets. req and token must come from a prior explore call's matching widget entry. Required: hl, tz, req, token. Returns the relatedsearches.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `hl` | string | Yes | — | UI/response language, e.g. en-US | — |
| `req` | string | Yes | — | JSON-encoded widget.request object copied verbatim from the matching explore() widget entry | — |
| `token` | string | Yes | — | Widget token copied verbatim from the matching explore() widget entry | — |
| `tz` | number | Yes | — | Timezone offset in minutes | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "hl": {
      "description": "UI/response language, e.g. en-US",
      "type": "string"
    },
    "req": {
      "description": "JSON-encoded widget.request object copied verbatim from the matching explore() widget entry",
      "type": "string"
    },
    "token": {
      "description": "Widget token copied verbatim from the matching explore() widget entry",
      "type": "string"
    },
    "tz": {
      "description": "Timezone offset in minutes",
      "type": "number"
    }
  },
  "required": [
    "hl",
    "tz",
    "req",
    "token"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- req, where present, is a JSON-encoded string: MCP schema does not expose nested comparison/widget schema or validate JSON locally; generic handler forwards values. Required fields are schema requirements, handler itself skips missing bindings. Extra arguments are forwarded despite no additionalProperties constraint.

Sources: [library/marketing/google-trends/internal/mcp/tools.go:33](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go) · [library/marketing/google-trends/internal/mcp/tools.go:212](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/tools.go)

<a id="tool-workflow"></a>

### `workflow`

Implementation status: **guidance-only**. Parent command returns subcommand guidance, no compound operation.

Compound workflows that combine multiple API operations

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

</details>

Implementation notes:

- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/channel\_workflow.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/channel_workflow.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-workflow-archive"></a>

### `workflow_archive`

Implementation status: **unsupported**. Opens local store and iterates an empty hard-coded resources list; archives zero records despite registered description.

Opens local store and iterates an empty hard-coded resources list; archives zero records despite registered description.

<details>
<summary>Full registered description</summary>

```text
Archive fetches all syncable resources from the API and stores them in a
local SQLite database. Supports incremental sync (only new data since last run)
and full resync. After archiving, use 'search' for instant full-text search.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `db` | string | No | — | SQLite database file path (default: resolved data directory data.db) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `full` | boolean | No | — | Full re-archive (ignore previous sync state) (default: false) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "db": {
      "description": "SQLite database file path (default: resolved data directory data.db)",
      "type": "string"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "full": {
      "description": "Full re-archive (ignore previous sync state) (default: false)",
      "type": "boolean"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

</details>

Implementation notes:

- Hard-coded resources list is empty; this registered command is a no-op for API archival.
- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/channel\_workflow.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/channel_workflow.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

<a id="tool-workflow-status"></a>

### `workflow_status`

Show local archive status and sync state for all resources

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `agent` | boolean | No | — | Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false) | — |
| `allow-partial-failure` | boolean | No | — | Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false) | — |
| `compact` | boolean | No | — | Return only key fields (id, name, status, timestamps) for minimal token usage (default: false) | — |
| `csv` | boolean | No | — | Output as CSV (table and array responses) (default: false) | — |
| `db` | string | No | — | SQLite database file path (default: resolved data directory data.db) | — |
| `dry-run` | boolean | No | — | Show request without sending (default: false) | — |
| `human-friendly` | boolean | No | — | Enable colored output and rich formatting (default: false) | — |
| `idempotent` | boolean | No | — | Treat already-existing create results as a successful no-op (default: false) | — |
| `json` | boolean | No | — | Output as JSON (default: false) | — |
| `max-age` | string | No | — | Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s) | — |
| `no-cache` | boolean | No | — | Bypass response cache (default: false) | — |
| `no-color` | boolean | No | — | Disable colored output (default: false) | — |
| `no-input` | boolean | No | — | Disable all interactive prompts (for CI/agents) (default: false) | — |
| `plain` | boolean | No | — | Output as plain tab-separated text (default: false) | — |
| `quiet` | boolean | No | — | Bare output, one value per line (default: false) | — |
| `select` | string | No | — | Comma-separated fields to include in output (e.g. --select id,name,status) | — |
| `timeout` | string | No | — | Request timeout (default: 1m0s) | — |
| `yes` | boolean | No | — | Skip confirmation prompts (for agents and scripts) (default: false) | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "agent": {
      "description": "Set all agent-friendly defaults (--json --compact --no-input --no-color --yes) (default: false)",
      "type": "boolean"
    },
    "allow-partial-failure": {
      "description": "Downgrade response-body partial-failure (e.g. partialFailureError) to a warning instead of a non-zero exit (default: false)",
      "type": "boolean"
    },
    "compact": {
      "description": "Return only key fields (id, name, status, timestamps) for minimal token usage (default: false)",
      "type": "boolean"
    },
    "csv": {
      "description": "Output as CSV (table and array responses) (default: false)",
      "type": "boolean"
    },
    "db": {
      "description": "SQLite database file path (default: resolved data directory data.db)",
      "type": "string"
    },
    "dry-run": {
      "description": "Show request without sending (default: false)",
      "type": "boolean"
    },
    "human-friendly": {
      "description": "Enable colored output and rich formatting (default: false)",
      "type": "boolean"
    },
    "idempotent": {
      "description": "Treat already-existing create results as a successful no-op (default: false)",
      "type": "boolean"
    },
    "json": {
      "description": "Output as JSON (default: false)",
      "type": "boolean"
    },
    "max-age": {
      "description": "Maximum acceptable age of local-store data before a stderr hint suggests sync; 0 disables (default: 30m0s)",
      "type": "string"
    },
    "no-cache": {
      "description": "Bypass response cache (default: false)",
      "type": "boolean"
    },
    "no-color": {
      "description": "Disable colored output (default: false)",
      "type": "boolean"
    },
    "no-input": {
      "description": "Disable all interactive prompts (for CI/agents) (default: false)",
      "type": "boolean"
    },
    "plain": {
      "description": "Output as plain tab-separated text (default: false)",
      "type": "boolean"
    },
    "quiet": {
      "description": "Bare output, one value per line (default: false)",
      "type": "boolean"
    },
    "select": {
      "description": "Comma-separated fields to include in output (e.g. --select id,name,status)",
      "type": "string"
    },
    "timeout": {
      "description": "Request timeout (default: 1m0s)",
      "type": "string"
    },
    "yes": {
      "description": "Skip confirmation prompts (for agents and scripts) (default: false)",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

</details>

Implementation notes:

- Command mirror shells out to companion google-trends-pp-cli; missing binary produces tool error. Handler rejects unknown named parameters and flag-like positional arguments. Cobra flag defaults are documented in property descriptions, not JSON Schema default values; numeric flags are schema number even when CLI flag parses integer, and stringSlice flags are schema strings.

Sources: [library/marketing/google-trends/internal/mcp/cobratree/walker.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/walker.go) · [library/marketing/google-trends/internal/mcp/cobratree/typemap.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/typemap.go) · [library/marketing/google-trends/internal/cli/root.go:149](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/root.go) · [library/marketing/google-trends/internal/cli/channel\_workflow.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/cli/channel_workflow.go) · [library/marketing/google-trends/internal/mcp/cobratree/shellout.go:1](https://github.com/mvanhorn/printing-press-library/blob/985f5d7cc305b38b501c1e6302ac731a38eac503/library/marketing/google-trends/internal/mcp/cobratree/shellout.go)

## Schema provenance

Built actual Google Trends MCP main with pinned Go dependencies and requested local stdio initialize + tools/list only. Preserved all 27 returned descriptions and input schemas verbatim; inspected fixed registration, runtime Cobra walker and handlers. Raw response saved under subtree audit-tools-list.json.

- No remote tool calls or live Google Trends functionality tested. Runtime schemas verified locally; command mirrors require separately installed companion CLI.
- Registered import always errors; workflow_archive resources list and default sync resources are empty. Parent tools trends/trends_history/workflow return guidance.
- Descriptions/defaults may overstate generic sync and archival support; context tool_count=6 is not actual registered count.
