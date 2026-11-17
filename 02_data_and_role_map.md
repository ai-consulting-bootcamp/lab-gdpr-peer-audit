# Phase 2: Personal Data and Role Map

**Audited system:** Interview Prep Report (Julia Antunes) · **Input:** [00_julia_brief.md](00_julia_brief.md) · **Evidence:** [01_annotations.md](01_annotations.md) · **Date:** 17 Nov 2026

Based only on the brief. Purpose numbers (1) to (7) follow section 3 of the brief. "Gap" means the brief is silent.

## Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| CV (text extracted from PDF) | Candidate | (1), (2), (3), (4) | Yes: OpenAI (US); n8n location gap | Possible: photo, date of birth, nationality, health, religion or union roles if the candidate includes them (A1) |
| Referees and other people named in the CV | Candidate (third-party data) | Carried through (1) to (4) | Yes: OpenAI | Unlikely |
| GitHub username / profile URL | Candidate | (2) | Yes: GitHub, OpenAI (US) | No |
| Public GitHub repository data and READMEs | GitHub API | (1), (2), (3) | Yes: GitHub, OpenAI (US) | Unlikely, could be inferred from personal projects |
| Job description (may name a recruiter) | Candidate | (1), (2) | Yes: OpenAI; Tavily via query (US) | No |
| Company research (news may name people) | Tavily, GNews | (1) | Yes: Tavily (US); GNews location gap | No |
| Generated report (fit summary, skill gaps) | OpenAI | (1), (3), (4) | Yes: generated in the US | Possible: repeats CV content (A7) |
| Validation results and error messages | n8n, OpenAI | (3), (6) | Yes: OpenAI; storage location gap | Possible if errors quote CV text |
| Validation-error records ("related submission data") | n8n | (5), (6) | Yes: Notion (US), when enabled | Gap: content undefined (A9) |
| Technical data (IP, request metadata, execution logs) | System | (6), (7) | Gap: depends on deployment | No |

**Gaps:** no lawful basis per purpose, no retention period for any category, no definition of "related submission data", no n8n or hosting region.

## Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Client | **Gap: not named in the brief.** If an organisation offers the tool (for example a career service), it is the controller | Decides purposes and means | Must sign DPAs with all processors |
| Builder (Julia) | **Controller** if she runs the tool for the public herself (assumed, see Q1); **processor** if she runs it for a client | Builds and operates the workflow | Yes, with the client, if she is processor |
| n8n (Cloud or self-hosted) | Processor (n8n Cloud or the hosting provider) | Runs every step; keeps execution history with CV text | Yes. None documented |
| OpenAI | Processor | Generates and validates the report from CV, GitHub and job data | Yes. None documented |
| Tavily | Processor | Web search from company and job details | Yes, if queries can carry personal data. None documented |
| GNews | Likely independent controller of its news service | News search by company name | Probably not: no personal data expected |
| GitHub REST API | Independent controller of its platform (data source) | Returns public repo data for a username | No; the operator still needs a basis to use what it retrieves |
| Notion (optional) | Processor | Stores invalid submissions | Yes, if enabled. None documented |
| Browser / hosting | Processor | Receives form data and uploads; request logs | Yes. Provider not named |

## International transfers

| Flow | Destination | Mechanism needed | Evidence in brief |
|---|---|---|---|
| OpenAI | US | EU-US Data Privacy Framework if certified, otherwise SCCs with a transfer impact assessment | None |
| Tavily | US | Same | None |
| Notion | US | Same | None |
| GitHub | US | GitHub's own terms (it acts as controller); low risk, username only | None |
| n8n, hosting | Not documented | Unknown until the region is known; none needed if EU-hosted | None |
| GNews | Not documented | Probably none (no personal data) | None |

The brief states that DPAs and retention settings are not documented and that all integrations are free or trial plans, so no transfer mechanism can be assumed to be in place.
