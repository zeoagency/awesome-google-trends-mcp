# goncaloaguer/unofficial-google-trends-mcp

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/goncaloaguer/unofficial-google-trends-mcp) · [JSON definitions](../../data/mcp/goncaloaguer-google-trends-mcp.json)

Reviewed 2026-10-13 at commit [`7967a0b5313e`](https://github.com/goncaloaguer/unofficial-google-trends-mcp/tree/7967a0b5313ec21263ed9040be6def24f4a3b31a).

Explore keyword time series, regional interest, related searches, categories, and location codes.

**10 tool definitions; 8 marked Google Trends.**

- Use the default trendspy backend. The optional official backend is a stub that raises NotImplementedError.
- Related-query and related-topic tools are implemented, but their descriptions warn of upstream quota failures.

## Tools

| Tool | Scope |
|---|---|
| [`interest_over_time`](#tool-interest-over-time) | google-trends |
| [`interest_by_region`](#tool-interest-by-region) | google-trends |
| [`related_queries`](#tool-related-queries) | google-trends |
| [`related_topics`](#tool-related-topics) | google-trends |
| [`trending_now`](#tool-trending-now) | google-trends |
| [`keyword_suggestions`](#tool-keyword-suggestions) | google-trends |
| [`search_categories`](#tool-search-categories) | google-trends |
| [`search_locations`](#tool-search-locations) | google-trends |
| [`keyword_ideas`](#tool-keyword-ideas) | other |
| [`server_status`](#tool-server-status) | server-management |

<a id="tool-interest-over-time"></a>

### `interest_over_time`

Calls trendspy interest\_over\_time with up to five terms and returns relative 0–100 series, query context and scale note; caches for 12 hours.

<details>
<summary>Full registered description</summary>

```text
Relative search interest over time for up to 5 terms (Google Trends' main chart).

Values are 0-100 within the query: 100 is the peak of the most popular
term in the requested period/geo. Passing multiple terms makes them
directly comparable to each other.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | 1 to 5 search terms to compare. | minItems: 1; maxItems: 5 |
| `timeframe` | string | No | `"today 12-m"` | Time range: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m' (default), 'today 5-y', 'all', or explicit dates 'YYYY-MM-DD YYYY-MM-DD'. | — |
| `geo` | string | No | `""` | Two-letter country code ('US', 'PT', 'GB') or region code ('US-CA'). Empty string = worldwide. | — |
| `category` | integer | No | `0` | Google Trends category ID to narrow results (0 = all categories). Use search\_categories to find IDs. | — |
| `gprop` | string | No | `""` | Google property: '' = web search (default), 'images', 'news', 'youtube', or 'froogle' (shopping). | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keywords": {
      "description": "1 to 5 search terms to compare.",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Keywords",
      "type": "array"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Time range: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m' (default), 'today 5-y', 'all', or explicit dates 'YYYY-MM-DD YYYY-MM-DD'.",
      "title": "Timeframe",
      "type": "string"
    },
    "geo": {
      "default": "",
      "description": "Two-letter country code ('US', 'PT', 'GB') or region code ('US-CA'). Empty string = worldwide.",
      "title": "Geo",
      "type": "string"
    },
    "category": {
      "default": 0,
      "description": "Google Trends category ID to narrow results (0 = all categories). Use search_categories to find IDs.",
      "title": "Category",
      "type": "integer"
    },
    "gprop": {
      "default": "",
      "description": "Google property: '' = web search (default), 'images', 'news', 'youtube', or 'froogle' (shopping).",
      "title": "Gprop",
      "type": "string"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "interest_over_timeArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- keywords minItems=1 and maxItems=5 are schema constraints; string items have no nonempty constraint. gprop options are prose only, not enum.

Sources: [server.py:89](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/server.py#L89) · [backends/trendspy\_backend.py:189](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/backends/trendspy_backend.py#L189)

<a id="tool-interest-by-region"></a>

### `interest_by_region`

Where a term is searched most — relative interest broken down by geography.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | A single search term. | — |
| `timeframe` | string | No | `"today 12-m"` | Time range: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m' (default), 'today 5-y', 'all', or explicit dates 'YYYY-MM-DD YYYY-MM-DD'. | — |
| `geo` | string | No | `""` | Two-letter country code ('US', 'PT', 'GB') or region code ('US-CA'). Empty string = worldwide. | — |
| `resolution` | string | No | `""` | Geographic granularity: 'COUNTRY' (default when worldwide), 'REGION' (states/districts), 'CITY', or 'DMA' (US metro areas). | — |
| `category` | integer | No | `0` | Google Trends category ID to narrow results (0 = all categories). Use search\_categories to find IDs. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "description": "A single search term.",
      "title": "Keyword",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Time range: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m' (default), 'today 5-y', 'all', or explicit dates 'YYYY-MM-DD YYYY-MM-DD'.",
      "title": "Timeframe",
      "type": "string"
    },
    "geo": {
      "default": "",
      "description": "Two-letter country code ('US', 'PT', 'GB') or region code ('US-CA'). Empty string = worldwide.",
      "title": "Geo",
      "type": "string"
    },
    "resolution": {
      "default": "",
      "description": "Geographic granularity: 'COUNTRY' (default when worldwide), 'REGION' (states/districts), 'CITY', or 'DMA' (US metro areas).",
      "title": "Resolution",
      "type": "string"
    },
    "category": {
      "default": 0,
      "description": "Google Trends category ID to narrow results (0 = all categories). Use search_categories to find IDs.",
      "title": "Category",
      "type": "integer"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "interest_by_regionArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- resolution options are prose only; empty string is converted to None for trendspy, although caller null is not in input schema.

Sources: [server.py:116](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/server.py#L116) · [backends/trendspy\_backend.py:209](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/backends/trendspy_backend.py#L209)

<a id="tool-related-queries"></a>

### `related_queries`

Calls trendspy related\_queries and returns top/rising query data with context and growth note; cached 12 hours; dedicated quota cooldown.

<details>
<summary>Full registered description</summary>

```text
Top and rising search queries related to a term.

WARNING: Google has quota-starved this endpoint for automated clients —
it fails most of the time. Prefer keyword_ideas for keyword research;
only call this if the user explicitly asks for Trends related queries.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | A single search term. | — |
| `timeframe` | string | No | `"today 12-m"` | Time range: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m' (default), 'today 5-y', 'all', or explicit dates 'YYYY-MM-DD YYYY-MM-DD'. | — |
| `geo` | string | No | `""` | Two-letter country code ('US', 'PT', 'GB') or region code ('US-CA'). Empty string = worldwide. | — |
| `category` | integer | No | `0` | Google Trends category ID to narrow results (0 = all categories). Use search\_categories to find IDs. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "description": "A single search term.",
      "title": "Keyword",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Time range: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m' (default), 'today 5-y', 'all', or explicit dates 'YYYY-MM-DD YYYY-MM-DD'.",
      "title": "Timeframe",
      "type": "string"
    },
    "geo": {
      "default": "",
      "description": "Two-letter country code ('US', 'PT', 'GB') or region code ('US-CA'). Empty string = worldwide.",
      "title": "Geo",
      "type": "string"
    },
    "category": {
      "default": 0,
      "description": "Google Trends category ID to narrow results (0 = all categories). Use search_categories to find IDs.",
      "title": "Category",
      "type": "integer"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "related_queriesArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Registered and implemented, but description and backend warn Google quota makes endpoint usually fail; not a stub on default backend.

Sources: [server.py:138](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/server.py#L138) · [backends/trendspy\_backend.py:226](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/backends/trendspy_backend.py#L226)

<a id="tool-related-topics"></a>

### `related_topics`

Calls trendspy related\_topics for Knowledge Graph related topics with query context; cached 12 hours; dedicated quota cooldown.

<details>
<summary>Full registered description</summary>

```text
Top and rising topics (Knowledge Graph entities) related to a term.

WARNING: same quota-starved endpoint as related_queries — usually fails.
Prefer keyword_ideas unless the user explicitly asks for this.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | A single search term. | — |
| `timeframe` | string | No | `"today 12-m"` | Time range: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m' (default), 'today 5-y', 'all', or explicit dates 'YYYY-MM-DD YYYY-MM-DD'. | — |
| `geo` | string | No | `""` | Two-letter country code ('US', 'PT', 'GB') or region code ('US-CA'). Empty string = worldwide. | — |
| `category` | integer | No | `0` | Google Trends category ID to narrow results (0 = all categories). Use search\_categories to find IDs. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "description": "A single search term.",
      "title": "Keyword",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Time range: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m' (default), 'today 5-y', 'all', or explicit dates 'YYYY-MM-DD YYYY-MM-DD'.",
      "title": "Timeframe",
      "type": "string"
    },
    "geo": {
      "default": "",
      "description": "Two-letter country code ('US', 'PT', 'GB') or region code ('US-CA'). Empty string = worldwide.",
      "title": "Geo",
      "type": "string"
    },
    "category": {
      "default": 0,
      "description": "Google Trends category ID to narrow results (0 = all categories). Use search_categories to find IDs.",
      "title": "Category",
      "type": "integer"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "related_topicsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Registered and implemented, but description and backend warn Google quota makes endpoint usually fail; not a stub on default backend.

Sources: [server.py:153](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/server.py#L153) · [backends/trendspy\_backend.py:245](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/backends/trendspy_backend.py#L245)

<a id="tool-trending-now"></a>

### `trending_now`

Searches trending right now in a country (Google Trends 'Trending now' feed).

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string | No | `"US"` | Two-letter country code, e.g. 'US', 'PT'. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "geo": {
      "default": "US",
      "description": "Two-letter country code, e.g. 'US', 'PT'.",
      "title": "Geo",
      "type": "string"
    }
  },
  "title": "trending_nowArguments",
  "type": "object"
}
```

</details>

Sources: [server.py:167](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/server.py#L167) · [backends/trendspy\_backend.py:260](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/backends/trendspy_backend.py#L260)

<a id="tool-keyword-suggestions"></a>

### `keyword_suggestions`

Calls trendspy suggestions for topic disambiguation; returns suggestions and seed term, cached seven days.

<details>
<summary>Full registered description</summary>

```text
Disambiguation suggestions for a term (e.g. 'python' → programming language vs snake).

Returned topic IDs can be used as more precise 'keywords' in other tools.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Term to get Google Trends topic suggestions for. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "description": "Term to get Google Trends topic suggestions for.",
      "title": "Keyword",
      "type": "string"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "keyword_suggestionsArguments",
  "type": "object"
}
```

</details>

Sources: [server.py:177](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/server.py#L177) · [backends/trendspy\_backend.py:278](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/backends/trendspy_backend.py#L278)

<a id="tool-search-categories"></a>

### `search_categories`

Find Google Trends category IDs by name, for the 'category' parameter of other tools.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `query` | string | Yes | — | Category name to search for, e.g. 'finance', 'health'. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "query": {
      "description": "Category name to search for, e.g. 'finance', 'health'.",
      "title": "Query",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "title": "search_categoriesArguments",
  "type": "object"
}
```

</details>

Sources: [server.py:189](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/server.py#L189) · [backends/trendspy\_backend.py:285](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/backends/trendspy_backend.py#L285)

<a id="tool-search-locations"></a>

### `search_locations`

Find geo codes by location name, for the 'geo' parameter of other tools.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `query` | string | Yes | — | Location name to search for, e.g. 'Portugal', 'California'. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "query": {
      "description": "Location name to search for, e.g. 'Portugal', 'California'.",
      "title": "Query",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "title": "search_locationsArguments",
  "type": "object"
}
```

</details>

Sources: [server.py:199](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/server.py#L199) · [backends/trendspy\_backend.py:292](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/backends/trendspy_backend.py#L292)

<a id="tool-keyword-ideas"></a>

### `keyword_ideas`

Requests Google Autocomplete directly for seed plus how/best/vs/why/near expansions; uses geo/language, caches 24 hours, returns suggestions without search-volume ranking.

<details>
<summary>Full registered description</summary>

```text
Keyword research via Google Autocomplete: what people actually type into Google.

Reliable and fast (no Trends quota). Returns direct suggestions plus
expansions for intent modifiers (how/best/vs/why/near). Use this instead
of related_queries.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Seed keyword to expand. | — |
| `geo` | string | No | `""` | Two-letter country code to localize results, e.g. 'PT', 'US'. | — |
| `language` | string | No | `"en"` | Language code for suggestions, e.g. 'en', 'pt'. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "description": "Seed keyword to expand.",
      "title": "Keyword",
      "type": "string"
    },
    "geo": {
      "default": "",
      "description": "Two-letter country code to localize results, e.g. 'PT', 'US'.",
      "title": "Geo",
      "type": "string"
    },
    "language": {
      "default": "en",
      "description": "Language code for suggestions, e.g. 'en', 'pt'.",
      "title": "Language",
      "type": "string"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "keyword_ideasArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Individual HTTP failures become empty suggestion lists; raises RuntimeError when all seed/expansion results are empty.

Sources: [server.py:209](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/server.py#L209) · [backends/trendspy\_backend.py:297](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/backends/trendspy_backend.py#L297)

<a id="tool-server-status"></a>

### `server_status`

Health check: which data backend is active and how the server is configured.

No caller parameters.

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {},
  "title": "server_statusArguments",
  "type": "object"
}
```

</details>

Sources: [server.py:227](https://github.com/goncaloaguer/unofficial-google-trends-mcp/blob/7967a0b5313ec21263ed9040be6def24f4a3b31a/server.py#L227)

## Schema provenance

Local FastMCP.list_tools() introspection with installed mcp 1.30.0 and Pydantic 2.13.5; TRENDS_BACKEND=official selected to avoid constructing network client. Full unconditional decorator registration and default trendspy implementations inspected. No tool invoked.

- Remote endpoint behavior was not tested. Dependencies are range-pinned, so schema formatting may vary across supported MCP/Pydantic versions.
- Official backend is a stub: every data method raises NotImplementedError. Default trendspy backend provides actual implementations.
- Underlying trendspy dependency validation was not exhaustively inspected; wrapper/schema validation is reported.
