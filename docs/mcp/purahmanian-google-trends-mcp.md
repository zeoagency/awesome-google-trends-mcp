# purahmanian/google-trends-mcp

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/purahmanian/google-trends-mcp) · [JSON definitions](../../data/mcp/purahmanian-google-trends-mcp.json)

Reviewed 2026-10-13 at commit [`a505da1ebe99`](https://github.com/purahmanian/google-trends-mcp/tree/a505da1ebe99ab78742381d776530b81075e86f4).

Fetch time series, compare terms, inspect related queries or regional interest, and read current RSS searches.

**5 tool definitions; 5 marked Google Trends.**

- Advertised JSON Schema and stricter Zod handler validation differ; both are documented without merging them.

## Tools

| Tool | Scope |
|---|---|
| [`interest_over_time`](#tool-interest-over-time) | google-trends |
| [`compare_terms`](#tool-compare-terms) | google-trends |
| [`related_queries`](#tool-related-queries) | google-trends |
| [`trending_now`](#tool-trending-now) | google-trends |
| [`interest_by_region`](#tool-interest-by-region) | google-trends |

<a id="tool-interest-over-time"></a>

### `interest_over_time`

Fetch Google Trends interest scores (0-100) for up to 5 search terms over a time range. Returns a time series with one value per term per data point. Useful for spotting seasonality, growth, or decline in search interest.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `terms` | array of string | Yes | — | Search terms (1-5). | minItems: 1; maxItems: 5 |
| `geo` | string | No | `""` | Two-letter country code (e.g. "US") or empty for worldwide. | — |
| `timeframe` | string | No | `"today 12-m"` | Trends timeframe string, e.g. "today 12-m", "today 5-y", "now 7-d". | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "terms": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "maxItems": 5,
      "description": "Search terms (1-5)."
    },
    "geo": {
      "type": "string",
      "default": "",
      "description": "Two-letter country code (e.g. \"US\") or empty for worldwide."
    },
    "timeframe": {
      "type": "string",
      "default": "today 12-m",
      "description": "Trends timeframe string, e.g. \"today 12-m\", \"today 5-y\", \"now 7-d\"."
    }
  },
  "required": [
    "terms"
  ]
}
```

</details>

Implementation notes:

- Handler validates input with Zod independently of the advertised inputSchema; invalid input returns isError text. Zod object strips unknown keys; registered schema does not specify additionalProperties.
- Implementation additionally requires each terms item to be a nonempty string (min length 1), absent from advertised items schema.
- geo and timeframe default to empty string and today 12-m respectively; both accept arbitrary strings locally, with endpoint rejection handled as an error.
- No input permits null. No injected context arguments.

Sources: [src/index.ts:96](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L96-L132) · [src/index.ts:299](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L299-L344) · [src/index.ts:37](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L37-L89) · [src/index.ts:541](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L541-L572) · [src/trends-client.ts:147](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/trends-client.ts#L147-L207)

<a id="tool-compare-terms"></a>

### `compare_terms`

Compare 2-5 search terms against each other using Google Trends normalized interest scores. Returns the time series, averages per term, and identifies which term has the highest overall interest.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `terms` | array of string | Yes | — | Search terms to compare (2-5). | minItems: 2; maxItems: 5 |
| `geo` | string | No | `""` | Two-letter country code or empty for worldwide. | — |
| `timeframe` | string | No | `"today 12-m"` | Trends timeframe string. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "terms": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 2,
      "maxItems": 5,
      "description": "Search terms to compare (2-5)."
    },
    "geo": {
      "type": "string",
      "default": "",
      "description": "Two-letter country code or empty for worldwide."
    },
    "timeframe": {
      "type": "string",
      "default": "today 12-m",
      "description": "Trends timeframe string."
    }
  },
  "required": [
    "terms"
  ]
}
```

</details>

Implementation notes:

- Handler validates input with Zod independently of the advertised inputSchema; invalid input returns isError text. Zod object strips unknown keys; registered schema does not specify additionalProperties.
- Implementation additionally requires each terms item to be a nonempty string (min length 1), absent from advertised items schema.
- geo and timeframe default to empty string and today 12-m respectively; both accept arbitrary strings locally, with endpoint rejection handled as an error.
- No input permits null. No injected context arguments.

Sources: [src/index.ts:133](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L133-L167) · [src/index.ts:346](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L346-L400) · [src/index.ts:37](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L37-L89) · [src/index.ts:541](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L541-L572) · [src/trends-client.ts:147](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/trends-client.ts#L147-L207)

<a id="tool-related-queries"></a>

### `related_queries`

Get rising and top related search queries for a given term from Google Trends. Rising queries have seen the largest recent growth; top queries have the most overall volume. Useful for discovering adjacent keywords and content ideas.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `term` | string | Yes | — | The search term to get related queries for. | — |
| `geo` | string | No | `""` | Two-letter country code or empty for worldwide. | — |
| `timeframe` | string | No | `"today 12-m"` | Trends timeframe string. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "term": {
      "type": "string",
      "description": "The search term to get related queries for."
    },
    "geo": {
      "type": "string",
      "default": "",
      "description": "Two-letter country code or empty for worldwide."
    },
    "timeframe": {
      "type": "string",
      "default": "today 12-m",
      "description": "Trends timeframe string."
    }
  },
  "required": [
    "term"
  ]
}
```

</details>

Implementation notes:

- Handler validates input with Zod independently of the advertised inputSchema; invalid input returns isError text. Zod object strips unknown keys; registered schema does not specify additionalProperties.
- Implementation additionally requires term length at least 1, absent from advertised schema.
- geo and timeframe default to empty string and today 12-m respectively; both accept arbitrary strings locally, with endpoint rejection handled as an error.
- No input permits null. No injected context arguments.

Sources: [src/index.ts:168](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L168-L199) · [src/index.ts:402](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L402-L447) · [src/index.ts:37](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L37-L89) · [src/index.ts:541](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L541-L572) · [src/trends-client.ts:222](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/trends-client.ts#L222-L239)

<a id="tool-trending-now"></a>

### `trending_now`

Get today's daily trending searches for a country from Google Trends. Returns the top trending queries with estimated traffic and linked news articles.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string | No | `"US"` | Two-letter country code (e.g. "US", "GB", "IN", "AU"). | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "geo": {
      "type": "string",
      "default": "US",
      "description": "Two-letter country code (e.g. \"US\", \"GB\", \"IN\", \"AU\")."
    }
  },
  "required": []
}
```

</details>

Implementation notes:

- Handler validates input with Zod independently of the advertised inputSchema; invalid input returns isError text. Zod object strips unknown keys; registered schema does not specify additionalProperties.
- Implementation additionally requires geo length exactly 2, absent from advertised schema; no ISO-code enumeration or regex.
- geo defaults to US; country code is uppercased by RSS client.
- No input permits null. No injected context arguments.

Sources: [src/index.ts:200](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L200-L222) · [src/index.ts:449](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L449-L483) · [src/index.ts:37](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L37-L89) · [src/index.ts:541](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L541-L572) · [src/trends-client.ts:309](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/trends-client.ts#L309-L373)

<a id="tool-interest-by-region"></a>

### `interest_by_region`

Get Google Trends interest scores broken down by region (sub-country or country, depending on the geo parameter). Returns top regions with the highest relative interest for the given term.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `term` | string | Yes | — | The search term to get regional interest for. | — |
| `geo` | string | No | `""` | Two-letter country code to drill into sub-regions (e.g. "US" gives US states), or empty for worldwide country-level breakdown. | — |
| `timeframe` | string | No | `"today 12-m"` | Trends timeframe string. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "term": {
      "type": "string",
      "description": "The search term to get regional interest for."
    },
    "geo": {
      "type": "string",
      "default": "",
      "description": "Two-letter country code to drill into sub-regions (e.g. \"US\" gives US states), or empty for worldwide country-level breakdown."
    },
    "timeframe": {
      "type": "string",
      "default": "today 12-m",
      "description": "Trends timeframe string."
    }
  },
  "required": [
    "term"
  ]
}
```

</details>

Implementation notes:

- Handler validates input with Zod independently of the advertised inputSchema; invalid input returns isError text. Zod object strips unknown keys; registered schema does not specify additionalProperties.
- Implementation additionally requires term length at least 1, absent from advertised schema.
- geo and timeframe default to empty string and today 12-m respectively; both accept arbitrary strings locally, with endpoint rejection handled as an error.
- No input permits null. No injected context arguments.

Sources: [src/index.ts:223](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L223-L256) · [src/index.ts:485](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L485-L523) · [src/index.ts:37](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L37-L89) · [src/index.ts:541](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/index.ts#L541-L572) · [src/trends-client.ts:256](https://github.com/purahmanian/google-trends-mcp/blob/a505da1ebe99ab78742381d776530b81075e86f4/src/trends-client.ts#L256-L273)

## Schema provenance

Static source inspection of the sole ListToolsRequestSchema handler; evaluated only its standalone TOOLS literal in a Node VM after removing TypeScript as const assertions, preserving exact advertised descriptions and schemas. Cross-checked all five call dispatch branches, Zod validation and client implementations.

- No remote tools executed; live Google endpoint availability was not verified. Schema extraction evaluates only literal metadata, not a running MCP server.
