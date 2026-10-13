# HasData/google-trends-mcp

[Catalog](../../README.md) · [Tool name index](../tools.md) · [Repository](https://github.com/HasData/google-trends-mcp) · [JSON definitions](../../data/mcp/hasdata-google-trends-mcp.json)

Reviewed 2026-10-13 at commit [`f6fd4c341ffc`](https://github.com/HasData/google-trends-mcp/tree/f6fd4c341ffc3eeb09e93de4a281e7084d691f35).

Select time series, geographic interest, related queries, or related topics through one hosted tool.

**1 tool definitions; 1 marked Google Trends.**

- The schema was captured from the hosted tools/list endpoint. A HasData API key is required by the connector; hosted execution and validation were not tested.

## Tools

| Tool | Scope |
|---|---|
| [`hasdata_google_trends_search_getTrendsData`](#tool-hasdata-google-trends-search-gettrendsdata) | google-trends |

<a id="tool-hasdata-google-trends-search-gettrendsdata"></a>

### `hasdata_google_trends_search_getTrendsData`

Hosted Google Trends retrieval for one or multiple queries: interest over time, geography, related topics, or related queries selected by dataType. Local Node/Python packages only proxy the remote server; remote implementation is not public in this repository.

<details>
<summary>Full registered description</summary>

```text
Get Google Trends Data

Pulls Google Trends data for one or more queries with geo targeting, region granularity (country/subregion/metro/city), date range, category, time zone, Google property (web, images, news, shopping, YouTube), and dataType (timeseries, geoMap, relatedTopics, relatedQueries). Returns interest-over-time series, geo-level breakdowns, and rising/top related topics/queries with relative scores. Use for keyword/content strategy, demand forecasting, seasonality analysis, topic discovery, campaign timing, and adding live-trend signals to marketing or research agents.
```

</details>

| Parameter | Type | Required | Schema default | Description | Constraints |
|---|---|---|---|---|---|
| `q` | string | Yes | — | Specify the search term for which you want to retrieve trends data. | — |
| `geo` | string | No | — | Specifies the location for the search. Defaults to Worldwide if not set or empty. Provide one exact documented value (3517 allowed), e.g. `AF`, `AF-BDS`. | — |
| `region` | string | No | — | Used to get more specific results when using "Interest by region" data type. Other data types do not accept this parameter. The default value depends on the geo location that is set.<br><br>Available options:<br> - `country`: Country<br> - `region`: Subregion<br> - `dma`: Metro<br> - `city`: City<br><br>Note: Not all region options will return results for every geo location.<br> | enum: ["country", "region", "dma", "city"] |
| `dataType` | string | No | — | Defines the type of search to perform.<br><br>Available options:<br>  - `timeseries`: Interest over time (default). Accepts both single and multiple queries per search.<br>  - `geoMap`: Interest by region. Accepts both single and multiple queries per search.<br>  - `relatedTopics`: Related topics. Accepts only single query per search.<br>  - `relatedQueries`: Related queries. Accepts only single query per search.<br> | enum: ["timeseries", "geoMap", "relatedTopics", "relatedQueries"] |
| `tz` | number | No | — | Defines a time zone offset in minutes. The default value is 420 (Pacific Daylight Time (PDT): UTC-7). The valid range for this parameter is from -1439 to 1439.<br><br>To calculate the `tz` value for a specific time zone, you can use the time difference between UTC +0 and the desired time zone.<br><br>Examples:<br>- `420`: Pacific Daylight Time (PDT)<br>- `60`: Central European Time (CET)<br>- `-540`: Japan Standard Time<br> | — |
| `cat` | string | No | — | Category of the search term. The default value is 0 ("All categories"). Provide one exact documented value (1133 allowed), e.g. `0`, `3`. | — |
| `gprop` | string | No | — | Sorts results by a specific property. The default property is Web Search (applied when the gprop parameter is not set or empty).<br><br>Available options:<br>  - `images`: Image Search<br>  - `news`: News Search<br>  - `froogle`: Google Shopping<br>  - `youtube`: YouTube Search<br> | enum: ["images", "news", "froogle", "youtube"] |
| `date` | string | No | — | Defines a date range for the search. Available options:<br><br>- `now 1-H`: Past hour<br>- `now 4-H`: Past 4 hours<br>- `now 1-d`: Past day<br>- `now 7-d`: Past 7 days<br>- `today 1-m`: Past 30 days<br>- `today 3-m`: Past 90 days<br>- `today 12-m`: Past 12 months<br>- `today 5-y`: Past 5 years<br>- `all`: 2004 - present<br><br>You can also specify a custom date range using one of the following formats:<br><br>- `yyyy-mm-dd yyyy-mm-dd` - (e.g. 2021-10-15 2022-05-25) for dates from 2004 to present.<br>- `yyyy-mm-ddThh yyyy-mm-ddThh` - (e.g. 2022-05-19T10 2022-05-24T22) for dates with hours within a week range. The hours will be calculated based on the tz (time zone) parameter.<br> | — |

<details>
<summary>Complete input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "q": {
      "type": "string",
      "description": "Specify the search term for which you want to retrieve trends data."
    },
    "geo": {
      "type": "string",
      "description": "Specifies the location for the search. Defaults to Worldwide if not set or empty. Provide one exact documented value (3517 allowed), e.g. `AF`, `AF-BDS`."
    },
    "region": {
      "type": "string",
      "enum": [
        "country",
        "region",
        "dma",
        "city"
      ],
      "description": "Used to get more specific results when using \"Interest by region\" data type. Other data types do not accept this parameter. The default value depends on the geo location that is set.\n\nAvailable options:\n - `country`: Country\n - `region`: Subregion\n - `dma`: Metro\n - `city`: City\n\nNote: Not all region options will return results for every geo location.\n"
    },
    "dataType": {
      "type": "string",
      "enum": [
        "timeseries",
        "geoMap",
        "relatedTopics",
        "relatedQueries"
      ],
      "description": "Defines the type of search to perform.\n\nAvailable options:\n  - `timeseries`: Interest over time (default). Accepts both single and multiple queries per search.\n  - `geoMap`: Interest by region. Accepts both single and multiple queries per search.\n  - `relatedTopics`: Related topics. Accepts only single query per search.\n  - `relatedQueries`: Related queries. Accepts only single query per search.\n"
    },
    "tz": {
      "type": "number",
      "description": "Defines a time zone offset in minutes. The default value is 420 (Pacific Daylight Time (PDT): UTC-7). The valid range for this parameter is from -1439 to 1439.\n\nTo calculate the `tz` value for a specific time zone, you can use the time difference between UTC +0 and the desired time zone.\n\nExamples:\n- `420`: Pacific Daylight Time (PDT)\n- `60`: Central European Time (CET)\n- `-540`: Japan Standard Time\n"
    },
    "cat": {
      "type": "string",
      "description": "Category of the search term. The default value is 0 (\"All categories\"). Provide one exact documented value (1133 allowed), e.g. `0`, `3`."
    },
    "gprop": {
      "type": "string",
      "enum": [
        "images",
        "news",
        "froogle",
        "youtube"
      ],
      "description": "Sorts results by a specific property. The default property is Web Search (applied when the gprop parameter is not set or empty).\n\nAvailable options:\n  - `images`: Image Search\n  - `news`: News Search\n  - `froogle`: Google Shopping\n  - `youtube`: YouTube Search\n"
    },
    "date": {
      "type": "string",
      "description": "Defines a date range for the search. Available options:\n\n- `now 1-H`: Past hour\n- `now 4-H`: Past 4 hours\n- `now 1-d`: Past day\n- `now 7-d`: Past 7 days\n- `today 1-m`: Past 30 days\n- `today 3-m`: Past 90 days\n- `today 12-m`: Past 12 months\n- `today 5-y`: Past 5 years\n- `all`: 2004 - present\n\nYou can also specify a custom date range using one of the following formats:\n\n- `yyyy-mm-dd yyyy-mm-dd` - (e.g. 2021-10-15 2022-05-25) for dates from 2004 to present.\n- `yyyy-mm-ddThh yyyy-mm-ddThh` - (e.g. 2022-05-19T10 2022-05-24T22) for dates with hours within a week range. The hours will be calculated based on the tz (time zone) parameter.\n"
    }
  },
  "required": [
    "q"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

Implementation notes:

- Only q is required. No JSON Schema defaults, minimum/maximum bounds, or nullable alternatives are declared. additionalProperties is false, and the schema declares JSON Schema draft-07.
- tz description states a valid range of -1439 to 1439 and default 420, but neither is encoded as a schema constraint/default.
- geo and cat are strings, with documented allowed-value counts in descriptions, not schema enums. README reports backend rejection of unknown identifiers; this was not tested.
- Descriptions specify timeseries default, region applicability/default, Google property default and single-versus-multiple-query compatibility; these are descriptive behavior, not additional JSON Schema constraints.
- README reports at most five comma-separated queries for timeseries/geoMap; this limit is not encoded in the input schema and was not tested.

Sources: [index.mjs:1](https://github.com/HasData/google-trends-mcp/blob/f6fd4c341ffc3eeb09e93de4a281e7084d691f35/index.mjs) · [test/tools.test.mjs:17](https://github.com/HasData/google-trends-mcp/blob/f6fd4c341ffc3eeb09e93de4a281e7084d691f35/test/tools.test.mjs) · [README.md:174](https://github.com/HasData/google-trends-mcp/blob/f6fd4c341ffc3eeb09e93de4a281e7084d691f35/README.md) · [Hosted tools/list](https://mcp.hasdata.com/mcp?apis=google_trends)

## Schema provenance

Anonymous JSON-RPC tools/list POST to the exact hosted endpoint configured in both launchers; full response saved verbatim and parsed. Public default-branch repository source inspected to verify launcher scope and contract expectations. No tools/call requests, credentials, installation, or launcher execution.

- Schema and registration verified live on 2026-10-13 at 15:27:34 UTC; hosted registration may change independently of the pinned repository commit.
- Remote tool implementation is absent from repository, so actual scraping behavior and backend validation are provider-documented rather than source-verified.
- Extraction covers configured apis=google_trends endpoint only; unfiltered and other filtered variants are distinct configurations and are not merged.
- README missing-key authorization claim contradicts successful anonymous tools/list observation; no credential was supplied.
- Provider product page uses /api/mcp and simplified five-parameter documentation; current pinned launchers use /mcp and live tool schema has eight parameters.
