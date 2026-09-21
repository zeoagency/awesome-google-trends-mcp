# Awesome Google Trends MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated plain-English index of Model Context Protocol (MCP) servers, autonomous agent tools, scrapers, and data pipelines for Google Trends.

Official links: [Google Trends](https://trends.google.com/) · [Model Context Protocol](https://modelcontextprotocol.io/) · [PyPI](https://pypi.org/) · [NPM](https://www.npmjs.com/) · [Zeo Agency](https://zeo.org/)

---

## Contents

1. [Scrape with proxy resilience and anti-bot bypass (9)](#1-scrape-with-proxy-resilience-and-anti-bot-bypass)
   - [Rotating residential proxy pools and failover tracking (3)](#rotating-residential-proxy-pools-and-failover-tracking)
   - [Anti-detect browser emulation and fingerprint masking (3)](#anti-detect-browser-emulation-and-fingerprint-masking)
   - [Session cookie jars and NID token persistence (3)](#session-cookie-jars-and-nid-token-persistence)
2. [Persist, cache, and archive historical trends (6)](#2-persist-cache-and-archive-historical-trends)
   - [Embedded SQLite storage in WAL mode (2)](#embedded-sqlite-storage-in-wal-mode)
   - [Ephemeral daily trend snapshot archives (2)](#ephemeral-daily-trend-snapshot-archives)
   - [Multi-tier cache TTL and stale-while-error fallback (2)](#multi-tier-cache-ttl-and-stale-while-error-fallback)
3. [Connect through hosted commercial APIs (7)](#3-connect-through-hosted-commercial-apis)
   - [Consolidated single-tool enum MCP servers (1)](#consolidated-single-tool-enum-mcp-servers)
   - [Multi-search gateways and commercial SERP aggregators (2)](#multi-search-gateways-and-commercial-serp-aggregators)
   - [Marketing analytics and reporting integrations (2)](#marketing-analytics-and-reporting-integrations)
   - [Containerized Cloud Run and Docker deployments (2)](#containerized-cloud-run-and-docker-deployments)
4. [Monitor rate-immune RSS and news intelligence (6)](#4-monitor-rate-immune-rss-and-news-intelligence)
   - [Rate-immune public XML syndication harvesters (2)](#rate-immune-public-xml-syndication-harvesters)
   - [Trending news clustering and article distillation (2)](#trending-news-clustering-and-article-distillation)
   - [Autonomous trend monitoring agents and recurring scanners (2)](#autonomous-trend-monitoring-agents-and-recurring-scanners)
5. [Integrate with developer assistants and coding IDEs (6)](#5-integrate-with-developer-assistants-and-coding-ides)
   - [Zero-config Claude Code marketplace servers (2)](#zero-config-claude-code-marketplace-servers)
   - [Claude-specific trend agents and prompts (2)](#claude-specific-trend-agents-and-prompts)
   - [Regional market locators and Asian language editions (2)](#regional-market-locators-and-asian-language-editions)
6. [Execute high-performance binaries and terminal CLIs (12)](#6-execute-high-performance-binaries-and-terminal-clis)
   - [Compiled Go engines and multi-transport daemons (2)](#compiled-go-engines-and-multi-transport-daemons)
   - [High-performance Rust scrapers and pipelines (3)](#high-performance-rust-scrapers-and-pipelines)
   - [Interactive terminal shells and CLI query tools (5)](#interactive-terminal-shells-and-cli-query-tools)
   - [Lightweight TypeScript and JavaScript engines (2)](#lightweight-typescript-and-javascript-engines)
7. [Aggregate cross-platform trends and retail intent (10)](#7-aggregate-cross-platform-trends-and-retail-intent)
   - [Cross-network momentum aggregators (4)](#cross-network-momentum-aggregators)
   - [E-commerce search demand and retail price trackers (3)](#e-commerce-search-demand-and-retail-price-trackers)
   - [Social media community and video trend scanners (3)](#social-media-community-and-video-trend-scanners)
8. [Orchestrate enterprise pipelines and warehouse ingestion (8)](#8-orchestrate-enterprise-pipelines-and-warehouse-ingestion)
   - [Airflow orchestration DAGs and dbt star schemas (2)](#airflow-orchestration-dags-and-dbt-star-schemas)
   - [Official Google Cloud BigQuery public dataset connectors (1)](#official-google-cloud-bigquery-public-dataset-connectors)
   - [Data lake batch pipelines and columnar storage (2)](#data-lake-batch-pipelines-and-columnar-storage)
   - [Clean architecture adapters and territorial intelligence (3)](#clean-architecture-adapters-and-territorial-intelligence)
9. [Developer comparison table](#developer-comparison-table)
10. [Resources](#resources)
11. [Reference](#reference)

---

## 1. Scrape with proxy resilience and anti-bot bypass

*9 projects. Scrapers, proxy pools, and anti-detect browsers designed to bypass Google's 429 rate limits and HTML challenge blocks.*

### Rotating residential proxy pools and failover tracking

*3 projects. Multi-proxy pool ingestion, randomized per-request rotation, and active failover tracking.*

| Project | What it does |
|---|---|
| [**den-indance/google-trends-mcp**](https://github.com/den-indance/google-trends-mcp) | Rotates authenticated residential proxies per-request and validates candidate pools against Google autocomplete before scraping. Protects JSON parsers with a string-level `looksLikeHtml` check that catches challenge pages and ejects dead proxies after three consecutive failures. |
| [**Eason-Gao3/google-trends-mcp**](https://github.com/Eason-Gao3/google-trends-mcp) | Combines proxy pool rotation with an embedded SQLite cache to reduce repeat network lookups. Serves historical queries from local disk while falling back to rotating proxies when fresh explore data is required. |
| [**akvise/trends-checker**](https://github.com/akvise/trends-checker) | Executes interactive terminal search audits with configurable per-request proxy flags and rich CLI tables. Enforces jittered backoff intervals to stay safely below Google's 130-call daily IP threshold. |

### Anti-detect browser emulation and fingerprint masking

*3 projects. Headless browser engines (Camoufox, Playwright) that solve Google bot challenges and bypass TLS fingerprints.*

| Project | What it does |
|---|---|
| [**yiromo/pytrends-modern**](https://github.com/yiromo/pytrends-modern) | Drives headless Camoufox anti-detect browsers with dynamic Chrome extension proxy authentication to solve Google challenge screens. Bypasses TLS fingerprinting at the cost of higher startup latency and memory overhead. |
| [**calipsow/gtrends**](https://github.com/calipsow/gtrends) | Wraps modern pytrends with automated headless browser session bootstrapping and disk caching. Ingests NID session cookies before issuing explore requests to prevent repetitive consent roadblocks. |
| [**iswangwenbin/ohmytrends**](https://github.com/iswangwenbin/ohmytrends) | Provides a high-speed Bun CLI and API engine that queries Google Trends and Baidu Index in parallel. Employs persistent browser profile cloaking to scrape real-time search trends without external proxy fleets. |

### Session cookie jars and NID token persistence

*3 projects. Persistent cookie storage across server lifecycles to maintain authenticated Google session trust.*

| Project | What it does |
|---|---|
| [**ducnhd/google-data-mcp**](https://github.com/ducnhd/google-data-mcp) | Exposes unified MCP tools for Google Trends and Google Ads with automatic session cookie reuse. Retries failed explore requests using exponential backoff to handle intermittent upstream throttling. |
| [**tuckerelbon-hash/pytrends-proxy**](https://github.com/tuckerelbon-hash/pytrends-proxy) | Forwards pytrends network traffic through an authenticated HTTP proxy tunnel with retry wrapping. Simplifies containerized deployment by abstracting proxy configuration into standard environment variables. |
| [**senolalgul8-alt/google-trends-proxy**](https://github.com/senolalgul8-alt/google-trends-proxy) | Operates a lightweight local proxy forwarder daemon specifically tuned for Google Trends explore endpoints. Intercepts outgoing client requests to inject rotating residential proxy headers transparently. |

## 2. Persist, cache, and archive historical trends

*6 projects. Embedded databases and caching layers that shield Google endpoints and archive ephemeral daily trends.*

### Embedded SQLite storage in WAL mode

*2 projects. Local SQLite databases providing sub-20ms reads and historical trend querying.*

| Project | What it does |
|---|---|
| [**flack0x/trendspyg**](https://github.com/flack0x/trendspyg) | Archives historical trend data in an embedded SQLite database running in WAL mode, returning cached queries in under 15 milliseconds. Persists Google NID session cookies to disk and captures ephemeral daily trends before Google drops them. |
| [**david-wulf/trends-mcp-local**](https://github.com/david-wulf/trends-mcp-local) | Caches Google Trends explore payloads in a local SQLite file to minimize external network egress. Validates keyword parameters before querying to avoid wasting upstream rate-limit budget on malformed requests. |

### Ephemeral daily trend snapshot archives

*2 projects. Scheduled snapshot capture preventing permanent loss of Google's 24-48h daily trending feeds.*

| Project | What it does |
|---|---|
| [**mamboyepez17/trendscope**](https://github.com/mamboyepez17/trendscope) | Schedules daily background snapshots of rising search queries into persistent storage. Pairs keyword velocity tracking with local caching to maintain a permanent historical record of viral spikes. |
| [**Quadstronaut/SocialScour**](https://github.com/Quadstronaut/SocialScour) | Collects and archives multi-source trending topics from Google and social platforms into a local relational database. Structures daily keyword rankings with chronological timestamps for historical trend analysis. |

### Multi-tier cache TTL and stale-while-error fallback

*2 projects. Configurable expiration policies with graceful fallback to cached data upon upstream 429 blocks.*

| Project | What it does |
|---|---|
| [**pipeworx-io/mcp-google-trends**](https://github.com/pipeworx-io/mcp-google-trends) | Maintains a dual-layer memory and file cache with configurable TTL policies for Google News and Trends data. Returns stale cached entries gracefully when upstream Google endpoints respond with HTTP 429 rate limits. |
| [**RuochenLyu/google-trends-now**](https://github.com/RuochenLyu/google-trends-now) | Fetches trending searches with automatic fallback to Google's public XML RSS feed when scraper endpoints throttle. Prunes internal widget hashes to return clean, high-density JSON directly to calling agents. |

## 3. Connect through hosted commercial APIs

*7 projects. Cloud-managed APIs and commercial gateways that offload anti-bot mitigation and guarantee uptime SLAs.*

### Consolidated single-tool enum MCP servers

*1 project. Single-tool servers utilizing discriminated mode enums to minimize prompt token footprint.*

| Project | What it does |
|---|---|
| [**HasData/google-trends-mcp**](https://github.com/HasData/google-trends-mcp) | Delegates anti-bot mitigation, proxy rotation, and CAPTCHA bypass to HasData's managed cloud infrastructure. Employs a single consolidated MCP tool with a discriminated dataType enum, consuming only 380 prompt tokens while offering 1,000 free monthly credits. |

### Multi-search gateways and commercial SERP aggregators

*2 projects. Hosted search platforms integrating Google Trends alongside crawling and SERP feeds.*

| Project | What it does |
|---|---|
| [**superagents-lab/search1api-mcp**](https://github.com/superagents-lab/search1api-mcp) | Integrates Google Trends timeseries queries alongside web search and crawling tools under a single hosted API gateway. Normalizes search volume curves for multi-agent workflows without requiring local proxy management. |
| [**nonatin1000/02-google-trends-agent-z**](https://github.com/nonatin1000/02-google-trends-agent-z) | Orchestrates LangGraph agent research workflows using SerpApi's managed Google Trends integration. Routes keyword comparison tasks through SLA-backed endpoints with automated error recovery. |

### Marketing analytics and reporting integrations

*2 projects. Commercial connectors syncing Google Trends with BI dashboards and automated client reports.*

| Project | What it does |
|---|---|
| [**twominutereports/google-trends-mcp**](https://github.com/twominutereports/google-trends-mcp) | Connects Google Trends search metrics directly into automated BI reporting pipelines and marketing dashboards. Formats multi-region interest data into structured tables ready for scheduled reporting. |
| [**openclaw-easy/ViralMint**](https://github.com/openclaw-easy/ViralMint) | Scores keyword trend velocity across commercial search APIs to calculate breakout potential for content publishers. Cross-references relative interest curves against commercial keyword metrics. |

### Containerized Cloud Run and Docker deployments

*2 projects. Packaged container images deployable to cloud runtimes with pre-configured API keys.*

| Project | What it does |
|---|---|
| [**goncaloaguer/unofficial-google-trends-mcp**](https://github.com/goncaloaguer/unofficial-google-trends-mcp) | Packages an unofficial Google Trends MCP server into a lightweight Google Cloud Run container. Exposes Streamable HTTP and SSE transports with container-level environment variable configuration. |
| [**costrict-plugins-repo/github-trending-mcp-servers-docker**](https://github.com/costrict-plugins-repo/github-trending-mcp-servers-docker) | Maintains pre-built Docker container manifests for deploying Google Trends and developer MCP servers with zero host configuration. Isolate runtime dependencies inside reproducible container environments. |

## 4. Monitor rate-immune RSS and news intelligence

*6 projects. Tools that bypass Google anti-bot systems via public XML syndication and correlate trends with news coverage.*

### Rate-immune public XML syndication harvesters

*2 projects. Zero-proxy RSS parsers completely immune to HTTP 429 bans and CAPTCHAs.*

| Project | What it does |
|---|---|
| [**AKzar1el/mcp-trendpulse**](https://github.com/AKzar1el/mcp-trendpulse) | Queries Google's public XML RSS syndication feeds, making it 100% immune to HTTP 429 rate limits and anti-bot challenges without proxies. Correlates search momentum with Google News article clustering and supports custom growth windows. |
| [**ski-p3r/google-news-trends-mcp**](https://github.com/ski-p3r/google-news-trends-mcp) | Extracts trending search feeds via public XML syndication and parses associated news publisher metadata. Runs entirely without proxy pools or API credentials. |

### Trending news clustering and article distillation

*2 projects. Pipelines correlating search surges with publisher news articles and NLP summaries.*

| Project | What it does |
|---|---|
| [**jmanek/google-news-trends-mcp**](https://github.com/jmanek/google-news-trends-mcp) | Pioneered rate-immune trend extraction by pairing Google News RSS feeds with NLP article summarization. Distills publisher coverage to explain the context behind viral search surges without triggering bot traps. |
| [**ToolOracle/newsoracle**](https://github.com/ToolOracle/newsoracle) | Monitors news coverage surges paired with Google search interest signals to detect emerging media narratives. Extracts key entity quotes and publisher consensus before delivering structured summaries. |

### Autonomous trend monitoring agents and recurring scanners

*2 projects. Agentic background loops scanning topic momentum on scheduled intervals.*

| Project | What it does |
|---|---|
| [**0xmariowu/Autosearch**](https://github.com/0xmariowu/Autosearch) | Drives autonomous background research loops that detect emerging search spikes and initiate multi-source web deep dives. Employs token-efficient response pruning to protect LLM context windows. |
| [**claude-world/trend-pulse**](https://github.com/claude-world/trend-pulse) | Integrates 20 trending data sources into a unified Python library and MCP server with scheduled scanners. Normalizes Google Trends data alongside developer feeds for automated morning briefing agents. |

## 5. Integrate with developer assistants and coding IDEs

*6 projects. Zero-config MCP servers tailored for Claude Code, Cursor, Windsurf, and developer coding workflows.*

### Zero-config Claude Code marketplace servers

*2 projects. Keyless FastMCP servers installable via uvx or marketplace commands without configuration.*

| Project | What it does |
|---|---|
| [**lhitches/google-trends-mcp**](https://github.com/lhitches/google-trends-mcp) | Provides a keyless FastMCP server designed specifically for Claude Code and Cursor desktop assistants. Exposes four clean tools covering interest over time, related queries, regional interest, and trending searches. |
| [**purahmanian/google-trends-mcp**](https://github.com/purahmanian/google-trends-mcp) | Installs with a single command via uvx to deliver zero-config Google Trends exploration for local AI coding assistants. Handles parameter validation internally to prevent cryptic upstream errors. |

### Claude-specific trend agents and prompts

*2 projects. Specialized prompt packs and tool plugins optimized for Claude desktop assistants.*

| Project | What it does |
|---|---|
| [**trendsmcp-ai/trends-agent-claude**](https://github.com/trendsmcp-ai/trends-agent-claude) | Delivers a Claude-tailored prompt pack and MCP tool wrapper pre-configured for market analysis. Formats relative interest curves with explicit 0-100 scaling documentation to prevent hallucinated volume claims. |
| [**GoogleCloudPlatform/gcp-getting-started-lab-jp**](https://github.com/GoogleCloudPlatform/gcp-getting-started-lab-jp) | Demonstrates enterprise AI agent integration using Google Trends MCP tooling within the official GCP architecture framework. Provides reference configurations for multi-agent tool multiplexing. |

### Regional market locators and Asian language editions

*2 projects. Localized MCP configurations pre-tuned for regional Google Trends indices and DMA codes.*

| Project | What it does |
|---|---|
| [**asgard-ai-platform/mcp-google-trends-tw**](https://github.com/asgard-ai-platform/mcp-google-trends-tw) | Specializes in East Asian market intelligence with pre-configured Taiwan DMA and regional language parameters. Optimizes UTF-8 character handling for Traditional Chinese search terms. |
| [**costrict-plugins-repo/github-trending-google-workspace-mcp**](https://github.com/costrict-plugins-repo/github-trending-google-workspace-mcp) | Integrates Google Trends search monitoring into Google Workspace workflows and collaborative sheets. Dispatches automated trend digests into shared organizational channels. |

## 6. Execute high-performance binaries and terminal CLIs

*12 projects. Compiled binaries, terminal utilities, and lightweight runtimes built for execution speed and low memory.*

### Compiled Go engines and multi-transport daemons

*2 projects. Ultra-fast Go binaries with sub-10ms cold starts and dual stdio/HTTP transports.*

| Project | What it does |
|---|---|
| [**mvanhorn/printing-press-library**](https://github.com/mvanhorn/printing-press-library) | Compiles into a native Go binary delivering sub-10ms cold starts and under 15MB of resident memory. Exposes dual stdio and Streamable HTTP transports with optional DataForSEO Explore integration. |
| [**groovili/gogtrends**](https://github.com/groovili/gogtrends) | Provides the canonical Go client library for Google Trends internal endpoints with native concurrency support. Handles cookie management and request pacing across parallel goroutines. |

### High-performance Rust scrapers and pipelines

*3 projects. Type-safe Rust implementations with zero-cost async networking and minimal RSS memory.*

| Project | What it does |
|---|---|
| [**shadawck/rust-trend**](https://github.com/shadawck/rust-trend) | Implements an ultra-lightweight, memory-safe Google Trends scraper in Rust using async reqwest networking. Minimizes CPU overhead for embedded systems and containerized microservices. |
| [**LafCorentin/gtrend-rs**](https://github.com/LafCorentin/gtrend-rs) | Exposes a type-safe Rust API for querying Google Trends explore and related query endpoints. Validates timeframe strings and ISO country codes at compile time. |
| [**t3chnicallyinclined/autoseo**](https://github.com/t3chnicallyinclined/autoseo) | Embeds Google Trends exploration into a high-performance Rust SEO optimization pipeline for YouTube search ranking. Ranks keyword tags by breakout momentum to optimize video metadata. |

### Interactive terminal shells and CLI query tools

*5 projects. Command-line interfaces outputting structured JSON to stdout for shell pipelines and agent execution.*

| Project | What it does |
|---|---|
| [**Nao-30/google-trends-cli**](https://github.com/Nao-30/google-trends-cli) | Queries Google Trends from the command line with clean JSON stdout formatting suitable for shell pipelines and agent execution. Supports custom date ranges and regional filtering flags. |
| [**rcsolis/trendscli**](https://github.com/rcsolis/trendscli) | Delivers an interactive terminal utility for exploring keyword interest curves with ASCII terminal charts. Outputs structured JSON when invoked with automation flags. |
| [**blacknbunny/Google-Trends-CLI**](https://github.com/blacknbunny/Google-Trends-CLI) | Offers an interactive terminal shell for real-time trending topic monitoring and keyword comparisons. Allows developers to monitor search interest shifts directly inside their terminal workflow. |
| [**Bostigger/google-trends-cli**](https://github.com/Bostigger/google-trends-cli) | Provides a compact command-line scraper for fetching daily trending topics with minimal external dependencies. Easily callable from shell scripts and cron automation. |
| [**Hudson-Pufferfish/google-trends-cli**](https://github.com/Hudson-Pufferfish/google-trends-cli) | Executes rapid keyword search queries from the terminal with lightweight argument parsing. Designed for quick one-off inspections without browser dependencies. |

### Lightweight TypeScript and JavaScript engines

*2 projects. Node and Bun packages providing clean programmatic client interfaces.*

| Project | What it does |
|---|---|
| [**Shaivpidadi/trends-js**](https://github.com/Shaivpidadi/trends-js) | Provides a modern TypeScript client library for Google Trends with full type definitions and promise-based interfaces. Handles response payload parsing and sanitization across modern Node runtimes. |
| [**pat310/google-trends-api**](https://github.com/pat310/google-trends-api) | Serves as the foundational JavaScript library underpinning numerous community scrapers and MCP servers. Encapsulates request signing and widget token resolution for explore queries. |

## 7. Aggregate cross-platform trends and retail intent

*10 projects. Multi-network engines monitoring search and viral momentum across Google, social media, and retail platforms.*

### Cross-network momentum aggregators

*4 projects. Engines simultaneously querying Google Trends, TikTok, YouTube, and Reddit.*

| Project | What it does |
|---|---|
| [**trendsmcp-ai/Trends-MCP**](https://github.com/trendsmcp-ai/Trends-MCP) | Aggregates search momentum across Google Trends, TikTok, and YouTube to provide multi-platform trend intelligence. Compares relative search interest against social video engagement. |
| [**trendsmcp-ai/TrendWatch**](https://github.com/trendsmcp-ai/TrendWatch) | Monitors emerging keyword velocity across search engines and social platforms using unified agent tools. Generates consolidated momentum alerts for social listening pipelines. |
| [**caicai-yao/social-trends-mcp**](https://github.com/caicai-yao/social-trends-mcp) | Collects trending topics across Google Trends, Weibo, and international social platforms. Normalizes disparate ranking metrics into a unified cross-network schema. |
| [**trendsmcp-ai/google-trends-mcp**](https://github.com/trendsmcp-ai/google-trends-mcp) | Provides real-time Google search trends with automated multi-region support and category filtering. Prepares trend data for downstream LLM synthesis and agent tool calls. |

### E-commerce search demand and retail price trackers

*3 projects. Cross-correlating Google search interest with Amazon product demand and sales velocity.*

| Project | What it does |
|---|---|
| [**cosjef/keepa_MCP**](https://github.com/cosjef/keepa_MCP) | Cross-correlates Google Trends relative search popularity with Amazon product price history and Keepa sales ranks. Calibrates search interest spikes against concrete e-commerce purchasing velocity. |
| [**dan1d/mercadolibre-mcp**](https://github.com/dan1d/mercadolibre-mcp) | Tracks e-commerce product demand across Latin American markets by pairing Google search trends with MercadoLibre inventory data. Identifies high-demand product niches for cross-border retailers. |
| [**trendsmcp-ai/amazon-trends-mcp**](https://github.com/trendsmcp-ai/amazon-trends-mcp) | Monitors Amazon product search demand and category interest shifts alongside Google search trends. Helps e-commerce sellers identify rising consumer purchase intent. |

### Social media community and video trend scanners

*3 projects. Monitoring video engagement and discussion volume alongside Google search spikes.*

| Project | What it does |
|---|---|
| [**trendsmcp-ai/tiktok-trends-mcp**](https://github.com/trendsmcp-ai/tiktok-trends-mcp) | Tracks viral hashtag velocity on TikTok to compare social media engagement against Google search queries. Highlights cultural trends before they surface in traditional search indices. |
| [**trendsmcp-ai/youtube-trends-mcp**](https://github.com/trendsmcp-ai/youtube-trends-mcp) | Analyzes YouTube search demand and video view growth rates alongside web search interest. Optimizes video publishing schedules based on rising topic momentum. |
| [**trendsmcp-ai/reddit-trends-mcp**](https://github.com/trendsmcp-ai/reddit-trends-mcp) | Scans Reddit community discussions and keyword frequency to surface grass-roots sentiment preceding Google search spikes. Correlates forum discussions with macro search interest. |

## 8. Orchestrate enterprise pipelines and warehouse ingestion

*8 projects. Production data engineering pipelines, BigQuery public datasets, and territorial intelligence systems.*

### Airflow orchestration DAGs and dbt star schemas

*2 projects. Scheduled workflow orchestration syncing Google Trends into relational star schemas.*

| Project | What it does |
|---|---|
| [**VytautasPliadis/Google-Trends-pipeline**](https://github.com/VytautasPliadis/Google-Trends-pipeline) | Orchestrates production Airflow DAGs that ingest Google Trends data into a dbt star schema in PostgreSQL. Automates batch scheduling, schema migrations, and enterprise data modeling. |
| [**cspoppuppy/DE-GoogleTrendsPipeline-Batch**](https://github.com/cspoppuppy/DE-GoogleTrendsPipeline-Batch) | Executes batch data engineering pipelines that extract, transform, and load historical Google Trends datasets into analytical warehouses. Structures timeseries data for longitudinal statistical analysis. |

### Official Google Cloud BigQuery public dataset connectors

*1 project. SQL-driven queries against Google Cloud's official BigQuery public trends datasets.*

| Project | What it does |
|---|---|
| [**jp-caldas/bigquery-google-trends-mcp**](https://github.com/jp-caldas/bigquery-google-trends-mcp) | Queries Google Cloud's official BigQuery public dataset (bigquery-public-data.google_trends) using standard SQL tools. Delivers zero-scraping enterprise compliance and multi-year historical depth with zero proxy risk. |

### Data lake batch pipelines and columnar storage

*2 projects. Batch extractors structuring historical trends into Parquet, DuckDB, and Postgres tables.*

| Project | What it does |
|---|---|
| [**pohjanlaakso/google_trends_pipeline**](https://github.com/pohjanlaakso/google_trends_pipeline) | Streams Google Trends timeseries into a Parquet-backed data lake with automated partition management. Enables sub-second columnar queries via DuckDB or Apache Spark. |
| [**kuwala-io/kuwala**](https://github.com/kuwala-io/kuwala) | Integrates Google Trends data extraction into an open-source data workspace for spatial and business intelligence. Combines search intent with regional demographic datasets. |

### Clean architecture adapters and territorial intelligence

*3 projects. Domain-driven adapters integrating Google Trends into regional and geospatial intelligence platforms.*

| Project | What it does |
|---|---|
| [**tawiza/tawiza**](https://github.com/tawiza/tawiza) | Applies Clean Architecture principles to encapsulate pytrends data fetching inside an enterprise territorial intelligence platform. Decouples upstream scraping from core business analytics. |
| [**rainmanjam/headwater**](https://github.com/rainmanjam/headwater) | Exposes a unified self-hosted REST and MCP API for Google Maps, News, Trends, and Autocomplete. Centralizes credential and proxy management behind a single local microservice. |
| [**A1-x-Tech/mcp-google-crux**](https://github.com/A1-x-Tech/mcp-google-crux) | Combines Chrome User Experience Report (CrUX) performance data with Google Trends search popularity. Correlates web vitals performance with brand search interest shifts. |

## Developer comparison table

*64 projects. Side-by-side technical decision matrix across 15 architectural, runtime, and economic dimensions. Project names link internally to their detailed section.*

| Project | Data Route | Anti-Bot Armor | HTML Challenge Guard | Storage Engine | Fast-Path Latency | Tool Topology | Schema Tokens | Runtime | Cold Start | Transport | Cost / 1k Calls | Free Tier | 2026 Active | Test CI |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [**0xmariowu/Autosearch**](#autonomous-trend-monitoring-agents-and-recurring-scanners) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**A1-x-Tech/mcp-google-crux**](#clean-architecture-adapters-and-territorial-intelligence) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**AKzar1el/mcp-trendpulse**](#rate-immune-public-xml-syndication-harvesters) | Public XML RSS Syndica | Rate-Immune (Zero Pr | XML Strict Parser | In-Memory Feed Cac | In-Memory | 5 News Tools | 540 tokens (News | Python | <90ms | Stdio | $0.00 (Public  | 100% Free Public | Yes (2026) | Unit Tests |
| [**Bostigger/google-trends-cli**](#interactive-terminal-shells-and-cli-query-tools) | Standalone Terminal CL | CLI --proxy Flag / E | Status Code Inspecti | Stdout JSON / Loca | N/A | CLI Flags | N/A (CLI Interfa | Go | <50ms | Stdout JSON | Free (OSS) | 100% Free Open S | Legacy | Basic Tests |
| [**Eason-Gao3/google-trends-mcp**](#rotating-residential-proxy-pools-and-failover-tracking) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | HTML | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**GoogleCloudPlatform/gcp-getting-started-lab-jp**](#claude-specific-trend-agents-and-prompts) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Jupyter Notebook / Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**HasData/google-trends-mcp**](#consolidated-single-tool-enum-mcp-servers) | Commercial Managed Gat | Cloud Proxy Fleet (M | Pre-parse Cloud Veri | Stateless (Pass-Th | N/A (Cloud) | 1 Consolidated E | 380 tokens (Cons | JavaScript | <25ms | Stdio + HTTP | 1k Free / SaaS | 1,000 credits/mo | Yes (2026) | Jest + CI |
| [**Hudson-Pufferfish/google-trends-cli**](#interactive-terminal-shells-and-cli-query-tools) | Standalone Terminal CL | CLI --proxy Flag / E | Status Code Inspecti | Stdout JSON / Loca | N/A | CLI Flags | N/A (CLI Interfa | Go | <50ms | Stdout JSON | Free (OSS) | 100% Free Open S | Legacy | Basic Tests |
| [**LafCorentin/gtrend-rs**](#high-performance-rust-scrapers-and-pipelines) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**Nao-30/google-trends-cli**](#interactive-terminal-shells-and-cli-query-tools) | Standalone Terminal CL | CLI --proxy Flag / E | Status Code Inspecti | Stdout JSON / Loca | N/A | CLI Flags | N/A (CLI Interfa | Python | <50ms | Stdout JSON | Free (OSS) | 100% Free Open S | Legacy | Basic Tests |
| [**Quadstronaut/SocialScour**](#ephemeral-daily-trend-snapshot-archives) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**RuochenLyu/google-trends-now**](#multi-tier-cache-ttl-and-stale-while-error-fallback) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**Shaivpidadi/trends-js**](#lightweight-typescript-and-javascript-engines) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**ToolOracle/newsoracle**](#trending-news-clustering-and-article-distillation) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Dockerfile | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**VytautasPliadis/Google-Trends-pipeline**](#airflow-orchestration-dags-and-dbt-star-schemas) | Airflow DAG + dbt Pipe | Configurable Proxy M | Retry Exception Catc | PostgreSQL Star Sc | N/A | 1-4 Tools | N/A (Pipeline Wo | Python / Airflow / dbt | Batch Scheduled | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**akvise/trends-checker**](#rotating-residential-proxy-pools-and-failover-tracking) | Standalone Terminal CL | CLI --proxy Flag / E | Status Code Inspecti | Stdout JSON / Loca | N/A | 1-4 Tools | N/A (CLI Interfa | Python | <50ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**asgard-ai-platform/mcp-google-trends-tw**](#regional-market-locators-and-asian-language-editions) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**blacknbunny/Google-Trends-CLI**](#interactive-terminal-shells-and-cli-query-tools) | Standalone Terminal CL | CLI --proxy Flag / E | Status Code Inspecti | Stdout JSON / Loca | N/A | CLI Flags | N/A (CLI Interfa | JavaScript | <50ms | Stdout JSON | Free (OSS) | 100% Free Open S | Legacy | Basic Tests |
| [**caicai-yao/social-trends-mcp**](#cross-network-momentum-aggregators) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**calipsow/gtrends**](#anti-detect-browser-emulation-and-fingerprint-masking) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Legacy | Basic Tests |
| [**claude-world/trend-pulse**](#autonomous-trend-monitoring-agents-and-recurring-scanners) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**cosjef/keepa_MCP**](#e-commerce-search-demand-and-retail-price-trackers) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**costrict-plugins-repo/github-trending-google-workspace-mcp**](#regional-market-locators-and-asian-language-editions) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**costrict-plugins-repo/github-trending-mcp-servers-docker**](#containerized-cloud-run-and-docker-deployments) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**cspoppuppy/DE-GoogleTrendsPipeline-Batch**](#airflow-orchestration-dags-and-dbt-star-schemas) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**dan1d/mercadolibre-mcp**](#e-commerce-search-demand-and-retail-price-trackers) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**david-wulf/trends-mcp-local**](#embedded-sqlite-storage-in-wal-mode) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**den-indance/google-trends-mcp**](#rotating-residential-proxy-pools-and-failover-tracking) | Direct Reverse-Enginee | Rotating Residential | looksLikeHtml Pre-Pa | In-Memory / proxie | N/A (Live) | 4 Discrete Tools | 610 tokens (4 Di | JavaScript | <120ms | Stdio | <$0.15 (Proxy) | 100% Free Open S | Yes (2026) | Vitest + Actions |
| [**ducnhd/google-data-mcp**](#session-cookie-jars-and-nid-token-persistence) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**flack0x/trendspyg**](#embedded-sqlite-storage-in-wal-mode) | Direct Scraper + Sessi | Single Configured Pr | JSONDecodeError Hand | Embedded SQLite (W | <15ms (SQLite) | 4 Discrete Tools | 720 tokens (Disc | Python | <85ms (<15ms Cached Read) | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Pytest + Coverage |
| [**goncaloaguer/unofficial-google-trends-mcp**](#containerized-cloud-run-and-docker-deployments) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**groovili/gogtrends**](#compiled-go-engines-and-multi-transport-daemons) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Go | <200ms | Stdio | Free (OSS) | 100% Free Open S | Legacy | Basic Tests |
| [**iswangwenbin/ohmytrends**](#anti-detect-browser-emulation-and-fingerprint-masking) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript / Bun | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**jmanek/google-news-trends-mcp**](#trending-news-clustering-and-article-distillation) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**jp-caldas/bigquery-google-trends-mcp**](#official-google-cloud-bigquery-public-dataset-connectors) | Google Cloud BigQuery  | GCP ADC / Service Ac | Official SQL API (No | Google BigQuery Da | BigQuery Indexed | SQL Tools | 510 tokens (SQL  | Python | <150ms | Stdio | GCP 1TB Free | GCP 1TB/mo Free  | Yes (2026) | SQL Mock Tests |
| [**kuwala-io/kuwala**](#data-lake-batch-pipelines-and-columnar-storage) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python / JavaScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Legacy | Basic Tests |
| [**lhitches/google-trends-mcp**](#zero-config-claude-code-marketplace-servers) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**mamboyepez17/trendscope**](#ephemeral-daily-trend-snapshot-archives) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**mvanhorn/printing-press-library**](#compiled-go-engines-and-multi-transport-daemons) | Compiled Go Native Scr | HTTP/SOCKS5 Transpor | HTTP Response Status | In-Memory | <10ms | 3 Explore Tools | 450 tokens (Go M | Go | <10ms | Stdio + HTTP :77 | Free / SERP | 100% Free Open S | Yes (2026) | Go Test + CI |
| [**nonatin1000/02-google-trends-agent-z**](#multi-search-gateways-and-commercial-serp-aggregators) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**openclaw-easy/ViralMint**](#marketing-analytics-and-reporting-integrations) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**pat310/google-trends-api**](#lightweight-typescript-and-javascript-engines) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**pipeworx-io/mcp-google-trends**](#multi-tier-cache-ttl-and-stale-while-error-fallback) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**pohjanlaakso/google_trends_pipeline**](#data-lake-batch-pipelines-and-columnar-storage) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**purahmanian/google-trends-mcp**](#zero-config-claude-code-marketplace-servers) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**rainmanjam/headwater**](#clean-architecture-adapters-and-territorial-intelligence) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**rcsolis/trendscli**](#interactive-terminal-shells-and-cli-query-tools) | Standalone Terminal CL | CLI --proxy Flag / E | Status Code Inspecti | Stdout JSON / Loca | N/A | CLI Flags | N/A (CLI Interfa | Go | <50ms | Stdout JSON | Free (OSS) | 100% Free Open S | Legacy | Basic Tests |
| [**senolalgul8-alt/google-trends-proxy**](#session-cookie-jars-and-nid-token-persistence) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Legacy | Basic Tests |
| [**shadawck/rust-trend**](#high-performance-rust-scrapers-and-pipelines) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Rust | <200ms | Stdio | Free (OSS) | 100% Free Open S | Legacy | Basic Tests |
| [**ski-p3r/google-news-trends-mcp**](#rate-immune-public-xml-syndication-harvesters) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**superagents-lab/search1api-mcp**](#multi-search-gateways-and-commercial-serp-aggregators) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | $1-$3 SaaS | 100% Free Open S | Yes (2026) | Basic Tests |
| [**t3chnicallyinclined/autoseo**](#high-performance-rust-scrapers-and-pipelines) | Standalone Terminal CL | CLI --proxy Flag / E | Status Code Inspecti | Stdout JSON / Loca | N/A | CLI Flags | N/A (CLI Interfa | Rust | <50ms | Stdout JSON | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**tawiza/tawiza**](#clean-architecture-adapters-and-territorial-intelligence) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**trendsmcp-ai/TrendWatch**](#cross-network-momentum-aggregators) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**trendsmcp-ai/Trends-MCP**](#cross-network-momentum-aggregators) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**trendsmcp-ai/amazon-trends-mcp**](#e-commerce-search-demand-and-retail-price-trackers) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**trendsmcp-ai/google-trends-mcp**](#cross-network-momentum-aggregators) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**trendsmcp-ai/reddit-trends-mcp**](#social-media-community-and-video-trend-scanners) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**trendsmcp-ai/tiktok-trends-mcp**](#social-media-community-and-video-trend-scanners) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**trendsmcp-ai/trends-agent-claude**](#claude-specific-trend-agents-and-prompts) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**trendsmcp-ai/youtube-trends-mcp**](#social-media-community-and-video-trend-scanners) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**tuckerelbon-hash/pytrends-proxy**](#session-cookie-jars-and-nid-token-persistence) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | Python | <200ms | Stdio | Free (OSS) | 100% Free Open S | Legacy | Basic Tests |
| [**twominutereports/google-trends-mcp**](#marketing-analytics-and-reporting-integrations) | Direct Scraper (Pytren | Basic / Environment  | Standard Exception H | In-Memory / Flat F | N/A | 1-4 Tools | 500-1000 tokens | TypeScript | <200ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Basic Tests |
| [**yiromo/pytrends-modern**](#anti-detect-browser-emulation-and-fingerprint-masking) | Headless Browser (Camo | Dynamic Chrome Exten | Browser CAPTCHA Solv | File-based Cache | File Cache | 5 Scraper Tools | 820 tokens | Python | >2,000ms | Stdio | Free (OSS) | 100% Free Open S | Yes (2026) | Pytest |

---

## Resources

- **[Google Trends Web Surface](https://trends.google.com/):** The public web portal exposing realtime and historical search interest exploration.
- **[Model Context Protocol (MCP) Specification](https://modelcontextprotocol.io/):** Open standard connecting AI models to external tools, data sources, and execution environments.
- **[Google BigQuery Public Dataset](https://cloud.google.com/bigquery/public-data):** Official enterprise Google Trends dataset (`bigquery-public-data.google_trends`).
- **[Google Trends Proxy Resilience Guide](docs/proxy-architecture.md):** Architectural patterns for rotating residential proxies, 3-strike dead proxy ejection, and challenge guards.
- **[Embedded SQLite WAL Ingestion Architecture](docs/sqlite-persistence.md):** Deep-dive on sub-20ms reads and historical trend preservation.
- **[The Relative 0-100 Scaling Law](docs/relative-scaling-guide.md):** Guidance on avoiding hallucinated search volumes in agent workflows.

## Reference

- **Direct JSON Endpoints:** Google's internal endpoints (`explore/PAGE`, `widgetdata/multirange`) require residential IP rotation and NID cookie persistence.
- **Public XML RSS Syndication:** Public feed at `trends.google.com/trending/rss` provides rate-immune trending topics without proxies.
- **Relative 0–100 Scaling Index:** Trends values represent popularity relative to the peak query point in the selected timeframe and geography, not absolute search volume.
- **Un-Proxied IP Ceiling:** Empirical tests confirm an un-proxied quota ceiling of approximately ~130 explore requests per 24 hours per IP before Google issues 429 or HTML challenge blocks.
- **Fast-Path Retrieval:** Embedding SQLite in WAL mode reduces repeat query latency from 1.5s–5.0s down to <15ms.
