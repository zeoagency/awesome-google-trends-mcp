# claude-world/trend-pulse

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/claude-world/trend-pulse) · [JSON definitions](../../data/mcp/claude-world-trend-pulse.json)

Reviewed 2026-10-13 at commit [`d8e5fdbcf42c`](https://github.com/claude-world/trend-pulse/tree/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e).

Save country RSS snapshots, compare local history, measure velocity, and export reports.

**29 tool definitions; 10 marked Google Trends.**

- Google Trends keyword search is not implemented; search_trends skips that source. Historical analyses use saved snapshots, not Google’s historical keyword-interest series.
- Select google_trends through sources/source when a tool supports source filtering. Content-writing and other-source tools remain documented separately.

## Tools

| Tool | Scope |
|---|---|
| [`get_trending`](#tool-get-trending) | google-trends |
| [`search_trends`](#tool-search-trends) | other |
| [`list_sources`](#tool-list-sources) | server-management |
| [`get_trend_history`](#tool-get-trend-history) | google-trends |
| [`take_snapshot`](#tool-take-snapshot) | google-trends |
| [`get_content_brief`](#tool-get-content-brief) | other |
| [`get_scoring_guide`](#tool-get-scoring-guide) | other |
| [`get_platform_specs`](#tool-get-platform-specs) | other |
| [`get_review_checklist`](#tool-get-review-checklist) | other |
| [`get_reel_guide`](#tool-get-reel-guide) | other |
| [`render_page`](#tool-render-page) | other |
| [`search_semantic`](#tool-search-semantic) | google-trends |
| [`get_trend_clusters`](#tool-get-trend-clusters) | google-trends |
| [`get_lifecycle_prediction`](#tool-get-lifecycle-prediction) | google-trends |
| [`list_sources_extended`](#tool-list-sources-extended) | server-management |
| [`run_content_workflow`](#tool-run-content-workflow) | other |
| [`get_ab_variants`](#tool-get-ab-variants) | other |
| [`score_content_hybrid`](#tool-score-content-hybrid) | other |
| [`get_campaign_calendar`](#tool-get-campaign-calendar) | other |
| [`get_trend_report`](#tool-get-trend-report) | google-trends |
| [`compare_trends`](#tool-compare-trends) | google-trends |
| [`export_data`](#tool-export-data) | google-trends |
| [`send_notification`](#tool-send-notification) | other |
| [`adapt_content`](#tool-adapt-content) | other |
| [`analyze_viral_factors`](#tool-analyze-viral-factors) | other |
| [`generate_hashtags`](#tool-generate-hashtags) | other |
| [`get_source_status`](#tool-get-source-status) | server-management |
| [`get_trend_velocity`](#tool-get-trend-velocity) | google-trends |
| [`batch_score_content`](#tool-batch-score-content) | other |

<a id="tool-get-trending"></a>

### `get_trending`

Fetch selected sources concurrently, merge normalized scores, optionally save local snapshot and enrich velocity; Google Trends uses country RSS.

<details>
<summary>Full registered description</summary>

```text
Get trending topics from free sources.

Args:
    sources: Comma-separated source names (default: all).
             Built-in (20): google_trends, hackernews, mastodon, bluesky, wikipedia,
             github, pypi, google_news, lobsters, devto, npm, reddit,
             coingecko, dockerhub, stackoverflow, arxiv, producthunt, lemmy, dcard, ptt
             Plugins (17+): weibo, youtube_trending, threads, line_today, mobile01,
             bahamut, ettoday, yahoo_tw, udn, coinmarketcap, dexscreener,
             indie_hackers, x_trending, tiktok_trending, xiaohongshu,
             pinterest, linkedin_trending
    geo: Country code for regional trends (e.g. TW, US, JP)
    count: Number of results per source (default: 20)
    save: Save snapshot to history DB for velocity tracking (default: false)

Returns:
    JSON with merged ranking + per-source results (includes direction/velocity if history exists)
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `sources` | string | No | `""` | — | — |
| `geo` | string | No | `""` | — | — |
| `count` | integer | No | `20` | — | — |
| `save` | boolean | No | `false` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "sources": {
      "default": "",
      "title": "Sources",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "count": {
      "default": 20,
      "title": "Count",
      "type": "integer"
    },
    "save": {
      "default": false,
      "title": "Save",
      "type": "boolean"
    }
  },
  "title": "get_trendingArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: count = max(1, min(count, 200))
- sources is a comma-separated string; whitespace/empty items stripped; empty means all. Unknown names are skipped (trending reports errors).

Sources: [src/trend\_pulse/server.py:42](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L42-L70) · [src/trend\_pulse/sources/google\_trends.py:12](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/sources/google_trends.py#L12-L78) · [src/trend\_pulse/aggregator.py:55](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/aggregator.py#L55-L191)

<a id="tool-search-trends"></a>

### `search_trends`

Search only sources overriding search(); Google Trends is skipped and cannot search keywords.

<details>
<summary>Full registered description</summary>

```text
Search for a keyword across trend sources.

Args:
    query: Search keyword
    sources: Comma-separated source names (default: all searchable)
    geo: Country code

Returns:
    JSON with search results across sources
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `query` | string | Yes | — | — | — |
| `sources` | string | No | `""` | — | — |
| `geo` | string | No | `""` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "sources": {
      "default": "",
      "title": "Sources",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "title": "search_trendsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- sources is a comma-separated string; whitespace/empty items stripped; empty means all. Unknown names are skipped (trending reports errors).
- google\_trends is not searchable: source inherits base search and aggregator excludes it.

Sources: [src/trend\_pulse/server.py:73](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L73-L91) · [src/trend\_pulse/sources/google\_trends.py:12](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/sources/google_trends.py#L12-L78) · [src/trend\_pulse/aggregator.py:55](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/aggregator.py#L55-L191)

<a id="tool-list-sources"></a>

### `list_sources`

List all available trend sources and their properties.

No caller parameters.

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {},
  "title": "list_sourcesArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:94](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L94-L97)

<a id="tool-get-trend-history"></a>

### `get_trend_history`

Query local SQLite snapshots by partial keyword, days and optional source; no Google Trends historical API.

<details>
<summary>Full registered description</summary>

```text
Query historical trend data for a keyword.

Args:
    keyword: The keyword to look up (partial match supported)
    days: Number of days to look back (default: 30)
    source: Filter by source name (default: all sources)

Returns:
    JSON with historical records including timestamps and scores
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | — | — |
| `days` | integer | No | `30` | — | — |
| `source` | string | No | `""` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "title": "Keyword",
      "type": "string"
    },
    "days": {
      "default": 30,
      "title": "Days",
      "type": "integer"
    },
    "source": {
      "default": "",
      "title": "Source",
      "type": "string"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "get_trend_historyArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:100](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L100-L117) · [src/trend\_pulse/sources/google\_trends.py:12](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/sources/google_trends.py#L12-L78) · [src/trend\_pulse/aggregator.py:55](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/aggregator.py#L55-L191)

<a id="tool-take-snapshot"></a>

### `take_snapshot`

Fetch selected sources and save their current results to local SQLite history.

<details>
<summary>Full registered description</summary>

```text
Take a trend snapshot: fetch from all sources and save to history DB.

Args:
    sources: Comma-separated source names (default: all)
    geo: Country code for regional trends
    count: Number of results per source (default: 20)

Returns:
    JSON with trending results (snapshot saved to DB for velocity tracking)
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `sources` | string | No | `""` | — | — |
| `geo` | string | No | `""` | — | — |
| `count` | integer | No | `20` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "sources": {
      "default": "",
      "title": "Sources",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "count": {
      "default": 20,
      "title": "Count",
      "type": "integer"
    }
  },
  "title": "take_snapshotArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: count = max(1, min(count, 200))
- sources is a comma-separated string; whitespace/empty items stripped; empty means all. Unknown names are skipped (trending reports errors).

Sources: [src/trend\_pulse/server.py:120](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L120-L139) · [src/trend\_pulse/sources/google\_trends.py:12](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/sources/google_trends.py#L12-L78) · [src/trend\_pulse/aggregator.py:55](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/aggregator.py#L55-L191)

<a id="tool-get-content-brief"></a>

### `get_content_brief`

Return static writing frameworks, hooks, patent strategies and platform guidance, not generated content.

<details>
<summary>Full registered description</summary>

```text
Get a structured writing brief for creating viral content.

Returns hook examples, patent strategies, scoring dimensions, platform specs,
and content type guidance. Use this data to craft original posts — the LLM
creates the content, this tool provides the optimization framework.

Args:
    topic: Subject to create content about (e.g. "AI tools", "Claude Code")
    content_type: Post style — opinion, story, debate, howto, list, question, news, meme
    platform: Target platform — threads (500 chars), instagram (2200), facebook (63206)
    lang: Language — "auto" (detect from topic), "en", "zh-TW"

Returns:
    JSON with hook examples, CTA examples, patent strategies, scoring dimensions,
    platform specs, content type guidance, char limit, and quality gate thresholds
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `topic` | string | Yes | — | — | — |
| `content_type` | string | No | `"debate"` | — | — |
| `platform` | string | No | `"threads"` | — | — |
| `lang` | string | No | `"auto"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "topic": {
      "title": "Topic",
      "type": "string"
    },
    "content_type": {
      "default": "debate",
      "title": "Content Type",
      "type": "string"
    },
    "platform": {
      "default": "threads",
      "title": "Platform",
      "type": "string"
    },
    "lang": {
      "default": "auto",
      "title": "Lang",
      "type": "string"
    }
  },
  "required": [
    "topic"
  ],
  "title": "get_content_briefArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:147](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L147-L173)

<a id="tool-get-scoring-guide"></a>

### `get_scoring_guide`

Return static five-dimension evaluation criteria and grading instructions.

<details>
<summary>Full registered description</summary>

```text
Get the 5-dimension scoring framework for evaluating posts.

Returns evaluation criteria, high/low signal examples, and grade thresholds
for each patent-derived dimension. The LLM uses this guide to score posts
itself — no regex heuristics.

Dimensions (weighted):
- Hook Power 25% (EdgeRank Weight + Andromeda)
- Engagement Trigger 25% (Story-Viewer Tuple + Dear Algo)
- Conversation Durability 20% (Threads 72hr window)
- Velocity Potential 15% (Andromeda Real-time)
- Format Score 15% (Multi-modal Indexing)

Args:
    lang: Language for criteria text — "auto", "en", "zh-TW"
    topic: Optional topic hint for auto language detection

Returns:
    JSON with 5 dimensions (weight, criteria, signals), grade thresholds, and instructions
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `lang` | string | No | `"auto"` | — | — |
| `topic` | string | No | `""` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "lang": {
      "default": "auto",
      "title": "Lang",
      "type": "string"
    },
    "topic": {
      "default": "",
      "title": "Topic",
      "type": "string"
    }
  },
  "title": "get_scoring_guideArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:176](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L176-L204)

<a id="tool-get-platform-specs"></a>

### `get_platform_specs`

Return platform specification data for one or all supported platforms.

<details>
<summary>Full registered description</summary>

```text
Get platform specifications for content adaptation.

Returns character limits, content strengths, algorithm priorities,
best posting times, and format guidelines for each platform.
Use this to adapt content for specific platforms.

Args:
    platform: Platform name — threads, instagram, facebook (empty = all platforms)
    lang: Language for descriptions — "en" or "zh-TW" (default: "zh-TW")

Returns:
    JSON with platform specs (char limits, strengths, format tips, algo priority, best times)
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `platform` | string | No | `""` | — | — |
| `lang` | string | No | `"zh-TW"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "platform": {
      "default": "",
      "title": "Platform",
      "type": "string"
    },
    "lang": {
      "default": "zh-TW",
      "title": "Lang",
      "type": "string"
    }
  },
  "title": "get_platform_specsArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:207](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L207-L228)

<a id="tool-get-review-checklist"></a>

### `get_review_checklist`

Return static quality thresholds and content review criteria.

<details>
<summary>Full registered description</summary>

```text
Get a structured review checklist for evaluating content quality.

Returns platform limits, quality thresholds, and detailed checklist items.
The LLM reviews the post against this checklist itself — the tool only
provides criteria, not judgment.

Checklist covers:
- Character limit compliance
- Overall score quality gate (>= 70)
- Conversation durability gate (>= 55)
- Hook effectiveness
- CTA presence
- Question/engagement triggers
- Format/readability

Args:
    platform: Target platform — threads (500 chars), instagram (2200), facebook (63206)
    lang: Language for checklist text — "auto", "en", "zh-TW"
    topic: Optional topic hint for auto language detection

Returns:
    JSON with platform limits, quality gate thresholds, checklist items, and verdict rules
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `platform` | string | No | `"threads"` | — | — |
| `lang` | string | No | `"auto"` | — | — |
| `topic` | string | No | `""` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "platform": {
      "default": "threads",
      "title": "Platform",
      "type": "string"
    },
    "lang": {
      "default": "auto",
      "title": "Lang",
      "type": "string"
    },
    "topic": {
      "default": "",
      "title": "Topic",
      "type": "string"
    }
  },
  "title": "get_review_checklistArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:231](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L231-L263)

<a id="tool-get-reel-guide"></a>

### `get_reel_guide`

Return static scene structures and allocated timings for short-video scripts.

<details>
<summary>Full registered description</summary>

```text
Get a structured guide for creating Reels/Short video scripts.

Returns scene structure, timing allocations, visual guidance, and editing tips.
The LLM fills in original captions, voiceover, and visual directions.

Styles: educational (problem→solution), storytelling (conflict→resolution),
listicle (numbered points)

Args:
    style: Script style — educational, storytelling, listicle
    duration: Target duration in seconds (default: 30)
    lang: Language for guide text — "auto", "en", "zh-TW"
    topic: Optional topic hint for auto language detection

Returns:
    JSON with scene structure, timing, music suggestion, editing tips, and instructions
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `style` | string | No | `"educational"` | — | — |
| `duration` | integer | No | `30` | — | — |
| `lang` | string | No | `"auto"` | — | — |
| `topic` | string | No | `""` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "style": {
      "default": "educational",
      "title": "Style",
      "type": "string"
    },
    "duration": {
      "default": 30,
      "title": "Duration",
      "type": "integer"
    },
    "lang": {
      "default": "auto",
      "title": "Lang",
      "type": "string"
    },
    "topic": {
      "default": "",
      "title": "Topic",
      "type": "string"
    }
  },
  "title": "get_reel_guideArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:266](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L266-L293)

<a id="tool-render-page"></a>

### `render_page`

Validate URL then use configured Cloudflare Browser Rendering to obtain markdown, HTML or structured JSON.

<details>
<summary>Full registered description</summary>

```text
Render a JS-heavy page using Cloudflare Browser Rendering.

Requires CF_ACCOUNT_ID and CF_API_TOKEN environment variables.
Returns rendered page content in the requested format.

Args:
    url: The page URL to render.
    format: Output format — "markdown" (clean text), "content" (full HTML),
            or "json" (AI structured extraction, returns raw page data).

Returns:
    JSON with url, format, and rendered content (or error message).
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `url` | string | Yes | — | — | — |
| `format` | string | No | `"markdown"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "url": {
      "title": "Url",
      "type": "string"
    },
    "format": {
      "default": "markdown",
      "title": "Format",
      "type": "string"
    }
  },
  "required": [
    "url"
  ],
  "title": "render_pageArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Only http/https; blocks literal private/loopback/link-local/multicast IPs. Arbitrary format strings fall back to markdown. Requires configured Cloudflare credentials at execution.

Sources: [src/trend\_pulse/server.py:301](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L301-L368)

<a id="tool-search-semantic"></a>

### `search_semantic`

Fetch live trends, construct local TF-IDF vector store, return similarity-ranked items.

<details>
<summary>Full registered description</summary>

```text
Semantic similarity search across trend sources.

Fetches trends from the specified sources, indexes them with TF-IDF, and
returns the k most semantically similar results to the query. Useful for
finding thematically related trends even when keywords don't match exactly.

Args:
    query: Natural-language search query (e.g. "machine learning tools").
    sources: Comma-separated source names (default: all).
    geo: Country code for regional trends (e.g. TW, US).
    count: Number of items to fetch per source before similarity ranking.
    k: Number of results to return (default: 10).

Returns:
    JSON with ranked list of semantically similar TrendItems.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `query` | string | Yes | — | — | — |
| `sources` | string | No | `""` | — | — |
| `geo` | string | No | `""` | — | — |
| `count` | integer | No | `20` | — | — |
| `k` | integer | No | `10` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "sources": {
      "default": "",
      "title": "Sources",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "count": {
      "default": 20,
      "title": "Count",
      "type": "integer"
    },
    "k": {
      "default": 10,
      "title": "K",
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "title": "search_semanticArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: count = max(1, min(count, 200))
- sources is a comma-separated string; whitespace/empty items stripped; empty means all. Unknown names are skipped (trending reports errors).

Sources: [src/trend\_pulse/server.py:376](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L376-L426) · [src/trend\_pulse/sources/google\_trends.py:12](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/sources/google_trends.py#L12-L78) · [src/trend\_pulse/aggregator.py:55](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/aggregator.py#L55-L191)

<a id="tool-get-trend-clusters"></a>

### `get_trend_clusters`

Fetch live trends and group TF-IDF similar topics across sources.

<details>
<summary>Full registered description</summary>

```text
Cluster trends from multiple sources into semantic topic groups.

Fetches trends, embeds them with TF-IDF, and groups similar items into
TrendClusters. Cross-source clusters (same topic appearing in 2+ sources)
are ranked highest — these are the most validated viral topics.

Args:
    sources: Comma-separated source names (default: all).
    geo: Country code for regional trends.
    count: Items to fetch per source before clustering.
    threshold: Cosine similarity threshold (0-1). Lower = larger clusters.
               Default 0.25 is a good balance for short trend keywords.

Returns:
    JSON with clusters sorted by (cross_source desc, score desc).
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `sources` | string | No | `""` | — | — |
| `geo` | string | No | `""` | — | — |
| `count` | integer | No | `20` | — | — |
| `threshold` | number | No | `0.25` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "sources": {
      "default": "",
      "title": "Sources",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "count": {
      "default": 20,
      "title": "Count",
      "type": "integer"
    },
    "threshold": {
      "default": 0.25,
      "title": "Threshold",
      "type": "number"
    }
  },
  "title": "get_trend_clustersArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: count = max(1, min(count, 200))
- sources is a comma-separated string; whitespace/empty items stripped; empty means all. Unknown names are skipped (trending reports errors).

Sources: [src/trend\_pulse/server.py:429](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L429-L475) · [src/trend\_pulse/sources/google\_trends.py:12](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/sources/google_trends.py#L12-L78) · [src/trend\_pulse/aggregator.py:55](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/aggregator.py#L55-L191)

<a id="tool-get-lifecycle-prediction"></a>

### `get_lifecycle_prediction`

Predict lifecycle from chronological local snapshot scores; does not retrieve remote historical Google Trends data.

<details>
<summary>Full registered description</summary>

```text
Predict the lifecycle stage of a trend keyword.

Queries the local history DB for the keyword's score trajectory, then
predicts whether it's emerging, at peak, declining, or fading.

Args:
    keyword: The trend keyword to analyse.
    days: How many days of history to include (default: 30).
    source: Filter history by source name (default: all sources).

Returns:
    JSON with stage, current_score, velocity, history_count, and emoji.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | — | — |
| `days` | integer | No | `30` | — | — |
| `source` | string | No | `""` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "title": "Keyword",
      "type": "string"
    },
    "days": {
      "default": 30,
      "title": "Days",
      "type": "integer"
    },
    "source": {
      "default": "",
      "title": "Source",
      "type": "string"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "get_lifecycle_predictionArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:478](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L478-L513) · [src/trend\_pulse/sources/google\_trends.py:12](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/sources/google_trends.py#L12-L78) · [src/trend\_pulse/aggregator.py:55](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/aggregator.py#L55-L191)

<a id="tool-list-sources-extended"></a>

### `list_sources_extended`

Enrich instantiated source metadata with optional plugin properties.

<details>
<summary>Full registered description</summary>

```text
List all available trend sources with extended plugin metadata.

Returns all built-in sources plus plugin sources with additional fields:
category, frequency, plugin_version, difficulty, and dependencies.

Returns:
    JSON array of source info objects with full metadata.
```

</details>

No caller parameters.

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {},
  "title": "list_sources_extendedArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:516](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L516-L545)

<a id="tool-run-content-workflow"></a>

### `run_content_workflow`

Fetch trend context, then run six sequential Python template/heuristic workflow stages to draft and score platform posts.

<details>
<summary>Full registered description</summary>

```text
Run the full 6-agent content workflow to auto-generate viral posts.

Executes a multi-agent pipeline: researcher → strategist → copywriter →
optimizer → compliance checker → distributor. Returns platform-ready content
for all specified platforms.

Agents:
1. Researcher: selects top trends relevant to the topic
2. Strategist: generates 3 content angles / hooks
3. Copywriter: drafts platform-specific posts
4. Optimizer: creates A/B variants and scores them
5. Compliance: flags spammy language (reduces score)
6. Distributor: picks best variant per platform

Args:
    topic: Content topic / keyword (e.g. "AI agents", "Claude Code").
    platforms: Comma-separated platform names
               (threads, x, instagram, linkedin, tiktok, youtube, xiaohongshu, facebook).
    brand_voice: Tone — "casual", "professional", "provocative", "educational".
    sources: Comma-separated trend source names to fetch context from (default: all).
    geo: Country code for trend context (e.g. TW, US).
    count: Items to fetch per source for trend context (default: 20).

Returns:
    JSON with final_content (platform→text), strategy, scored_drafts, and any errors.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `topic` | string | Yes | — | — | — |
| `platforms` | string | No | `"threads"` | — | — |
| `brand_voice` | string | No | `"casual"` | — | — |
| `sources` | string | No | `""` | — | — |
| `geo` | string | No | `""` | — | — |
| `count` | integer | No | `20` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "topic": {
      "title": "Topic",
      "type": "string"
    },
    "platforms": {
      "default": "threads",
      "title": "Platforms",
      "type": "string"
    },
    "brand_voice": {
      "default": "casual",
      "title": "Brand Voice",
      "type": "string"
    },
    "sources": {
      "default": "",
      "title": "Sources",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "count": {
      "default": 20,
      "title": "Count",
      "type": "integer"
    }
  },
  "required": [
    "topic"
  ],
  "title": "run_content_workflowArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: count = max(1, min(count, 200))
- sources is a comma-separated string; whitespace/empty items stripped; empty means all. Unknown names are skipped (trending reports errors).

Sources: [src/trend\_pulse/server.py:553](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L553-L628)

<a id="tool-get-ab-variants"></a>

### `get_ab_variants`

Apply up to five fixed text mutations, truncate to platform limit, score original and variants.

<details>
<summary>Full registered description</summary>

```text
Generate A/B content variants for testing different approaches.

Creates multiple variants of the input content by applying different
mutation strategies: emoji boost, question hook, urgency framing, etc.
Each variant is scored with the heuristic engine.

Args:
    content: Original post text to create variants from.
    platform: Target platform for char-limit compliance (default: threads).
    count: Number of variants to generate (1-5, default: 3).

Returns:
    JSON with original + variant posts, scores, and recommended pick.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `content` | string | Yes | — | — | — |
| `platform` | string | No | `"threads"` | — | — |
| `count` | integer | No | `3` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "content": {
      "title": "Content",
      "type": "string"
    },
    "platform": {
      "default": "threads",
      "title": "Platform",
      "type": "string"
    },
    "count": {
      "default": 3,
      "title": "Count",
      "type": "integer"
    }
  },
  "required": [
    "content"
  ],
  "title": "get_ab_variantsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: count = max(1, min(count, 5))
- Implementation: best = max(variants, key=lambda v: v["score"])

Sources: [src/trend\_pulse/server.py:631](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L631-L695)

<a id="tool-score-content-hybrid"></a>

### `score_content_hybrid`

Apply heuristic scoring and optional Anthropic LLM judge; wrapper supplies no history keywords, so advertised RAG history bonus is not enabled here.

<details>
<summary>Full registered description</summary>

```text
Score content using the Hybrid Scoring 2.0 engine.

Applies L1 heuristic analysis (always available) + L2 LLM judge
(requires ANTHROPIC_API_KEY) + L3 RAG history bonus if history exists.

Scoring dimensions (weights):
- Hook Power 25%: Opening line strength, emoji, question words
- Engagement Trigger 25%: CTA presence, debate language
- Conversation Durability 20%: Length, depth, substance
- Velocity Potential 15%: Trending keywords alignment
- Format Score 15%: Char limit compliance, readability

Args:
    content: Post text to evaluate.
    platform: Target platform for format scoring
              (threads, x, instagram, linkedin, tiktok, youtube, xiaohongshu, facebook).

Returns:
    JSON with total score (0-100), grade, dimension breakdown, mode, and signals.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `content` | string | Yes | — | — | — |
| `platform` | string | No | `"threads"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "content": {
      "title": "Content",
      "type": "string"
    },
    "platform": {
      "default": "threads",
      "title": "Platform",
      "type": "string"
    }
  },
  "required": [
    "content"
  ],
  "title": "score_content_hybridArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:698](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L698-L726)

<a id="tool-get-campaign-calendar"></a>

### `get_campaign_calendar`

Cycle topics, platforms and fixed angle templates over days; one calendar entry per day, rather than one per topic per day as description claims.

<details>
<summary>Full registered description</summary>

```text
Generate a content calendar for multiple topics over N days.

Plans one post per topic per day, distributing across platforms and
varying content angles to avoid repetition. Uses the strategy layer
to assign angles and the platform adapter for format guidance.

Args:
    topics: Comma-separated topic list (e.g. "AI tools,Python,Claude Code").
    days: Number of days to plan (1-30, default: 7).
    platforms: Comma-separated target platforms (default: threads).
    brand_voice: Tone — "casual", "professional", "provocative", "educational".

Returns:
    JSON calendar with day-by-day posting plan.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `topics` | string | Yes | — | — | — |
| `days` | integer | No | `7` | — | — |
| `platforms` | string | No | `"threads"` | — | — |
| `brand_voice` | string | No | `"casual"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "topics": {
      "title": "Topics",
      "type": "string"
    },
    "days": {
      "default": 7,
      "title": "Days",
      "type": "integer"
    },
    "platforms": {
      "default": "threads",
      "title": "Platforms",
      "type": "string"
    },
    "brand_voice": {
      "default": "casual",
      "title": "Brand Voice",
      "type": "string"
    }
  },
  "required": [
    "topics"
  ],
  "title": "get_campaign_calendarArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: days = max(1, min(days, 30))
- Empty parsed topic list returns error; empty platform list falls back to threads.

Sources: [src/trend\_pulse/server.py:729](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L729-L789)

<a id="tool-get-trend-report"></a>

### `get_trend_report`

Fetch current trends, cluster them and consult local history for lifecycle summary and top items.

<details>
<summary>Full registered description</summary>

```text
Generate an automated trend intelligence report.

Fetches trends, clusters them, predicts lifecycle stages, and assembles a
structured report showing what's emerging, peaking, and fading across sources.

Args:
    period: Number of days of history to include for lifecycle context (default: 7).
    sources: Comma-separated source names (default: all).
    geo: Country code filter (e.g. TW, US).
    count: Items per source to include (default: 20).

Returns:
    JSON report with executive summary, top trends, cross-source clusters,
    and lifecycle breakdown (emerging/peak/declining/fading counts).
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `period` | integer | No | `7` | — | — |
| `sources` | string | No | `""` | — | — |
| `geo` | string | No | `""` | — | — |
| `count` | integer | No | `20` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "period": {
      "default": 7,
      "title": "Period",
      "type": "integer"
    },
    "sources": {
      "default": "",
      "title": "Sources",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "count": {
      "default": 20,
      "title": "Count",
      "type": "integer"
    }
  },
  "title": "get_trend_reportArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: count = max(1, min(count, 200))
- sources is a comma-separated string; whitespace/empty items stripped; empty means all. Unknown names are skipped (trending reports errors).

Sources: [src/trend\_pulse/server.py:797](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L797-L879) · [src/trend\_pulse/sources/google\_trends.py:12](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/sources/google_trends.py#L12-L78) · [src/trend\_pulse/aggregator.py:55](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/aggregator.py#L55-L191)

<a id="tool-compare-trends"></a>

### `compare_trends`

Compare local history scores, peaks, average and mean change per record for two partial keyword matches.

<details>
<summary>Full registered description</summary>

```text
Compare two trend keywords side-by-side.

Looks up history for both keywords and computes momentum, average score,
peak score, and lifecycle stage for each. Returns a head-to-head comparison.

Args:
    keyword_a: First keyword to compare.
    keyword_b: Second keyword to compare.
    days: Days of history to query (default: 30).

Returns:
    JSON with side-by-side comparison of both keywords.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword_a` | string | Yes | — | — | — |
| `keyword_b` | string | Yes | — | — | — |
| `days` | integer | No | `30` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword_a": {
      "title": "Keyword A",
      "type": "string"
    },
    "keyword_b": {
      "title": "Keyword B",
      "type": "string"
    },
    "days": {
      "default": 30,
      "title": "Days",
      "type": "integer"
    }
  },
  "required": [
    "keyword_a",
    "keyword_b"
  ],
  "title": "compare_trendsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: peak = max(scores, default=0.0)

Sources: [src/trend\_pulse/server.py:882](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L882-L935) · [src/trend\_pulse/sources/google\_trends.py:12](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/sources/google_trends.py#L12-L78) · [src/trend\_pulse/aggregator.py:55](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/aggregator.py#L55-L191)

<a id="tool-export-data"></a>

### `export_data`

Fetch live trends, flatten and sort scores, return JSON object containing rows or CSV text.

<details>
<summary>Full registered description</summary>

```text
Export trend data in JSON or CSV format.

Fetches live trends and formats them for export. Useful for feeding into
spreadsheets, BI tools, or external analysis pipelines.

Args:
    format: Output format — "json" (structured) or "csv" (comma-separated).
    sources: Comma-separated source names (default: all).
    geo: Country code filter.
    count: Items per source (default: 50).

Returns:
    JSON or CSV string with trend data.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `format` | string | No | `"json"` | — | — |
| `sources` | string | No | `""` | — | — |
| `geo` | string | No | `""` | — | — |
| `count` | integer | No | `50` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "format": {
      "default": "json",
      "title": "Format",
      "type": "string"
    },
    "sources": {
      "default": "",
      "title": "Sources",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "count": {
      "default": 50,
      "title": "Count",
      "type": "integer"
    }
  },
  "title": "export_dataArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: count = max(1, min(count, 200))
- sources is a comma-separated string; whitespace/empty items stripped; empty means all. Unknown names are skipped (trending reports errors).

Sources: [src/trend\_pulse/server.py:938](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L938-L998) · [src/trend\_pulse/sources/google\_trends.py:12](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/sources/google_trends.py#L12-L78) · [src/trend\_pulse/aggregator.py:55](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/aggregator.py#L55-L191)

<a id="tool-send-notification"></a>

### `send_notification`

Send title/body through selected configured notification channel.

<details>
<summary>Full registered description</summary>

```text
Send a trend alert notification to a configured channel.

Requires the channel's credentials to be set as environment variables.
Channels: discord, telegram, webhook, line, email.

Environment variables:
- discord:  DISCORD_WEBHOOK_URL
- telegram: TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID
- webhook:  GENERIC_WEBHOOK_URL
- line:     LINE_NOTIFY_TOKEN
- email:    SMTP_HOST + SMTP_USER + SMTP_PASS + SMTP_FROM + SMTP_TO

Args:
    channel: Channel name — "discord", "telegram", "webhook", "line", or "email".
    title: Notification title.
    message: Notification body text.

Returns:
    JSON with success status and channel used.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `channel` | string | Yes | — | — | — |
| `title` | string | Yes | — | — | — |
| `message` | string | Yes | — | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "channel": {
      "title": "Channel",
      "type": "string"
    },
    "title": {
      "title": "Title",
      "type": "string"
    },
    "message": {
      "title": "Message",
      "type": "string"
    }
  },
  "required": [
    "channel",
    "title",
    "message"
  ],
  "title": "send_notificationArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:1001](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L1001-L1044)

<a id="tool-adapt-content"></a>

### `adapt_content`

Prepend target-specific opener, truncate, add LinkedIn line breaks and score; no general semantic rewriting.

<details>
<summary>Full registered description</summary>

```text
Adapt content from one platform format to another.

Rewrites the post to fit the target platform's char limit, tone, and
best-practices (e.g. Threads→X requires tightening to 280 chars;
Threads→LinkedIn requires adding professional framing).

Args:
    content: Original post text.
    from_platform: Source platform (threads, instagram, facebook, x, linkedin,
                   tiktok, youtube, xiaohongshu).
    to_platform: Target platform.

Returns:
    JSON with adapted content, char counts before/after, and platform specs.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `content` | string | Yes | — | — | — |
| `from_platform` | string | No | `"threads"` | — | — |
| `to_platform` | string | No | `"x"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "content": {
      "title": "Content",
      "type": "string"
    },
    "from_platform": {
      "default": "threads",
      "title": "From Platform",
      "type": "string"
    },
    "to_platform": {
      "default": "x",
      "title": "To Platform",
      "type": "string"
    }
  },
  "required": [
    "content"
  ],
  "title": "adapt_contentArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:1053](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L1053-L1108)

<a id="tool-analyze-viral-factors"></a>

### `analyze_viral_factors`

Score content, compute regex signals and return heuristic suggestions and strengths/weaknesses.

<details>
<summary>Full registered description</summary>

```text
Deep analysis of what makes (or doesn't make) content go viral.

Breaks down the post across 5 patent-derived dimensions with specific
per-signal feedback and actionable improvement suggestions.

Args:
    content: Post text to analyse.
    platform: Target platform (affects char-limit and format scoring).

Returns:
    JSON with dimension scores, per-signal breakdown, strengths,
    weaknesses, and top 3 improvement suggestions.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `content` | string | Yes | — | — | — |
| `platform` | string | No | `"threads"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "content": {
      "title": "Content",
      "type": "string"
    },
    "platform": {
      "default": "threads",
      "title": "Platform",
      "type": "string"
    }
  },
  "required": [
    "content"
  ],
  "title": "analyze_viral_factorsArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:1111](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L1111-L1167)

<a id="tool-generate-hashtags"></a>

### `generate_hashtags`

Construct topic-word hashtags and fixed context tags, deduplicate and truncate; no live popularity lookup.

<details>
<summary>Full registered description</summary>

```text
Generate optimized hashtags for a topic and platform.

Returns a ranked list of hashtags based on topic relevance and
platform-specific best practices (e.g. LinkedIn prefers 3-5 tags,
Instagram up to 30, TikTok 3-7 challenge-style tags).

Args:
    topic: Content topic or keyword (e.g. "AI agents", "Python tutorial").
    platform: Target platform — affects volume and style recommendations.
    count: Number of hashtags to generate (1-30, default: 10).
    lang: Language hint — "en" or "zh-TW" (for Chinese topics).

Returns:
    JSON with hashtag list, platform recommendation, and usage tips.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `topic` | string | Yes | — | — | — |
| `platform` | string | No | `"threads"` | — | — |
| `count` | integer | No | `10` | — | — |
| `lang` | string | No | `"en"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "topic": {
      "title": "Topic",
      "type": "string"
    },
    "platform": {
      "default": "threads",
      "title": "Platform",
      "type": "string"
    },
    "count": {
      "default": 10,
      "title": "Count",
      "type": "integer"
    },
    "lang": {
      "default": "en",
      "title": "Lang",
      "type": "string"
    }
  },
  "required": [
    "topic"
  ],
  "title": "generate_hashtagsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: count = max(1, min(count, 30))

Sources: [src/trend\_pulse/server.py:1170](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L1170-L1251)

<a id="tool-get-source-status"></a>

### `get_source_status`

Concurrently call fetch\_trending(count=1) for instantiated sources with ten-second timeouts.

<details>
<summary>Full registered description</summary>

```text
Check health status of all registered trend sources.

Performs a lightweight ping to verify each source is reachable and
returning data. Useful for debugging which sources are failing.

Returns:
    JSON with per-source status (ok / error / skipped) and summary counts.
```

</details>

No caller parameters.

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {},
  "title": "get_source_statusArguments",
  "type": "object"
}
```

</details>

Sources: [src/trend\_pulse/server.py:1254](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L1254-L1301)

<a id="tool-get-trend-velocity"></a>

### `get_trend_velocity`

Read local snapshots and compute mean change per record and acceleration; hours is converted to day window, not exact hourly filtering, and velocity is not time-normalized.

<details>
<summary>Full registered description</summary>

```text
Get real-time velocity and momentum for a trend keyword.

Queries recent history to compute how fast the keyword is rising or falling.
Returns velocity (score change per hour), acceleration, and projected
score in the next 6 and 24 hours.

Args:
    keyword: Trend keyword to analyse.
    hours: Lookback window in hours (1-168, default: 24).
    source: Filter by source name (default: all sources).

Returns:
    JSON with velocity, acceleration, trend_direction, and projections.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | — | — |
| `hours` | integer | No | `24` | — | — |
| `source` | string | No | `""` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "title": "Keyword",
      "type": "string"
    },
    "hours": {
      "default": 24,
      "title": "Hours",
      "type": "integer"
    },
    "source": {
      "default": "",
      "title": "Source",
      "type": "string"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "get_trend_velocityArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation: hours = max(1, min(hours, 168))  # clamp to 1h–7d
- Implementation: days = max(1, min(hours // 24 + 1, 30))
- Implementation: mid = max(1, len(deltas) // 2)
- Implementation: proj\_6h = max(0.0, min(100.0, current + velocity \* 0.25))
- Implementation: proj\_24h = max(0.0, min(100.0, current + velocity))

Sources: [src/trend\_pulse/server.py:1304](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L1304-L1377) · [src/trend\_pulse/sources/google\_trends.py:12](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/sources/google_trends.py#L12-L78) · [src/trend\_pulse/aggregator.py:55](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/aggregator.py#L55-L191)

<a id="tool-batch-score-content"></a>

### `batch_score_content`

Parse contents string as JSON list, retain first ten entries, ignore nonstrings, score concurrently and rank successes.

<details>
<summary>Full registered description</summary>

```text
Score multiple posts at once using the Hybrid Scoring 2.0 engine.

Accepts a JSON array of post strings and returns a scored ranking.
Useful for comparing multiple drafts before publishing.

Args:
    contents: JSON array of post strings, e.g. ["Post A text", "Post B text"].
              Max 10 posts per batch.
    platform: Target platform for format scoring (default: threads).

Returns:
    JSON with ranked list of posts by score, including dimension breakdowns.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `contents` | string | Yes | — | — | — |
| `platform` | string | No | `"threads"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "contents": {
      "title": "Contents",
      "type": "string"
    },
    "platform": {
      "default": "threads",
      "title": "Platform",
      "type": "string"
    }
  },
  "required": [
    "contents"
  ],
  "title": "batch_score_contentArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- contents remains string schema, not array; decoded value must be a list; first ten entries considered, nonstrings skipped; score exceptions omitted.

Sources: [src/trend\_pulse/server.py:1380](https://github.com/claude-world/trend-pulse/blob/d8e5fdbcf42cc02d0149ecb2b4ab1a93430c654e/src/trend_pulse/server.py#L1380-L1435)

## Schema provenance

AST enumerated all top-level @mcp.tool() functions; reproduced unchanged signatures, defaults, annotations, decorators and docstrings with inert bodies in isolated FastMCP, then locally awaited list_tools(). MCP 1.30.0, Pydantic 2.13.5. Implementations separately inspected. No source module import, credential reads or tool calls.

- Dependency range mcp[cli]>=1.0 is unbounded; schemas reflect installed MCP 1.30.0 and Pydantic 2.13.5, not every possible dependency version.
- Network source availability and credential-dependent execution not tested. Available plugin sources vary with optional dependencies, but all 29 MCP tools register unconditionally.
- Google Trends supports current country RSS trends only; historical analyses operate on local saved snapshots. Google Trends keyword search is not implemented.
