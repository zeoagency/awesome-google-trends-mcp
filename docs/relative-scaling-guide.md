# The Google Trends Relative Scaling Law

> **Crucial Guidance for LLMs and Autonomous Agents: Understanding the 0–100 Relative Popularity Index.**

---

## 1. The Common Hallucination

Autonomous agents frequently hallucinate that a Google Trends score of `100` means "100 searches" or "100,000 searches". **This is completely false.**

---

## 2. How Google Trends Normalizes Data

1. **Normalization to Peak:** Google calculates search interest for each query across the requested timeframe and geography, dividing each point by the highest peak in that specific query.
2. **0–100 Scale:** The peak point is assigned `100`, and all other points are scaled from `0` to `100` proportionally.
3. **Query Comparison Relativity:** When comparing up to 5 keywords in a single request, Google normalizes all 5 keywords against the single highest peak across all 5 terms.
