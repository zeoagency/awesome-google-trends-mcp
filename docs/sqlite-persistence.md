# Embedded SQLite Persistence & Ingestion Architecture

> **Engineering Guide to Shielding Upstream Google Endpoints, Enabling Sub-20ms Reads, and Preserving Ephemeral Daily Trends.**

---

## 1. Why SQLite WAL Mode is Mandatory

Issuing live Google Trends queries on every agent tool call introduces 1.5s–5.0s of latency and rapidly exhausts IP rate limits. Embedding a local SQLite database running in Write-Ahead Logging (WAL) mode enables:

- **Sub-15ms Read Latency:** Cached keyword timeseries return instantly.
- **80%+ Rate-Limit Reduction:** Shielding upstream endpoints from repetitive agent tool calls.
- **Historical Snapshot Preservation:** Capturing Google's ephemeral 24–48 hour daily trending searches before they are permanently purged.

---

## 2. Recommended Schema

```sql
CREATE TABLE IF NOT EXISTS snapshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT NOT NULL,
    geo TEXT NOT NULL,
    timeframe TEXT NOT NULL,
    data_json TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_snapshots_query 
ON snapshots(keyword, geo, timeframe);
```
