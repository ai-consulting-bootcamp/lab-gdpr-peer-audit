# Phase 2 — Personal data summary and role map · VC startup-screening agent

Based **only** on the teammate's AI Act System Brief. Her GDPR data processing brief has not been received. Where the brief is silent, the gap is noted.
**Tags:** [D] declared · [A] assumption · [NC] not covered · [V] verified by me in an official source.

## Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Founders' and team members' names, roles | Tavily search extracts; company website via Jina; news via GDELT [D] | Screen the startup for a first meeting; LLM extraction of HQ and funding stage [D] | **Likely**: Tavily (US company) and OpenAI (US; EU residency optional) [A]. Not documented [NC] | No by design. **Art. 10** (criminal allegations) possible in news [A] |
| Founders' bios, photos, LinkedIn links on team pages | Website via Jina [A] | Same (incidental) | Jina's processing location not checked [NC] | Photos are not biometric data unless processed to identify people [A] |
| People named in news articles | GDELT [D] | Recent-news check | GDELT is a public, US-run project [A]; only the query is sent | Possible (health, political or criminal context) [A] |
| Short extracts possibly containing names | Tavily → **OpenAI** [D] | Find evidence of HQ and funding stage | **Likely** [A] | Unlikely |
| Report contents (findings, quotes, links) that may name people | System output [D] | Internal report for the analyst | Storage location **not stated** [NC] | Inherits the above |
| Analyst's identity and usage (user) | Fund staff [A] | Operating the tool | Unknown [NC] | No |
| Real test data: Kalipso, Lawra | Same tools [D] | Prototype testing | As above | As above |

**Purpose-limitation flag:** no incompatible reuse is visible in the brief. To watch: reusing reports for other purposes (e.g. a founder database or marketing) would be a new purpose.

## Role map (provisional — no contracts seen)

| Entity | Role (GDPR) | Processing activity | DPA needed? |
|---|---|---|---|
| **Client:** VC fund (Puente Ventures, fictional) [D] | **Controller** [A]: it decides to screen startups and why | Screening, reporting, meeting decision | n/a |
| **Builder:** teammate | Prototype tests: **controller** of her own test runs [A]. Pilot: **processor** if she runs the agent for the fund; **software vendor** (no GDPR role) if the fund runs it alone [A] | Development, tests (Kalipso, Lawra) | **Yes, if she processes data for the fund** (Art. 28) |
| **OpenAI** (API) | **Processor** to whoever holds the API account, when used under OpenAI's business terms and DPA [A] | Extracting HQ/funding evidence from extracts | **Yes.** OpenAI offers a DPA [V: openai.com/business-data]; signature not evidenced [NC] |
| **Tavily** | **TBD.** Processor for query handling, or independent controller. Tavily states it is controller of its own search index [V: Tavily docs] | Web search | **Likely yes** if processor; to be confirmed [NC] |
| **Jina Reader** | **TBD.** Likely processor (fetches and converts pages on request) [A] | Reading the startup website | **Likely yes** [NC] |
| **GDELT** | **Independent source**, not a processor. Only a query is sent [A] | News lookup | No (check its terms of use) |
| Hosting / storage of reports | Unknown [NC] | Storing reports | If third-party: yes |

**International transfers:** OpenAI and Tavily are US companies [V]. A provider's nationality alone does not prove a transfer. If personal data is processed in the US:
- the fund needs an adequacy route, i.e. the EU–US Data Privacy Framework, valid but under appeal C‑703/25 P, and only for **certified** recipients (certification not checked); or
- SCCs (often built into vendor DPAs) plus a transfer impact assessment.

OpenAI offers **European data residency** for eligible new API projects [V], which could avoid the question. **The brief gives no evidence of any mechanism.**

**Not to confuse:** in her AI Act analysis, the teammate is *provider* and the fund is *deployer*. Those labels do not decide the GDPR roles above.

## Update after her GDPR brief (18 Nov 2026)

- **New recipient: GitHub.** The two test reports are public, so they are visible outside the analyst team. The builder is the controller of that publication.
- **OpenAI** is accessed with a **Gmail sign-in**. Plan, region and DPA are unverified. An organisation API account with OpenAI's DPA is needed before any pilot.
- **Jina:** its text is not sent to OpenAI (declared). Its own processing location is still not checked.
- **GDELT** receives the startup name only.
- **Retention:** no deletion rule, and no archive of the full API responses.
