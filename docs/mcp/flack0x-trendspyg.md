# flack0x/trendspyg

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/flack0x/trendspyg) · [JSON definitions](../../data/mcp/flack0x-trendspyg.json)

Reviewed 2026-10-13 at commit [`9f07b2573e72`](https://github.com/flack0x/trendspyg/tree/9f07b2573e7287df85df9202da206569024723e9).

Compare live trends across regions, diff fresh observations, and query archived snapshots or keyword interest.

**9 tool definitions; 9 marked Google Trends.**

- Historical trending lookup covers only locally recorded observations. Enable archive on fresh fetches to build that history.
- The keyword-interest and full Trending Now CSV tools require a local Chrome browser; RSS tools do not.

## Tools

| Tool | Scope |
|---|---|
| [`get_trending_now`](#tool-get-trending-now) | google-trends |
| [`compare_trending`](#tool-compare-trending) | google-trends |
| [`get_trend_changes`](#tool-get-trend-changes) | google-trends |
| [`list_supported_options`](#tool-list-supported-options) | google-trends |
| [`get_interest_over_time`](#tool-get-interest-over-time) | google-trends |
| [`compare_interest_over_time`](#tool-compare-interest-over-time) | google-trends |
| [`get_trending_full`](#tool-get-trending-full) | google-trends |
| [`get_trending_history`](#tool-get-trending-history) | google-trends |
| [`suggest_keywords`](#tool-suggest-keywords) | google-trends |

<a id="tool-get-trending-now"></a>

### `get_trending_now`

Fetches current country/state Google Trends RSS feed as a normalized envelope; optional local archive writes.

<details>
<summary>Full registered description</summary>

```text
Get what is trending on Google right now for a country or US state.

Fast (typically 0.2-2s, no browser). Returns a normalized envelope with ~10-20
trends: keyword, rank, search volume (text + numeric minimum), start
time, related queries, news articles with sources, and an image.
geo examples: "US", "GB", "JP", "US-CA". Use list_supported_options
for the full list.
Pass archive=true from the first fetch to record fresh observations locally
for get_trending_history. Cached reads do not add history; use
get_trend_changes(archive=true) to record a fresh poll when needed.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string | No | `"US"` | — | — |
| `archive` | boolean | No | `false` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "geo": {
      "default": "US",
      "title": "Geo",
      "type": "string"
    },
    "archive": {
      "default": false,
      "title": "Archive",
      "type": "boolean"
    }
  },
  "title": "get_trending_nowArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation uppercases geo and requires membership in COUNTRIES or US\_STATES; schema is unrestricted string.

Sources: [trendspyg/mcp\_server.py:70](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L70-L86) · [trendspyg/mcp\_server.py:396](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L396-L454) · [trendspyg/rss\_downloader.py:340](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/rss_downloader.py#L340-L593)

<a id="tool-compare-trending"></a>

### `compare_trending`

Batch fetches country/state RSS envelopes; optional compact output removes news/images/related queries/URLs; optional local archiving.

<details>
<summary>Full registered description</summary>

```text
Get current Google trends for several countries/states in one call.

Fast (typically 0.2-2s per geo, no browser). Returns {geo: envelope} with the same
normalized shape as get_trending_now. Accepts 1-20 geo codes, e.g.
["US", "GB", "DE"]. The full envelopes are large (about 15 KB per geo:
news articles and images per trend) — pass compact=true to get only
keyword, rank, volume_min and is_active per trend (about 1 KB per geo),
which is enough to compare what is trending where.
Pass archive=true from the first fetch to record fresh observations locally
for get_trending_history. Cached reads do not add history; use
get_trend_changes(archive=true) to record a fresh poll when needed.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geos` | array of string | Yes | — | — | — |
| `compact` | boolean | No | `false` | — | — |
| `archive` | boolean | No | `false` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "geos": {
      "items": {
        "type": "string"
      },
      "title": "Geos",
      "type": "array"
    },
    "compact": {
      "default": false,
      "title": "Compact",
      "type": "boolean"
    },
    "archive": {
      "default": false,
      "title": "Archive",
      "type": "boolean"
    }
  },
  "required": [
    "geos"
  ],
  "title": "compare_trendingArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation requires 1–20 geos; input schema has no minItems/maxItems.
- Implementation uppercases geo and requires membership in COUNTRIES or US\_STATES; schema is unrestricted string.

Sources: [trendspyg/mcp\_server.py:111](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L111-L137) · [trendspyg/mcp\_server.py:396](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L396-L454) · [trendspyg/rss\_downloader.py:340](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/rss_downloader.py#L340-L372)

<a id="tool-get-trend-changes"></a>

### `get_trend_changes`

Fetches fresh RSS without cache and diffs against process-local last snapshot for the supplied geo; first call establishes baseline; optional local archiving.

<details>
<summary>Full registered description</summary>

```text
Report what changed in Google trends for a geo since this tool was last called.

Fast (typically 0.2-2s, no browser). The first call for a geo captures a baseline
and reports no changes; each later call returns events diffed against
the previous call: new, dropped, volume_up, volume_down, rank_change.
Useful for monitoring a topic over a conversation or scheduled runs.
Pass archive=true from the first fetch to record fresh observations locally
for get_trending_history. Cached reads do not add history; use
get_trend_changes(archive=true) to record a fresh poll when needed.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string | No | `"US"` | — | — |
| `archive` | boolean | No | `false` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "geo": {
      "default": "US",
      "title": "Geo",
      "type": "string"
    },
    "archive": {
      "default": false,
      "title": "Archive",
      "type": "boolean"
    }
  },
  "title": "get_trend_changesArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation uppercases geo and requires membership in COUNTRIES or US\_STATES; schema is unrestricted string.
- Baseline snapshot dictionary is keyed by caller-supplied geo before uppercasing in downloader.

Sources: [trendspyg/mcp\_server.py:140](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L140-L178) · [trendspyg/mcp\_server.py:396](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L396-L454) · [trendspyg/rss\_downloader.py:340](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/rss_downloader.py#L340-L593)

<a id="tool-list-supported-options"></a>

### `list_supported_options`

Returns local configured country/state codes, CSV categories/hour windows, and Explore timeframe examples without network.

<details>
<summary>Full registered description</summary>

```text
List every supported geo code plus the filters get_trending_full accepts.

Instant (no network). Returns 125 country codes, 51 US state codes,
the category keys and hour windows for get_trending_full, and
timeframe examples for get_interest_over_time.
```

</details>

No caller parameters.

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {},
  "title": "list_supported_optionsArguments",
  "type": "object"
}
```

</details>

Sources: [trendspyg/mcp\_server.py:181](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L181-L194) · [trendspyg/mcp\_server.py:396](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L396-L454) · [trendspyg/config.py:1](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/config.py#L1-L237)

<a id="tool-get-interest-over-time"></a>

### `get_interest_over_time`

Fetches keyword or topic-ID Google Explore time series using browser engine, local disk cache and disk cookies; returns date/value/is\_partial points.

<details>
<summary>Full registered description</summary>

```text
Get Google's 0-100 relative search interest for a keyword over time.

SLOW on a fresh fetch: drives a real Chrome browser against Google's
Explore page — typically 10-40 seconds. Page loads and widget requests
have timeouts, with a 44s browser-work budget between phases; driver
setup/download and cleanup add time. Requires Chrome on this machine; Google
rate-limits it aggressively — NEVER poll it or call it in a loop (roughly
8-10 fresh sessions in a short burst triggers Google's hard 429 block for
this machine's IP); if it fails with a rate-limit error, stop for tens of
minutes at least — do not retry. Repeating an
IDENTICAL request is instant: results come from a local disk cache while
fresh (up to 1h old for "now *" timeframes, 24h otherwise). Sessions
reuse Google's cookies (a small file beside the cache) so this machine
looks like one returning visitor — Google refuses new visitors first.
Returns [{date, value, is_partial}, ...]; a keyword Google has no data
for comes back as all zeros (Google's own answer). timeframe examples:
"now 7-d", "today 12-m", "today 5-y", "all". gprop selects the Google
property: "" (web search, default), "youtube" (YouTube search interest),
"images", "news", or "froogle" (Google Shopping).
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | — | — |
| `geo` | string | No | `"US"` | — | — |
| `timeframe` | string | No | `"today 12-m"` | — | — |
| `gprop` | string | No | `""` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "title": "Keyword",
      "type": "string"
    },
    "geo": {
      "default": "US",
      "title": "Geo",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "title": "Timeframe",
      "type": "string"
    },
    "gprop": {
      "default": "",
      "title": "Gprop",
      "type": "string"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "get_interest_over_timeArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Non-empty stripped keyword strings required; geo may be empty for worldwide, otherwise uppercase country/state membership validation.
- Implementation accepts gprop '', 'web' (normalized to ''), 'images', 'news', 'youtube', 'froogle'; schema has no enum.
- timeframe is forwarded as a Google date-range string; no schema enum or explicit timeframe syntax validator.

Sources: [trendspyg/mcp\_server.py:197](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L197-L231) · [trendspyg/mcp\_server.py:396](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L396-L454) · [trendspyg/explore/\_\_init\_\_.py:788](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/explore/__init__.py#L788-L832) · [trendspyg/explore/\_\_init\_\_.py:321](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/explore/__init__.py#L321-L336) · [trendspyg/downloader.py:181](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/downloader.py#L181-L214)

<a id="tool-compare-interest-over-time"></a>

### `compare_interest_over_time`

Fetches 2–5 keyword/topic-ID Google Explore comparison on one shared 0–100 scale using browser, disk cache and cookies; disables regional output.

<details>
<summary>Full registered description</summary>

```text
Compare 2-5 keywords' search interest on ONE shared 0-100 scale.

Use this (not repeated get_interest_over_time calls) to compare terms:
Google scales each single-keyword series independently, so only this
comparison returns directly comparable numbers. SLOW on a fresh fetch:
drives a real Chrome browser — typically 10-40 seconds (fail-fast retry
profile; 44s browser-work budget between phases, plus driver setup and cleanup).
Requires Chrome on this machine; rate-limited by Google — NEVER poll it
or call it in a loop (roughly 8-10 fresh sessions in a short burst
triggers Google's hard 429 block for this machine's IP; a rate-limit
error means stop for tens of minutes at least, not retry). Repeating an
IDENTICAL comparison is instant:
results come from a local disk cache while fresh (up to 1h old for
"now *" timeframes, 24h otherwise). Returns {keywords, averages:
{kw: 0-100}, interest_over_time: [{date, values: {kw: 0-100},
is_partial}], ...}. keywords: 2-5 distinct terms, no commas. timeframe
examples: "now 7-d", "today 12-m", "today 5-y". gprop selects the Google
property: "" (web, default), "youtube", "images", "news", "froogle".
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | — | — |
| `geo` | string | No | `"US"` | — | — |
| `timeframe` | string | No | `"today 12-m"` | — | — |
| `gprop` | string | No | `""` | — | — |

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
    "geo": {
      "default": "US",
      "title": "Geo",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "title": "Timeframe",
      "type": "string"
    },
    "gprop": {
      "default": "",
      "title": "Gprop",
      "type": "string"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "compare_interest_over_timeArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation strips terms; requires 2–5 non-empty distinct keywords (case-insensitive uniqueness), rejecting commas; schema has no minItems/maxItems/uniqueItems.
- Implementation accepts gprop '', 'web' (normalized to ''), 'images', 'news', 'youtube', 'froogle'; schema has no enum.
- timeframe is forwarded as a Google date-range string; no schema enum or explicit timeframe syntax validator.
- geo may be empty for worldwide; otherwise uppercase country/state membership validation.

Sources: [trendspyg/mcp\_server.py:234](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L234-L271) · [trendspyg/mcp\_server.py:396](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L396-L454) · [trendspyg/explore/\_\_init\_\_.py:225](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/explore/__init__.py#L225-L268) · [trendspyg/explore/\_\_init\_\_.py:961](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/explore/__init__.py#L961-L996) · [trendspyg/explore/\_\_init\_\_.py:321](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/explore/__init__.py#L321-L336)

<a id="tool-get-trending-full"></a>

### `get_trending_full`

Downloads complete Google Trending Now CSV via Chrome with country/state, hours and category filters; normalizes envelope and cleans temporary download directory; optional archiving.

<details>
<summary>Full registered description</summary>

```text
Get the full trending list (480+ trends) with time and category filters.

SLOW: drives a real Chrome browser (~10-15 seconds, requires Chrome on
this machine). Use only when get_trending_now's ~20 trends are not
enough or you need category/time filtering. hours: 4, 24, 48 or 168.
category examples: "all", "sports", "entertainment" — see
list_supported_options. Returns the same normalized envelope shape as
get_trending_now.
Pass archive=true from the first fetch to record fresh observations locally
for get_trending_history. Cached reads do not add history; use
get_trend_changes(archive=true) to record a fresh poll when needed.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string | No | `"US"` | — | — |
| `hours` | integer | No | `24` | — | — |
| `category` | string | No | `"all"` | — | — |
| `archive` | boolean | No | `false` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "geo": {
      "default": "US",
      "title": "Geo",
      "type": "string"
    },
    "hours": {
      "default": 24,
      "title": "Hours",
      "type": "integer"
    },
    "category": {
      "default": "all",
      "title": "Category",
      "type": "string"
    },
    "archive": {
      "default": false,
      "title": "Archive",
      "type": "boolean"
    }
  },
  "title": "get_trending_fullArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation uppercases geo and requires membership in COUNTRIES or US\_STATES; schema is unrestricted string.
- Implementation accepts hours 4,24,48,168 only; schema has no enum.
- Implementation lowercases category and requires configured CATEGORIES membership; schema has no enum.

Sources: [trendspyg/mcp\_server.py:274](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L274-L304) · [trendspyg/mcp\_server.py:396](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L396-L454) · [trendspyg/downloader.py:181](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/downloader.py#L181-L270) · [trendspyg/downloader.py:398](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/downloader.py#L398-L400)

<a id="tool-get-trending-history"></a>

### `get_trending_history`

Reads only locally archived RSS/CSV snapshots, optionally filtered by geo/keyword/time; returns compact newest-first snapshots and keyword appearance timeline; never reconstructs Google historical data.

<details>
<summary>Full registered description</summary>

```text
Get what WAS trending on past dates, from this machine's local archive.

Instant, no network, no browser — reads snapshots that earlier fetches
recorded locally (fetch tools with archive=true, library archive=True,
CLI --archive). Google offers no
such history; it exists only if it was recorded here, so an empty result
means "nothing was archived for these filters", not "nothing trended".
Snapshots are compact: keyword, rank and minimum search volume per trend
(newest snapshot first). If keyword is given, also returns that keyword's
appearance timeline, oldest first — "when did X first trend?".
start/end are ISO 8601 times like "2026-08-01". limit: 1-100 snapshots.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string / null | No | `null` | — | — |
| `keyword` | string / null | No | `null` | — | — |
| `start` | string / null | No | `null` | — | — |
| `end` | string / null | No | `null` | — | — |
| `limit` | integer | No | `10` | — | — |

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
      "title": "Geo"
    },
    "keyword": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Keyword"
    },
    "start": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Start"
    },
    "end": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "End"
    },
    "limit": {
      "default": 10,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "get_trending_historyArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation enforces limit 1–100; schema has no minimum/maximum.
- start/end must be non-empty strings when supplied; they are stripped and compared lexically as stored ISO timestamps, with no actual ISO parsing.
- Archive geo filtering uses exact supplied text, without uppercasing or configured geo validation.

Sources: [trendspyg/mcp\_server.py:307](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L307-L371) · [trendspyg/mcp\_server.py:396](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L396-L454) · [trendspyg/archive.py:361](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/archive.py#L361-L402) · [trendspyg/archive.py:406](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/archive.py#L406-L469) · [trendspyg/archive.py:492](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/archive.py#L492-L556)

<a id="tool-suggest-keywords"></a>

### `suggest_keywords`

Uses Google Trends HTTP topic suggestions lookup with one-hour process cache, returning matching topic IDs/title/type and query/language/count; no automatic topic selection.

<details>
<summary>Full registered description</summary>

```text
Find Google Trends topic IDs and meanings before choosing a research query.

No Chrome: a single HTTP lookup with one-hour caching in this server process.
Returns {query, language, count, suggestions: [{mid, title, type}]}.
Language controls the displayed labels, not a later analysis's geography.
Select the intended meaning explicitly (e.g. Apple/Fruit versus
Apple/Technology company), then pass its mid to get_interest_over_time or
compare_interest_over_time. Retain the ID-to-label mapping in your answer.
These are matching suggestions, not related searches or a popularity ranking;
count=0 means no candidates were offered, not zero search interest.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keyword` | string | Yes | — | — | — |
| `language` | string | No | `"en-US"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "keyword": {
      "title": "Keyword",
      "type": "string"
    },
    "language": {
      "default": "en-US",
      "title": "Language",
      "type": "string"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "suggest_keywordsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation strips keyword and rejects empty/whitespace-only strings.
- language must match ^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})\*$; schema has no pattern.

Sources: [trendspyg/mcp\_server.py:374](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L374-L392) · [trendspyg/mcp\_server.py:396](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/mcp_server.py#L396-L454) · [trendspyg/keywords.py:16](https://github.com/flack0x/trendspyg/blob/9f07b2573e7287df85df9202da206569024723e9/trendspyg/keywords.py#L16-L113)

## Schema provenance

Local build_server().list_tools() without tool execution: MCP SDK 2.3.0 and fallback SDK 1.30.0, Python 3.14, Pydantic 2.14.1. Complete registered descriptions and input schemas match across both SDK branches. Source inspection of _TOOLS registration and implementations.

- No live Google requests or tool implementations executed; browser/network behavior verified by source inspection.
