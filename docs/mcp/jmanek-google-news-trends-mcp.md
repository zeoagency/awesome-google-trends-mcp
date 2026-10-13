# jmanek/google-news-trends-mcp

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/jmanek/google-news-trends-mcp) · [JSON definitions](../../data/mcp/jmanek-google-news-trends-mcp.json)

Reviewed 2026-10-13 at commit [`3e474d5b4499`](https://github.com/jmanek/google-news-trends-mcp/tree/3e474d5b449925b124ed99509ee166b18884e934).

Read current Google Trends RSS terms and optional related-news metadata, alongside news-search tools.

**5 tool definitions; 1 marked Google Trends.**

- The only Google Trends tool is get_trending_terms; the other four tools search or summarize news.

## Tools

| Tool | Scope |
|---|---|
| [`get_news_by_keyword`](#tool-get-news-by-keyword) | news |
| [`get_news_by_location`](#tool-get-news-by-location) | news |
| [`get_news_by_topic`](#tool-get-news-by-topic) | news |
| [`get_top_news`](#tool-get-top-news) | news |
| [`get_trending_terms`](#tool-get-trending-terms) | google-trends |

<a id="tool-get-news-by-keyword"></a>

### `get_news_by_keyword`

Queries Google News through GNews.get\_news, sets period in days and max\_results, decodes RSS URLs and downloads publisher articles using newspaper4k with cloudscraper/Playwright fallback. Returns article fields according to full\_data; summarize tries client LLM sampling then newspaper NLP fallback.

<details>
<summary>Full registered description</summary>

```text

    Find articles by keyword using Google News.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | Search term to find articles. | — |
| `period` | integer | No | `7` | Number of days to look back for articles. | minimum: 1 |
| `max_results` | integer | No | `10` | Maximum number of results to return. | minimum: 1; maximum: 25 |
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
      "maximum": 25,
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

Implementation notes:

- Pydantic Field enforces period >= 1 and 1 <= max\_results <= 25 as represented in the schema; there is no period upper bound.
- Search selector is a free string with no minLength or enum.

Sources: [src/google\_news\_trends\_mcp/server.py:161](https://github.com/jmanek/google-news-trends-mcp/blob/3e474d5b449925b124ed99509ee166b18884e934/src/google_news_trends_mcp/server.py#L165) · [src/google\_news\_trends\_mcp/news.py:202](https://github.com/jmanek/google-news-trends-mcp/blob/3e474d5b449925b124ed99509ee166b18884e934/src/google_news_trends_mcp/news.py#L202)

<a id="tool-get-news-by-location"></a>

### `get_news_by_location`

Find articles by location using Google News.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `location` | string | Yes | — | Name of city/state/country. | — |
| `period` | integer | No | `7` | Number of days to look back for articles. | minimum: 1 |
| `max_results` | integer | No | `10` | Maximum number of results to return. | minimum: 1; maximum: 25 |
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
      "maximum": 25,
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

Implementation notes:

- Pydantic Field enforces period >= 1 and 1 <= max\_results <= 25 as represented in the schema; there is no period upper bound.
- Search selector is a free string with no minLength or enum.

Sources: [src/google\_news\_trends\_mcp/server.py:197](https://github.com/jmanek/google-news-trends-mcp/blob/3e474d5b449925b124ed99509ee166b18884e934/src/google_news_trends_mcp/server.py#L201) · [src/google\_news\_trends\_mcp/news.py:239](https://github.com/jmanek/google-news-trends-mcp/blob/3e474d5b449925b124ed99509ee166b18884e934/src/google_news_trends_mcp/news.py#L239)

<a id="tool-get-news-by-topic"></a>

### `get_news_by_topic`

Queries Google News through GNews.get\_news\_by\_topic, sets period in days and max\_results, decodes RSS URLs and downloads publisher articles using newspaper4k with cloudscraper/Playwright fallback. Returns article fields according to full\_data; summarize tries client LLM sampling then newspaper NLP fallback.

<details>
<summary>Full registered description</summary>

```text
Find articles by topic using Google News.
    topic is one of
    WORLD, NATION, BUSINESS, TECHNOLOGY, ENTERTAINMENT, SPORTS, SCIENCE, HEALTH,
    POLITICS, CELEBRITIES, TV, MUSIC, MOVIES, THEATER, SOCCER, CYCLING, MOTOR SPORTS,
    TENNIS, COMBAT SPORTS, BASKETBALL, BASEBALL, FOOTBALL, SPORTS BETTING, WATER SPORTS,
    HOCKEY, GOLF, CRICKET, RUGBY, ECONOMY, PERSONAL FINANCE, FINANCE, DIGITAL CURRENCIES,
    MOBILE, ENERGY, GAMING, INTERNET SECURITY, GADGETS, VIRTUAL REALITY, ROBOTICS, NUTRITION,
    PUBLIC HEALTH, MENTAL HEALTH, MEDICINE, SPACE, WILDLIFE, ENVIRONMENT, NEUROSCIENCE, PHYSICS,
    GEOLOGY, PALEONTOLOGY, SOCIAL SCIENCES, EDUCATION, JOBS, ONLINE EDUCATION, HIGHER EDUCATION,
    VEHICLES, ARTS-DESIGN, BEAUTY, FOOD, TRAVEL, SHOPPING, HOME, OUTDOORS, FASHION.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `topic` | string | Yes | — | Topic to search for articles. | — |
| `period` | integer | No | `7` | Number of days to look back for articles. | minimum: 1 |
| `max_results` | integer | No | `10` | Maximum number of results to return. | minimum: 1; maximum: 25 |
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
      "maximum": 25,
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

Implementation notes:

- Pydantic Field enforces period >= 1 and 1 <= max\_results <= 25 as represented in the schema; there is no period upper bound.
- Search selector is a free string with no minLength or enum.
- The listed topic names appear only in the registered description, not as a schema enum or explicit local validation; the string is delegated to GNews.

Sources: [src/google\_news\_trends\_mcp/server.py:233](https://github.com/jmanek/google-news-trends-mcp/blob/3e474d5b449925b124ed99509ee166b18884e934/src/google_news_trends_mcp/server.py#L234) · [src/google\_news\_trends\_mcp/news.py:256](https://github.com/jmanek/google-news-trends-mcp/blob/3e474d5b449925b124ed99509ee166b18884e934/src/google_news_trends_mcp/news.py#L256)

<a id="tool-get-top-news"></a>

### `get_top_news`

Queries Google News through GNews.get\_top\_news, sets period in days and max\_results, decodes RSS URLs and downloads publisher articles using newspaper4k with cloudscraper/Playwright fallback. Returns article fields according to full\_data; summarize tries client LLM sampling then newspaper NLP fallback.

<details>
<summary>Full registered description</summary>

```text

    Get top news stories from Google News.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `period` | integer | No | `3` | Number of days to look back for top articles. | minimum: 1 |
| `max_results` | integer | No | `10` | Maximum number of results to return. | minimum: 1; maximum: 25 |
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
      "maximum": 25,
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

Implementation notes:

- Pydantic Field enforces period >= 1 and 1 <= max\_results <= 25 as represented in the schema; there is no period upper bound.
- All input fields are optional with defaults.

Sources: [src/google\_news\_trends\_mcp/server.py:266](https://github.com/jmanek/google-news-trends-mcp/blob/3e474d5b449925b124ed99509ee166b18884e934/src/google_news_trends_mcp/server.py#L267) · [src/google\_news\_trends\_mcp/news.py:221](https://github.com/jmanek/google-news-trends-mcp/blob/3e474d5b449925b124ed99509ee166b18884e934/src/google_news_trends_mcp/news.py#L221)

<a id="tool-get-trending-terms"></a>

### `get_trending_terms`

Fetches current Google Trends trending terms via trendspy Trends.trending\_now\_by\_rss(geo); sorts descending using int(volume[:-1]); returns keyword/volume only by default or richer trend objects with related news when full\_data is true. Any fetch/sort exception is logged and returns an empty list.

<details>
<summary>Full registered description</summary>

```text

    Returns google trends for a specific geo location.
```

</details>

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

Implementation notes:

- geo is a free string: geographic examples in its description are not pattern/enum constraints. The wrapper performs no geo format validation; downstream trendspy behavior was not exercised.

Sources: [src/google\_news\_trends\_mcp/server.py:297](https://github.com/jmanek/google-news-trends-mcp/blob/3e474d5b449925b124ed99509ee166b18884e934/src/google_news_trends_mcp/server.py#L298) · [src/google\_news\_trends\_mcp/news.py:291](https://github.com/jmanek/google-news-trends-mcp/blob/3e474d5b449925b124ed99509ee166b18884e934/src/google_news_trends_mcp/news.py#L291)

## Schema provenance

AST-preserved registered decorators, full signatures and Pydantic model definitions evaluated locally with FastMCP 3.1.1 and Pydantic 2.11.7 (versions pinned in uv.lock), followed by in-process FastMCP Client.list_tools. Tool bodies replaced with pass only for schema extraction; news descriptions populated verbatim from AST docstrings. Full implementations inspected separately.

- Source module imports, backend initialization, middleware and browser lifespan were bypassed during schema-only introspection to avoid unrelated dependencies and any network/browser side effects. No tool implementation was executed.
- FastMCP and Pydantic match uv.lock; other transitive framework dependencies use available compatible versions. pyproject.toml permits newer FastMCP >=3/Pydantic >=2.11.7, whose future schema behavior may vary.
- Runtime Google Trends geographic support and remote availability were not tested.
