# jp-caldas/bigquery-google-trends-mcp

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/jp-caldas/bigquery-google-trends-mcp) · [JSON definitions](../../data/mcp/jp-caldas-bigquery-google-trends-mcp.json)

Reviewed 2026-10-13 at commit [`55fa5a3941e5`](https://github.com/jp-caldas/bigquery-google-trends-mcp/tree/55fa5a3941e5c45a143f1b056b63d086b2df1db3).

Query top terms, rising terms, or recorded weekly scores for one term and country.

**3 tool definitions; 3 marked Google Trends.**

- Requires a Google Cloud project and application-default credentials. Country values are validated in implementation, not an input-schema enum.
- comparar_termo_tool retrieves one term’s recorded history; it does not compare multiple terms. Registrations provide no descriptions, so the English behavior summaries come from SQL source.

## Tools

| Tool | Scope |
|---|---|
| [`buscar_termos_em_alta_tool`](#tool-buscar-termos-em-alta-tool) | google-trends |
| [`buscar_termos_emergentes_tool`](#tool-buscar-termos-emergentes-tool) | google-trends |
| [`comparar_termo_tool`](#tool-comparar-termo-tool) | google-trends |

<a id="tool-buscar-termos-em-alta-tool"></a>

### `buscar_termos_em_alta_tool`

Queries bigquery-public-data.google\_trends.international\_top\_terms for a country with week >= data\_limite, ordered by newest week then ascending rank. Returns term, nullable score, and rank for each row; no result limit or deduplication.

*The registration supplies no description.*

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `pais` | string | Yes | — | — | — |
| `data_limite` | string | Yes | — | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "pais": {
      "title": "Pais",
      "type": "string"
    },
    "data_limite": {
      "title": "Data Limite",
      "type": "string"
    }
  },
  "required": [
    "pais",
    "data_limite"
  ],
  "title": "buscar_termos_em_alta_toolArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation uppercases pais, then restricts it to AU, BR, CA, DE, ES, FR, GB, IN, JP, US; this restriction is not an input-schema enum.
- All input fields are required strings with no defaults, nullable variants, bounds, patterns, or date formats in the schema. additionalProperties is unspecified.
- Dates are not parsed or validated locally. They are passed as STRING BigQuery query parameters, and any query/type/date failure becomes BigQueryError.
- An initialized BigQuery client is required for execution; startup validates GOOGLE\_CLOUD\_PROJECT and creates an ADC-authenticated client. No client or server context is caller-supplied.
- No rows yields an empty list.

Sources: [src/mcp\_google\_trends/server.py:36](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/server.py#L36-L38) · [src/mcp\_google\_trends/tools.py:47](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/tools.py#L47-L61) · [src/mcp\_google\_trends/tools.py:9](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/tools.py#L9-L19) · [src/mcp\_google\_trends/bigquery\_client.py:6](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/bigquery_client.py#L6-L35)

<a id="tool-buscar-termos-emergentes-tool"></a>

### `buscar_termos_emergentes_tool`

Queries bigquery-public-data.google\_trends.international\_top\_rising\_terms for a country with week >= data\_limite, ordered by descending percent\_gain. Returns term, percent\_gain, and nullable score; no result limit or deduplication.

*The registration supplies no description.*

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `pais` | string | Yes | — | — | — |
| `data_limite` | string | Yes | — | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "pais": {
      "title": "Pais",
      "type": "string"
    },
    "data_limite": {
      "title": "Data Limite",
      "type": "string"
    }
  },
  "required": [
    "pais",
    "data_limite"
  ],
  "title": "buscar_termos_emergentes_toolArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation uppercases pais, then restricts it to AU, BR, CA, DE, ES, FR, GB, IN, JP, US; this restriction is not an input-schema enum.
- All input fields are required strings with no defaults, nullable variants, bounds, patterns, or date formats in the schema. additionalProperties is unspecified.
- Dates are not parsed or validated locally. They are passed as STRING BigQuery query parameters, and any query/type/date failure becomes BigQueryError.
- An initialized BigQuery client is required for execution; startup validates GOOGLE\_CLOUD\_PROJECT and creates an ADC-authenticated client. No client or server context is caller-supplied.
- No rows yields an empty list.

Sources: [src/mcp\_google\_trends/server.py:41](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/server.py#L41-L45) · [src/mcp\_google\_trends/tools.py:64](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/tools.py#L64-L78) · [src/mcp\_google\_trends/tools.py:9](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/tools.py#L9-L19) · [src/mcp\_google\_trends/bigquery\_client.py:6](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/bigquery_client.py#L6-L35)

<a id="tool-comparar-termo-tool"></a>

### `comparar_termo_tool`

Queries bigquery-public-data.google\_trends.international\_top\_terms for one case-insensitively matched term and country, with week BETWEEN data\_inicio AND data\_fim, ordered by ascending week. Returns week, term, nullable score, and rank. Despite its name it does not compare multiple terms.

*The registration supplies no description.*

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `termo` | string | Yes | — | — | — |
| `pais` | string | Yes | — | — | — |
| `data_inicio` | string | Yes | — | — | — |
| `data_fim` | string | Yes | — | — | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "properties": {
    "termo": {
      "title": "Termo",
      "type": "string"
    },
    "pais": {
      "title": "Pais",
      "type": "string"
    },
    "data_inicio": {
      "title": "Data Inicio",
      "type": "string"
    },
    "data_fim": {
      "title": "Data Fim",
      "type": "string"
    }
  },
  "required": [
    "termo",
    "pais",
    "data_inicio",
    "data_fim"
  ],
  "title": "comparar_termo_toolArguments",
  "type": "object"
}
```

</details>

Implementation notes:

- Implementation uppercases pais, then restricts it to AU, BR, CA, DE, ES, FR, GB, IN, JP, US; this restriction is not an input-schema enum.
- All input fields are required strings with no defaults, nullable variants, bounds, patterns, or date formats in the schema. additionalProperties is unspecified.
- Dates are not parsed or validated locally. They are passed as STRING BigQuery query parameters, and any query/type/date failure becomes BigQueryError.
- An initialized BigQuery client is required for execution; startup validates GOOGLE\_CLOUD\_PROJECT and creates an ADC-authenticated client. No client or server context is caller-supplied.
- No rows yields an empty list.
- termo is lowercased before exact SQL equality; there is no empty-term or date-order validation. SQL BETWEEN includes both endpoints.

Sources: [src/mcp\_google\_trends/server.py:48](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/server.py#L48-L55) · [src/mcp\_google\_trends/tools.py:81](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/tools.py#L81-L107) · [src/mcp\_google\_trends/tools.py:9](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/tools.py#L9-L19) · [src/mcp\_google\_trends/bigquery\_client.py:6](https://github.com/jp-caldas/bigquery-google-trends-mcp/blob/55fa5a3941e5c45a143f1b056b63d086b2df1db3/src/mcp_google_trends/bigquery_client.py#L6-L35)

## Schema provenance

AST selected all @mcp.tool() wrapper definitions from server.py unchanged and executed their registrations in an isolated FastMCP instance; called local list_tools() with repository-locked mcp 1.28.1 and Pydantic 2.13.4. No wrapper body, repository startup/config import, credential read, client creation, or remote tool call executed. Inspected complete source tree for registrations and implementations.

- Runtime BigQuery execution and dataset availability were not tested. Local introspection bypasses lifespan/imports intentionally; registration definitions and annotations are executed unchanged.
- Project permits broad dependency versions; schemas are verified against its uv.lock versions, not every permitted version.
