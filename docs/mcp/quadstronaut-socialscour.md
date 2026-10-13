# Quadstronaut/SocialScour

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/Quadstronaut/SocialScour) · [JSON definitions](../../data/mcp/quadstronaut-socialscour.json)

Reviewed 2026-10-13 at commit [`33fc5ece8912`](https://github.com/Quadstronaut/SocialScour/tree/33fc5ece891230f78603af876441be3b5562ed0e).

Collect US trending candidates and single-keyword research into local runs; MCP returns paths and reads saved summaries.

**4 tool definitions; 2 marked Google Trends.**

- ask/discover return paths, not raw Google Trends series. Keyword interest and top related queries are saved as raw files; post summaries do not incorporate those measurements.
- discover can place Google Trends candidate names in a saved summary readable through read_summary; it is not a keyword comparison or region-interest tool.
- Requires reachable Ollama and instantiates other source clients even when Google Trends alone is selected. Experimental Reddit-only prototypes are excluded from the production list.

## Tools

| Tool | Scope |
|---|---|
| [`ask`](#tool-ask) | google-trends |
| [`discover`](#tool-discover) | google-trends |
| [`read_summary`](#tool-read-summary) | other |
| [`read_timeline`](#tool-read-timeline) | other |

<a id="tool-ask"></a>

### `ask`

Run the deterministic ask pipeline. Returns paths only.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `topic` | string | Yes | — | — | — |
| `window_days` | integer | No | `30` | — | — |
| `sources` | array of string / null | No | `null` | — | — |
| `summarizer` | string | No | `"ollama"` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "topic": {
      "title": "Topic",
      "type": "string"
    },
    "window_days": {
      "default": 30,
      "title": "Window Days",
      "type": "integer"
    },
    "sources": {
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
      "title": "Sources"
    },
    "summarizer": {
      "default": "ollama",
      "title": "Summarizer",
      "type": "string"
    }
  },
  "required": [
    "topic"
  ],
  "title": "askArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- sources schema is nullable array of unrestricted strings, not enum; implementation converts values to SourceKind (reddit, hn, indiehackers, google\_trends), raising ValueError for unknown strings.
- sources=null or [] selects every source.
- window\_days and top\_n have no schema bounds or explicit implementation positivity checks.
- Ollama ping is mandatory; every source client is constructed even when its source is not selected.
- summarizer is unrestricted string; copied into configuration/metadata, but ask always calls Ollama summarization and narration. No registered data\_root or geo parameter.

Sources: [social\_scraper/mcp\_server.py:115](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/mcp_server.py#L115-L120) · [social\_scraper/mcp\_server.py:17](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/mcp_server.py#L17-L49) · [social\_scraper/core/pipeline/ask.py:204](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/core/pipeline/ask.py#L204-L217) · [social\_scraper/core/sources/google\_trends.py:13](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/core/sources/google_trends.py#L13-L90)

<a id="tool-discover"></a>

### `discover`

Run the agentic discover loop. Returns paths only.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `window_days` | integer | No | `30` | — | — |
| `top_n` | integer | No | `5` | — | — |
| `sources` | array of string / null | No | `null` | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "window_days": {
      "default": 30,
      "title": "Window Days",
      "type": "integer"
    },
    "top_n": {
      "default": 5,
      "title": "Top N",
      "type": "integer"
    },
    "sources": {
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
      "title": "Sources"
    }
  },
  "title": "discoverArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- sources schema is nullable array of unrestricted strings, not enum; implementation converts values to SourceKind (reddit, hn, indiehackers, google\_trends), raising ValueError for unknown strings.
- sources=null or [] selects every source.
- window\_days and top\_n have no schema bounds or explicit implementation positivity checks.
- Ollama ping is mandatory; every source client is constructed even when its source is not selected.

Sources: [social\_scraper/mcp\_server.py:122](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/mcp_server.py#L122-L126) · [social\_scraper/mcp\_server.py:52](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/mcp_server.py#L52-L88) · [social\_scraper/core/agent/discover.py:39](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/core/agent/discover.py#L39-L53) · [social\_scraper/core/agent/discover.py:93](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/core/agent/discover.py#L93-L175)

<a id="tool-read-summary"></a>

### `read_summary`

Read the summary.md from a run folder.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `run_dir` | string | Yes | — | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "run_dir": {
      "title": "Run Dir",
      "type": "string"
    }
  },
  "required": [
    "run_dir"
  ],
  "title": "read_summaryArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- String paths/slugs have no format restrictions, traversal checks or existence constraints in schema; implementation only checks path.exists().

Sources: [social\_scraper/mcp\_server.py:128](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/mcp_server.py#L128-L131) · [social\_scraper/mcp\_server.py:91](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/mcp_server.py#L91-L95)

<a id="tool-read-timeline"></a>

### `read_timeline`

Read the timeline.md for a topic slug.

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `slug` | string | Yes | — | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "slug": {
      "title": "Slug",
      "type": "string"
    }
  },
  "required": [
    "slug"
  ],
  "title": "read_timelineArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- String paths/slugs have no format restrictions, traversal checks or existence constraints in schema; implementation only checks path.exists().

Sources: [social\_scraper/mcp\_server.py:133](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/mcp_server.py#L133-L136) · [social\_scraper/mcp\_server.py:98](https://github.com/Quadstronaut/SocialScour/blob/33fc5ece891230f78603af876441be3b5562ed0e/social_scraper/mcp_server.py#L98-L103)

## Schema provenance

Local FastMCP.list_tools() after calling actual main() with FastMCP.run patched to capture server without starting transport; MCP 1.30.0, Pydantic 2.13.5. No tool execution or network tool calls.

- Repository dependencies are lower-bounded, not locked; schema reflects installed MCP/Pydantic versions.
- Runtime service success and trendspy response compatibility were not tested.
- Independent dev-testing MCP prototypes excluded from production tool list; Claude prototype has five explicit schemas recorded separately; Aider prototype uses incompatible/nonexistent current MCP imports and decorator API, so exact registered schemas cannot be established.
