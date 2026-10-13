# ducnhd/google-data-mcp

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/ducnhd/google-data-mcp) · [JSON definitions](../../data/mcp/ducnhd-google-data-mcp.json)

Reviewed 2026-10-13 at commit [`b9328ccd8d5e`](https://github.com/ducnhd/google-data-mcp/tree/b9328ccd8d5e637175fcd71cc1122249123d0e71).

Fetch keyword interest or joint comparisons, plus current trending searches.

**7 tool definitions; 3 marked Google Trends.**

## Tools

| Tool | Scope |
|---|---|
| [`google_trends_interest`](#tool-google-trends-interest) | google-trends |
| [`google_trends_compare`](#tool-google-trends-compare) | google-trends |
| [`google_trends_trending`](#tool-google-trends-trending) | google-trends |
| [`youtube_listing`](#tool-youtube-listing) | other |
| [`google_ads_advertisers`](#tool-google-ads-advertisers) | ads |
| [`google_ads_creatives`](#tool-google-ads-creatives) | ads |
| [`google_play_reviews`](#tool-google-play-reviews) | other |

<a id="tool-google-trends-interest"></a>

### `google_trends_interest`

Google Trends interest over time for ONE keyword. Values are 0-100 relative WITHIN this single request, so they are not comparable to another call's numbers — use google\_trends\_compare when you need to rank terms against each other.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | A single search term. | — |
| `geo` | string | No | `""` | Country or sub-region code (US, VN, US-CA). Empty = worldwide. | — |
| `timeframe` | string | No | `"today 12-m"` | Google's own range string: 'today 12-m', 'today 5-y', 'now 7-d', 'all', or '2025-01-01 2025-12-31'. | — |

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
    "geo": {
      "default": "",
      "description": "Country or sub-region code (US, VN, US-CA). Empty = worldwide.",
      "title": "Geo",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Google's own range string: 'today 12-m', 'today 5-y', 'now 7-d', 'all', or '2025-01-01 2025-12-31'.",
      "title": "Timeframe",
      "type": "string"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "google_trends_interestArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema allows empty keyword; TrendsClient rejects an empty/whitespace-only keyword. geo/timeframe are unrestricted strings; listed formats are documentation only.

Sources: [src/google\_data\_mcp/server.py:50](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/server.py#L50-L94) · [src/google\_data\_mcp/trends.py:197](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/trends.py#L197-L256)

<a id="tool-google-trends-compare"></a>

### `google_trends_compare`

Compare up to 5 keywords in ONE Google Trends request, so their 0-100 values ARE normalised against each other and can be ranked. Google silently drops a 6th term, so 6+ is refused rather than answered with a term missing.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | 2 to 5 search terms. | — |
| `geo` | string | No | `""` | Country or sub-region code. Empty = worldwide. | — |
| `timeframe` | string | No | `"today 12-m"` | Google range string, e.g. 'today 12-m'. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keywords": {
      "description": "2 to 5 search terms.",
      "items": {
        "type": "string"
      },
      "title": "Keywords",
      "type": "array"
    },
    "geo": {
      "default": "",
      "description": "Country or sub-region code. Empty = worldwide.",
      "title": "Geo",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Google range string, e.g. 'today 12-m'.",
      "title": "Timeframe",
      "type": "string"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "google_trends_compareArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema has list[str] without minItems/maxItems. Implementation strips terms, discards empty values and requires 2–5 remaining terms. No uniqueness constraint; duplicate terms overwrite keys in output values. geo/timeframe are unrestricted strings.

Sources: [src/google\_data\_mcp/server.py:97](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/server.py#L97-L141) · [src/google\_data\_mcp/trends.py:197](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/trends.py#L197-L256)

<a id="tool-google-trends-trending"></a>

### `google_trends_trending`

What is trending on Google right now in one country. `searchVolume` is Google's own rounded bucket (100000, 1000000), not a precise count.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string | No | `"US"` | Two-letter country code, e.g. US, VN, GB. | — |
| `limit` | integer | No | `25` | How many terms to return. | minimum: 1; maximum: 200 |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "geo": {
      "default": "US",
      "description": "Two-letter country code, e.g. US, VN, GB.",
      "title": "Geo",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "description": "How many terms to return.",
      "maximum": 200,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "google_trends_trendingArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- limit bounds 1–200 are schema constraints. geo has no country-code pattern or enum; two-letter code is documentary.

Sources: [src/google\_data\_mcp/server.py:144](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/server.py#L144-L163) · [src/google\_data\_mcp/trends.py:259](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/trends.py#L259-L293)

<a id="tool-youtube-listing"></a>

### `youtube_listing`

List videos from YouTube: a channel's Shorts tab, a channel's videos tab, or search results. Returns videoId, title, view count, and (for videos/search) a publish date. Transcripts are NOT available from this server — Google gates them behind a token this server cannot mint.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `target` | string | Yes | — | A channel (@handle, UC… id or URL) for 'shorts'/'videos'; a search query for 'search'. | — |
| `kind` | string | No | `"videos"` | Which listing to read. | enum: ["shorts", "videos", "search"] |
| `limit` | integer | No | `30` | Maximum rows. Pagination stops early if the listing runs out. | minimum: 1; maximum: 300 |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "target": {
      "description": "A channel (@handle, UC… id or URL) for 'shorts'/'videos'; a search query for 'search'.",
      "title": "Target",
      "type": "string"
    },
    "kind": {
      "default": "videos",
      "description": "Which listing to read.",
      "enum": [
        "shorts",
        "videos",
        "search"
      ],
      "title": "Kind",
      "type": "string"
    },
    "limit": {
      "default": 30,
      "description": "Maximum rows. Pagination stops early if the listing runs out.",
      "maximum": 300,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "target"
  ],
  "title": "youtube_listingArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- kind enum and limit 1–300 are schema constraints. For channel listings, whitespace-only target raises empty channel; no schema minLength/pattern.

Sources: [src/google\_data\_mcp/server.py:167](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/server.py#L167-L211) · [src/google\_data\_mcp/youtube.py:99](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/youtube.py#L99-L269)

<a id="tool-google-ads-advertisers"></a>

### `google_ads_advertisers`

Find advertisers in Google's Ads Transparency Center by name. Returns each advertiser's id, country and Google's declared ad count — pass the id to google\_ads\_creatives.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Advertiser or brand name to search. | — |
| `limit` | integer | No | `10` | How many matches to return. | minimum: 1; maximum: 20 |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "description": "Advertiser or brand name to search.",
      "title": "Keyword",
      "type": "string"
    },
    "limit": {
      "default": 10,
      "description": "How many matches to return.",
      "maximum": 20,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "google_ads_advertisersArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- limit 1–20 is a schema constraint. keyword has no minLength and is not explicitly validated.

Sources: [src/google\_data\_mcp/server.py:215](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/server.py#L215-L233) · [src/google\_data\_mcp/ads.py:171](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/ads.py#L171-L201)

<a id="tool-google-ads-creatives"></a>

### `google_ads_creatives`

Every ad an advertiser is currently running, from Google's Ads Transparency Center: creative id, format, preview URL and first/last shown dates. An advertiser with zero ads is a real answer — Google keeps advertisers whose ads have stopped running.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `advertiser` | string | Yes | — | An AR… advertiser id, or a Transparency Center URL containing one. | — |
| `limit` | integer | No | `40` | Maximum ads to return. | minimum: 1; maximum: 300 |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "advertiser": {
      "description": "An AR… advertiser id, or a Transparency Center URL containing one.",
      "title": "Advertiser",
      "type": "string"
    },
    "limit": {
      "default": 40,
      "description": "Maximum ads to return.",
      "maximum": 300,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "advertiser"
  ],
  "title": "google_ads_creativesArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- limit 1–300 is a schema constraint. Implementation requires AR followed by digits, either alone or as a slash-separated URL component after replacing ? and & with /. No input-schema pattern.

Sources: [src/google\_data\_mcp/server.py:236](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/server.py#L236-L272) · [src/google\_data\_mcp/ads.py:71](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/ads.py#L71-L82)

<a id="tool-google-play-reviews"></a>

### `google_play_reviews`

Reviews for an Android app: rating, text, date, app version, thumbs-up and the developer's reply. Reviewer names and avatars are omitted unless you ask for them. Note each language/country returns a DIFFERENT set of reviews, so vary hl/gl to widen coverage.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `app_id` | string | Yes | — | Android package name, e.g. com.spotify.music. | — |
| `limit` | integer | No | `60` | Maximum reviews. | minimum: 1; maximum: 400 |
| `sort` | string | No | `"relevant"` | Google's own ordering. | enum: ["relevant", "newest"] |
| `hl` | string | No | `"en"` | Language code. Each language returns a different set of reviews. | — |
| `gl` | string | No | `"US"` | Country code. | — |
| `include_author` | boolean | No | `false` | Include the reviewer's display name. Off by default: it is personal data and rarely needed for product or ASO analysis. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "app_id": {
      "description": "Android package name, e.g. com.spotify.music.",
      "title": "App Id",
      "type": "string"
    },
    "limit": {
      "default": 60,
      "description": "Maximum reviews.",
      "maximum": 400,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    },
    "sort": {
      "default": "relevant",
      "description": "Google's own ordering.",
      "enum": [
        "relevant",
        "newest"
      ],
      "title": "Sort",
      "type": "string"
    },
    "hl": {
      "default": "en",
      "description": "Language code. Each language returns a different set of reviews.",
      "title": "Hl",
      "type": "string"
    },
    "gl": {
      "default": "US",
      "description": "Country code.",
      "title": "Gl",
      "type": "string"
    },
    "include_author": {
      "default": false,
      "description": "Include the reviewer's display name. Off by default: it is personal data and rarely needed for product or ASO analysis.",
      "title": "Include Author",
      "type": "boolean"
    }
  },
  "required": [
    "app_id"
  ],
  "title": "google_play_reviewsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- sort enum and limit 1–400 are schema constraints. app\_id/hl/gl have no schema format, pattern or enum. include\_author only adds display name; avatars and account IDs remain omitted.

Sources: [src/google\_data\_mcp/server.py:276](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/server.py#L276-L325) · [src/google\_data\_mcp/play.py:156](https://github.com/ducnhd/google-data-mcp/blob/b9328ccd8d5e637175fcd71cc1122249123d0e71/src/google_data_mcp/play.py#L156-L219)

## Schema provenance

Imported actual src/google_data_mcp/server.py and awaited MCPServer.list_tools() locally with mcp 2.3.0 and Pydantic 2.14.1 in an isolated source-local venv; inspected every registration and backing implementation. No tool invocation or Google network request.

- Runtime dependencies are unpinned (mcp>=2.0); recorded schemas reflect mcp 2.3.0/Pydantic 2.14.1. External Google endpoint functionality was not tested.
