# david-wulf/trends-mcp-local

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/david-wulf/trends-mcp-local) · [JSON definitions](../../data/mcp/david-wulf-trends-mcp-local.json)

Reviewed 2026-10-13 at commit [`1349b49e28a4`](https://github.com/david-wulf/trends-mcp-local/tree/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0).

Resolve topic IDs, compare search properties, and discover category or regional demand.

**22 tool definitions; 7 marked Google Trends.**

- Google Trends Explore supports trendspy or DataForSEO backends; current trending searches always use trendspy. DataForSEO’s own demography/subregion datasets are not Google Trends.
- Default locale is German/DE; language and geo are caller parameters where registered.

## Tools

| Tool | Scope |
|---|---|
| [`gt_resolve_topic`](#tool-gt-resolve-topic) | google-trends |
| [`gt_topic_across_properties`](#tool-gt-topic-across-properties) | google-trends |
| [`gt_compare`](#tool-gt-compare) | google-trends |
| [`gt_interest_by_region`](#tool-gt-interest-by-region) | google-trends |
| [`gt_categories`](#tool-gt-categories) | google-trends |
| [`gt_discover_category`](#tool-gt-discover-category) | google-trends |
| [`gt_trending_now`](#tool-gt-trending-now) | google-trends |
| [`gt_backend`](#tool-gt-backend) | server-management |
| [`gt_cache`](#tool-gt-cache) | server-management |
| [`dfs_demography`](#tool-dfs-demography) | other |
| [`dfs_subregion_interests`](#tool-dfs-subregion-interests) | other |
| [`news_search`](#tool-news-search) | news |
| [`news_headlines`](#tool-news-headlines) | news |
| [`yt_search`](#tool-yt-search) | other |
| [`yt_trending`](#tool-yt-trending) | other |
| [`yt_video_stats`](#tool-yt-video-stats) | other |
| [`yt_categories`](#tool-yt-categories) | other |
| [`reddit_search`](#tool-reddit-search) | other |
| [`reddit_rising`](#tool-reddit-rising) | other |
| [`reddit_hot`](#tool-reddit-hot) | other |
| [`reddit_top`](#tool-reddit-top) | other |
| [`reddit_find_subreddits`](#tool-reddit-find-subreddits) | other |

<a id="tool-gt-resolve-topic"></a>

### `gt_resolve_topic`

Resolves a keyword to up to eight Google Trends topic candidates using trendspy suggestions or DataForSEO Google Trends Explore topics; cached 30 days.

<details>
<summary>Full registered description</summary>

```text
SUCHE 1 (Schritt 1): Begriff in ein Google-Trends-Thema aufloesen.

Gibt Kandidaten mit 'mid' (z. B. '/m/0bwlch6', '/g/11v0b99rt0'), Titel und
Typ zurueck. Immer zuerst aufrufen und die 'mid' des besten Topics als
'topic' fuer gt_topic_across_properties verwenden, damit ueber das *Thema*
(Entitaet) statt ueber einen mehrdeutigen Suchbegriff gemessen wird.

'geo' wirkt nur im DataForSEO-Backend (die Auflösung kommt dort aus der
Topics-Liste eines Explore-Requests und ist regional). 30 Tage gecacht.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `thema` | string | Yes | — | — | — |
| `language` | string | No | `"de"` | — | — |
| `geo` | string | No | `"DE"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "thema": {
      "title": "Thema",
      "type": "string"
    },
    "language": {
      "default": "de",
      "title": "Language",
      "type": "string"
    },
    "geo": {
      "default": "DE",
      "title": "Geo",
      "type": "string"
    }
  },
  "required": [
    "thema"
  ],
  "title": "gt_resolve_topicArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- DataForSEO accepts source-defined relative timeframes, all, or two YYYY-MM-DD tokens; unsupported values may fall back to trendspy unless DataForSEO explicitly forced. Geo translation uses provider location codes.

Sources: [server.py:62](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L62-L74) · [trends\_mcp/gtrends.py:1172](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L1172-L1183) · [trends\_mcp/gtrends.py:191](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L191-L215) · [trends\_mcp/gtrends.py:259](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L259-L279) · [trends\_mcp/gtrends.py:837](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L837-L888)

<a id="tool-gt-topic-across-properties"></a>

### `gt_topic_across_properties`

Obtains separately normalized Google Trends time series per property and computes spike/outlier analysis; optionally omits series.

<details>
<summary>Full registered description</summary>

```text
SUCHE 1: Interesse eines Themas ueber die verschiedenen Google-Suchen hinweg.

Misst das Thema (mid aus gt_resolve_topic oder Keyword) in mehreren
Google-Properties. Liefert je Property die 0-100-Zeitreihe plus
Ausreisser-/Spike-Analyse (Peak, aktueller Wert, Ausreisser mit Z-Wert).

properties: None = ['web','news'] (Discover-relevant, schnell); volle
Liste: ['web','youtube','news','images','shopping']. include_series=False
liefert nur die kompakte Analyse (fuer Massen-Screenings). timeframe z. B.
'today 12-m', 'today 5-y', 'now 7-d' (stuendlich, mit Uhrzeit).
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `topic` | string | Yes | — | — | — |
| `geo` | string | No | `"DE"` | — | — |
| `timeframe` | string | No | `"today 12-m"` | — | — |
| `category` | integer | No | `0` | — | — |
| `properties` | array of string / null | No | `null` | — | — |
| `include_series` | boolean | No | `true` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "topic": {
      "title": "Topic",
      "type": "string"
    },
    "geo": {
      "default": "DE",
      "title": "Geo",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "title": "Timeframe",
      "type": "string"
    },
    "category": {
      "default": 0,
      "title": "Category",
      "type": "integer"
    },
    "properties": {
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
      "title": "Properties"
    },
    "include_series": {
      "default": true,
      "title": "Include Series",
      "type": "boolean"
    }
  },
  "required": [
    "topic"
  ],
  "title": "gt_topic_across_propertiesArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation accepts web, youtube, news, images, shopping (trimmed/lowercased); unknown properties return errors. Nullable/empty properties selects default web/news.
- DataForSEO accepts source-defined relative timeframes, all, or two YYYY-MM-DD tokens; unsupported values may fall back to trendspy unless DataForSEO explicitly forced. Geo translation uses provider location codes.

Sources: [server.py:77](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L77-L100) · [trends\_mcp/gtrends.py:1186](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L1186-L1204) · [trends\_mcp/gtrends.py:191](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L191-L215) · [trends\_mcp/gtrends.py:300](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L300-L389) · [trends\_mcp/gtrends.py:891](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L891-L961)

<a id="tool-gt-compare"></a>

### `gt_compare`

Compares up to five keywords/topic IDs in one jointly normalized Google Trends time series request and ranks current interest.

<details>
<summary>Full registered description</summary>

```text
Bis zu 5 Keywords/Themen-mids in EINEM Request direkt vergleichen.

Die 0-100-Skala ist ueber alle Keywords gemeinsam normiert - ideal, um
Themen-Kandidaten fuer Discover-Artikel zu priorisieren ('welches Thema
zieht gerade am staerksten?'). Liefert je Keyword Zeitreihe + Analyse
plus ein Ranking nach aktuellem Interesse.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | — | — |
| `geo` | string | No | `"DE"` | — | — |
| `timeframe` | string | No | `"today 3-m"` | — | — |
| `category` | integer | No | `0` | — | — |
| `gprop` | string | No | `"web"` | — | — |
| `include_series` | boolean | No | `true` | — | — |

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
      "default": "DE",
      "title": "Geo",
      "type": "string"
    },
    "timeframe": {
      "default": "today 3-m",
      "title": "Timeframe",
      "type": "string"
    },
    "category": {
      "default": 0,
      "title": "Category",
      "type": "integer"
    },
    "gprop": {
      "default": "web",
      "title": "Gprop",
      "type": "string"
    },
    "include_series": {
      "default": true,
      "title": "Include Series",
      "type": "boolean"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "gt_compareArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation drops blank keywords, truncates to first five, and rejects an empty effective list; no schema maxItems/minItems.
- Implementation accepts web, youtube, news, images, shopping (trimmed/lowercased); unknown properties return errors.
- DataForSEO accepts source-defined relative timeframes, all, or two YYYY-MM-DD tokens; unsupported values may fall back to trendspy unless DataForSEO explicitly forced. Geo translation uses provider location codes.

Sources: [server.py:103](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L103-L122) · [trends\_mcp/gtrends.py:1207](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L1207-L1219) · [trends\_mcp/gtrends.py:191](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L191-L215) · [trends\_mcp/gtrends.py:392](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L392-L462) · [trends\_mcp/gtrends.py:964](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L964-L1045)

<a id="tool-gt-interest-by-region"></a>

### `gt_interest_by_region`

Retrieves Google Trends regional interest; removes zero values, sorts descending, and limits results.

<details>
<summary>Full registered description</summary>

```text
Regionale Verteilung des Interesses fuer ein Thema (Ausreisser-Regionen).

Absteigend nach Interesse sortiert, Null-Regionen entfernt, auf 'limit'
gekuerzt.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `topic` | string | Yes | — | — | — |
| `geo` | string | No | `"DE"` | — | — |
| `timeframe` | string | No | `"today 12-m"` | — | — |
| `category` | integer | No | `0` | — | — |
| `gprop` | string | No | `"web"` | — | — |
| `limit` | integer | No | `25` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "topic": {
      "title": "Topic",
      "type": "string"
    },
    "geo": {
      "default": "DE",
      "title": "Geo",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "title": "Timeframe",
      "type": "string"
    },
    "category": {
      "default": 0,
      "title": "Category",
      "type": "integer"
    },
    "gprop": {
      "default": "web",
      "title": "Gprop",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "topic"
  ],
  "title": "gt_interest_by_regionArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation accepts web, youtube, news, images, shopping (trimmed/lowercased); unknown properties return errors.
- Implementation applies max(1, limit) when slicing output; no schema lower bound.
- DataForSEO accepts source-defined relative timeframes, all, or two YYYY-MM-DD tokens; unsupported values may fall back to trendspy unless DataForSEO explicitly forced. Geo translation uses provider location codes.

Sources: [server.py:125](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L125-L141) · [trends\_mcp/gtrends.py:1222](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L1222-L1234) · [trends\_mcp/gtrends.py:191](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L191-L215) · [trends\_mcp/gtrends.py:465](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L465-L529) · [trends\_mcp/gtrends.py:1048](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L1048-L1097)

<a id="tool-gt-categories"></a>

### `gt_categories`

Searches cached Google Trends category trees across requested language and English; falls back to DataForSEO category metadata.

<details>
<summary>Full registered description</summary>

```text
SUCHE 2 (Schritt 1): Kategorie-Baum von Google Trends durchsuchen.

Der Baum hat ~1133 Eintraege - Haupt- UND Unterkategorien (z. B.
'Home & Garden'=11 und die Unterkategorien 'Home Appliances'=271,
'Home Furnishings'=270). Jede 'id' - auch die einer Unterkategorie - ist
direkt als 'category' in gt_topic_across_properties und
gt_discover_category verwendbar.

WICHTIG zu 'find': Die Kategorienamen stehen in der gewaehlten 'language'
(bei language='de' also 'Erneuerbare und alternative Energien', nicht
'Renewable & Alternative Energy'). Damit eine englische Suche trotzdem
trifft, matcht 'find' gegen BEIDE Baeume - find='Energy' und find='Energie'
liefern dieselben ids (233, 954, 657). Die ids sind sprachunabhaengig.
Jeder Treffer enthaelt 'name' (Zielsprache) und 'name_en'.

Bei 0 Treffern also nicht auf category=0 zurueckfallen, sondern ein
kuerzeres Stichwort probieren ('Solar' statt 'Solaranlage').
Der Baum ist 30 Tage gecacht (wiederholte Aufrufe sind gratis).
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `find` | string / null | No | `null` | — | — |
| `language` | string | No | `"de"` | — | — |
| `limit` | integer | No | `100` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "find": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Find"
    },
    "language": {
      "default": "de",
      "title": "Language",
      "type": "string"
    },
    "limit": {
      "default": 100,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "gt_categoriesArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation applies max(1, limit) when slicing output; no schema lower bound.

Sources: [server.py:144](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L144-L164) · [trends\_mcp/gtrends.py:563](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L563-L666) · [trends\_mcp/gtrends.py:191](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L191-L215)

<a id="tool-gt-discover-category"></a>

### `gt_discover_category`

Obtains rising/top related topics and queries for category and optional seed; DataForSEO Google Trends Explore with seed, trendspy fallback otherwise unless paid backend forced.

<details>
<summary>Full registered description</summary>

```text
SUCHE 2: Klassisches Entdecken innerhalb einer (Unter-)Kategorie.

seed='' = reine Kategorie-Entdeckung (wie 'nur Kategorie gewaehlt' in der
Google-Trends-Oberflaeche). Optional Seed-Keyword setzen, um innerhalb der
Kategorie zu fokussieren. Liefert aufsteigende (rising) und Top-Themen sowie
-Suchanfragen.

gprop waehlt die Art der Suche: 'web' (Default), 'youtube', 'news',
'images', 'shopping'. Damit gibt es auch fuer Shopping und YouTube echte
Queries statt nur Interessekurven. Ein unbekannter Wert wird abgewiesen und
faellt NICHT still auf 'web' zurueck.

Backend-Hinweis: MIT Seed laeuft das ueber DataForSEO - Queries und Topics
kommen dann in EINEM Request ($0,011 zusammen) und ohne Quota-Risiko. OHNE
Seed (reine Kategorie-Entdeckung) kann DataForSEO nicht helfen, weil dort
ein Keyword Pflicht ist; dann uebernimmt trendspy mit dem bekannten
Google-Kontingent. Ergebnisse werden 6 Stunden gecacht; bei erschoepftem
Kontingent kommt automatisch der letzte bekannte Stand mit
'cache': {'stale': true, 'age_min': ...} zurueck, statt dass der Aufruf
scheitert.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `category` | integer | Yes | — | — | — |
| `geo` | string | No | `"DE"` | — | — |
| `timeframe` | string | No | `"today 3-m"` | — | — |
| `seed` | string | No | `""` | — | — |
| `language` | string | No | `"de"` | — | — |
| `gprop` | string | No | `"web"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "category": {
      "title": "Category",
      "type": "integer"
    },
    "geo": {
      "default": "DE",
      "title": "Geo",
      "type": "string"
    },
    "timeframe": {
      "default": "today 3-m",
      "title": "Timeframe",
      "type": "string"
    },
    "seed": {
      "default": "",
      "title": "Seed",
      "type": "string"
    },
    "language": {
      "default": "de",
      "title": "Language",
      "type": "string"
    },
    "gprop": {
      "default": "web",
      "title": "Gprop",
      "type": "string"
    }
  },
  "required": [
    "category"
  ],
  "title": "gt_discover_categoryArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation accepts web, youtube, news, images, shopping (trimmed/lowercased); unknown properties return errors.
- DataForSEO accepts source-defined relative timeframes, all, or two YYYY-MM-DD tokens; unsupported values may fall back to trendspy unless DataForSEO explicitly forced. Geo translation uses provider location codes.

Sources: [server.py:167](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L167-L199) · [trends\_mcp/gtrends.py:1237](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L1237-L1255) · [trends\_mcp/gtrends.py:191](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L191-L215) · [trends\_mcp/gtrends.py:669](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L669-L754) · [trends\_mcp/gtrends.py:1100](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L1100-L1166)

<a id="tool-gt-trending-now"></a>

### `gt_trending_now`

Obtains current Google Trends searches using trendspy only; sorts by growth and volume, filters category substring, and limits output; quota failures may return stale cache.

<details>
<summary>Full registered description</summary>

```text
SUCHE 2: Aktuell trendende Suchen mit Volumen und Wachstum in Prozent.

Robuster Einstieg ins 'Trends entdecken'. Optional per 'category' (Name)
filtern - Google liefert diese Namen in der Regel englisch aus, auch bei
language='de' ('Sports', 'Politics', 'Entertainment', 'Other'). Bei 0
Treffern listet der 'hinweis' die tatsaechlich vorhandenen Namen auf.
'hours_since_started' ist das Alter des Trends in Stunden.
30 Minuten gecacht.

Laeuft IMMER ueber trendspy: DataForSEO hat fuer 'Trends jetzt' keinen
Endpunkt. Bei erschoepftem Kontingent kommt hier also weiterhin der
Stale-Cache.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `geo` | string | No | `"DE"` | — | — |
| `language` | string | No | `"de"` | — | — |
| `hours` | integer | No | `24` | — | — |
| `category` | string / null | No | `null` | — | — |
| `limit` | integer | No | `40` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "geo": {
      "default": "DE",
      "title": "Geo",
      "type": "string"
    },
    "language": {
      "default": "de",
      "title": "Language",
      "type": "string"
    },
    "hours": {
      "default": 24,
      "title": "Hours",
      "type": "integer"
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
      "title": "Category"
    },
    "limit": {
      "default": 40,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "gt_trending_nowArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation applies max(1, limit) when slicing output; no schema lower bound.

Sources: [server.py:202](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L202-L219) · [trends\_mcp/gtrends.py:757](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L757-L831) · [trends\_mcp/gtrends.py:191](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L191-L215)

<a id="tool-gt-backend"></a>

### `gt_backend`

Reports configured backend, availability of credentials (without revealing them), source-defined prices, and local cost ledger summary.

<details>
<summary>Full registered description</summary>

```text
Welches Trends-Backend ist aktiv, und was hat DataForSEO bisher gekostet.

Zeigt die Wirkung von TRENDS_BACKEND ('auto' | 'dataforseo' | 'trendspy'),
ob Zugangsdaten vorhanden sind, die Preise pro Request und die Ausgaben der
letzten 30 Tage (Summe, je Endpunkt, je Tag). Gratis - liest nur die lokale
Cache-DB.
```

</details>

No caller parameters.

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {},
  "title": "gt_backendArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.

Sources: [server.py:222](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L222-L231) · [trends\_mcp/gtrends.py:170](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L170-L188) · [trends\_mcp/gtrends.py:191](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/gtrends.py#L191-L215)

<a id="tool-gt-cache"></a>

### `gt_cache`

Reads SQLite cache statistics or costs, or clears selected namespace/all cache entries.

<details>
<summary>Full registered description</summary>

```text
Wartung des Trends-Caches (SQLite, ueberlebt Neustarts) + Kostenledger.

action='stats' zeigt Eintraege, TTL und Alter pro Namespace.
action='cost' zeigt die DataForSEO-Ausgaben der letzten 'days' Tage.
action='clear' leert alles oder - mit 'namespace' - nur einen Bereich
('suggestions', 'categories', 'iot', 'compare', 'ibr', 'related_queries',
'related_topics', 'trending_now', 'dfs_discover', 'dfs_locations',
'dfs_categories'), um frische Daten zu erzwingen.

Achtung: 'clear' auf einen Namespace, der ueber DataForSEO gefuellt wurde,
bedeutet, dass die naechsten Aufrufe wieder echtes Geld kosten.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `action` | string | No | `"stats"` | — | — |
| `namespace` | string / null | No | `null` | — | — |
| `days` | integer | No | `30` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "action": {
      "default": "stats",
      "title": "Action",
      "type": "string"
    },
    "namespace": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Namespace"
    },
    "days": {
      "default": 30,
      "title": "Days",
      "type": "integer"
    }
  },
  "title": "gt_cacheArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- action is normalized and dispatched for stats/cost/clear; other values return an error. Cost lookback uses max(1, days). Namespace has no schema enumeration.

Sources: [server.py:234](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L234-L255) · [trends\_mcp/cache.py:300](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/cache.py#L300-L326)

<a id="tool-dfs-demography"></a>

### `dfs_demography`

Retrieves age/gender demand distributions from DataForSEO own clickstream Trends, explicitly not Google Trends.

<details>
<summary>Full registered description</summary>

```text
Alters- und Geschlechtsverteilung der Nachfrage je Keyword ($0,0024).

Diese Zahlen stammen NICHT von Google Trends - Google gibt Demografie per
API nicht heraus. Es ist DataForSEOs eigene Clickstream-Mischmetrik
(0-100 normiert, typischerweise einige Wochen Verzug). Nie mit
Google-Trends-Kurven in eine Grafik legen; taugt fuer die
Zielgruppen-Einordnung ('wer sucht das?'), nicht fuer Zeitverlaeufe.

gprop: 'web' (Default), 'news' oder 'shopping'. Bis 5 Keywords.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | — | — |
| `geo` | string | No | `"DE"` | — | — |
| `timeframe` | string | No | `"today 12-m"` | — | — |
| `gprop` | string | No | `"web"` | — | — |

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
      "default": "DE",
      "title": "Geo",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "title": "Timeframe",
      "type": "string"
    },
    "gprop": {
      "default": "web",
      "title": "Gprop",
      "type": "string"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "dfs_demographyArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation drops blank keywords, truncates to first five, and rejects an empty effective list; no schema maxItems/minItems.
- Wrapper uses PROPERTIES.get(gprop, ""): unknown gprop silently becomes web; own Trends accepts only web/news/shopping and rejects mapped youtube/images.

Sources: [server.py:262](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L262-L282) · [trends\_mcp/dfs.py:458](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/dfs.py#L458-L482)

<a id="tool-dfs-subregion-interests"></a>

### `dfs_subregion_interests`

Retrieves regional demand from DataForSEO own Trends, explicitly not Google Trends, sorts descending and limits output.

<details>
<summary>Full registered description</summary>

```text
Regionale Nachfrage aus DataForSEO-eigenen Daten ($0,0024) - Zweitmeinung.

Fuer 'wo ist das Thema stark?' ist gt_interest_by_region die erste Wahl
(echte Google-Trends-Map). Dieser Endpunkt ist die guenstigere Zweitquelle
mit anderer Metrik und mehrwoechigem Verzug - nur fuer einen Quervergleich
nutzen und Werte nicht mit Google-Trends mischen.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | — | — |
| `geo` | string | No | `"DE"` | — | — |
| `timeframe` | string | No | `"today 12-m"` | — | — |
| `gprop` | string | No | `"web"` | — | — |
| `limit` | integer | No | `25` | — | — |

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
      "default": "DE",
      "title": "Geo",
      "type": "string"
    },
    "timeframe": {
      "default": "today 12-m",
      "title": "Timeframe",
      "type": "string"
    },
    "gprop": {
      "default": "web",
      "title": "Gprop",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "dfs_subregion_interestsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation drops blank keywords, truncates to first five, and rejects an empty effective list; no schema maxItems/minItems.
- Wrapper uses PROPERTIES.get(gprop, ""): unknown gprop silently becomes web; own Trends accepts only web/news/shopping and rejects mapped youtube/images.
- Implementation applies max(1, limit) when slicing output; no schema lower bound.

Sources: [server.py:285](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L285-L306) · [trends\_mcp/dfs.py:485](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/dfs.py#L485-L516)

<a id="tool-news-search"></a>

### `news_search`

Searches public Google News RSS with optional when query filter; cleans/deduplicates headlines and counts recurring terms; links are Google News redirects.

<details>
<summary>Full registered description</summary>

```text
Google-News-Suche zu einem Thema -> Schlagzeilen als Content-Ideen (Titel).

Ergaenzt die Trends-Analyse um konkrete redaktionelle Aufhaenger: liefert
saubere Titel (Quelle abgetrennt), Quelle, Datum, Link sowie haeufige
Begriffe (idea_keywords). 'when' als Recency-Filter, z. B. '1d', '7d', '24h'.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `thema` | string | Yes | — | — | — |
| `language` | string | No | `"de"` | — | — |
| `country` | string | No | `"DE"` | — | — |
| `when` | string / null | No | `null` | — | — |
| `max_results` | integer | No | `25` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "thema": {
      "title": "Thema",
      "type": "string"
    },
    "language": {
      "default": "de",
      "title": "Language",
      "type": "string"
    },
    "country": {
      "default": "DE",
      "title": "Country",
      "type": "string"
    },
    "when": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "When"
    },
    "max_results": {
      "default": 25,
      "title": "Max Results",
      "type": "integer"
    }
  },
  "required": [
    "thema"
  ],
  "title": "news_searchArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation clamps max\_results to 1..100; no schema bounds.

Sources: [server.py:313](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L313-L327) · [trends\_mcp/news.py:95](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/news.py#L95-L124)

<a id="tool-news-headlines"></a>

### `news_headlines`

Fetches general or section Google News RSS headlines for country/language; cleans and deduplicates titles.

<details>
<summary>Full registered description</summary>

```text
Aktuelle Top-Schlagzeilen eines Landes oder News-Ressorts.

topic leer = allgemeine Top-News; sonst Ressort-Kuerzel wie 'TECHNOLOGY',
'BUSINESS', 'SCIENCE', 'HEALTH', 'ENTERTAINMENT', 'SPORTS'.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `topic` | string | No | `""` | — | — |
| `language` | string | No | `"de"` | — | — |
| `country` | string | No | `"DE"` | — | — |
| `max_results` | integer | No | `25` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "topic": {
      "default": "",
      "title": "Topic",
      "type": "string"
    },
    "language": {
      "default": "de",
      "title": "Language",
      "type": "string"
    },
    "country": {
      "default": "DE",
      "title": "Country",
      "type": "string"
    },
    "max_results": {
      "default": 25,
      "title": "Max Results",
      "type": "integer"
    }
  },
  "title": "news_headlinesArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation clamps max\_results to 1..100; no schema bounds.

Sources: [server.py:330](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L330-L337) · [trends\_mcp/news.py:127](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/news.py#L127-L149)

<a id="tool-yt-search"></a>

### `yt_search`

Uses YouTube Data API search plus statistics lookup to return videos and actual view/like counts.

<details>
<summary>Full registered description</summary>

```text
YouTube-Videos zu einem Keyword suchen (mit echten View-/Like-Zahlen).

order: 'relevance' | 'date' | 'viewCount' | 'rating' | 'title'.
published_after: ISO 8601 (z. B. '2026-01-01T00:00:00Z'), fuer 'nur neue'.
Kostet 100 Quota-Einheiten pro Aufruf.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `query` | string | Yes | — | — | — |
| `region` | string | No | `"DE"` | — | — |
| `language` | string | No | `"de"` | — | — |
| `max_results` | integer | No | `25` | — | — |
| `order` | string | No | `"relevance"` | — | — |
| `published_after` | string / null | No | `null` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "region": {
      "default": "DE",
      "title": "Region",
      "type": "string"
    },
    "language": {
      "default": "de",
      "title": "Language",
      "type": "string"
    },
    "max_results": {
      "default": 25,
      "title": "Max Results",
      "type": "integer"
    },
    "order": {
      "default": "relevance",
      "title": "Order",
      "type": "string"
    },
    "published_after": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Published After"
    }
  },
  "required": [
    "query"
  ],
  "title": "yt_searchArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation clamps max\_results to 1..50; order/date/category validation is delegated to Google API; description values are not schema enums.

Sources: [server.py:344](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L344-L362) · [trends\_mcp/youtube.py:78](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/youtube.py#L78-L124)

<a id="tool-yt-trending"></a>

### `yt_trending`

Uses YouTube videos.list mostPopular chart with optional category and returns video statistics.

<details>
<summary>Full registered description</summary>

```text
Aktuell populaere YouTube-Videos einer Region (chart=mostPopular).

Optional category_id (siehe yt_categories). Kostet 1 Quota-Einheit.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `region` | string | No | `"DE"` | — | — |
| `category_id` | string / null | No | `null` | — | — |
| `max_results` | integer | No | `25` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "region": {
      "default": "DE",
      "title": "Region",
      "type": "string"
    },
    "category_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Category Id"
    },
    "max_results": {
      "default": 25,
      "title": "Max Results",
      "type": "integer"
    }
  },
  "title": "yt_trendingArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation clamps max\_results to 1..50; order/date/category validation is delegated to Google API; description values are not schema enums.

Sources: [server.py:365](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L365-L371) · [trends\_mcp/youtube.py:127](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/youtube.py#L127-L159)

<a id="tool-yt-video-stats"></a>

### `yt_video_stats`

Statistiken (Views/Likes/Kommentare) zu konkreten Video-IDs.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `video_ids` | array of string | Yes | — | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "video_ids": {
      "items": {
        "type": "string"
      },
      "title": "Video Ids",
      "type": "array"
    }
  },
  "required": [
    "video_ids"
  ],
  "title": "yt_video_statsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.

Sources: [server.py:374](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L374-L377) · [trends\_mcp/youtube.py:181](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/youtube.py#L181-L204)

<a id="tool-yt-categories"></a>

### `yt_categories`

YouTube-Videokategorien einer Region (fuer yt\_trending category\_id).

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `region` | string | No | `"DE"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "region": {
      "default": "DE",
      "title": "Region",
      "type": "string"
    }
  },
  "title": "yt_categoriesArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.

Sources: [server.py:380](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L380-L383) · [trends\_mcp/youtube.py:207](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/youtube.py#L207-L215)

<a id="tool-reddit-search"></a>

### `reddit_search`

Searches Reddit posts via PRAW in supplied subreddit or all.

<details>
<summary>Full registered description</summary>

```text
Reddit-Beitraege durchsuchen.

sort: 'relevance' | 'hot' | 'top' | 'new' | 'comments'.
time_filter: 'hour' | 'day' | 'week' | 'month' | 'year' | 'all'.
subreddit='all' sucht global; sonst gezielt (z. B. 'smarthome').
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `query` | string | Yes | — | — | — |
| `subreddit` | string | No | `"all"` | — | — |
| `sort` | string | No | `"relevance"` | — | — |
| `time_filter` | string | No | `"month"` | — | — |
| `limit` | integer | No | `25` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "subreddit": {
      "default": "all",
      "title": "Subreddit",
      "type": "string"
    },
    "sort": {
      "default": "relevance",
      "title": "Sort",
      "type": "string"
    },
    "time_filter": {
      "default": "month",
      "title": "Time Filter",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "title": "reddit_searchArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation clamps limit to 1..100 (1..50 for find\_subreddits); sort/time\_filter validation is delegated to PRAW; documented values are not schema enums.

Sources: [server.py:390](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L390-L404) · [trends\_mcp/reddit\_api.py:89](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/reddit_api.py#L89-L106)

<a id="tool-reddit-rising"></a>

### `reddit_rising`

Aufsteigende Beitraege eines Subreddits (frueher Trend-Indikator).

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `subreddit` | string | Yes | — | — | — |
| `limit` | integer | No | `25` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "subreddit": {
      "title": "Subreddit",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "subreddit"
  ],
  "title": "reddit_risingArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation clamps limit to 1..100 (1..50 for find\_subreddits); sort/time\_filter validation is delegated to PRAW; documented values are not schema enums.

Sources: [server.py:407](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L407-L410) · [trends\_mcp/reddit\_api.py:110](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/reddit_api.py#L110-L113)

<a id="tool-reddit-hot"></a>

### `reddit_hot`

Aktuell heisse Beitraege eines Subreddits.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `subreddit` | string | Yes | — | — | — |
| `limit` | integer | No | `25` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "subreddit": {
      "title": "Subreddit",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "subreddit"
  ],
  "title": "reddit_hotArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation clamps limit to 1..100 (1..50 for find\_subreddits); sort/time\_filter validation is delegated to PRAW; documented values are not schema enums.

Sources: [server.py:413](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L413-L416) · [trends\_mcp/reddit\_api.py:117](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/reddit_api.py#L117-L120)

<a id="tool-reddit-top"></a>

### `reddit_top`

Top-Beitraege eines Subreddits im Zeitfenster (day/week/month/year/all).

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `subreddit` | string | Yes | — | — | — |
| `time_filter` | string | No | `"week"` | — | — |
| `limit` | integer | No | `25` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "subreddit": {
      "title": "Subreddit",
      "type": "string"
    },
    "time_filter": {
      "default": "week",
      "title": "Time Filter",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "subreddit"
  ],
  "title": "reddit_topArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation clamps limit to 1..100 (1..50 for find\_subreddits); sort/time\_filter validation is delegated to PRAW; documented values are not schema enums.

Sources: [server.py:419](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L419-L422) · [trends\_mcp/reddit\_api.py:124](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/reddit_api.py#L124-L130)

<a id="tool-reddit-find-subreddits"></a>

### `reddit_find_subreddits`

Passende Subreddits zu einem Thema finden (nach Abonnenten sortiert).

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `query` | string | Yes | — | — | — |
| `limit` | integer | No | `15` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "limit": {
      "default": 15,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "title": "reddit_find_subredditsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Schema reconstructed from registered signature; no explicit enum/bounds/minItems/maxItems/additionalProperties constraints are declared.
- Implementation clamps limit to 1..100 (1..50 for find\_subreddits); sort/time\_filter validation is delegated to PRAW; documented values are not schema enums.

Sources: [server.py:425](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/server.py#L425-L428) · [trends\_mcp/reddit\_api.py:134](https://github.com/david-wulf/trends-mcp-local/blob/1349b49e28a494eb72fd84be7c8ef5a6eab37bf0/trends_mcp/reddit_api.py#L134-L148)

## Schema provenance

Subagent enumerated AST registrations and implementation source. Parent independently registered exact signature-only AST functions in MCPServer 2.3.0 / Pydantic 2.14.1 and captured all 22 tools via local list_tools(), without importing providers, loading dotenv, or executing tools.

- Requirements are unpinned; schemas reflect MCP 2.3.0 and Pydantic 2.14.1.
- No remote tool calls were executed; external API behavior was reviewed in implementation source.
