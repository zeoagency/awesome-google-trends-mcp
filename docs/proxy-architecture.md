# Google Trends Proxy Resilience Architecture

> **Engineering Guide to Bypassing Google Trends HTTP 429 Rate Limits, CAPTCHA Challenges, and Bot Detection Traps in Autonomous Agent Workflows.**

---

## 1. The Datacenter IP Quota Ceiling

Direct unauthenticated HTTP requests to Google Trends from cloud datacenter providers (AWS, GCP, DigitalOcean, Hetzner) trigger HTTP 429 rate limits or HTML challenge blocks after approximately **~130 requests per 24 hours per IP**.

Public proxy lists have an empirically verified **0% survival rate** against Google Trends defenses.

---

## 2. Core Architectural Requirements

1. **Rotating Residential Proxies:** Use commercial rotating residential proxy pools (e.g. Webshare, IPRoyal, Bright Data) with authenticated user/pass proxies.
2. **Proactive Health Validation:** Pre-flight candidate proxies against lightweight autocomplete endpoints (`/complete/search?client=chrome`) before sending explore requests.
3. **Dead Proxy Ejection:** Track proxy failures and eject dead proxies from the active pool after 3 consecutive failures.
4. **Pre-Parse HTML Challenge Guard:** Always inspect response status, `content-type`, and body text prefixes (`looksLikeHtml`) before calling `JSON.parse` to avoid fatal `SyntaxError: Unexpected token 'l'` crashes.
