# Google Trends CLIs and SDKs

[Back to the MCP catalog](../README.md) · [Tool name index](tools.md)

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
