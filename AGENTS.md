# AGENTS.md

Working rules and language guidelines for anyone — human or agent — editing this repository. It is a curated, plain-English index of the Google Trends Model Context Protocol (MCP) and agent tooling ecosystem. Keep it lean, minimalist, and immediately useful.

---

## 1. Project Philosophy & Minimalist Structure

- **No Onboarding Tutorials:** Do not add introductory installation essays, "how to choose your layer" tables, or getting-started walkthroughs to the catalog root. Keep the README strictly minimalist: title, official links, Table of Contents with counts, direct jump links into the tables, and the developer decision matrix.
- **Fast Jump Navigation:** Readers should jump straight to the relevant problem domain from the Table of Contents in 1 click.

---

## 2. Project Language & Voice Values

The language of this catalog must be simple, direct, and developer-friendly:

### 2.1. Plain-English, Verb-First Prose

- Lead with active verbs (*Adds*, *Scrapes*, *Caches*, *Rotates*, *Normalizes*, *Exposes*, *Orchestrates*, *Monitors*).
- Avoid passive constructions, convoluted em-dash chains, and marketing buzzwords (*"ultimate"*, *"blazing fast"*, *"revolutionary"*).
- State clearly what an agent or developer can *do* with the tool, not a laundry list of generic features.

### 2.2. The 1–2 Sentence Rule

Every project entry must be strictly 1 or 2 concise sentences (never exceeding 3 sentences):

- **Sentence 1:** What the tool specifically does for a developer or agent.
- **Sentence 2:** How it differs from its closest alternatives (e.g. proxy handling, SQLite caching, single consolidated enum vs multi-tool sprawl, or public RSS bypass).

### 2.3. Subcategory Header & Table Standards

Every subcategory begins with a count and a 1-sentence summary, followed by a clean 2-column markdown table:

```markdown
### Rotating residential proxy pools and failover tracking

*3 projects. Multi-proxy pool ingestion, randomized per-request rotation, and active failover tracking.*

| Project | What it does |
|---|---|
| [**owner/repo**](https://github.com/owner/repo) | Plain-English explanation of what the tool does and who it is for. |
```

---

## 3. Strict Exclusion Criteria (What NEVER Belongs Here)

To maintain a high-signal catalog, the following must **never** be added:

1. **NO Generic SEO or Keyword Tools:** Only tools explicitly interfacing with Google Trends data endpoints qualify.
2. **NO Empty Scaffolds or Incomplete Stubs:** Repositories without working command implementations, design-only documents, or broken builds.
3. **NO Trivial Copy-Paste Wrappers:** Near-duplicate forks or minimal shims without substantive standalone utility.
4. **NO Marketing Hype or AI Filler:** Descriptions must remain factual, concise, and neutral.

---

## 4. Before Committing

1. Run `npx markdownlint-cli2 "**/*.md"` — it must exit clean with **0 issues** (same check CI runs).
2. Ensure every internal anchor link resolves correctly.
3. Commit with the conventional commit format: `docs(awesome-list): <summary>`.
