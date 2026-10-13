# AKzar1el/mcp-trendpulse

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/AKzar1el/mcp-trendpulse) · [JSON definitions](../../data/mcp/akzar1el-mcp-trendpulse.json)

Reviewed 2026-10-13 at commit [`e9d7788938ac`](https://github.com/AKzar1el/mcp-trendpulse/tree/e9d7788938ac43bb591871c1929a81aa16a38f93).

Explore keyword growth, related queries, topic IDs, regional interest, and hosted SEO opportunity research.

**22 tool definitions; 16 marked Google Trends.**

Tool sets from different server surfaces are listed separately.

- Community and hosted registrations are separate server surfaces: 16 community tools and 6 hosted tools.

## Tools

| Tool | Scope | Surface |
|---|---|---|
| [`get_news_by_keyword`](#tool-community-get-news-by-keyword) | news | community |
| [`get_news_by_location`](#tool-community-get-news-by-location) | news | community |
| [`get_news_by_topic`](#tool-community-get-news-by-topic) | news | community |
| [`get_top_news`](#tool-community-get-top-news) | news | community |
| [`get_trending_terms`](#tool-community-get-trending-terms) | google-trends | community |
| [`get_trends`](#tool-community-get-trends) | google-trends | community |
| [`get_growth`](#tool-community-get-growth) | google-trends | community |
| [`get_ranked_trends`](#tool-community-get-ranked-trends) | google-trends | community |
| [`get_top_trends`](#tool-community-get-top-trends) | google-trends | community |
| [`get_news_by_site`](#tool-community-get-news-by-site) | news | community |
| [`get_article_content`](#tool-community-get-article-content) | news | community |
| [`get_interest_by_region`](#tool-community-get-interest-by-region) | google-trends | community |
| [`get_related_queries`](#tool-community-get-related-queries) | google-trends | community |
| [`get_related_topics`](#tool-community-get-related-topics) | google-trends | community |
| [`get_suggestions`](#tool-community-get-suggestions) | google-trends | community |
| [`get_categories`](#tool-community-get-categories) | google-trends | community |
| [`discover_trends`](#tool-hosted-discover-trends) | google-trends | hosted |
| [`analyze_keyword_trend`](#tool-hosted-analyze-keyword-trend) | google-trends | hosted |
| [`compare_keyword_trends`](#tool-hosted-compare-keyword-trends) | google-trends | hosted |
| [`discover_related_demand`](#tool-hosted-discover-related-demand) | google-trends | hosted |
| [`get_trend_context`](#tool-hosted-get-trend-context) | google-trends | hosted |
| [`find_seo_opportunities`](#tool-hosted-find-seo-opportunities) | google-trends | hosted |

<a id="tool-community-get-news-by-keyword"></a>

### `get_news_by_keyword` (community)

Find recent Google News articles for a free-form keyword or phrase. Use this for ad-hoc subject searches; use get\_news\_by\_topic for a predefined topic category or get\_news\_by\_site for one publisher.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Search term to find articles. | minLength: 1; pattern: ".*\\S.*" |
| `period` | integer | No | `7` | Number of days to look back for articles. | minimum: 1 |
| `max_results` | integer | No | `10` | Maximum number of results to return. | minimum: 1 |
| `full_data` | boolean | No | `false` | Return full data for each article. If False a summary should be created by setting the summarize flag | — |
| `summarize` | boolean | No | `true` | Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keyword": {
      "description": "Search term to find articles.",
      "minLength": 1,
      "pattern": ".*\\S.*",
      "type": "string"
    },
    "period": {
      "default": 7,
      "description": "Number of days to look back for articles.",
      "minimum": 1,
      "type": "integer"
    },
    "max_results": {
      "default": 10,
      "description": "Maximum number of results to return.",
      "minimum": 1,
      "type": "integer"
    },
    "full_data": {
      "default": false,
      "description": "Return full data for each article. If False a summary should be created by setting the summarize flag",
      "type": "boolean"
    },
    "summarize": {
      "default": true,
      "description": "Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp",
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

Sources: [src/mcp\_trendpulse/server.py:333](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L333-L382) · [src/mcp\_trendpulse/news.py:755](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L755-L776)

<a id="tool-community-get-news-by-location"></a>

### `get_news_by_location` (community)

Find recent Google News articles about a place-focused location such as a city, state, or country. Use this when geography is the primary filter; use get\_news\_by\_keyword for general subject searches.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `location` | string | Yes | — | Name of city/state/country. | minLength: 1; pattern: ".*\\S.*" |
| `period` | integer | No | `7` | Number of days to look back for articles. | minimum: 1 |
| `max_results` | integer | No | `10` | Maximum number of results to return. | minimum: 1 |
| `full_data` | boolean | No | `false` | Return full data for each article. If False a summary should be created by setting the summarize flag | — |
| `summarize` | boolean | No | `true` | Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "location": {
      "description": "Name of city/state/country.",
      "minLength": 1,
      "pattern": ".*\\S.*",
      "type": "string"
    },
    "period": {
      "default": 7,
      "description": "Number of days to look back for articles.",
      "minimum": 1,
      "type": "integer"
    },
    "max_results": {
      "default": 10,
      "description": "Maximum number of results to return.",
      "minimum": 1,
      "type": "integer"
    },
    "full_data": {
      "default": false,
      "description": "Return full data for each article. If False a summary should be created by setting the summarize flag",
      "type": "boolean"
    },
    "summarize": {
      "default": true,
      "description": "Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp",
      "type": "boolean"
    }
  },
  "required": [
    "location"
  ],
  "type": "object"
}
```

</details>

Sources: [src/mcp\_trendpulse/server.py:385](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L385-L434) · [src/mcp\_trendpulse/news.py:801](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L801-L827)

<a id="tool-community-get-news-by-topic"></a>

### `get_news_by_topic` (community)

Find recent Google News articles from a predefined Google News topic category. Use this for topic category browsing such as BUSINESS, TECHNOLOGY, or SPORTS; use get\_news\_by\_keyword for a free-form query.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `topic` | string | Yes | — | Topic to search for articles. | minLength: 1; pattern: ".*\\S.*" |
| `period` | integer | No | `7` | Number of days to look back for articles. | minimum: 1 |
| `max_results` | integer | No | `10` | Maximum number of results to return. | minimum: 1 |
| `full_data` | boolean | No | `false` | Return full data for each article. If False a summary should be created by setting the summarize flag | — |
| `summarize` | boolean | No | `true` | Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "topic": {
      "description": "Topic to search for articles.",
      "minLength": 1,
      "pattern": ".*\\S.*",
      "type": "string"
    },
    "period": {
      "default": 7,
      "description": "Number of days to look back for articles.",
      "minimum": 1,
      "type": "integer"
    },
    "max_results": {
      "default": 10,
      "description": "Maximum number of results to return.",
      "minimum": 1,
      "type": "integer"
    },
    "full_data": {
      "default": false,
      "description": "Return full data for each article. If False a summary should be created by setting the summarize flag",
      "type": "boolean"
    },
    "summarize": {
      "default": true,
      "description": "Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp",
      "type": "boolean"
    }
  },
  "required": [
    "topic"
  ],
  "type": "object"
}
```

</details>

Sources: [src/mcp\_trendpulse/server.py:437](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L437-L486) · [src/mcp\_trendpulse/news.py:830](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L830-L861)

<a id="tool-community-get-top-news"></a>

### `get_top_news` (community)

Return general headline and top-news stories from Google News without a keyword or topic seed. Use this for a broad news snapshot; use the keyword, location, topic, or site tools when the user gives a filter.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `period` | integer | No | `3` | Number of days to look back for top articles. | minimum: 1 |
| `max_results` | integer | No | `10` | Maximum number of results to return. | minimum: 1 |
| `full_data` | boolean | No | `false` | Return full data for each article. If False a summary should be created by setting the summarize flag | — |
| `summarize` | boolean | No | `true` | Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "period": {
      "default": 3,
      "description": "Number of days to look back for top articles.",
      "minimum": 1,
      "type": "integer"
    },
    "max_results": {
      "default": 10,
      "description": "Maximum number of results to return.",
      "minimum": 1,
      "type": "integer"
    },
    "full_data": {
      "default": false,
      "description": "Return full data for each article. If False a summary should be created by setting the summarize flag",
      "type": "boolean"
    },
    "summarize": {
      "default": true,
      "description": "Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

</details>

Sources: [src/mcp\_trendpulse/server.py:489](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L489-L536) · [src/mcp\_trendpulse/news.py:779](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L779-L798)

<a id="tool-community-get-trending-terms"></a>

### `get_trending_terms` (community)

Return terms that are trending now for a geography, optionally with related news metadata. Use this for current trend discovery; use get\_trends when the user wants historical interest over time for known keywords.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string | No | `"US"` | Geographic target for trending terms. Supports four levels of granularity:<br>- Worldwide: empty string ''<br>- Country: ISO 3166-1 alpha-2 code, e.g. 'US', 'GB', 'CA'<br>- Subdivision (state/province/region): ISO 3166-2 format 'CC-XX' or 'CC-XXX', e.g. 'US-CA' (California), 'BE-BRU' (Brussels)<br>- US metro area: bare Nielsen DMA code (numeric string), e.g. '807' (San Francisco Bay Area), '501' (New York City) | — |
| `full_data` | boolean | No | `false` | Return full data for each trend including related news stories. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "geo": {
      "default": "US",
      "description": "Geographic target for trending terms. Supports four levels of granularity:\n- Worldwide: empty string ''\n- Country: ISO 3166-1 alpha-2 code, e.g. 'US', 'GB', 'CA'\n- Subdivision (state/province/region): ISO 3166-2 format 'CC-XX' or 'CC-XXX', e.g. 'US-CA' (California), 'BE-BRU' (Brussels)\n- US metro area: bare Nielsen DMA code (numeric string), e.g. '807' (San Francisco Bay Area), '501' (New York City)",
      "type": "string"
    },
    "full_data": {
      "default": false,
      "description": "Return full data for each trend including related news stories.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

</details>

Sources: [src/mcp\_trendpulse/server.py:539](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L539-L577) · [src/mcp\_trendpulse/news.py:872](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L872-L891)

<a id="tool-community-get-trends"></a>

### `get_trends` (community)

Return historical Google Trends interest-over-time points for one or more known keywords. Use this for trajectory and comparisons across a timeframe; values are normalized 0-100 interest scores, not absolute search volume. Use get\_trending\_terms for what is trending now.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string / array of string | Yes | — | Search keyword(s) to analyze; comparison lists support 1-5 keywords. | — |
| `source` | string | No | `"google search"` | Search source. | enum: ["google search", "youtube search", "news search", "image search", "google shopping"] |
| `data_mode` | string | No | `"weekly"` | Legacy resolution hint used only when timeframe is omitted. | enum: ["weekly", "daily", "monthly"] |
| `geo` | string | No | `"US"` | Geographic region code (e.g. 'US'). | — |
| `timeframe` | string / null | No | `null` | Explicit TrendsPy range, for example 'today 12-m', 'today 90-d', 'all', or 'YYYY-MM-DD YYYY-MM-DD'. Overrides data\_mode when supplied. | — |
| `cat` | integer | No | `0` | Google Trends category ID; use 0 for all categories or a value from get\_categories. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keyword": {
      "anyOf": [
        {
          "minLength": 1,
          "type": "string"
        },
        {
          "items": {
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 5,
          "minItems": 1,
          "type": "array"
        }
      ],
      "description": "Search keyword(s) to analyze; comparison lists support 1-5 keywords."
    },
    "source": {
      "default": "google search",
      "description": "Search source.",
      "enum": [
        "google search",
        "youtube search",
        "news search",
        "image search",
        "google shopping"
      ],
      "type": "string"
    },
    "data_mode": {
      "default": "weekly",
      "description": "Legacy resolution hint used only when timeframe is omitted.",
      "enum": [
        "weekly",
        "daily",
        "monthly"
      ],
      "type": "string"
    },
    "geo": {
      "default": "US",
      "description": "Geographic region code (e.g. 'US').",
      "type": "string"
    },
    "timeframe": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Explicit TrendsPy range, for example 'today 12-m', 'today 90-d', 'all', or 'YYYY-MM-DD YYYY-MM-DD'. Overrides data_mode when supplied."
    },
    "cat": {
      "default": 0,
      "description": "Google Trends category ID; use 0 for all categories or a value from get_categories.",
      "type": "integer"
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

- Implementation strips keyword whitespace, rejects empty terms and duplicate normalized keywords, and requires 1-5 comparison keywords; hosted comparison schema requires 2-5. These normalization/uniqueness checks are not encoded as uniqueItems in the input schema.
- Omitted/null timeframe maps weekly to today 5-y, daily to today 3-m, monthly to all; explicit timeframe passes through to TrendsPy.

Sources: [src/mcp\_trendpulse/server.py:580](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L580-L605) · [src/mcp\_trendpulse/news.py:1095](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L1095-L1138)

<a id="tool-community-get-growth"></a>

### `get_growth` (community)

Estimate momentum for one or more known keywords across requested growth windows. Use this when percentage growth is the goal; use get\_trends when the user needs the underlying historical time series.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string / array of string | Yes | — | Search keyword(s) to analyze; comparison lists support 1-5 keywords. | — |
| `source` | string | No | `"google search"` | Search source. | enum: ["google search", "youtube search", "news search", "image search", "google shopping"] |
| `percent_growth` | array of string / null | No | `null` | Timeframes to calculate growth (e.g. ['3M', '1Y']). | — |
| `geo` | string | No | `"US"` | Geographic region code (e.g. 'US'). | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keyword": {
      "anyOf": [
        {
          "minLength": 1,
          "type": "string"
        },
        {
          "items": {
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 5,
          "minItems": 1,
          "type": "array"
        }
      ],
      "description": "Search keyword(s) to analyze; comparison lists support 1-5 keywords."
    },
    "source": {
      "default": "google search",
      "description": "Search source.",
      "enum": [
        "google search",
        "youtube search",
        "news search",
        "image search",
        "google shopping"
      ],
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
      "description": "Timeframes to calculate growth (e.g. ['3M', '1Y'])."
    },
    "geo": {
      "default": "US",
      "description": "Geographic region code (e.g. 'US').",
      "type": "string"
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

- Implementation strips keyword whitespace, rejects empty terms and duplicate normalized keywords, and requires 1-5 comparison keywords; hosted comparison schema requires 2-5. These normalization/uniqueness checks are not encoded as uniqueItems in the input schema.
- Null percent\_growth becomes [3M,1Y]. Each supplied string is trimmed/uppercased and must match positive integer plus D/W/M/Y; this pattern is implementation validation, not an input-schema pattern.

Sources: [src/mcp\_trendpulse/server.py:608](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L608-L628) · [src/mcp\_trendpulse/news.py:1141](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L1141-L1170)

<a id="tool-community-get-ranked-trends"></a>

### `get_ranked_trends` (community)

Return currently trending keywords ranked by week-over-week growth or volume. Use this when explicit ranked order matters; use get\_top\_trends for a simpler current feed and get\_trends for historical series.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `source` | string | No | `"google search"` | Search source. | const: "google search" |
| `sort` | string | No | `"wow_pct_change"` | Field to sort by. | enum: ["wow_pct_change", "volume"] |
| `limit` | integer | No | `20` | Maximum number of trends to return. | minimum: 1 |
| `geo` | string | No | `"US"` | Geographic region code (e.g. 'US'). | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "source": {
      "const": "google search",
      "default": "google search",
      "description": "Search source.",
      "type": "string"
    },
    "sort": {
      "default": "wow_pct_change",
      "description": "Field to sort by.",
      "enum": [
        "wow_pct_change",
        "volume"
      ],
      "type": "string"
    },
    "limit": {
      "default": 20,
      "description": "Maximum number of trends to return.",
      "minimum": 1,
      "type": "integer"
    },
    "geo": {
      "default": "US",
      "description": "Geographic region code (e.g. 'US').",
      "type": "string"
    }
  },
  "type": "object"
}
```

</details>

Implementation notes:

- wow\_pct\_change naming/description does not compute a separate weekly baseline here; it sorts the current provider volume\_growth\_pct from a 24-hour feed.

Sources: [src/mcp\_trendpulse/server.py:631](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L631-L654) · [src/mcp\_trendpulse/news.py:1173](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L1173-L1236)

<a id="tool-community-get-top-trends"></a>

### `get_top_trends` (community)

Return a bounded current topic discovery feed from Google Trends RSS, including related news where available. Use this for current top or daily trends; use get\_ranked\_trends when explicit ranking by growth or volume matters.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `type` | string | No | `"Google Trends"` | Type of trends feed. | enum: ["Google Trends", "Daily Trends"] |
| `limit` | integer | No | `20` | Maximum number of trends to return. | minimum: 1 |
| `geo` | string | No | `"US"` | Geographic region code (e.g. 'US'). | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "type": {
      "default": "Google Trends",
      "description": "Type of trends feed.",
      "enum": [
        "Google Trends",
        "Daily Trends"
      ],
      "type": "string"
    },
    "limit": {
      "default": 20,
      "description": "Maximum number of trends to return.",
      "minimum": 1,
      "type": "integer"
    },
    "geo": {
      "default": "US",
      "description": "Geographic region code (e.g. 'US').",
      "type": "string"
    }
  },
  "type": "object"
}
```

</details>

Implementation notes:

- Registered description mentions top or daily RSS; actual Daily Trends implementation calls trending\_now(hours=24), whereas Google Trends calls trending\_now\_by\_rss.

Sources: [src/mcp\_trendpulse/server.py:657](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L657-L678) · [src/mcp\_trendpulse/news.py:1239](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L1239-L1296)

<a id="tool-community-get-news-by-site"></a>

### `get_news_by_site` (community)

Find recent Google News articles from one publisher domain. Use this when the user wants source-specific coverage; use get\_news\_by\_keyword for cross-publisher subject search.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `site` | string | Yes | — | Domain of the news site, e.g. 'cnn.com'. | minLength: 1; pattern: ".*\\S.*" |
| `period` | integer | No | `7` | Number of days to look back for articles. | minimum: 1 |
| `max_results` | integer | No | `10` | Maximum number of results to return. | minimum: 1 |
| `full_data` | boolean | No | `false` | Return full data for each article. If False a summary should be created by setting the summarize flag | — |
| `summarize` | boolean | No | `true` | Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "site": {
      "description": "Domain of the news site, e.g. 'cnn.com'.",
      "minLength": 1,
      "pattern": ".*\\S.*",
      "type": "string"
    },
    "period": {
      "default": 7,
      "description": "Number of days to look back for articles.",
      "minimum": 1,
      "type": "integer"
    },
    "max_results": {
      "default": 10,
      "description": "Maximum number of results to return.",
      "minimum": 1,
      "type": "integer"
    },
    "full_data": {
      "default": false,
      "description": "Return full data for each article. If False a summary should be created by setting the summarize flag",
      "type": "boolean"
    },
    "summarize": {
      "default": true,
      "description": "Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp",
      "type": "boolean"
    }
  },
  "required": [
    "site"
  ],
  "type": "object"
}
```

</details>

Sources: [src/mcp\_trendpulse/server.py:681](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L681-L730) · [src/mcp\_trendpulse/news.py:1299](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L1299-L1318)

<a id="tool-community-get-article-content"></a>

### `get_article_content` (community)

Download and parse one specific news article when you already have an article URL. Use it to retrieve article text or metadata or summarize that URL; do not use it for discovery - use the news search tools instead.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `url` | string | Yes | — | The URL of the news article to download and parse. | — |
| `full_data` | boolean | No | `false` | Return full data for the article. If False a summary should be created by setting the summarize flag | — |
| `summarize` | boolean | No | `true` | Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "url": {
      "description": "The URL of the news article to download and parse.",
      "type": "string"
    },
    "full_data": {
      "default": false,
      "description": "Return full data for the article. If False a summary should be created by setting the summarize flag",
      "type": "boolean"
    },
    "summarize": {
      "default": true,
      "description": "Generate a summary of the article, will first try LLM Sampling but if unavailable will use nlp",
      "type": "boolean"
    }
  },
  "required": [
    "url"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Schema URL is an unrestricted string. Implementation rejects whitespace/control characters, non-HTTP(S), missing host, embedded credentials and invalid ports; downloader separately rejects nonpublic addresses and unsafe redirects.

Sources: [src/mcp\_trendpulse/server.py:733](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L733-L764)

<a id="tool-community-get-interest-by-region"></a>

### `get_interest_by_region` (community)

Return geographic Google Trends interest for one or more known keywords at country, region, city, or DMA resolution. Use this to compare where demand is strongest; use get\_trends for interest over time instead.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | string / array of string | Yes | — | Search keyword(s) to analyze. | — |
| `timeframe` | string | No | `"today 12-m"` | Timeframe for search volume analysis (e.g., 'today 12-m'). | — |
| `geo` | string | No | `"US"` | Geographic region code (e.g. 'US' or empty '' for worldwide). | — |
| `cat` | integer | No | `0` | Category ID (default: 0 for all). | — |
| `gprop` | string | No | `""` | Google property filter. | enum: ["", "youtube", "news", "images", "froogle"] |
| `resolution` | string | No | `"REGION"` | Geographic resolution. | enum: ["COUNTRY", "REGION", "CITY", "DMA"] |
| `inc_low_vol` | boolean | No | `false` | Include regions with low search volume. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keywords": {
      "anyOf": [
        {
          "minLength": 1,
          "type": "string"
        },
        {
          "items": {
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 5,
          "minItems": 1,
          "type": "array"
        }
      ],
      "description": "Search keyword(s) to analyze."
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Timeframe for search volume analysis (e.g., 'today 12-m').",
      "type": "string"
    },
    "geo": {
      "default": "US",
      "description": "Geographic region code (e.g. 'US' or empty '' for worldwide).",
      "type": "string"
    },
    "cat": {
      "default": 0,
      "description": "Category ID (default: 0 for all).",
      "type": "integer"
    },
    "gprop": {
      "default": "",
      "description": "Google property filter.",
      "enum": [
        "",
        "youtube",
        "news",
        "images",
        "froogle"
      ],
      "type": "string"
    },
    "resolution": {
      "default": "REGION",
      "description": "Geographic resolution.",
      "enum": [
        "COUNTRY",
        "REGION",
        "CITY",
        "DMA"
      ],
      "type": "string"
    },
    "inc_low_vol": {
      "default": false,
      "description": "Include regions with low search volume.",
      "type": "boolean"
    }
  },
  "required": [
    "keywords"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation strips keyword whitespace, rejects empty terms and duplicate normalized keywords, and requires 1-5 comparison keywords; hosted comparison schema requires 2-5. These normalization/uniqueness checks are not encoded as uniqueItems in the input schema.

Sources: [src/mcp\_trendpulse/server.py:767](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L767-L799) · [src/mcp\_trendpulse/news.py:1321](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L1321-L1366)

<a id="tool-community-get-related-queries"></a>

### `get_related_queries` (community)

Return top and rising literal search queries related to one seed keyword. Use this for query expansion; use get\_related\_topics for topic entities or get\_suggestions for autocomplete candidates.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Search keyword to analyze. | minLength: 1; pattern: ".*\\S.*" |
| `timeframe` | string | No | `"today 12-m"` | Timeframe for search volume analysis (e.g., 'today 12-m'). | — |
| `geo` | string | No | `"US"` | Geographic region code (e.g. 'US'). | — |
| `cat` | integer | No | `0` | Category ID (default: 0 for all). | — |
| `gprop` | string | No | `""` | Google property filter. | enum: ["", "youtube", "news", "images", "froogle"] |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keyword": {
      "description": "Search keyword to analyze.",
      "minLength": 1,
      "pattern": ".*\\S.*",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Timeframe for search volume analysis (e.g., 'today 12-m').",
      "type": "string"
    },
    "geo": {
      "default": "US",
      "description": "Geographic region code (e.g. 'US').",
      "type": "string"
    },
    "cat": {
      "default": 0,
      "description": "Category ID (default: 0 for all).",
      "type": "integer"
    },
    "gprop": {
      "default": "",
      "description": "Google property filter.",
      "enum": [
        "",
        "youtube",
        "news",
        "images",
        "froogle"
      ],
      "type": "string"
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

- Implementation trims the seed and rejects whitespace-only input through provider validation, in addition to registered string constraints.

Sources: [src/mcp\_trendpulse/server.py:802](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L802-L830) · [src/mcp\_trendpulse/news.py:1369](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L1369-L1400)

<a id="tool-community-get-related-topics"></a>

### `get_related_topics` (community)

Return top and rising Google Trends topic entities related to one seed keyword. Use this for entity or topic expansion; use get\_related\_queries for literal search queries.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Search keyword to analyze. | minLength: 1; pattern: ".*\\S.*" |
| `timeframe` | string | No | `"today 12-m"` | Timeframe for search volume analysis (e.g., 'today 12-m'). | — |
| `geo` | string | No | `"US"` | Geographic region code (e.g. 'US'). | — |
| `cat` | integer | No | `0` | Category ID (default: 0 for all). | — |
| `gprop` | string | No | `""` | Google property filter. | enum: ["", "youtube", "news", "images", "froogle"] |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keyword": {
      "description": "Search keyword to analyze.",
      "minLength": 1,
      "pattern": ".*\\S.*",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Timeframe for search volume analysis (e.g., 'today 12-m').",
      "type": "string"
    },
    "geo": {
      "default": "US",
      "description": "Geographic region code (e.g. 'US').",
      "type": "string"
    },
    "cat": {
      "default": 0,
      "description": "Category ID (default: 0 for all).",
      "type": "integer"
    },
    "gprop": {
      "default": "",
      "description": "Google property filter.",
      "enum": [
        "",
        "youtube",
        "news",
        "images",
        "froogle"
      ],
      "type": "string"
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

- Implementation trims the seed and rejects whitespace-only input through provider validation, in addition to registered string constraints.

Sources: [src/mcp\_trendpulse/server.py:833](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L833-L861) · [src/mcp\_trendpulse/news.py:1403](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L1403-L1436)

<a id="tool-community-get-suggestions"></a>

### `get_suggestions` (community)

Return Google Trends autocomplete suggestions for a seed keyword. Use this for lightweight autocomplete or entity candidates; use get\_related\_queries when you need top or rising demand signals.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Query string to autocomplete. | minLength: 1; pattern: ".*\\S.*" |
| `language` | string / null | No | `null` | Language code, e.g. 'en'. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keyword": {
      "description": "Query string to autocomplete.",
      "minLength": 1,
      "pattern": ".*\\S.*",
      "type": "string"
    },
    "language": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Language code, e.g. 'en'."
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

- Implementation trims the seed and rejects whitespace-only input through provider validation, in addition to registered string constraints.

Sources: [src/mcp\_trendpulse/server.py:864](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L864-L883) · [src/mcp\_trendpulse/news.py:1439](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L1439-L1456)

<a id="tool-community-get-categories"></a>

### `get_categories` (community)

Return a bounded page of Google Trends category IDs and names for use in the cat parameter of trend tools. Use query to find categories by name and offset/limit to page through broader results; do not guess category IDs.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `query` | string / null | No | `null` | Optional case-insensitive substring to match against category names. | — |
| `limit` | integer | No | `50` | Maximum categories to return in this page. | minimum: 1; maximum: 100 |
| `offset` | integer | No | `0` | Zero-based offset into the filtered category list. | minimum: 0 |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "query": {
      "anyOf": [
        {
          "minLength": 1,
          "pattern": ".*\\S.*",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional case-insensitive substring to match against category names."
    },
    "limit": {
      "default": 50,
      "description": "Maximum categories to return in this page.",
      "maximum": 100,
      "minimum": 1,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Zero-based offset into the filtered category list.",
      "minimum": 0,
      "type": "integer"
    }
  },
  "type": "object"
}
```

</details>

Sources: [src/mcp\_trendpulse/server.py:886](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/server.py#L886-L916) · [src/mcp\_trendpulse/news.py:1459](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/news.py#L1459-L1466)

<a id="tool-hosted-discover-trends"></a>

### `discover_trends` (hosted)

Discover broad, currently trending search topics in a geographic market. Use this when the user has no specific seed keyword yet and wants emerging topics ranked by growth or volume.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string | No | `"US"` | Geographic market, typically an ISO country code such as US, GB, or DE. | — |
| `sort_by` | string | No | `"growth"` | Rank by recent growth or current trend volume. | enum: ["growth", "volume"] |
| `limit` | integer | No | `10` | Maximum trends to return. | minimum: 1; maximum: 20 |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "geo": {
      "default": "US",
      "description": "Geographic market, typically an ISO country code such as US, GB, or DE.",
      "type": "string"
    },
    "sort_by": {
      "default": "growth",
      "description": "Rank by recent growth or current trend volume.",
      "enum": [
        "growth",
        "volume"
      ],
      "type": "string"
    },
    "limit": {
      "default": 10,
      "description": "Maximum trends to return.",
      "maximum": 20,
      "minimum": 1,
      "type": "integer"
    }
  },
  "type": "object"
}
```

</details>

Sources: [src/mcp\_trendpulse/hosted.py:394](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/hosted.py#L394-L442)

<a id="tool-hosted-analyze-keyword-trend"></a>

### `analyze_keyword_trend` (hosted)

Analyze one known keyword's Google Trends trajectory. Use this for direction, recent/average/peak normalized interest, growth windows, and a bounded time series; do not use it to compare multiple keywords.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Single keyword or topic phrase to analyze. | minLength: 1; maxLength: 200 |
| `geo` | string | No | `"US"` | Geographic market such as US or GB. | — |
| `source` | string | No | `"google search"` | Google Trends search property. | enum: ["google search", "youtube search", "news search", "image search", "google shopping"] |
| `timeframe` | string | No | `"today 12-m"` | Google Trends window such as 'today 12-m', 'today 90-d', 'today 5-y', or an exact date range. | — |
| `max_points` | integer | No | `60` | Maximum time-series points returned after deterministic downsampling. | minimum: 10; maximum: 120 |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keyword": {
      "description": "Single keyword or topic phrase to analyze.",
      "maxLength": 200,
      "minLength": 1,
      "type": "string"
    },
    "geo": {
      "default": "US",
      "description": "Geographic market such as US or GB.",
      "type": "string"
    },
    "source": {
      "default": "google search",
      "description": "Google Trends search property.",
      "enum": [
        "google search",
        "youtube search",
        "news search",
        "image search",
        "google shopping"
      ],
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Google Trends window such as 'today 12-m', 'today 90-d', 'today 5-y', or an exact date range.",
      "type": "string"
    },
    "max_points": {
      "default": 60,
      "description": "Maximum time-series points returned after deterministic downsampling.",
      "maximum": 120,
      "minimum": 10,
      "type": "integer"
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

- Implementation trims the seed and rejects whitespace-only input through provider validation, in addition to registered string constraints.

Sources: [src/mcp\_trendpulse/hosted.py:445](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/hosted.py#L445-L484)

<a id="tool-hosted-compare-keyword-trends"></a>

### `compare_keyword_trends` (hosted)

Compare 2-5 known keywords on the same Google Trends scale and window. Use this when relative momentum between alternatives matters; use analyze\_keyword\_trend for only one keyword.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | Two to five unique keywords to compare on one normalized Trends request. | minItems: 2; maxItems: 5 |
| `geo` | string | No | `"US"` | Geographic market such as US or GB. | — |
| `source` | string | No | `"google search"` | Google Trends search property. | enum: ["google search", "youtube search", "news search", "image search", "google shopping"] |
| `timeframe` | string | No | `"today 12-m"` | Google Trends window shared by all keywords. | — |
| `max_points_per_keyword` | integer | No | `40` | Maximum returned points for each keyword. | minimum: 10; maximum: 80 |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keywords": {
      "description": "Two to five unique keywords to compare on one normalized Trends request.",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 2,
      "type": "array"
    },
    "geo": {
      "default": "US",
      "description": "Geographic market such as US or GB.",
      "type": "string"
    },
    "source": {
      "default": "google search",
      "description": "Google Trends search property.",
      "enum": [
        "google search",
        "youtube search",
        "news search",
        "image search",
        "google shopping"
      ],
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Google Trends window shared by all keywords.",
      "type": "string"
    },
    "max_points_per_keyword": {
      "default": 40,
      "description": "Maximum returned points for each keyword.",
      "maximum": 80,
      "minimum": 10,
      "type": "integer"
    }
  },
  "required": [
    "keywords"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation strips keyword whitespace, rejects empty terms and duplicate normalized keywords, and requires 1-5 comparison keywords; hosted comparison schema requires 2-5. These normalization/uniqueness checks are not encoded as uniqueItems in the input schema.

Sources: [src/mcp\_trendpulse/hosted.py:487](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/hosted.py#L487-L533)

<a id="tool-hosted-discover-related-demand"></a>

### `discover_related_demand` (hosted)

Expand one seed keyword into related search demand. Use this for top/rising queries, related topics, and entity suggestions; it does not return a time-series analysis.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Seed keyword or topic phrase. | minLength: 1; maxLength: 200 |
| `geo` | string | No | `"US"` | Geographic market such as US or GB. | — |
| `source` | string | No | `"google search"` | Google Trends search property used for related-demand data. | enum: ["google search", "youtube search", "news search", "image search", "google shopping"] |
| `timeframe` | string | No | `"today 12-m"` | Google Trends window such as 'today 12-m'. | — |
| `limit` | integer | No | `10` | Maximum items returned in each related-demand section. | minimum: 1; maximum: 15 |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keyword": {
      "description": "Seed keyword or topic phrase.",
      "maxLength": 200,
      "minLength": 1,
      "type": "string"
    },
    "geo": {
      "default": "US",
      "description": "Geographic market such as US or GB.",
      "type": "string"
    },
    "source": {
      "default": "google search",
      "description": "Google Trends search property used for related-demand data.",
      "enum": [
        "google search",
        "youtube search",
        "news search",
        "image search",
        "google shopping"
      ],
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Google Trends window such as 'today 12-m'.",
      "type": "string"
    },
    "limit": {
      "default": 10,
      "description": "Maximum items returned in each related-demand section.",
      "maximum": 15,
      "minimum": 1,
      "type": "integer"
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

- Implementation trims the seed and rejects whitespace-only input through provider validation, in addition to registered string constraints.

Sources: [src/mcp\_trendpulse/hosted.py:536](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/hosted.py#L536-L578)

<a id="tool-hosted-get-trend-context"></a>

### `get_trend_context` (hosted)

Add current-news context to one keyword and return a compact recent trend snapshot. Use this when the user asks why a term may be moving now or wants sources to investigate; use analyze\_keyword\_trend for trend metrics without news.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Keyword or topic to contextualize. | minLength: 1; maxLength: 200 |
| `geo` | string | No | `"US"` | Geographic market for the trend snapshot. | — |
| `news_period_days` | integer | No | `7` | How many recent days of news to inspect. | minimum: 1; maximum: 30 |
| `max_articles` | integer | No | `5` | Maximum article links returned. | minimum: 1; maximum: 8 |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keyword": {
      "description": "Keyword or topic to contextualize.",
      "maxLength": 200,
      "minLength": 1,
      "type": "string"
    },
    "geo": {
      "default": "US",
      "description": "Geographic market for the trend snapshot.",
      "type": "string"
    },
    "news_period_days": {
      "default": 7,
      "description": "How many recent days of news to inspect.",
      "maximum": 30,
      "minimum": 1,
      "type": "integer"
    },
    "max_articles": {
      "default": 5,
      "description": "Maximum article links returned.",
      "maximum": 8,
      "minimum": 1,
      "type": "integer"
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

- Implementation trims the seed and rejects whitespace-only input through provider validation, in addition to registered string constraints.

Sources: [src/mcp\_trendpulse/hosted.py:581](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/hosted.py#L581-L621)

<a id="tool-hosted-find-seo-opportunities"></a>

### `find_seo_opportunities` (hosted)

Find trend-driven SEO keyword candidates from one seed. Use this for rising related queries that are checked against current Google Trends interest. If project\_id is supplied, annotate candidates with exact-query Search Console metrics for that authenticated DigestSEO project; without it results remain trend-only. Do not treat either signal as absolute search volume.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `seed_keyword` | string | Yes | — | Seed keyword defining the SEO topic space. | minLength: 1; maxLength: 200 |
| `geo` | string | No | `"US"` | Geographic market such as US or GB. | — |
| `source` | string | No | `"google search"` | Google Trends search property. | enum: ["google search", "youtube search", "news search", "image search", "google shopping"] |
| `timeframe` | string | No | `"today 12-m"` | Window used for related demand and trend validation. | — |
| `limit` | integer | No | `5` | Maximum validated opportunity candidates. Google Trends comparisons are capped at five keywords. | minimum: 1; maximum: 5 |
| `project_id` | string / null | No | `null` | Optional DigestSEO Site Audit project ID owned by the authenticated account. Enables a 28-day exact-query Search Console validation pass. | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "seed_keyword": {
      "description": "Seed keyword defining the SEO topic space.",
      "maxLength": 200,
      "minLength": 1,
      "type": "string"
    },
    "geo": {
      "default": "US",
      "description": "Geographic market such as US or GB.",
      "type": "string"
    },
    "source": {
      "default": "google search",
      "description": "Google Trends search property.",
      "enum": [
        "google search",
        "youtube search",
        "news search",
        "image search",
        "google shopping"
      ],
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "description": "Window used for related demand and trend validation.",
      "type": "string"
    },
    "limit": {
      "default": 5,
      "description": "Maximum validated opportunity candidates. Google Trends comparisons are capped at five keywords.",
      "maximum": 5,
      "minimum": 1,
      "type": "integer"
    },
    "project_id": {
      "anyOf": [
        {
          "maxLength": 128,
          "minLength": 1,
          "pattern": "^[A-Za-z0-9_-]+$",
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional DigestSEO Site Audit project ID owned by the authenticated account. Enables a 28-day exact-query Search Console validation pass."
    }
  },
  "required": [
    "seed_keyword"
  ],
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation trims the seed and rejects whitespace-only input through provider validation, in addition to registered string constraints.
- project\_id is nullable but constrained when provided; credentials/auth context are internal, not caller input. Optional DigestSEO failures may be represented as unavailable project context.

Sources: [src/mcp\_trendpulse/hosted.py:624](https://github.com/AKzar1el/mcp-trendpulse/blob/e9d7788938ac43bb591871c1929a81aa16a38f93/src/mcp_trendpulse/hosted.py#L624-L721)

## Schema provenance

Offline FastMCP list_tools on AST-selected registration declarations: original model classes, type aliases, decorator arguments, function signatures and return annotations preserved; function bodies replaced with pass solely to avoid provider imports, credentials, lifespans and remote calls. Actual implementations inspected separately.

- Community and hosted are separate server surfaces, not one merged deployment. No live provider calls were made. Installed current compatible FastMCP/Pydantic versions for schema generation rather than full project lock environment.
