# Phase 3 — Clarifying questions log · VC startup-screening agent

- **Questions sent:** 17 Nov 2026 (`Questions for Sandra – VC startup-screening agent`).
- **Answers received:** in Sandra's document *GDPR Questions and Answers for the VC Screening Agent*, which also contains her data processing brief.

The provisional assumptions were written before her answers arrived, and are kept as the audit trail.

| # | What I needed to know | Why it matters (GDPR obligation) | Provisional assumption (before answers) | Answer from Sandra (summary) | Effect on the audit |
|---|---|---|---|---|---|
| Q1 | Her GDPR data processing brief | Accountability, records of processing (Arts. 5(2), 30) | System as in the AI Act brief | **Received.** Tavily: name + domain. Jina: website URL. GDELT: name. OpenAI: name, links, Tavily excerpts. Local reports; **Kalipso and Lawra reports public on GitHub**. Locations, retention and transfer safeguards unverified | New finding F1 (public reports) |
| Q2 | What reaches OpenAI; plan, region, DPA | Arts. 28, 44–46, 5(1)(c) | Names may be included; US; no DPA | Only Tavily excerpts + URLs + startup name. Names cannot be confirmed (full responses unavailable). **Signed in with Gmail.** Plan, region and DPA unverified | Assumption confirmed; F2 adds the Gmail sign-in (no organisation account confirmed) |
| Q3 | Are founders assessed as people? | Art. 6(1)(f) balancing, DPIA criterion 1, Art. 22, Art. 10 | Company-level only | Checks cover company facts. Founder information is marked "Not verified"; a name can still appear in a title or quote | Assumption confirmed |
| Q4 | Storage, retention, access | Arts. 5(1)(e), 32, 15, 17 | Local, no retention rule, analysts only | Local reports folder; no archive of full API responses; **no deletion rule; the published reports are visible outside the analyst team** | Partly wrong: not "analysts only" → F1, F6 |
| Q5 | Lawful basis; Art. 14; rights | Arts. 6, 14, 21 | LI intended, no LIA, no notice, no process | LI considered, **initial assessment drafted**, marked `TBD — legal review`. No Art. 14 notice or exception; no process for access, erasure or objection | Assumption mostly confirmed (an LIA draft exists) → F3, F4 |

**Follow-up from Sandra (18 Nov 2026):** she sent links to the OpenAI Data Processing Addendum and Tavily's DPA documentation. She has **not confirmed that they cover the API accounts used** for Kalipso and Lawra, and asked to record the DPA status as **pending verification for both providers**. She also shared her repository (`Sobregonm/project3-vc-screening`) so the data flows can be checked.

**Code check (18 Nov, commit `84afd71`):**
- Tavily receives the startup name and domain in a search query (`tavily_search.py`).
- OpenAI receives only `target_company` plus Tavily snippets keyed by URL, each capped at 3,000 characters (`headquarters_extractor.py`).
- Jina's page text and the GDELT results are **not** passed to OpenAI (`main.py`).
- GDELT receives the startup name in a news query (`gdelt_news.py`).
- `.env` is git-ignored.
- A scan of the two public reports found no person names; the founder section reads "Not verified".

**Detail seen in Sandra's message (18 Nov, link preview of Tavily's Help Center):** "Tavily offers a Data Processing Agreement (DPA) to Enterprise customers and to self-serve customers subject to GDPR; contact sales@tavily.com". So a Tavily DPA is available on request. Whether Sandra's account has one stays **pending verification**.
