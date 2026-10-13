# asgard-ai-platform/mcp-google-trends-tw

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/asgard-ai-platform/mcp-google-trends-tw) · [JSON definitions](../../data/mcp/asgard-google-trends-tw.json)

Reviewed 2026-10-13 at commit [`1f72f63c94f4`](https://github.com/asgard-ai-platform/mcp-google-trends-tw/tree/1f72f63c94f45f4a48694657aab5e2a9abce9994).

Explore keyword time series, regional interest, and topic suggestions with configurable Taiwan defaults.

**5 tool definitions; 5 marked Google Trends.**

- Daily and realtime search tools rely on legacy pytrends endpoints; they are registered, but current upstream availability was not tested.

## Tools

| Tool | Scope |
|---|---|
| [`tw_daily_trending_searches`](#tool-tw-daily-trending-searches) | google-trends |
| [`tw_realtime_trending_searches`](#tool-tw-realtime-trending-searches) | google-trends |
| [`tw_interest_over_time`](#tool-tw-interest-over-time) | google-trends |
| [`tw_interest_by_region`](#tool-tw-interest-by-region) | google-trends |
| [`tw_keyword_suggestions`](#tool-tw-keyword-suggestions) | google-trends |

<a id="tool-tw-daily-trending-searches"></a>

### `tw_daily_trending_searches`

Daily trending searches (Google Daily Trends) for the given region (default Taiwan).

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string / null | No | `null` | Region geo code (default TW). Use ISO 3166-1 alpha-2, e.g. TW. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "geo": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Region geo code (default TW). Use ISO 3166-1 alpha-2, e.g. TW.",
      "title": "Geo"
    }
  },
  "title": "tw_daily_trending_searchesArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Null or empty geo falls back to TW; no ISO-code pattern or length validation is declared.
- All successful results report top-level geo=TW even when the query geo is overridden. Client construction occurs before the error-catching try block.

Sources: [tools/google\_trends\_tools.py:65](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/tools/google_trends_tools.py#L65-L81) · [tools/google\_trends\_tools.py:54](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/tools/google_trends_tools.py#L54-L62) · [connectors/pytrends\_client.py:14](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/connectors/pytrends_client.py#L14-L114) · [config/settings.py:5](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/config/settings.py#L5-L18) · [mcp\_server.py:5](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/mcp_server.py#L5-L12)

<a id="tool-tw-realtime-trending-searches"></a>

### `tw_realtime_trending_searches`

Realtime search trends for the given region (default Taiwan).

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string / null | No | `null` | Region geo code (default TW), e.g. TW. | — |
| `category` | string | No | `"all"` | Category filter (pytrends passthrough; default all). | — |
| `count` | integer | No | `25` | Max number of trending stories (1–300). | minimum: 1; maximum: 300 |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "geo": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Region geo code (default TW), e.g. TW.",
      "title": "Geo"
    },
    "category": {
      "default": "all",
      "description": "Category filter (pytrends passthrough; default all).",
      "title": "Category",
      "type": "string"
    },
    "count": {
      "default": 25,
      "description": "Max number of trending stories (1–300).",
      "maximum": 300,
      "minimum": 1,
      "title": "Count",
      "type": "integer"
    }
  },
  "title": "tw_realtime_trending_searchesArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- count is constrained to 1–300 by the input schema; implementation casts to int and maps count into Google ri/rs request parameters without a final result slice.
- category is an unconstrained string, not an enum; empty category falls back to all. Null or empty geo falls back to TW.
- All successful results report top-level geo=TW even when the query geo is overridden. Client construction occurs before the error-catching try block.

Sources: [tools/google\_trends\_tools.py:84](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/tools/google_trends_tools.py#L84-L110) · [tools/google\_trends\_tools.py:54](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/tools/google_trends_tools.py#L54-L62) · [connectors/pytrends\_client.py:14](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/connectors/pytrends_client.py#L14-L114) · [config/settings.py:5](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/config/settings.py#L5-L18) · [mcp\_server.py:5](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/mcp_server.py#L5-L12)

<a id="tool-tw-interest-over-time"></a>

### `tw_interest_over_time`

Interest over time for Taiwan (or overridden geo) for up to five keywords.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | Search terms to compare (1–5 keywords). | minItems: 1; maxItems: 5 |
| `timeframe` | string | No | `"now 7-d"` | Google Trends timeframe, e.g. 'now 7-d', 'today 3-m', 'today 5-y'. | — |
| `gprop` | string | No | `""` | Property: '' (web), images, news, youtube, froogle (Shopping). | — |
| `geo` | string / null | No | `null` | Geo for the series (default TW). | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keywords": {
      "description": "Search terms to compare (1–5 keywords).",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Keywords",
      "type": "array"
    },
    "timeframe": {
      "default": "now 7-d",
      "description": "Google Trends timeframe, e.g. 'now 7-d', 'today 3-m', 'today 5-y'.",
      "title": "Timeframe",
      "type": "string"
    },
    "gprop": {
      "default": "",
      "description": "Property: '' (web), images, news, youtube, froogle (Shopping).",
      "title": "Gprop",
      "type": "string"
    },
    "geo": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Geo for the series (default TW).",
      "title": "Geo"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "tw_interest_over_timeArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- keywords has schema bounds 1–5; implementation also rejects an empty list. Array items have no nonempty-string constraint.
- timeframe and gprop are strings, not enums. Empty timeframe falls back to now 7-d; null or empty geo falls back to TW.
- pytrends 4.9.2 build\_payload additionally validates gprop against ['', 'images', 'news', 'youtube', 'froogle']; this is dependency implementation validation, not an input-schema enum.
- All successful results report top-level geo=TW even when the query geo is overridden. Client construction occurs before the error-catching try block.

Sources: [tools/google\_trends\_tools.py:113](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/tools/google_trends_tools.py#L113-L146) · [tools/google\_trends\_tools.py:54](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/tools/google_trends_tools.py#L54-L62) · [connectors/pytrends\_client.py:14](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/connectors/pytrends_client.py#L14-L114) · [config/settings.py:5](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/config/settings.py#L5-L18) · [mcp\_server.py:5](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/mcp_server.py#L5-L12)

<a id="tool-tw-interest-by-region"></a>

### `tw_interest_by_region`

Interest by sub-region within Taiwan (default) or another geo you set.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | Search terms (1–5 keywords). | minItems: 1; maxItems: 5 |
| `timeframe` | string | No | `"now 7-d"` | Time window for regional breakdown. | — |
| `resolution` | string | No | `"REGION"` | REGION, CITY, DMA, or COUNTRY (availability depends on geo). | — |
| `include_low_volume` | boolean | No | `true` | Include low-volume regions when True. | — |
| `include_geo_code` | boolean | No | `false` | Include ISO geo codes when True. | — |
| `gprop` | string | No | `""` | Same as interest over time. | — |
| `geo` | string / null | No | `null` | Geo for the payload (default TW). | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keywords": {
      "description": "Search terms (1–5 keywords).",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Keywords",
      "type": "array"
    },
    "timeframe": {
      "default": "now 7-d",
      "description": "Time window for regional breakdown.",
      "title": "Timeframe",
      "type": "string"
    },
    "resolution": {
      "default": "REGION",
      "description": "REGION, CITY, DMA, or COUNTRY (availability depends on geo).",
      "title": "Resolution",
      "type": "string"
    },
    "include_low_volume": {
      "default": true,
      "description": "Include low-volume regions when True.",
      "title": "Include Low Volume",
      "type": "boolean"
    },
    "include_geo_code": {
      "default": false,
      "description": "Include ISO geo codes when True.",
      "title": "Include Geo Code",
      "type": "boolean"
    },
    "gprop": {
      "default": "",
      "description": "Same as interest over time.",
      "title": "Gprop",
      "type": "string"
    },
    "geo": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Geo for the payload (default TW).",
      "title": "Geo"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "tw_interest_by_regionArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- keywords has schema bounds 1–5; implementation also rejects an empty list. Items need not be nonempty strings.
- resolution is an unconstrained string, not an enum; an empty value falls back to REGION. pytrends applies resolution conditionally by geo.
- gprop is a string without an enum; pytrends 4.9.2 additionally validates ['', 'images', 'news', 'youtube', 'froogle'].
- Empty timeframe falls back to now 7-d; null or empty geo falls back to TW.
- All successful results report top-level geo=TW even when the query geo is overridden. Client construction occurs before the error-catching try block.

Sources: [tools/google\_trends\_tools.py:149](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/tools/google_trends_tools.py#L149-L198) · [tools/google\_trends\_tools.py:54](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/tools/google_trends_tools.py#L54-L62) · [connectors/pytrends\_client.py:14](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/connectors/pytrends_client.py#L14-L114) · [config/settings.py:5](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/config/settings.py#L5-L18) · [mcp\_server.py:5](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/mcp_server.py#L5-L12)

<a id="tool-tw-keyword-suggestions"></a>

### `tw_keyword_suggestions`

Keyword / topic suggestions (autocomplete) for refining a Trends query.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Partial or full query to get Google Trends suggestions. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "description": "Partial or full query to get Google Trends suggestions.",
      "title": "Keyword",
      "type": "string"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "tw_keyword_suggestionsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- keyword is a required string with no schema minLength; implementation rejects an empty string.
- All successful results report top-level geo=TW even when the query geo is overridden. Client construction occurs before the error-catching try block.

Sources: [tools/google\_trends\_tools.py:201](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/tools/google_trends_tools.py#L201-L214) · [tools/google\_trends\_tools.py:54](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/tools/google_trends_tools.py#L54-L62) · [connectors/pytrends\_client.py:14](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/connectors/pytrends_client.py#L14-L114) · [config/settings.py:5](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/config/settings.py#L5-L18) · [mcp\_server.py:5](https://github.com/asgard-ai-platform/mcp-google-trends-tw/blob/1f72f63c94f45f4a48694657aab5e2a9abce9994/mcp_server.py#L5-L12)

## Schema provenance

Imported the default-branch mcp_server entrypoint and awaited its FastMCP singleton list_tools() locally using uv sync --frozen dependencies (mcp 1.27.0, Pydantic 2.13.2, pytrends 4.9.2). Blocked socket.connect during introspection. Preserved returned descriptions and inputSchema verbatim; inspected every decorator and implementation. Raw list_tools response retained in source clone/listed_tools.json.

- No remote tool calls were executed; Google endpoint availability and response correctness are not verified. Daily/realtime use unofficial Google Trends endpoints that may change or be blocked.
- Declared dependencies allow newer MCP/Pydantic versions; schemas here are from the checked-in uv.lock versions.
