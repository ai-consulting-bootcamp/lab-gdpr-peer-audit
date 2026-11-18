# GDPR Peer Audit – Career Intelligence Agent
**Auditor:** Murat Çömez · **Builder:** Max · **Date:** 17 Nov 2026
**Input:** [builder's data processing brief](teammate_gdpr_data_brief_career_intelligence_agent.pdf) only (no code). **Scope:** production version with real users. The MVP uses synthetic profiles.

> **Headline:** the builder described the tool as using no personal data. His own brief shows it does in production: candidate profiles, employment history and matching scores about identifiable people. The synthetic MVP is out of scope; a production launch is fully in scope of the GDPR.

## Phase 1 – Personal data inventory

| # | Data category | Data subjects | Source | Purpose | Where it goes | Special / sensitive? | Retention (per brief) |
|---|---|---|---|---|---|---|---|
| 1 | Name or display name | Job seekers | User input (Streamlit) | Identify profile / report | Session, reports | No | None defined |
| 2 | Professional profile: experience, employment history, education, qualifications, skills, career level | Job seekers | User input | Matching | Session, reports, **OpenAI** (if AI analysis on) | No, but education dates and career level are **age proxies** | None defined |
| 3 | Preferences: occupations, location, working arrangements | Job seekers | User input | Job discovery | Session, job API queries (location / occupation terms) | No | None defined |
| 4 | Free-text profile fields | Job seekers | User input | Matching | Session, **OpenAI** | **Possible Art. 9** (health, disability, religion, origin typed in by users) | None defined |
| 5 | Inferred data: matching scores, gaps, recommended / review lists | Job seekers | Generated | Recommendation | Session, reports, OpenAI context | No, but **profiling** (Art. 4(4)) | None defined |
| 6 | Downloaded reports (PDF / MD / JSON) | Job seekers | Generated | User's own use | User's device; local files if saved server-side (verify) | As above | None defined |
| 7 | Research queries | Job seekers (indirectly) | Generated | Company research, skill mapping | **Tavily**, ESCO | Normally no; **verify** no profile data in queries (brief says unverified) | Vendor defaults |
| 8 | Technical data: session, IP, logs; user accounts if added | Job seekers | Hosting / Streamlit | Operation | Hosting provider | No | None defined |

Job ads (Arbeitnow, Himalayas), ESCO classifications and labour-market publications (Pinecone) are **not personal data about the users**. Job ads can contain recruiter names; this is low risk.

## Phase 2 – Role map

| Role | Entity | Key GDPR obligations |
|---|---|---|
| **Controller** | The operator of the app: the builder now, the "future commercial provider" in production | Lawful basis, privacy notice (Art. 13), records (Art. 30), DPIA, security, DPAs, transfers, handling rights requests |
| **Data subject** | Job seekers | Their personal use of the report is household activity, but the **operator** is still the controller of what the app processes |
| **Processor** | OpenAI (API) | DPA, transfer safeguards, retention settings |
| **Processor (verify)** | Tavily, if any profile data is in queries | DPA or a design change to send only company names |
| **Processor** | Hosting (e.g. Streamlit Community Cloud or a cloud provider) in production | DPA, EU region |
| **Not a processor (as described)** | Pinecone (only public knowledge base), Arbeitnow, Himalayas, ESCO (data sources) | Verify no user data is written to Pinecone or sent in job API calls beyond generic search terms |

## Phase 3 – Lawful basis (Art. 6)
**Chosen basis: Art. 6(1)(b), performance of a contract.** The user signs up for a career guidance service. Processing their profile to find and match jobs is objectively necessary to deliver that service.
- The **optional OpenAI analysis** is part of the requested service when the user switches it on. Explain clearly that profile data then goes to OpenAI (US).
- **Art. 6(1)(f) legitimate interest** only for secondary uses (security logs, service improvement). An LIA is needed if these are added. **Using profiles to train or tune models** would need consent or a separate LIA.
- **Art. 9 data in free text:** no condition is planned. Prevent it with field guidance ("do not enter health, religion…"), a detection filter, or explicit consent (Art. 9(2)(a)) if sensitive data is genuinely useful (e.g. disability-related workplace needs).

## Phase 4 – Risks and rights
- **Special category data:** not requested, but realistic in free text (as the builder notes). Medium risk; mitigate as above.
- **Profiling:** yes. Scores evaluate work-related aspects of a person (Art. 4(4)). **Art. 22 is not triggered:** the output is advisory, the user decides, and there is no employer-side decision. This changes if scores are ever shared with employers.
- **DPIA: likely required at production scale.** EDPB criteria met: evaluation / scoring, new technology (LLM), possibly sensitive data, possibly large scale. Recommend a DPIA before launch.
- **Discrimination risk:** age, gender or origin proxies in the profile can bias the score. This is a fairness issue under Art. 5(1)(a) GDPR, plus AGG.
- **Transfers:** OpenAI (US) and possibly Tavily (US). The brief says locations and safeguards are unverified, so transfers cannot be ruled out. Need DPF certification or SCCs plus a transfer impact assessment.

| Right | Current support (per brief) | Gap |
|---|---|---|
| Information (Art. 13) | None mentioned | Privacy notice, incl. profiling logic in plain language |
| Access (Art. 15) | User sees profile and report | Covers live session only; need a process if data is stored |
| Rectification (Art. 16) | **Good:** user reviews and corrects the profile before the run | None |
| Erasure (Art. 17) | **No retention or deletion policy** | Define session-only storage or auto-delete; deletion at the vendors |
| Portability (Art. 20) | **Good:** JSON export | Confirm the profile itself is exportable, not only the report |
| Objection (Art. 21) | Not relevant under 6(1)(b) | Needed if 6(1)(f) uses are added |

## Phase 5 – Law tracking

| Law | Applies? | Why |
|---|---|---|
| **EU AI Act** | Yes | Limited risk (Art. 50(2) marking of AI text); **Annex III 4(a) high-risk** if ever used by or for employers (see yesterday's peer audit) |
| **ePrivacy / TDDDG** | **Yes, once hosted** | Cookies or local storage in a web app need consent, unless strictly necessary (§25 TDDDG) |
| **Consumer protection (UCPD, consumer contract rules)** | Yes | B2C service; claims about score accuracy must not mislead |
| **AGG (anti-discrimination)** | Partly | Indirect. Mainly relevant if employers use the scores, but biased guidance is a reputational and fairness risk |
| **Data Act** | No | No connected products |
| **API terms / copyright** | Yes | Arbeitnow, Himalayas, Tavily terms; licensing of labour-market publications |

## Findings and recommendation
| # | Finding | Severity |
|---|---|---|
| 1 | Personal data **is** processed in production, contrary to "no personal data"; the GDPR applies in full | Significant |
| 2 | No retention or deletion policy | Significant |
| 3 | Transfers to OpenAI / Tavily (US) unverified; no DPAs | Significant |
| 4 | Profiling plus possible sensitive free text, so a DPIA is likely required | Significant |
| 5 | No privacy notice; profiling logic not explained | Significant |
| 6 | Tavily and job API queries not verified for personal data | Minor (verify) |

**Recommendation: proceed with conditions.** Fine as a synthetic-data MVP. Before real users: privacy notice, DPAs and transfer check, retention policy, DPIA, free-text safeguards, cookie consent if hosted.

## Clarifying questions log (written, 17 Nov 2026)
| # | Question | Provisional assumption |
|---|---|---|
| Q1 | Are profiles stored after the session (server, database, logs)? | Session-only, but reports may be saved locally |
| Q2 | What exactly is sent to OpenAI and Tavily (full profile, or only skills and company names)? | Full profile to OpenAI; company names to Tavily |
| Q3 | Will there be user accounts, analytics or cookies when hosted? | Yes, if commercialised |
| Q4 | Will profiles be used to improve or train the system? | No |

**Answers received (18 Nov 2026, builder's written replies):**
- **Q1 Storage:** profiles are processed during the session, but **generated reports with candidate details and assessments are written to the local filesystem** and stay until deleted manually. No retention policy. → Confirms Finding 2.
- **Q2 Vendors:** OpenAI receives candidate context, recommendations and evidence **only when AI synthesis is switched on (off by default)**, never for the score. Pinecone stores only the knowledge base, but **retrieval queries contain the candidate's job titles, skills and gaps**. Tavily gets company queries; ESCO gets skill terms; the job APIs get role and search parameters. → Finding 6 narrowed: Tavily and job APIs are low risk. Pinecone queries are low-sensitivity personal data and need a DPA check.
- **Q3 Accounts / cookies:** not answered. Assumption kept (likely once hosted).
- **Q4 Training use:** not answered. Assumption kept (no).
- **Extra:** structured form only, no CV upload, no fields for photo, date of birth or nationality (good minimisation); free text can still contain sensitive data. Transfers and processing regions are confirmed as **open items**. The UI states the system is AI-assisted and explains the score's limits.

**Effect on the audit:** findings 1–5 unchanged; finding 6 narrowed. Recommendation unchanged: **proceed with conditions.**
