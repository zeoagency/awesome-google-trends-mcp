# Awesome Google Trends MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Discover what Google Trends MCP tools can do: compare search interest, find related demand, track live searches, and query published rankings.

[Google Trends](https://trends.google.com/) · [MCP](https://modelcontextprotocol.io/) · [Every tool name](docs/tools.md) · [CLIs and SDKs](docs/clients.md)

**18 MCP providers · 104 Google Trends tool definitions · 207 total definitions across documented surfaces.** Reviewed 2026-10-13. Grouping follows registered tools and their implementations.

## Contents

- [Measure keyword interest and growth (6)](#measure-keyword-interest-and-growth)
- [Explore topics, regions and related demand (4)](#explore-topics-regions-and-related-demand)
- [Research keyword batches (1)](#research-keyword-batches)
- [Discover live trends and research candidates (3)](#discover-live-trends-and-research-candidates)
- [Track changes and query saved history (3)](#track-changes-and-query-saved-history)
- [Query published weekly rankings (1)](#query-published-weekly-rankings)
- [Tool name index](docs/tools.md)
- [CLIs and SDKs](docs/clients.md)

## Measure keyword interest and growth

Fetch keyword time series, compare terms on a shared scale, or calculate changes in interest.

| MCP | What its tools do | Tools to explore |
|---|---|---|
| [**den-indance/google-trends-mcp**](docs/mcp/den-indance-google-trends-mcp.md) (5 tools) | Compare keyword interest, retrieve related queries, and rank regional interest. | [`compare_keywords`](docs/mcp/den-indance-google-trends-mcp.md#tool-compare-keywords) · [`get_related_queries`](docs/mcp/den-indance-google-trends-mcp.md#tool-get-related-queries) |
| [**ducnhd/google-data-mcp**](docs/mcp/ducnhd-google-data-mcp.md) (7 tools) | Fetch keyword interest or joint comparisons, plus current trending searches. | [`google_trends_interest`](docs/mcp/ducnhd-google-data-mcp.md#tool-google-trends-interest) · [`google_trends_compare`](docs/mcp/ducnhd-google-data-mcp.md#tool-google-trends-compare) · [`google_trends_trending`](docs/mcp/ducnhd-google-data-mcp.md#tool-google-trends-trending) |
| [**HasData/google-trends-mcp**](docs/mcp/hasdata-google-trends-mcp.md) (1 tool) | Select time series, geographic interest, related queries, or related topics through one hosted tool. | [`hasdata_google_trends_search_getTrendsData`](docs/mcp/hasdata-google-trends-mcp.md#tool-hasdata-google-trends-search-gettrendsdata) |
| [**lhitches/google-trends-mcp**](docs/mcp/lhitches-google-trends-mcp.md) (4 tools) | Fetch time series, related queries, regional interest, and current country RSS searches. | [`interest_over_time`](docs/mcp/lhitches-google-trends-mcp.md#tool-interest-over-time) · [`related_queries`](docs/mcp/lhitches-google-trends-mcp.md#tool-related-queries) · [`interest_by_region`](docs/mcp/lhitches-google-trends-mcp.md#tool-interest-by-region) |
| [**purahmanian/google-trends-mcp**](docs/mcp/purahmanian-google-trends-mcp.md) (5 tools) | Fetch time series, compare terms, inspect related queries or regional interest, and read current RSS searches. | [`interest_over_time`](docs/mcp/purahmanian-google-trends-mcp.md#tool-interest-over-time) · [`compare_terms`](docs/mcp/purahmanian-google-trends-mcp.md#tool-compare-terms) · [`related_queries`](docs/mcp/purahmanian-google-trends-mcp.md#tool-related-queries) |
| [**trendsmcp-ai/google-trends-mcp**](docs/mcp/trendsmcp-ai-google-trends-mcp.md) (3 tools) | Request hosted keyword series, point-to-point growth, and current overall or category boards. | [`get_growth`](docs/mcp/trendsmcp-ai-google-trends-mcp.md#tool-get-growth) · [`get_time_series`](docs/mcp/trendsmcp-ai-google-trends-mcp.md#tool-get-time-series) · [`get_top_trends`](docs/mcp/trendsmcp-ai-google-trends-mcp.md#tool-get-top-trends) |

## Explore topics, regions and related demand

Resolve topic IDs, inspect regional interest, and discover related queries or category demand.

| MCP | What its tools do | Tools to explore |
|---|---|---|
| [**AKzar1el/mcp-trendpulse**](docs/mcp/akzar1el-mcp-trendpulse.md) (16 community + 6 hosted tools) | Explore keyword growth, related queries, topic IDs, regional interest, and hosted SEO opportunity research. | [`get_related_queries`](docs/mcp/akzar1el-mcp-trendpulse.md#tool-community-get-related-queries) · [`get_interest_by_region`](docs/mcp/akzar1el-mcp-trendpulse.md#tool-community-get-interest-by-region) · [`find_seo_opportunities`](docs/mcp/akzar1el-mcp-trendpulse.md#tool-hosted-find-seo-opportunities) |
| [**asgard-ai-platform/mcp-google-trends-tw**](docs/mcp/asgard-google-trends-tw.md) (5 tools) | Explore keyword time series, regional interest, and topic suggestions with configurable Taiwan defaults. | [`tw_interest_by_region`](docs/mcp/asgard-google-trends-tw.md#tool-tw-interest-by-region) · [`tw_keyword_suggestions`](docs/mcp/asgard-google-trends-tw.md#tool-tw-keyword-suggestions) |
| [**david-wulf/trends-mcp-local**](docs/mcp/david-wulf-trends-mcp-local.md) (22 tools) | Resolve topic IDs, compare search properties, and discover category or regional demand. | [`gt_resolve_topic`](docs/mcp/david-wulf-trends-mcp-local.md#tool-gt-resolve-topic) · [`gt_topic_across_properties`](docs/mcp/david-wulf-trends-mcp-local.md#tool-gt-topic-across-properties) · [`gt_discover_category`](docs/mcp/david-wulf-trends-mcp-local.md#tool-gt-discover-category) |
| [**goncaloaguer/unofficial-google-trends-mcp**](docs/mcp/goncaloaguer-google-trends-mcp.md) (10 tools) | Explore keyword time series, regional interest, related searches, categories, and location codes. | [`interest_by_region`](docs/mcp/goncaloaguer-google-trends-mcp.md#tool-interest-by-region) · [`search_categories`](docs/mcp/goncaloaguer-google-trends-mcp.md#tool-search-categories) · [`search_locations`](docs/mcp/goncaloaguer-google-trends-mcp.md#tool-search-locations) |

## Research keyword batches

Normalize keyword batches and submit research jobs for later retrieval.

| MCP | What its tools do | Tools to explore |
|---|---|---|
| [**Eason-Gao3/google-trends-mcp**](docs/mcp/eason-gao3-google-trends-mcp.md) (4 tools) | Compare terms and normalize larger keyword batches with a shared anchor, synchronously or as saved jobs. | [`research_keywords`](docs/mcp/eason-gao3-google-trends-mcp.md#tool-research-keywords) · [`research_keywords_async`](docs/mcp/eason-gao3-google-trends-mcp.md#tool-research-keywords-async) · [`get_research_task`](docs/mcp/eason-gao3-google-trends-mcp.md#tool-get-research-task) |

## Discover live trends and research candidates

Read current searches and their news context, or collect candidates for local research.

| MCP | What its tools do | Tools to explore |
|---|---|---|
| [**jmanek/google-news-trends-mcp**](docs/mcp/jmanek-google-news-trends-mcp.md) (5 tools) | Read current Google Trends RSS terms and optional related-news metadata, alongside news-search tools. | [`get_trending_terms`](docs/mcp/jmanek-google-news-trends-mcp.md#tool-get-trending-terms) |
| [**pipeworx-io/mcp-google-trends**](docs/mcp/pipeworx-google-trends.md) (1 local tool; hosted gateway also documented) | Read country RSS trending searches, traffic lower bounds, and related news through one local tool. | [`google_trending_searches`](docs/mcp/pipeworx-google-trends.md#tool-local-stdio-google-trending-searches) |
| [**Quadstronaut/SocialScour**](docs/mcp/quadstronaut-socialscour.md) (4 tools) | Collect US trending candidates and single-keyword research into local runs; MCP returns paths and reads saved summaries. | [`discover`](docs/mcp/quadstronaut-socialscour.md#tool-discover) |

## Track changes and query saved history

Record observations, inspect changes, and analyze data retained by the server.

| MCP | What its tools do | Tools to explore |
|---|---|---|
| [**claude-world/trend-pulse**](docs/mcp/claude-world-trend-pulse.md) (29 tools) | Save country RSS snapshots, compare local history, measure velocity, and export reports. | [`take_snapshot`](docs/mcp/claude-world-trend-pulse.md#tool-take-snapshot) · [`get_trend_history`](docs/mcp/claude-world-trend-pulse.md#tool-get-trend-history) · [`get_trend_velocity`](docs/mcp/claude-world-trend-pulse.md#tool-get-trend-velocity) |
| [**flack0x/trendspyg**](docs/mcp/flack0x-trendspyg.md) (9 tools) | Compare live trends across regions, diff fresh observations, and query archived snapshots or keyword interest. | [`compare_trending`](docs/mcp/flack0x-trendspyg.md#tool-compare-trending) · [`get_trend_changes`](docs/mcp/flack0x-trendspyg.md#tool-get-trend-changes) · [`get_trending_history`](docs/mcp/flack0x-trendspyg.md#tool-get-trending-history) |
| [**mvanhorn/printing-press-library**](docs/mcp/mvanhorn-google-trends.md) (27 tools) | Query live interest, regions, and related terms; inspect cached changes, seasonality, and historical trending snapshots. | [`trends_changes`](docs/mcp/mvanhorn-google-trends.md#tool-trends-changes) · [`trends_seasonality`](docs/mcp/mvanhorn-google-trends.md#tool-trends-seasonality) · [`trends_trending_at`](docs/mcp/mvanhorn-google-trends.md#tool-trends-trending-at) |

## Query published weekly rankings

Read top and rising terms from Google’s public BigQuery tables; coverage is limited to recorded terms.

| MCP | What its tools do | Tools to explore |
|---|---|---|
| [**jp-caldas/bigquery-google-trends-mcp**](docs/mcp/jp-caldas-bigquery-google-trends-mcp.md) (3 tools) | Query top terms, rising terms, or recorded weekly scores for one term and country. | [`buscar_termos_em_alta_tool`](docs/mcp/jp-caldas-bigquery-google-trends-mcp.md#tool-buscar-termos-em-alta-tool) · [`buscar_termos_emergentes_tool`](docs/mcp/jp-caldas-bigquery-google-trends-mcp.md#tool-buscar-termos-emergentes-tool) · [`comparar_termo_tool`](docs/mcp/jp-caldas-bigquery-google-trends-mcp.md#tool-comparar-termo-tool) |
