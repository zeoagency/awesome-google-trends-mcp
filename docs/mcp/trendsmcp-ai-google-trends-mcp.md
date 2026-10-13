# trendsmcp-ai/google-trends-mcp

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/trendsmcp-ai/google-trends-mcp) · [JSON definitions](../../data/mcp/trendsmcp-ai-google-trends-mcp.json)

Reviewed 2026-10-13 at commit [`a136fa9d5a25`](https://github.com/trendsmcp-ai/google-trends-mcp/tree/a136fa9d5a2552dc0f67a8e6b6297f027eacb7d2).

Request hosted keyword series, point-to-point growth, and current overall or category boards.

**3 tool definitions; 3 marked Google Trends.**

- Requires a TrendsMCP API key. Local schemas are verified; the hosted MCP endpoint’s schema equivalence is unverified.
- Tools multiplex Google Trends with other sources. Provider retrieval and growth calculations are proprietary; geographic breakdowns are not exposed.

## Tools

| Tool | Scope |
|---|---|
| [`get_growth`](#tool-get-growth) | google-trends |
| [`get_time_series`](#tool-get-time-series) | google-trends |
| [`get_top_trends`](#tool-get-top-trends) | google-trends |

<a id="tool-get-growth"></a>

### `get_growth`

Forwards keyword, source and percent\_growth as mode=get\_growth to the hosted REST API, then JSON-serializes its response. Supports Google search/images/news/shopping/YouTube and other attention sources; computation occurs remotely.

<details>
<summary>Full registered description</summary>

```text
Point-to-point growth for a keyword on one or more sources. Each window is a preset string (12M, 3M, YTD, and the other listed periods). Values are on a 0-100 scale, plus absolute volume when available. Prefer this over get_time_series for growth questions. app downloads and app rankings are keyword sources (Android bundle ID). They are not the App Store / Google Play live boards on get_top_trends. If the request is rate limited or the monthly quota is used up, tell the user their plan limit is reached.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | What to look up. The string format is required by source. Standard sources (google search, google images, google news, google shopping, youtube, wikipedia, tiktok, reddit, amazon, news sentiment, news volume): any name or phrase, e.g. 'nike'. npm: exact npmjs.com package name, case-sensitive. Right: 'react', '@babel/core'. Wrong: 'React', 'React.js'. python: exact PyPI project name. Right: 'pandas', 'requests'. Wrong: 'Pandas'. steam: game display name in plain English, not a Steam App ID. Right: 'Elden Ring', 'CS2'. First Steam store search result wins, so use an unambiguous name. app downloads and app rankings: Android bundle ID only (the id= value on Google Play). Right: 'com.openai.chatgpt', 'com.whatsapp'. Wrong: 'ChatGPT', 'WhatsApp', an iOS App Store ID, or a bundle ID that is not Android. Find it at play.google.com/store/apps/details?id=THIS\_PART. If the request includes app downloads or app rankings with other sources, keyword must still be the Android bundle ID. | — |
| `source` | string | Yes | — | One source, or comma-separated sources (e.g. 'amazon, tiktok, youtube'). Valid: 'google search', 'google images', 'google news', 'google shopping', 'youtube', 'wikipedia', 'tiktok', 'reddit', 'amazon', 'news sentiment', 'news volume', 'npm', 'python', 'steam', 'app downloads', 'app rankings'. | — |
| `percent_growth` | array of string / null | No | `null` | Growth windows. Default if omitted: ['12M']. Each item must be a preset string: '7D', '1W', '14D', '2W', '30D', '1M', '2M', '3M', '6M', '9M', '12M', '1Y', '18M', '24M', '2Y', '36M', '3Y', '48M', '4Y', '60M', '5Y', 'MTD', 'QTD', 'YTD'. Every preset is a two-date comparison. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "description": "What to look up. The string format is required by source. Standard sources (google search, google images, google news, google shopping, youtube, wikipedia, tiktok, reddit, amazon, news sentiment, news volume): any name or phrase, e.g. 'nike'. npm: exact npmjs.com package name, case-sensitive. Right: 'react', '@babel/core'. Wrong: 'React', 'React.js'. python: exact PyPI project name. Right: 'pandas', 'requests'. Wrong: 'Pandas'. steam: game display name in plain English, not a Steam App ID. Right: 'Elden Ring', 'CS2'. First Steam store search result wins, so use an unambiguous name. app downloads and app rankings: Android bundle ID only (the id= value on Google Play). Right: 'com.openai.chatgpt', 'com.whatsapp'. Wrong: 'ChatGPT', 'WhatsApp', an iOS App Store ID, or a bundle ID that is not Android. Find it at play.google.com/store/apps/details?id=THIS_PART. If the request includes app downloads or app rankings with other sources, keyword must still be the Android bundle ID.",
      "title": "Keyword",
      "type": "string"
    },
    "source": {
      "description": "One source, or comma-separated sources (e.g. 'amazon, tiktok, youtube'). Valid: 'google search', 'google images', 'google news', 'google shopping', 'youtube', 'wikipedia', 'tiktok', 'reddit', 'amazon', 'news sentiment', 'news volume', 'npm', 'python', 'steam', 'app downloads', 'app rankings'.",
      "title": "Source",
      "type": "string"
    },
    "percent_growth": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Growth windows. Default if omitted: ['12M']. Each item must be a preset string: '7D', '1W', '14D', '2W', '30D', '1M', '2M', '3M', '6M', '9M', '12M', '1Y', '18M', '24M', '2Y', '36M', '3Y', '48M', '4Y', '60M', '5Y', 'MTD', 'QTD', 'YTD'. Every preset is a two-date comparison.",
      "title": "Percent Growth"
    }
  },
  "required": [
    "keyword",
    "source"
  ],
  "title": "get_growthArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Local adapter validates parameter types via FastMCP/Pydantic; source/type values and keyword format requirements appear only in descriptions, without enum/pattern schema constraints or local validation.
- Actual upstream data retrieval and validation are not public in this repository and were not exercised. All calls require TRENDSMCP\_API\_KEY; local tools/list does not.
- No additionalProperties constraint is specified in the generated input schema.
- Schema default for percent\_growth is null, not ["12M"]. Implementation replaces omitted/null/empty list with ["12M"]. Presets are described but not an enum; arbitrary strings pass local schema. Date objects are not allowed by list[str] input schema.

Sources: [src/trends\_mcp\_server/server.py:115](https://github.com/trendsmcp-ai/google-trends-mcp/blob/a136fa9d5a2552dc0f67a8e6b6297f027eacb7d2/src/trends_mcp_server/server.py) · [src/trends\_mcp\_server/server.py:36](https://github.com/trendsmcp-ai/google-trends-mcp/blob/a136fa9d5a2552dc0f67a8e6b6297f027eacb7d2/src/trends_mcp_server/server.py) · [src/trends\_mcp\_server/server.py:74](https://github.com/trendsmcp-ai/google-trends-mcp/blob/a136fa9d5a2552dc0f67a8e6b6297f027eacb7d2/src/trends_mcp_server/server.py)

<a id="tool-get-time-series"></a>

### `get_time_series`

Full historical series for one keyword and one source (0-100 values, plus volume when available). Use for charting or custom math. Not for live 'what's trending now' boards (use get\_top\_trends). For most growth questions, use get\_growth. If the request is rate limited or the monthly quota is used up, tell the user their plan limit is reached.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | What to look up. The string format is required by source. Standard sources (google search, google images, google news, google shopping, youtube, wikipedia, tiktok, reddit, amazon, news sentiment, news volume): any name or phrase, e.g. 'tesla'. npm: exact npmjs.com package name, case-sensitive. Right: 'react', '@babel/core'. Wrong: 'React', 'React.js'. python: exact PyPI project name. Right: 'pandas', 'requests'. Wrong: 'Pandas'. steam: game display name in plain English, not a Steam App ID. Right: 'Elden Ring', 'CS2'. First Steam store search result wins, so use an unambiguous name. app downloads and app rankings: Android bundle ID only (the id= value on Google Play). Right: 'com.openai.chatgpt', 'com.whatsapp'. Wrong: 'ChatGPT', 'WhatsApp', an iOS App Store ID, or a bundle ID that is not Android. Find it at play.google.com/store/apps/details?id=THIS\_PART. | — |
| `source` | string | Yes | — | Exactly one source per request. Valid: 'google search', 'google images', 'google news', 'google shopping', 'youtube', 'wikipedia', 'tiktok', 'reddit', 'amazon', 'news sentiment', 'news volume', 'npm', 'python', 'steam', 'app downloads', 'app rankings'. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "description": "What to look up. The string format is required by source. Standard sources (google search, google images, google news, google shopping, youtube, wikipedia, tiktok, reddit, amazon, news sentiment, news volume): any name or phrase, e.g. 'tesla'. npm: exact npmjs.com package name, case-sensitive. Right: 'react', '@babel/core'. Wrong: 'React', 'React.js'. python: exact PyPI project name. Right: 'pandas', 'requests'. Wrong: 'Pandas'. steam: game display name in plain English, not a Steam App ID. Right: 'Elden Ring', 'CS2'. First Steam store search result wins, so use an unambiguous name. app downloads and app rankings: Android bundle ID only (the id= value on Google Play). Right: 'com.openai.chatgpt', 'com.whatsapp'. Wrong: 'ChatGPT', 'WhatsApp', an iOS App Store ID, or a bundle ID that is not Android. Find it at play.google.com/store/apps/details?id=THIS_PART.",
      "title": "Keyword",
      "type": "string"
    },
    "source": {
      "description": "Exactly one source per request. Valid: 'google search', 'google images', 'google news', 'google shopping', 'youtube', 'wikipedia', 'tiktok', 'reddit', 'amazon', 'news sentiment', 'news volume', 'npm', 'python', 'steam', 'app downloads', 'app rankings'.",
      "title": "Source",
      "type": "string"
    }
  },
  "required": [
    "keyword",
    "source"
  ],
  "title": "get_time_seriesArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Local adapter validates parameter types via FastMCP/Pydantic; source/type values and keyword format requirements appear only in descriptions, without enum/pattern schema constraints or local validation.
- Actual upstream data retrieval and validation are not public in this repository and were not exercised. All calls require TRENDSMCP\_API\_KEY; local tools/list does not.
- No additionalProperties constraint is specified in the generated input schema.
- Exactly one source is a descriptive requirement, not a local enforced constraint. data\_mode is REST-only in public docs and is not a registered MCP input.

Sources: [src/trends\_mcp\_server/server.py:158](https://github.com/trendsmcp-ai/google-trends-mcp/blob/a136fa9d5a2552dc0f67a8e6b6297f027eacb7d2/src/trends_mcp_server/server.py) · [src/trends\_mcp\_server/server.py:36](https://github.com/trendsmcp-ai/google-trends-mcp/blob/a136fa9d5a2552dc0f67a8e6b6297f027eacb7d2/src/trends_mcp_server/server.py) · [src/trends\_mcp\_server/server.py:74](https://github.com/trendsmcp-ai/google-trends-mcp/blob/a136fa9d5a2552dc0f67a8e6b6297f027eacb7d2/src/trends_mcp_server/server.py)

<a id="tool-get-top-trends"></a>

### `get_top_trends`

Forwards one type with limit, offset, sort and window as mode=get\_top\_trends to the hosted REST API; includes category only when truthy, then JSON-serializes the response. Google Trends and Google Trends by Category are supported along with news and other platform boards.

<details>
<summary>Full registered description</summary>

```text
Live top-trending board for exactly one feed type. No keyword. For 'Amazon Best Sellers by Category', 'Google Trends by Category', 'Top Websites', and 'Substack by Category', always pass category. Default sort is current rank. Use sort='rank_change' for climbers vs a prior snapshot (window 1d, 3d, 7d, 14d, or 30d). App Store Top Free, App Store Top Paid, and Google Play are live store boards, not keyword lookups. For an app's history use get_growth or get_time_series with source app downloads or app rankings and an Android bundle ID. Do not use get_time_series for live boards. If the request is rate limited or the monthly quota is used up, tell the user their plan limit is reached.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `type` | string | Yes | — | Exactly one live feed. Valid: 'Amazon Best Sellers Top Rated', 'Amazon Best Sellers by Category', 'App Store Top Free', 'App Store Top Paid', 'GitHub', 'Google News Top News', 'Google Play', 'Google Trends', 'Google Trends by Category', 'IMDb MOVIEmeter', 'Open Library Trending Books', 'Reddit Hot Posts', 'Reddit World News', 'Top Websites', 'Spotify Top Podcasts', 'Steam Most Played', 'Substack', 'Substack by Category', 'TikTok Trending Hashtags', 'TikTok Trending Searches', 'Wikipedia Trending', 'X (Twitter) Trending', 'YouTube Trending'. | — |
| `category` | string / null | No | `null` | Pass this whenever type is 'Amazon Best Sellers by Category', 'Google Trends by Category', 'Top Websites', or 'Substack by Category'. Use the official name. Without it those feeds mix every board. Only omit on a first pull to learn the official names. | — |
| `limit` | integer | No | `25` | Max rows to return. Default 25, min 1, max 200. | — |
| `offset` | integer | No | `0` | Rows to skip for pagination. Default 0. | — |
| `sort` | string | No | `"rank"` | How to rank the board. 'rank' (default): current leaders. 'rank\_change': biggest climbers vs a prior snapshot. Mover rows include rank, keyword, prev\_rank, and rank\_change. | — |
| `window` | string | No | `"30d"` | Lookback used only when sort is 'rank\_change'. One of '1d', '3d', '7d', '14d', '30d'. Default '30d'. Short windows only work on daily feeds; weekly and monthly feeds return a note pointing to a longer window. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "type": {
      "description": "Exactly one live feed. Valid: 'Amazon Best Sellers Top Rated', 'Amazon Best Sellers by Category', 'App Store Top Free', 'App Store Top Paid', 'GitHub', 'Google News Top News', 'Google Play', 'Google Trends', 'Google Trends by Category', 'IMDb MOVIEmeter', 'Open Library Trending Books', 'Reddit Hot Posts', 'Reddit World News', 'Top Websites', 'Spotify Top Podcasts', 'Steam Most Played', 'Substack', 'Substack by Category', 'TikTok Trending Hashtags', 'TikTok Trending Searches', 'Wikipedia Trending', 'X (Twitter) Trending', 'YouTube Trending'.",
      "title": "Type",
      "type": "string"
    },
    "category": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Pass this whenever type is 'Amazon Best Sellers by Category', 'Google Trends by Category', 'Top Websites', or 'Substack by Category'. Use the official name. Without it those feeds mix every board. Only omit on a first pull to learn the official names.",
      "title": "Category"
    },
    "limit": {
      "default": 25,
      "description": "Max rows to return. Default 25, min 1, max 200.",
      "title": "Limit",
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Rows to skip for pagination. Default 0.",
      "title": "Offset",
      "type": "integer"
    },
    "sort": {
      "default": "rank",
      "description": "How to rank the board. 'rank' (default): current leaders. 'rank_change': biggest climbers vs a prior snapshot. Mover rows include rank, keyword, prev_rank, and rank_change.",
      "title": "Sort",
      "type": "string"
    },
    "window": {
      "default": "30d",
      "description": "Lookback used only when sort is 'rank_change'. One of '1d', '3d', '7d', '14d', '30d'. Default '30d'. Short windows only work on daily feeds; weekly and monthly feeds return a note pointing to a longer window.",
      "title": "Window",
      "type": "string"
    }
  },
  "required": [
    "type"
  ],
  "title": "get_top_trendsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Local adapter validates parameter types via FastMCP/Pydantic; source/type values and keyword format requirements appear only in descriptions, without enum/pattern schema constraints or local validation.
- Actual upstream data retrieval and validation are not public in this repository and were not exercised. All calls require TRENDSMCP\_API\_KEY; local tools/list does not.
- No additionalProperties constraint is specified in the generated input schema.
- limit has no minimum/maximum schema constraints despite description saying min 1/max 200. offset has no minimum. sort/window/type have no enum. category is optional nullable, and no conditional-required schema exists; empty strings/null are omitted from forwarded body.

Sources: [src/trends\_mcp\_server/server.py:177](https://github.com/trendsmcp-ai/google-trends-mcp/blob/a136fa9d5a2552dc0f67a8e6b6297f027eacb7d2/src/trends_mcp_server/server.py) · [src/trends\_mcp\_server/server.py:36](https://github.com/trendsmcp-ai/google-trends-mcp/blob/a136fa9d5a2552dc0f67a8e6b6297f027eacb7d2/src/trends_mcp_server/server.py) · [src/trends\_mcp\_server/server.py:74](https://github.com/trendsmcp-ai/google-trends-mcp/blob/a136fa9d5a2552dc0f67a8e6b6297f027eacb7d2/src/trends_mcp_server/server.py)

## Schema provenance

Imported src/trends_mcp_server/server.py and called await mcp.list_tools() locally without invoking any tools. Raw result saved to sources/trendsmcp-ai-google-trends-mcp/local-tools-list.json; mcp 1.30.0 and Pydantic 2.13.5. Inspected all registration/forwarder code plus server.json, README and anonymous public provider documentation.

- The repository contains only a stdio REST adapter, not hosted MCP server code. Hosted tools/list was not requested; no remote tool calls or credential access occurred. The statement that definitions mirror hosted MCP is therefore unverified.
- Dependencies are version ranges without a lockfile; schema output reflects installed mcp 1.30.0 / Pydantic 2.13.5.
- Public hosted docs describe all three names and REST/MCP distinctions but do not supply a full registered hosted inputSchema or verbatim hosted descriptions. No hosted definition is inferred or merged into verified local tools.
- Tools are multi-domain multiplexers. The single domain field is google-trends because every tool supports Google Trends; they also support news and other platform data.
