# Eason-Gao3/google-trends-mcp

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/Eason-Gao3/google-trends-mcp) · [JSON definitions](../../data/mcp/eason-gao3-google-trends-mcp.json)

Reviewed 2026-10-13 at commit [`c173efbb941c`](https://github.com/Eason-Gao3/google-trends-mcp/tree/c173efbb941c64f204b329eba97c96b5ddb27db1).

Compare terms and normalize larger keyword batches with a shared anchor, synchronously or as saved jobs.

**4 tool definitions; 3 marked Google Trends.**

- Async submission/status require an initialized research_tasks SQLite table; the stdio entrypoint does not initialize it.

## Tools

| Tool | Scope |
|---|---|
| [`compare_keywords`](#tool-compare-keywords) | google-trends |
| [`research_keywords`](#tool-research-keywords) | google-trends |
| [`research_keywords_async`](#tool-research-keywords-async) | google-trends |
| [`get_research_task`](#tool-get-research-task) | server-management |

<a id="tool-compare-keywords"></a>

### `compare_keywords`

对比最多 5 个关键词在 Google Trends 上的时间序列热度。

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | — | — |
| `timeframe` | string | No | `"today 5-y"` | — | — |
| `geo` | string | No | `""` | — | — |
| `drop_partial` | boolean | No | `true` | — | — |

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
    "timeframe": {
      "default": "today 5-y",
      "title": "Timeframe",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "drop_partial": {
      "default": true,
      "title": "Drop Partial",
      "type": "boolean"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "compare_keywordsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Input schema has no keyword count/item-length bounds, geo pattern, timeframe enum, or TTL bounds; these must not be inferred from prose.
- Implementation strips timeframe and requires nonempty value; geo is stripped/uppercased and must be empty or match [A-Z0-9-]+.
- Rate limits are enabled only via GOOGLE\_TRENDS\_MCP\_RATE\_LIMIT; compare is 10/60s, research and async share 5/3600s.
- Keywords are trimmed, blank entries removed, case-insensitively deduplicated; resulting count must be 1–5.

Sources: [server.py:1828](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L1828-L1854) · [server.py:758](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L758-L804) · [server.py:1412](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L1412-L1504) · [server.py:923](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L923-L1017)

<a id="tool-research-keywords"></a>

### `research_keywords`

多关键词批量调研，支持最多 50 个关键词，使用 anchor 关键词进行跨批次归一化。

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | — | — |
| `timeframe` | string | No | `"today 5-y"` | — | — |
| `geo` | string | No | `""` | — | — |
| `anchor_keyword` | string / null | No | `null` | — | — |
| `drop_partial` | boolean | No | `true` | — | — |
| `cache_ttl_seconds` | integer | No | `900` | — | — |

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
    "timeframe": {
      "default": "today 5-y",
      "title": "Timeframe",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "anchor_keyword": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Anchor Keyword"
    },
    "drop_partial": {
      "default": true,
      "title": "Drop Partial",
      "type": "boolean"
    },
    "cache_ttl_seconds": {
      "default": 900,
      "title": "Cache Ttl Seconds",
      "type": "integer"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "research_keywordsArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Input schema has no keyword count/item-length bounds, geo pattern, timeframe enum, or TTL bounds; these must not be inferred from prose.
- Implementation strips timeframe and requires nonempty value; geo is stripped/uppercased and must be empty or match [A-Z0-9-]+.
- Rate limits are enabled only via GOOGLE\_TRENDS\_MCP\_RATE\_LIMIT; compare is 10/60s, research and async share 5/3600s.
- Keywords are trimmed, blank entries removed, case-insensitively deduplicated; resulting count must be 1–50. Anchor defaults to first cleaned keyword; a nonempty new anchor is appended and must fit within the 50-keyword limit.
- cache\_ttl\_seconds is an unconstrained integer; no positive-value validation is implemented.

Sources: [server.py:1857](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L1857-L1892) · [server.py:1575](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L1575-L1621) · [server.py:1661](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L1661-L1825) · [server.py:1020](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L1020-L1154)

<a id="tool-research-keywords-async"></a>

### `research_keywords_async`

提交批量调研任务，立即返回 task\_id。适用于 5+ 关键词的长任务。

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `keywords` | array of string | Yes | — | — | — |
| `timeframe` | string | No | `"today 5-y"` | — | — |
| `geo` | string | No | `""` | — | — |
| `anchor_keyword` | string / null | No | `null` | — | — |
| `drop_partial` | boolean | No | `true` | — | — |
| `cache_ttl_seconds` | integer | No | `900` | — | — |

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
    "timeframe": {
      "default": "today 5-y",
      "title": "Timeframe",
      "type": "string"
    },
    "geo": {
      "default": "",
      "title": "Geo",
      "type": "string"
    },
    "anchor_keyword": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Anchor Keyword"
    },
    "drop_partial": {
      "default": true,
      "title": "Drop Partial",
      "type": "boolean"
    },
    "cache_ttl_seconds": {
      "default": 900,
      "title": "Cache Ttl Seconds",
      "type": "integer"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "research_keywords_asyncArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Same research keyword/anchor normalization and 1–50 implementation count limit as research\_keywords.
- Timeframe and geo validation happens in the background research task after submission, not before returning task\_id.
- cache\_ttl\_seconds is an unconstrained integer; no positive-value validation is implemented.
- SQLite research\_tasks schema is initialized by web lifespan only; plain stdio mode does not call init\_database, so async tools require an already initialized database.

Sources: [server.py:1976](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L1976-L2032) · [server.py:1575](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L1575-L1621) · [server.py:1921](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L1921-L1973) · [server.py:390](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L390-L469) · [server.py:2939](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L2939-L2950)

<a id="tool-get-research-task"></a>

### `get_research_task`

查询异步调研任务的进度或拉取结果。

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `task_id` | string | Yes | — | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "task_id": {
      "title": "Task Id",
      "type": "string"
    }
  },
  "required": [
    "task_id"
  ],
  "title": "get_research_taskArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- task\_id has no format or length restriction; lookup uses a SQL parameter.
- No task ownership filter is present in this lookup.
- SQLite research\_tasks schema is initialized by web lifespan only; plain stdio mode requires an already initialized database.

Sources: [server.py:2035](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L2035-L2061) · [server.py:390](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L390-L469) · [server.py:2939](https://github.com/Eason-Gao3/google-trends-mcp/blob/c173efbb941c64f204b329eba97c96b5ddb27db1/server.py#L2939-L2950)

## Schema provenance

AST-isolated actual FastMCP registration: copied exact tool decorators, signatures, defaults and docstrings plus required constant/server assignments into a local module; replaced implementation bodies with inert returns; obtained schemas with FastMCP.list_tools(). No tool calls executed. Runtime mcp 1.30.0, Pydantic 2.13.5.

- Repository specifies mcp>=1.2.0 and unpinned dependencies; introspected with installed mcp 1.30.0/Pydantic 2.13.5, so another dependency version may emit different incidental schema details.
- Full server import was unavailable because pandas is not installed; AST isolation preserves every registration-relevant element and avoids provider/web runtime imports.
- Schemas and implementation verified from source; live Google Trends/provider behavior was not exercised.
