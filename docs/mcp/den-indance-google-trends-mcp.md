# den-indance/google-trends-mcp

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/den-indance/google-trends-mcp) · [JSON definitions](../../data/mcp/den-indance-google-trends-mcp.json)

Reviewed 2026-10-13 at commit [`2831f0da9097`](https://github.com/den-indance/google-trends-mcp/tree/2831f0da9097006ead3461b3329072746d963803).

Compare keyword interest, retrieve related queries, and rank regional interest.

**5 tool definitions; 3 marked Google Trends.**

- All three Trends tools accept timeframe but do not pass it to the request implementation. The registered default is not an implemented time filter.

## Tools

| Tool | Scope |
|---|---|
| [`compare_keywords`](#tool-compare-keywords) | google-trends |
| [`get_related_queries`](#tool-get-related-queries) | google-trends |
| [`get_interest_by_region`](#tool-get-interest-by-region) | google-trends |
| [`proxy_status`](#tool-proxy-status) | server-management |
| [`proxy_refresh`](#tool-proxy-refresh) | server-management |

<a id="tool-compare-keywords"></a>

### `compare_keywords`

Compare search interest over time for up to 5 keywords

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | Up to 5 keywords | — |
| `geo` | string | No | `""` | Country code e.g. US, RU (default: worldwide) | — |
| `timeframe` | string | No | `"today 12-m"` | e.g. today 12-m, today 5-y | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "keywords": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Up to 5 keywords"
    },
    "geo": {
      "type": "string",
      "description": "Country code e.g. US, RU (default: worldwide)",
      "default": ""
    },
    "timeframe": {
      "type": "string",
      "description": "e.g. today 12-m, today 5-y",
      "default": "today 12-m"
    }
  },
  "required": [
    "keywords"
  ]
}
```

</details>

Implementation notes:

- keywords description says up to 5, but schema has no maxItems or minItems and implementation does not enforce a count.
- timeframe schema default is today 12-m, but implementation neither reads nor forwards timeframe.
- geo uses nullish fallback to empty string; this does not make null valid under the registered string schema.
- No explicit server-side argument validation is performed in the call handler; downstream library errors are returned as isError.

Sources: [server.js:23](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/server.js#L23-L35) · [server.js:113](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/server.js#L113-L123) · [trends-client.js:15](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/trends-client.js#L15-L49)

<a id="tool-get-related-queries"></a>

### `get_related_queries`

Get top and rising related queries for a keyword

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | — | — |
| `geo` | string | No | `""` | — | — |
| `timeframe` | string | No | `"today 12-m"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "keyword": {
      "type": "string"
    },
    "geo": {
      "type": "string",
      "default": ""
    },
    "timeframe": {
      "type": "string",
      "default": "today 12-m"
    }
  },
  "required": [
    "keyword"
  ]
}
```

</details>

Implementation notes:

- timeframe schema default is today 12-m, but implementation neither reads nor forwards timeframe.
- No explicit server-side argument validation is performed in the call handler; downstream library errors are returned as isError.
- geo uses nullish fallback to empty string; schema permits strings only.

Sources: [server.js:36](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/server.js#L36-L48) · [server.js:125](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/server.js#L125-L132) · [trends-client.js:15](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/trends-client.js#L15-L49)

<a id="tool-get-interest-by-region"></a>

### `get_interest_by_region`

Get search interest by region/country for a keyword

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | — | — |
| `geo` | string | No | `""` | — | — |
| `timeframe` | string | No | `"today 12-m"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "keyword": {
      "type": "string"
    },
    "geo": {
      "type": "string",
      "default": ""
    },
    "timeframe": {
      "type": "string",
      "default": "today 12-m"
    }
  },
  "required": [
    "keyword"
  ]
}
```

</details>

Implementation notes:

- timeframe schema default is today 12-m, but implementation neither reads nor forwards timeframe.
- No explicit server-side argument validation is performed in the call handler; downstream library errors are returned as isError.
- geo uses nullish fallback to empty string; schema permits strings only.

Sources: [server.js:52](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/server.js#L52-L64) · [server.js:136](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/server.js#L136-L146) · [trends-client.js:15](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/trends-client.js#L15-L49)

<a id="tool-proxy-status"></a>

### `proxy_status`

Show proxy pool status: source, working count, age, freshness, and validation progress

No caller parameters.

<details>
<summary>Complete input schema</summary>

```json
{
  "type": "object",
  "properties": {}
}
```

</details>

Implementation notes:

- Parameterless tool; provided arguments are ignored.

Sources: [server.js:65](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/server.js#L65-L69) · [server.js:84](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/server.js#L84-L99) · [proxy-manager.js:207](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/proxy-manager.js#L207-L233)

<a id="tool-proxy-refresh"></a>

### `proxy_refresh`

Re-validate the current proxy source (PROXY\_LIST or PROXY\_LIST\_FILE). Blocks until done. No-op for PROXY\_URL single-proxy mode.

No caller parameters.

<details>
<summary>Complete input schema</summary>

```json
{
  "type": "object",
  "properties": {}
}
```

</details>

Implementation notes:

- Parameterless tool; provided arguments are ignored.

Sources: [server.js:70](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/server.js#L70-L74) · [server.js:101](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/server.js#L101-L111) · [proxy-manager.js:235](https://github.com/den-indance/google-trends-mcp/blob/2831f0da9097006ead3461b3329072746d963803/proxy-manager.js#L235-L245)

## Schema provenance

Evaluated only the isolated literal ListToolsRequestSchema registration in a Node VM with a stub server and invoked its local callback; inspected every CallToolRequestSchema branch and supporting implementation. No server startup, package installation, credentials or remote tool calls.

- Live Google responses and downstream google-trends-api validation were not tested.
- The registered timeframe input is ignored by all three Trends handlers; its declared default is preserved, not represented as implemented behavior.
