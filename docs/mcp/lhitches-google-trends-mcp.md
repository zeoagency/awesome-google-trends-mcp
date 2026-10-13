# lhitches/google-trends-mcp

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/lhitches/google-trends-mcp) · [JSON definitions](../../data/mcp/lhitches-google-trends-mcp.json)

Reviewed 2026-10-13 at commit [`4f23e7f3847a`](https://github.com/lhitches/google-trends-mcp/tree/4f23e7f3847addbb12627a6866749ea3033e7532).

Fetch time series, related queries, regional interest, and current country RSS searches.

**4 tool definitions; 4 marked Google Trends.**

- Requires compatible MCP 1.x. The repository’s unbounded MCP dependency can resolve to incompatible 2.x imports.

## Tools

| Tool | Scope |
|---|---|
| [`interest_over_time`](#tool-interest-over-time) | google-trends |
| [`related_queries`](#tool-related-queries) | google-trends |
| [`interest_by_region`](#tool-interest-by-region) | google-trends |
| [`trending_now`](#tool-trending-now) | google-trends |

<a id="tool-interest-over-time"></a>

### `interest_over_time`

Creates a fresh pytrends client, builds a web-search payload with category 0, returns relative interest time series with date-only rows and per-term peaks; removes isPartial.

<details>
<summary>Full registered description</summary>

```text
Search-interest time series for one or more terms (the core Trends chart).

Values are Google's 0-100 relative index, normalised across the terms in the
single request so they can be compared to each other.

Args:
    keywords: 1-5 search terms, e.g. ["seo agency", "digital marketing"].
    timeframe: Google Trends range string. Examples:
        "now 1-H", "now 7-d", "today 1-m", "today 3-m", "today 12-m",
        "today 5-y", "all", or an explicit "2024-01-01 2024-12-31".
    geo: Two-letter country code (e.g. "AU", "US", "GB") or "" for worldwide.
        Sub-regions also work, e.g. "AU-NSW".

Returns:
    dict with the resolved query and a list of {date, <term>:value, ...} rows.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | — | — |
| `timeframe` | string | No | `"today 12-m"` | — | — |
| `geo` | string | No | `""` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keywords": {
      "items": {
        "type": "string"
      },
      "title": "Keywords",
      "type": "array"
    },
    "timeframe": {
      "default": "today 12-m",
      "title": "Timeframe",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
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

- Schema has no minItems/maxItems. Implementation strips and removes blank terms, truncates to the first five, and returns an error if none remain.
- timeframe and geo are passed through without local format validation.

Sources: [server.py:83](https://github.com/lhitches/google-trends-mcp/blob/4f23e7f3847addbb12627a6866749ea3033e7532/server.py) · [server.py:31](https://github.com/lhitches/google-trends-mcp/blob/4f23e7f3847addbb12627a6866749ea3033e7532/server.py)

<a id="tool-related-queries"></a>

### `related_queries`

Builds a single-term pytrends web-search payload with category 0 and returns top/rising related query lists limited using DataFrame.head(limit).

<details>
<summary>Full registered description</summary>

```text
Top and rising related queries for a single term — the content-idea goldmine.

"top" = most popular related searches (relative 0-100). "rising" = fastest-growing
(value is percent growth; "Breakout" means >5000% growth).

Args:
    keyword: A single search term.
    timeframe: Google Trends range string (see interest_over_time).
    geo: Two-letter country code or "" for worldwide.
    limit: Max rows to return per list (default 25).
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | — | — |
| `timeframe` | string | No | `"today 12-m"` | — | — |
| `geo` | string | No | `""` | — | — |
| `limit` | integer | No | `25` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "title": "Keyword",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "title": "Timeframe",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
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

- Implementation strips keyword and returns an error for blank input.
- limit has no schema bounds or implementation positivity check; pandas head semantics apply, including negative limits.
- timeframe and geo are passed through without local format validation.

Sources: [server.py:142](https://github.com/lhitches/google-trends-mcp/blob/4f23e7f3847addbb12627a6866749ea3033e7532/server.py) · [server.py:31](https://github.com/lhitches/google-trends-mcp/blob/4f23e7f3847addbb12627a6866749ea3033e7532/server.py)

<a id="tool-interest-by-region"></a>

### `interest_by_region`

Calls pytrends interest\_by\_region with inc\_low\_vol=True and inc\_geo\_code=False, filters zero-interest rows, sorts descending, and returns region names and interest values.

<details>
<summary>Full registered description</summary>

```text
Geographic breakdown of interest for a term (which places search it most).

Args:
    keyword: A single search term.
    resolution: "COUNTRY" (worldwide), "REGION" (states/territories within a
        country — requires geo set, e.g. geo="AU"), "CITY", or "DMA" (US metro).
    timeframe: Google Trends range string.
    geo: Two-letter country code, or "" for worldwide. Required for REGION/CITY.
    limit: Max regions to return, ranked by interest (default 30).
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | — | — |
| `resolution` | string | No | `"COUNTRY"` | — | — |
| `timeframe` | string | No | `"today 12-m"` | — | — |
| `geo` | string | No | `""` | — | — |
| `limit` | integer | No | `30` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "title": "Keyword",
      "type": "string"
    },
    "resolution": {
      "default": "COUNTRY",
      "title": "Resolution",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "title": "Timeframe",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "limit": {
      "default": 30,
      "title": "Limit",
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

- resolution is a plain string in the schema, not an enum. Implementation strips/uppercases and requires COUNTRY, REGION, CITY or DMA.
- REGION and CITY require truthy geo; no country-code format validation is applied.
- Implementation strips keyword and returns an error for blank input.
- limit has no schema bounds or implementation positivity check; pandas head semantics apply, including negative limits.

Sources: [server.py:195](https://github.com/lhitches/google-trends-mcp/blob/4f23e7f3847addbb12627a6866749ea3033e7532/server.py) · [server.py:31](https://github.com/lhitches/google-trends-mcp/blob/4f23e7f3847addbb12627a6866749ea3033e7532/server.py)

<a id="tool-trending-now"></a>

### `trending_now`

Fetches Google Trends trending RSS directly for the country, returning term, approximate traffic and the first associated news headline/source for each item.

<details>
<summary>Full registered description</summary>

```text
Currently trending searches for a country — for newsjacking / reactive content.

Reads Google's live Trending RSS feed (the ``trends.google.com/trending/rss``
endpoint). Each item includes the search term, approximate traffic, and the
news headlines driving it.

Note: pytrends' own ``trending_searches`` was retired by Google (returns 404),
so this tool talks to the RSS feed directly instead.

Args:
    geo: Two-letter country code, e.g. "AU", "US", "GB", "NZ", "IN".
    limit: Max trending items to return (default 20).
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string | No | `"AU"` | — | — |
| `limit` | integer | No | `20` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "geo": {
      "default": "AU",
      "title": "Geo",
      "type": "string"
    },
    "limit": {
      "default": 20,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "trending_nowArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- geo is stripped and uppercased, then checked only for length 2; alphabetic or supported-country membership is not validated.
- limit has no schema bounds or positivity check. Because the break check follows append, zero or negative limits still return one item when a valid item exists.

Sources: [server.py:244](https://github.com/lhitches/google-trends-mcp/blob/4f23e7f3847addbb12627a6866749ea3033e7532/server.py) · [server.py:31](https://github.com/lhitches/google-trends-mcp/blob/4f23e7f3847addbb12627a6866749ea3033e7532/server.py)

## Schema provenance

Imported server.py without calling tool implementations and enumerated await mcp.list_tools() using MCP 1.30.0 / Pydantic 2.13.5; preserved returned descriptions and inputSchema verbatim. Inspected all registration and implementation source.

- requirements.txt specifies mcp[cli]>=1.28 without an upper bound; current resolution to MCP 2.3.0 fails importing mcp.server.fastmcp. Schemas were extracted using compatible MCP 1.30.0 instead.
- No remote tool calls were executed; Google endpoint availability and data responses were not tested.
