# Awesome Google Trends MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated plain-English index of Model Context Protocol (MCP) servers, autonomous agent tools, scrapers, and data pipelines for Google Trends.

Official links: [Google Trends](https://trends.google.com/) · [Model Context Protocol](https://modelcontextprotocol.io/) · [PyPI](https://pypi.org/) · [NPM](https://www.npmjs.com/) · [Zeo Agency](https://zeo.org/)

---

## Contents

- [Quick comparison table](#quick-comparison-table)
- [1. Scrape with proxy resilience and anti-bot bypass (9)](#1-scrape-with-proxy-resilience-and-anti-bot-bypass)
  - [Rotating residential proxy pools and failover tracking (3)](#rotating-residential-proxy-pools-and-failover-tracking)
  - [Anti-detect browser emulation and fingerprint masking (3)](#anti-detect-browser-emulation-and-fingerprint-masking)
  - [Session cookie jars and NID token persistence (3)](#session-cookie-jars-and-nid-token-persistence)
- [2. Persist, cache, and archive historical trends (6)](#2-persist-cache-and-archive-historical-trends)
  - [Embedded SQLite storage in WAL mode (2)](#embedded-sqlite-storage-in-wal-mode)
  - [Ephemeral daily trend snapshot archives (2)](#ephemeral-daily-trend-snapshot-archives)
  - [Multi-tier cache TTL and stale-while-error fallback (2)](#multi-tier-cache-ttl-and-stale-while-error-fallback)
- [3. Connect through hosted commercial APIs (5)](#3-connect-through-hosted-commercial-apis)
  - [Consolidated single-tool enum MCP servers (1)](#consolidated-single-tool-enum-mcp-servers)
  - [Multi-search gateways and commercial SERP aggregators (2)](#multi-search-gateways-and-commercial-serp-aggregators)
  - [Marketing analytics and reporting integrations (1)](#marketing-analytics-and-reporting-integrations)
  - [Containerized Cloud Run and Docker deployments (1)](#containerized-cloud-run-and-docker-deployments)
- [4. Monitor rate-immune RSS and news intelligence (6)](#4-monitor-rate-immune-rss-and-news-intelligence)
  - [Rate-immune public XML syndication harvesters (2)](#rate-immune-public-xml-syndication-harvesters)
  - [Trending news clustering and article distillation (2)](#trending-news-clustering-and-article-distillation)
  - [Autonomous trend monitoring agents and recurring scanners (2)](#autonomous-trend-monitoring-agents-and-recurring-scanners)
- [5. Integrate with developer assistants and coding IDEs (4)](#5-integrate-with-developer-assistants-and-coding-ides)
  - [Zero-config Claude Code marketplace servers (2)](#zero-config-claude-code-marketplace-servers)
  - [Claude-specific trend agents and prompts (1)](#claude-specific-trend-agents-and-prompts)
  - [Regional market locators and Asian language editions (1)](#regional-market-locators-and-asian-language-editions)
- [6. Execute high-performance binaries and terminal CLIs (9)](#6-execute-high-performance-binaries-and-terminal-clis)
  - [Compiled Go engines and multi-transport daemons (2)](#compiled-go-engines-and-multi-transport-daemons)
  - [High-performance Rust scrapers and pipelines (3)](#high-performance-rust-scrapers-and-pipelines)
  - [Interactive terminal shells and CLI query tools (2)](#interactive-terminal-shells-and-cli-query-tools)
  - [Lightweight TypeScript and JavaScript engines (2)](#lightweight-typescript-and-javascript-engines)
- [7. Aggregate multi-platform search momentum (3)](#7-aggregate-multi-platform-search-momentum)
  - [Cross-network momentum aggregators (3)](#cross-network-momentum-aggregators)
- [8. Orchestrate enterprise pipelines and warehouse ingestion (5)](#8-orchestrate-enterprise-pipelines-and-warehouse-ingestion)
  - [Airflow orchestration DAGs and dbt star schemas (1)](#airflow-orchestration-dags-and-dbt-star-schemas)
  - [Official Google Cloud BigQuery public dataset connectors (1)](#official-google-cloud-bigquery-public-dataset-connectors)
  - [Data lake batch pipelines and columnar storage (1)](#data-lake-batch-pipelines-and-columnar-storage)
  - [Clean architecture adapters and territorial intelligence (2)](#clean-architecture-adapters-and-territorial-intelligence)
- [Resources](#resources)
- [Reference](#reference)

---

## Quick comparison table

*47 projects. High-density decision matrix optimized for fast scanning. Project names link directly to detailed sections.*

**Legend:**

- **Resilience:** `🛡️ Pool` (rotating residential proxy pool) · `⚡ RSS/SQL` (rate-immune public XML or BigQuery SQL) · `🎭 Browser` (anti-detect browser engine) · `⚠️ Basic` (direct scraper, ~130 req/day quota)
- **Cache:** `💾 SQLite` (embedded WAL mode, <15ms reads) · `⏱️ Memory` (in-memory TTL or file cache) · `🗄️ Lake` (warehouse or Parquet lake) · `—` (stateless live pass-through)
- **Tier:** `★★★` (Production-grade / Battle-tested) · `★★☆` (Functional utility / Specialized) · `★☆☆` (Reference implementation)

| Project | Interface | Runtime | Anti-Bot Resilience | Cache Engine | Transport | Tier |
|---|---|---|---|---|---|---|
| [**0xmariowu/Autosearch**](#autonomous-trend-monitoring-agents-and-recurring-scanners) | Agent | Node | ⚡ RSS/SQL | ⏱️ Memory | CLI | ★★☆ |
| [**akvise/trends-checker**](#rotating-residential-proxy-pools-and-failover-tracking) | CLI | Python | 🛡️ Pool | ⏱️ Memory | CLI | ★★☆ |
| [**AKzar1el/mcp-trendpulse**](#rate-immune-public-xml-syndication-harvesters) | MCP | Python | ⚡ RSS/SQL | ⏱️ Memory | stdio | ★★★ |
| [**asgard-ai-platform/mcp-google-trends-tw**](#regional-market-locators-and-asian-language-editions) | MCP | Python | ⚠️ Basic | — | stdio | ★★☆ |
| [**calipsow/gtrends**](#anti-detect-browser-emulation-and-fingerprint-masking) | Library | Python | 🎭 Browser | ⏱️ Memory | CLI | ★★☆ |
| [**claude-world/trend-pulse**](#autonomous-trend-monitoring-agents-and-recurring-scanners) | MCP + CLI | Python | ⚡ RSS/SQL | ⏱️ Memory | stdio+CLI | ★★☆ |
| [**david-wulf/trends-mcp-local**](#embedded-sqlite-storage-in-wal-mode) | MCP | Python | ⚠️ Basic | 💾 SQLite | stdio | ★★☆ |
| [**den-indance/google-trends-mcp**](#rotating-residential-proxy-pools-and-failover-tracking) | MCP | Node | 🛡️ Pool | ⏱️ Memory | stdio | ★★★ |
| [**ducnhd/google-data-mcp**](#session-cookie-jars-and-nid-token-persistence) | MCP | Python | ⚠️ Basic | ⏱️ Memory | stdio | ★★☆ |
| [**Eason-Gao3/google-trends-mcp**](#rotating-residential-proxy-pools-and-failover-tracking) | MCP | Node | 🛡️ Pool | 💾 SQLite | stdio | ★★★ |
| [**flack0x/trendspyg**](#embedded-sqlite-storage-in-wal-mode) | MCP + CLI | Python | ⚠️ Basic | 💾 SQLite | stdio+CLI | ★★★ |
| [**goncaloaguer/unofficial-google-trends-mcp**](#containerized-cloud-run-and-docker-deployments) | MCP | Python | ⚠️ Basic | — | HTTP/SSE | ★★☆ |
| [**groovili/gogtrends**](#compiled-go-engines-and-multi-transport-daemons) | Library | Go | ⚠️ Basic | ⏱️ Memory | Library | ★★☆ |
| [**HasData/google-trends-mcp**](#consolidated-single-tool-enum-mcp-servers) | MCP | Node | 🛡️ Pool | — | stdio+HTTP | ★★★ |
| [**iswangwenbin/ohmytrends**](#anti-detect-browser-emulation-and-fingerprint-masking) | CLI + API | Bun | 🎭 Browser | ⏱️ Memory | CLI+HTTP | ★★☆ |
| [**jmanek/google-news-trends-mcp**](#trending-news-clustering-and-article-distillation) | MCP | Python | ⚡ RSS/SQL | ⏱️ Memory | stdio | ★★★ |
| [**jp-caldas/bigquery-google-trends-mcp**](#official-google-cloud-bigquery-public-dataset-connectors) | MCP | Python | ⚡ RSS/SQL | 🗄️ Lake | stdio | ★★★ |
| [**LafCorentin/gtrend-rs**](#high-performance-rust-scrapers-and-pipelines) | Library | Rust | ⚠️ Basic | ⏱️ Memory | Library | ★★☆ |
| [**lhitches/google-trends-mcp**](#zero-config-claude-code-marketplace-servers) | MCP | Python | ⚠️ Basic | — | stdio | ★★★ |
| [**mamboyepez17/trendscope**](#ephemeral-daily-trend-snapshot-archives) | Service | Python | ⚠️ Basic | 💾 SQLite | HTTP | ★★☆ |
| [**mvanhorn/printing-press-library**](#compiled-go-engines-and-multi-transport-daemons) | CLI | Go | ⚠️ Basic | ⏱️ Memory | CLI+HTTP | ★★★ |
| [**Nao-30/google-trends-cli**](#interactive-terminal-shells-and-cli-query-tools) | CLI | Python | ⚠️ Basic | — | CLI | ★★☆ |
| [**nonatin1000/02-google-trends-agent-z**](#multi-search-gateways-and-commercial-serp-aggregators) | Agent | Python | 🛡️ Pool | — | CLI | ★★☆ |
| [**pat310/google-trends-api**](#lightweight-typescript-and-javascript-engines) | Library | Node | ⚠️ Basic | — | Library | ★★★ |
| [**pipeworx-io/mcp-google-trends**](#multi-tier-cache-ttl-and-stale-while-error-fallback) | MCP | Node | ⚠️ Basic | ⏱️ Memory | stdio | ★★☆ |
| [**pohjanlaakso/google_trends_pipeline**](#data-lake-batch-pipelines-and-columnar-storage) | Pipeline | Node | ⚠️ Basic | 🗄️ Lake | Batch | ★★☆ |
| [**purahmanian/google-trends-mcp**](#zero-config-claude-code-marketplace-servers) | MCP | Node | ⚠️ Basic | — | stdio | ★★☆ |
| [**Quadstronaut/SocialScour**](#ephemeral-daily-trend-snapshot-archives) | Aggregator | Python | ⚠️ Basic | 💾 SQLite | CLI | ★★☆ |
| [**rainmanjam/headwater**](#clean-architecture-adapters-and-territorial-intelligence) | API + MCP | Python | ⚠️ Basic | ⏱️ Memory | stdio+HTTP | ★★☆ |
| [**rcsolis/trendscli**](#interactive-terminal-shells-and-cli-query-tools) | CLI | Go | ⚠️ Basic | — | CLI | ★★☆ |
| [**RuochenLyu/google-trends-now**](#multi-tier-cache-ttl-and-stale-while-error-fallback) | CLI + Node | Node | ⚡ RSS/SQL | ⏱️ Memory | CLI | ★★☆ |
| [**senolalgul8-alt/google-trends-proxy**](#session-cookie-jars-and-nid-token-persistence) | Proxy Tunnel | Python | 🛡️ Pool | — | HTTP | ★★☆ |
| [**shadawck/rust-trend**](#high-performance-rust-scrapers-and-pipelines) | Library | Rust | ⚠️ Basic | ⏱️ Memory | Library | ★★☆ |
| [**Shaivpidadi/trends-js**](#lightweight-typescript-and-javascript-engines) | Library | Node | ⚠️ Basic | — | Library | ★★☆ |
| [**ski-p3r/google-news-trends-mcp**](#rate-immune-public-xml-syndication-harvesters) | MCP | Python | ⚡ RSS/SQL | ⏱️ Memory | stdio | ★★☆ |
| [**superagents-lab/search1api-mcp**](#multi-search-gateways-and-commercial-serp-aggregators) | MCP | Node | 🛡️ Pool | — | stdio+HTTP | ★★☆ |
| [**t3chnicallyinclined/autoseo**](#high-performance-rust-scrapers-and-pipelines) | CLI | Rust | ⚠️ Basic | ⏱️ Memory | CLI | ★★☆ |
| [**tawiza/tawiza**](#clean-architecture-adapters-and-territorial-intelligence) | Platform | Node | ⚠️ Basic | 🗄️ Lake | HTTP | ★★☆ |
| [**ToolOracle/newsoracle**](#trending-news-clustering-and-article-distillation) | MCP | Docker | ⚡ RSS/SQL | ⏱️ Memory | stdio | ★★☆ |
| [**trendsmcp-ai/google-trends-mcp**](#cross-network-momentum-aggregators) | MCP | Python | ⚠️ Basic | — | stdio | ★★☆ |
| [**trendsmcp-ai/trends-agent-claude**](#claude-specific-trend-agents-and-prompts) | Agent | Node | ⚠️ Basic | — | stdio | ★★☆ |
| [**trendsmcp-ai/Trends-MCP**](#cross-network-momentum-aggregators) | MCP | Python | ⚠️ Basic | — | stdio | ★★☆ |
| [**trendsmcp-ai/TrendWatch**](#cross-network-momentum-aggregators) | Service | Python | ⚠️ Basic | ⏱️ Memory | CLI | ★★☆ |
| [**tuckerelbon-hash/pytrends-proxy**](#session-cookie-jars-and-nid-token-persistence) | Proxy Tunnel | Python | 🛡️ Pool | — | HTTP | ★★☆ |
| [**twominutereports/google-trends-mcp**](#marketing-analytics-and-reporting-integrations) | MCP | Node | ⚠️ Basic | — | stdio | ★★☆ |
| [**VytautasPliadis/Google-Trends-pipeline**](#airflow-orchestration-dags-and-dbt-star-schemas) | Pipeline | Python | ⚠️ Basic | 🗄️ Lake | Batch | ★★★ |
| [**yiromo/pytrends-modern**](#anti-detect-browser-emulation-and-fingerprint-masking) | Library | Python | 🎭 Browser | ⏱️ Memory | CLI | ★★☆ |

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

*5 projects. Cloud-managed APIs and commercial gateways that offload anti-bot mitigation and guarantee uptime SLAs.*

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

*1 project. Commercial connectors syncing Google Trends with BI dashboards and automated client reports.*

| Project | What it does |
|---|---|
| [**twominutereports/google-trends-mcp**](https://github.com/twominutereports/google-trends-mcp) | Connects Google Trends search metrics directly into automated BI reporting pipelines and marketing dashboards. Formats multi-region interest data into structured tables ready for scheduled reporting. |

### Containerized Cloud Run and Docker deployments

*1 project. Packaged container images deployable to cloud runtimes with pre-configured API keys.*

| Project | What it does |
|---|---|
| [**goncaloaguer/unofficial-google-trends-mcp**](https://github.com/goncaloaguer/unofficial-google-trends-mcp) | Packages an unofficial Google Trends MCP server into a lightweight Google Cloud Run container. Exposes Streamable HTTP and SSE transports with container-level environment variable configuration. |

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

*4 projects. Zero-config MCP servers tailored for Claude Code, Cursor, Windsurf, and developer coding workflows.*

### Zero-config Claude Code marketplace servers

*2 projects. Keyless FastMCP servers installable via uvx or marketplace commands without configuration.*

| Project | What it does |
|---|---|
| [**lhitches/google-trends-mcp**](https://github.com/lhitches/google-trends-mcp) | Provides a keyless FastMCP server designed specifically for Claude Code and Cursor desktop assistants. Exposes four clean tools covering interest over time, related queries, regional interest, and trending searches. |
| [**purahmanian/google-trends-mcp**](https://github.com/purahmanian/google-trends-mcp) | Installs with a single command via uvx to deliver zero-config Google Trends exploration for local AI coding assistants. Handles parameter validation internally to prevent cryptic upstream errors. |

### Claude-specific trend agents and prompts

*1 project. Specialized prompt packs and tool plugins optimized for Claude desktop assistants.*

| Project | What it does |
|---|---|
| [**trendsmcp-ai/trends-agent-claude**](https://github.com/trendsmcp-ai/trends-agent-claude) | Delivers a Claude-tailored prompt pack and MCP tool wrapper pre-configured for market analysis. Formats relative interest curves with explicit 0-100 scaling documentation to prevent hallucinated volume claims. |

### Regional market locators and Asian language editions

*1 project. Localized MCP configurations pre-tuned for regional Google Trends indices and DMA codes.*

| Project | What it does |
|---|---|
| [**asgard-ai-platform/mcp-google-trends-tw**](https://github.com/asgard-ai-platform/mcp-google-trends-tw) | Specializes in East Asian market intelligence with pre-configured Taiwan DMA and regional language parameters. Optimizes UTF-8 character handling for Traditional Chinese search terms. |

## 6. Execute high-performance binaries and terminal CLIs

*9 projects. Compiled binaries, terminal utilities, and lightweight runtimes built for execution speed and low memory.*

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

*2 projects. Command-line interfaces outputting structured JSON to stdout for shell pipelines and agent execution.*

| Project | What it does |
|---|---|
| [**Nao-30/google-trends-cli**](https://github.com/Nao-30/google-trends-cli) | Queries Google Trends from the command line with clean JSON stdout formatting suitable for shell pipelines and agent execution. Supports custom date ranges and regional filtering flags. |
| [**rcsolis/trendscli**](https://github.com/rcsolis/trendscli) | Delivers an interactive terminal utility for exploring keyword interest curves with ASCII terminal charts. Outputs structured JSON when invoked with automation flags. |

### Lightweight TypeScript and JavaScript engines

*2 projects. Node and Bun packages providing clean programmatic client interfaces.*

| Project | What it does |
|---|---|
| [**Shaivpidadi/trends-js**](https://github.com/Shaivpidadi/trends-js) | Provides a modern TypeScript client library for Google Trends with full type definitions and promise-based interfaces. Handles response payload parsing and sanitization across modern Node runtimes. |
| [**pat310/google-trends-api**](https://github.com/pat310/google-trends-api) | Serves as the foundational JavaScript library underpinning numerous community scrapers and MCP servers. Encapsulates request signing and widget token resolution for explore queries. |

## 7. Aggregate multi-platform search momentum

*3 projects. Multi-network engines monitoring search and viral momentum across Google and social platforms.*

### Cross-network momentum aggregators

*3 projects. Engines simultaneously querying Google Trends alongside social platforms.*

| Project | What it does |
|---|---|
| [**trendsmcp-ai/Trends-MCP**](https://github.com/trendsmcp-ai/Trends-MCP) | Aggregates search momentum across Google Trends, TikTok, and YouTube to provide multi-platform trend intelligence. Compares relative search interest against social video engagement. |
| [**trendsmcp-ai/TrendWatch**](https://github.com/trendsmcp-ai/TrendWatch) | Monitors emerging keyword velocity across search engines and social platforms using unified agent tools. Generates consolidated momentum alerts for social listening pipelines. |
| [**trendsmcp-ai/google-trends-mcp**](https://github.com/trendsmcp-ai/google-trends-mcp) | Provides real-time Google search trends with automated multi-region support and category filtering. Prepares trend data for downstream LLM synthesis and agent tool calls. |

## 8. Orchestrate enterprise pipelines and warehouse ingestion

*5 projects. Production data engineering pipelines, BigQuery public datasets, and territorial intelligence systems.*

### Airflow orchestration DAGs and dbt star schemas

*1 project. Scheduled workflow orchestration syncing Google Trends into relational star schemas.*

| Project | What it does |
|---|---|
| [**VytautasPliadis/Google-Trends-pipeline**](https://github.com/VytautasPliadis/Google-Trends-pipeline) | Orchestrates production Airflow DAGs that ingest Google Trends data into a dbt star schema in PostgreSQL. Automates batch scheduling, schema migrations, and enterprise data modeling. |

### Official Google Cloud BigQuery public dataset connectors

*1 project. SQL-driven queries against Google Cloud's official BigQuery public trends datasets.*

| Project | What it does |
|---|---|
| [**jp-caldas/bigquery-google-trends-mcp**](https://github.com/jp-caldas/bigquery-google-trends-mcp) | Queries Google Cloud's official BigQuery public dataset (`bigquery-public-data.google_trends`) using standard SQL tools. Delivers zero-scraping enterprise compliance and multi-year historical depth with zero proxy risk. |

### Data lake batch pipelines and columnar storage

*1 project. Batch extractors structuring historical trends into Parquet, DuckDB, and Postgres tables.*

| Project | What it does |
|---|---|
| [**pohjanlaakso/google_trends_pipeline**](https://github.com/pohjanlaakso/google_trends_pipeline) | Streams Google Trends timeseries into a Parquet-backed data lake with automated partition management. Enables sub-second columnar queries via DuckDB or Apache Spark. |

### Clean architecture adapters and territorial intelligence

*2 projects. Domain-driven adapters integrating Google Trends into regional and geospatial intelligence platforms.*

| Project | What it does |
|---|---|
| [**tawiza/tawiza**](https://github.com/tawiza/tawiza) | Applies Clean Architecture principles to encapsulate pytrends data fetching inside an enterprise territorial intelligence platform. Decouples upstream scraping from core business analytics. |
| [**rainmanjam/headwater**](https://github.com/rainmanjam/headwater) | Exposes a unified self-hosted REST and MCP API for Google Maps, News, Trends, and Autocomplete. Centralizes credential and proxy management behind a single local microservice. |

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
