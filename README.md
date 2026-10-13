# Awesome Google Trends MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of MCP servers, CLIs, and SDKs or client libraries with implemented Google Trends integrations.

Official links: [Google Trends](https://trends.google.com/) · [Model Context Protocol](https://modelcontextprotocol.io/) · [Zeo Agency](https://zeo.org/)

## Contents

- [Quick comparison table](#quick-comparison-table)
- [MCP servers (18)](#mcp-servers)
- [CLIs (5)](#clis)
- [SDKs and client libraries (7)](#sdks-and-client-libraries)

## Quick comparison table

*30 projects. Each project appears once under its primary interface.*

| Project | Interface | Runtime | Google Trends source | Access |
|---|---|---|---|---|
| [**AKzar1el/mcp-trendpulse**](#mcp-servers) | MCP | Python | Google endpoints + RSS via trendspy | No provider API key |
| [**asgard-ai-platform/mcp-google-trends-tw**](#mcp-servers) | MCP | Python | Google endpoints via pytrends | No provider API key |
| [**claude-world/trend-pulse**](#mcp-servers) | MCP + CLI + SDK | Python | Google Trends RSS | No provider API key |
| [**david-wulf/trends-mcp-local**](#mcp-servers) | MCP | Python | trendspy or DataForSEO | Credentials for optional DataForSEO backend |
| [**den-indance/google-trends-mcp**](#mcp-servers) | MCP | Node.js | Google explore/widget endpoints | Optional configured proxies |
| [**ducnhd/google-data-mcp**](#mcp-servers) | MCP | Python | Google explore/widget + Trending Now RPC | No provider API key |
| [**Eason-Gao3/google-trends-mcp**](#mcp-servers) | MCP | Python | trendspy or pytrends | Optional proxy |
| [**flack0x/trendspyg**](#mcp-servers) | MCP + CLI + SDK | Python | Google endpoints + RSS; browser option | No provider API key |
| [**goncaloaguer/unofficial-google-trends-mcp**](#mcp-servers) | MCP | Python | Google endpoints via trendspy | No provider API key |
| [**HasData/google-trends-mcp**](#mcp-servers) | MCP connector | Node.js or Python launcher | Hosted HasData Google Trends service | HasData API key |
| [**jmanek/google-news-trends-mcp**](#mcp-servers) | MCP + CLI | Python | Google Trends RSS via trendspy | No provider API key |
| [**jp-caldas/bigquery-google-trends-mcp**](#mcp-servers) | MCP | Python | Google Trends public BigQuery dataset | Google Cloud project and credentials |
| [**lhitches/google-trends-mcp**](#mcp-servers) | MCP | Python | pytrends + Google Trends RSS | No provider API key |
| [**mvanhorn/printing-press-library**](#mcp-servers) | MCP + CLI | Go | Google explore/widget endpoints + trending feeds | No provider API key |
| [**pipeworx-io/mcp-google-trends**](#mcp-servers) | MCP | Node.js | Google Trends RSS | Local mode or hosted Pipeworx gateway |
| [**purahmanian/google-trends-mcp**](#mcp-servers) | MCP | Node.js | Google explore/widget endpoints + RSS | No provider API key |
| [**Quadstronaut/SocialScour**](#mcp-servers) | MCP + CLI | Python | trendspy with pytrends fallback | No Trends provider API key |
| [**trendsmcp-ai/google-trends-mcp**](#mcp-servers) | MCP connector | Python | Hosted TrendsMCP API | TrendsMCP API key |
| [**akvise/trends-checker**](#clis) | CLI | Python | pytrends or DataForSEO | Credentials for optional DataForSEO backend |
| [**iswangwenbin/ohmytrends**](#clis) | CLI + HTTP API | Bun | Google Trends through browser sessions | Manual login when required |
| [**mamboyepez17/trendscope**](#clis) | CLI | Python | Google Trends RSS + pytrends | Optional services for report analysis |
| [**Nao-30/google-trends-cli**](#clis) | CLI + HTTP API | Python | Google endpoints via trendspy | No Trends provider API key |
| [**RuochenLyu/google-trends-now**](#clis) | CLI + SDK | Node.js | Google Trending Now RPC + RSS fallback | No provider API key |
| [**GeneralMills/pytrends**](#sdks-and-client-libraries) | SDK | Python | Google explore/widget and legacy endpoints | Archived |
| [**groovili/gogtrends**](#sdks-and-client-libraries) | SDK | Go | Google explore/widget and legacy endpoints | No provider API key |
| [**LafCorentin/gtrend-rs**](#sdks-and-client-libraries) | SDK | Rust | Google explore/widget endpoints | No provider API key |
| [**pat310/google-trends-api**](#sdks-and-client-libraries) | SDK | Node.js | Google explore/widget and legacy endpoints | No provider API key |
| [**shadawck/rust-trend**](#sdks-and-client-libraries) | SDK | Rust | Google explore/widget endpoints | No provider API key |
| [**Shaivpidadi/trends-js**](#sdks-and-client-libraries) | SDK | Node.js / TypeScript | Google Trending Now RPC + explore widgets | No provider API key |
| [**yiromo/pytrends-modern**](#sdks-and-client-libraries) | SDK + CLI | Python | Google endpoints + RSS; browser option | No provider API key |

## MCP servers

*18 projects. Servers and hosted-service connectors exposing Google Trends through MCP tools.*

| Project | What it does |
|---|---|
| [**AKzar1el/mcp-trendpulse**](https://github.com/AKzar1el/mcp-trendpulse) | Exposes Google Trends historical interest, growth, regional interest, related searches, and trending-search tools through trendspy. Also includes Google News tools. |
| [**asgard-ai-platform/mcp-google-trends-tw**](https://github.com/asgard-ai-platform/mcp-google-trends-tw) | Exposes keyword interest, regional interest, and suggestions with Taiwan and Traditional Chinese defaults. Its daily and realtime trending tools still depend on legacy pytrends endpoints. |
| [**claude-world/trend-pulse**](https://github.com/claude-world/trend-pulse) | Fetches country-specific Google Trends RSS alongside other sources through MCP, CLI, and Python interfaces. Stores snapshot history in SQLite. |
| [**david-wulf/trends-mcp-local**](https://github.com/david-wulf/trends-mcp-local) | Exposes keyword comparisons, topic discovery, and regional interest through trendspy or DataForSEO, plus current trends through trendspy. Caches results in SQLite with stale-result fallback after quota failures. |
| [**den-indance/google-trends-mcp**](https://github.com/den-indance/google-trends-mcp) | Exposes keyword comparisons, related queries, and regional interest through direct Google Trends requests. Includes authenticated proxy-list validation and rotation; its persistent cache stores proxy information. |
| [**ducnhd/google-data-mcp**](https://github.com/ducnhd/google-data-mcp) | Exposes Google Trends keyword interest, comparisons, and trending searches alongside Ads Transparency tools. Caches result data on disk. |
| [**Eason-Gao3/google-trends-mcp**](https://github.com/Eason-Gao3/google-trends-mcp) | Exposes comparisons and batch keyword research through trendspy or pytrends over stdio or Streamable HTTP. Uses memory and SQLite caches and supports a single configured proxy. |
| [**flack0x/trendspyg**](https://github.com/flack0x/trendspyg) | Fetches current trends, keyword comparisons, related searches, regional interest, and suggestions through Python, CLI, and MCP interfaces. Offers optional SQLite history, caching, and cookie persistence. |
| [**goncaloaguer/unofficial-google-trends-mcp**](https://github.com/goncaloaguer/unofficial-google-trends-mcp) | Exposes trendspy-backed Google Trends tools over stdio or Streamable HTTP with an in-memory TTL cache. Includes Docker and Cloud Run packaging; its README flags related-query and related-topic failures. |
| [**HasData/google-trends-mcp**](https://github.com/HasData/google-trends-mcp) | Connects local MCP clients to HasData’s hosted Google Trends server through a stdio-to-HTTP bridge. Requires a HasData API key; scraping runs in the hosted service. |
| [**jmanek/google-news-trends-mcp**](https://github.com/jmanek/google-news-trends-mcp) | Fetches country-specific trending searches through trendspy’s Google Trends RSS integration. Also exposes Google News search and optional article summaries through MCP and CLI tools. |
| [**jp-caldas/bigquery-google-trends-mcp**](https://github.com/jp-caldas/bigquery-google-trends-mcp) | Queries Google’s public BigQuery Trends dataset for top terms, rising terms, and recorded weekly scores. Requires Google Cloud credentials and covers terms present in that dataset. |
| [**lhitches/google-trends-mcp**](https://github.com/lhitches/google-trends-mcp) | Exposes four tools for interest over time, related queries, regional interest, and current trending searches. Uses pytrends for exploration and Google’s RSS feed for trending searches. |
| [**mvanhorn/printing-press-library**](https://github.com/mvanhorn/printing-press-library/tree/main/library/marketing/google-trends) | Queries Google Trends from the repository’s Google Trends CLI with JSON output, retries, and SQLite history. Exposes the same tool through an MCP server supporting stdio and Streamable HTTP. |
| [**pipeworx-io/mcp-google-trends**](https://github.com/pipeworx-io/mcp-google-trends) | Returns country-specific Google Trends RSS topics with approximate traffic values and related news. Runs as a local stdio server or through Pipeworx’s hosted gateway. |
| [**purahmanian/google-trends-mcp**](https://github.com/purahmanian/google-trends-mcp) | Exposes five tools for interest over time, keyword comparisons, related queries, trending searches, and regional interest. Calls Google’s exploration endpoints and public RSS feed. |
| [**Quadstronaut/SocialScour**](https://github.com/Quadstronaut/SocialScour) | Fetches Google Trends interest over time and related queries alongside Reddit and developer-community sources. Exposes CLI and MCP interfaces and saves run artifacts and digests as files. |
| [**trendsmcp-ai/google-trends-mcp**](https://github.com/trendsmcp-ai/google-trends-mcp) | Connects MCP tools to the hosted TrendsMCP API for historical series, growth comparisons, and live boards including Google Trends. Requires an API key and does not provide geographic breakdowns. |

## CLIs

*5 projects. Terminal tools with implemented Google Trends commands.*

| Project | What it does |
|---|---|
| [**akvise/trends-checker**](https://github.com/akvise/trends-checker) | Queries Google Trends across keywords, regions, and search properties, with proxy options, cookies, and retry delays. Exports JSON or CSV and offers an optional DataForSEO backend. |
| [**iswangwenbin/ohmytrends**](https://github.com/iswangwenbin/ohmytrends) | Queries Google Trends and Baidu Index through persistent browser sessions and returns tables or JSON. Provides a Bun CLI and a local HTTP API with SQLite result storage. |
| [**mamboyepez17/trendscope**](https://github.com/mamboyepez17/trendscope) | Combines Google Trends country RSS feeds and pytrends keyword interest with other sources in an interactive analysis CLI. Produces local JSON and report files. |
| [**Nao-30/google-trends-cli**](https://github.com/Nao-30/google-trends-cli) | Fetches trending searches, compares topics, and explores related and geographic interest through trendspy. Provides terminal tables, file exports, and a FastAPI service. |
| [**RuochenLyu/google-trends-now**](https://github.com/RuochenLyu/google-trends-now) | Fetches Google Trending Now through its web RPC endpoint, with a limited RSS fallback. Exports JSON, NDJSON, CSV, or Markdown through CLI and JavaScript interfaces. |

## SDKs and client libraries

*7 projects. Reusable clients for querying Google Trends from application code.*

| Project | What it does |
|---|---|
| [**GeneralMills/pytrends**](https://github.com/GeneralMills/pytrends) | Queries Google Trends interest over time, regional interest, related searches, and suggestions and returns pandas data structures. **Archived**; upstream changes can break its unofficial endpoints. |
| [**groovili/gogtrends**](https://github.com/groovili/gogtrends) | Fetches Google Trends interest over time and location, related searches, and autocomplete from Go. Also includes legacy trending-feed methods and caches category and location lists. |
| [**LafCorentin/gtrend-rs**](https://github.com/LafCorentin/gtrend-rs) | Queries Google Trends asynchronously and returns typed time series, geographic interest, related topics, and related queries. Provides enums for countries, categories, search properties, and predefined periods. |
| [**pat310/google-trends-api**](https://github.com/pat310/google-trends-api) | Queries Google Trends interest, geography, related searches, and autocomplete from JavaScript with promises or callbacks. Resolves explore widget tokens and includes legacy trending-feed methods. |
| [**shadawck/rust-trend**](https://github.com/shadawck/rust-trend) | Queries Google Trends interest over time and region, related topics, and related queries from Rust. Uses a blocking reqwest client with keyword and geographic filters. |
| [**Shaivpidadi/trends-js**](https://github.com/Shaivpidadi/trends-js) | Provides typed, promise-based access to Google Trending Now, autocomplete, explore widgets, regional interest, and related searches. Supports optional retry backoff. |
| [**yiromo/pytrends-modern**](https://github.com/yiromo/pytrends-modern) | Provides Python and CLI access to Google Trends interest, related searches, and RSS trending feeds, with retries and proxy options. Includes async support and an experimental Camoufox browser mode. |
