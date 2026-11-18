# Phase 1 — Annotated brief, GDPR lens (Elif Yurdakul, Unioptt programme fact-checker)

**Source:** Elif's Phase 1 system brief (received 17 November 2026). Her GDPR data processing brief has been requested; see the limitation in [lab_proof.md](lab_proof.md).

**Legend** (Markdown can't underline or circle):
- **[PD]** personal data category, with special-category status noted ("mark")
- **[?]** unclear, needs confirming ("circle")
- **[X]** data flow crossing an EU border or involving a non-EU vendor ("underline")
- **[P]** purpose that may be incompatible with the original collection purpose ("flag")

| # | Brief says | Tag | Annotation |
|---|---|---|---|
| 1 | "writes a report for a Turkish student and their family" | [?] | Where are the students, and where is Unioptt established? This decides whether GDPR applies (Art. 3) or Turkish KVKK, or both. |
| 2 | "student profile: grades, language test scores" | [PD] | Academic records. Not Art. 9, but sensitive in practice, and about minors. |
| 3 | "budget" | [PD] | Family financial data. Not Art. 9; often treated as highly personal (EDPB DPIA criterion 4). |
| 4 | "citizenship" | [PD] | Nationality. Not Art. 9 itself, but combined with name it can hint at ethnic origin. Needed for fee status and visa rules, so justified. |
| 5 | "often a minor's" | [PD] [?] | **Vulnerable data subjects.** Age range, who enters the data, parental involvement? Art. 8 and Art. 12 (child-friendly information) and the lawful basis depend on it. |
| 6 | "In the MVP this profile is synthetic" | [?] | Good: no real personal data yet, so GDPR obligations bite **before go-live**, not now. |
| 7 | "compares the requirements with the student's profile" → "met / gap / check" | [PD] [?] | The output is **new personal data** (an evaluation of the student), i.e. profiling. Is the comparison done in code, or does the profile go to OpenAI? |
| 8 | "scholarships" | [PD] [?] | Scholarship eligibility often depends on need, disability or refugee status. If the profile is extended for this, **special-category data (health)** may enter. |
| 9 | "OpenAI (a general-purpose language model for reading pages)" | [X] [?] | US vendor. Does it receive only web pages, or also the profile? |
| 10 | "Tavily (web search), Jina (page reading)" | [X] [?] | Tavily: US. Jina: location to verify. Likely receive only programme queries, no personal data. |
| 11 | "Pinecone (document library)" | [X] | US. Holds the 15 reference documents; no personal data unless profiles or reports are embedded. |
| 12 | "Frankfurter (exchange rates)" | — | Currency codes only; no personal data. |
| 13 | "n8n, Telegram and Airtable for delivery and logging" | [X] [PD] [?] | **Main transfer risk.** Telegram (non-EU, consumer messenger) carries the report, incl. the student's gaps, to minors. Airtable (US) stores logs, which likely contain profile and report. n8n hosting unknown. |
| 14 | "logging" | [P] [?] | Logged for what? Debugging is fine; reuse for analytics, product improvement or marketing would be a new purpose. |
| 15 | "Unioptt (my own platform) would offer it to students and families" | [P] [?] | What else does the platform do? If it earns referral fees from universities, using profiles for lead generation would be **incompatible** with "check facts for me". |
| 16 | "school counsellors and private high schools could use it" | [P] [?] | Role shift: the school becomes controller of its students' data, Unioptt its processor. Reusing school-provided data for Unioptt's own platform would be incompatible. |
