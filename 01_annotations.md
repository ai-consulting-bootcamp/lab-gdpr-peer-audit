# Phase 1: Read and Annotate

**Audited system:** Interview Prep Report (Julia Antunes) · **Input:** [00_julia_brief.md](00_julia_brief.md) · **Auditor:** Ayhan Demir · **Lens:** GDPR only · **Date:** 17 Nov 2026

Read once without notes, then annotated on the second read. Markdown cannot circle or underline, so each annotation uses a tag:

| Tag | Meaning |
|---|---|
| `[PD]` | Personal data category |
| `[SC]` | Special category applies or could be inferred (Art. 9) |
| `[?]` | Unclear; needs confirming before forming a view (circle) |
| `[EU]` | Data flow leaves the EU or involves a non-EU vendor (underline) |
| `[PURPOSE]` | Purpose possibly incompatible with the original collection purpose |

## Annotations

| # | Brief section | Text (short quote) | Tags | Note |
|---|---|---|---|---|
| A1 | 1, Candidate CV | "names, contact details, work experience, projects, education and other personal details" | `[PD]` `[SC]` | Core personal data of the candidate. CVs in Germany often carry a photo, date of birth, nationality or marital status; some show religion (church employers), disability or union roles. Special category can be present even if not asked for |
| A2 | 1, Candidate CV | (silent on referees) | `[PD]` `[?]` | CVs often list referees with names and phone numbers: third-party data the candidate supplies without those people knowing |
| A3 | 1, GitHub profile | "Optional public profile URL or username supplied by the user" | `[PD]` `[?]` | Direct identifier. Nothing says the system checks the profile belongs to the person submitting |
| A4 | 1, GitHub repo data | "personal/portfolio information shared publicly" | `[PD]` | Public data, but READMEs can name collaborators. Public does not mean free to reuse for any purpose |
| A5 | 1, Job description | "information from a third party" | `[PD]` `[?]` | Postings can name a recruiter or hiring manager with contact details |
| A6 | 1, Company research | "recent news" | `[PD]` | News items can name executives or employees; low risk, third-party data |
| A7 | 1, Generated report | "fit summary, project highlights, skill gaps" | `[PD]` `[SC]` | Evaluates the candidate's skills: profiling (Art. 4(4)), even though it serves the candidate. Can repeat any special-category detail from the CV |
| A8 | 1, Validation results | "retain validation metadata, including error messages" | `[PD]` `[?]` | Where retained, for how long, and do error messages contain CV text? |
| A9 | 1, Validation-error records | "including the form error and related submission data" | `[PD]` `[EU]` `[PURPOSE]` `[?]` | "Related submission data" is undefined: could be the full CV. Keeping a rejected submission for debugging goes beyond what the user asked for |
| A10 | 1, Technical data | "IP addresses, request metadata and execution logs" | `[PD]` `[?]` | No retention stated |
| A11 | 2 | "public third-party sources ... public GitHub repositories" | `[PURPOSE]` | GitHub content was published as a portfolio. Using it to prepare the candidate is compatible if it is the candidate's own; not if someone enters another person's username |
| A12 | 3, purpose (5) | "Logging invalid submissions when the Notion branch is enabled" | `[PURPOSE]` | Only purpose not requested by the user; needs its own basis (legitimate interests) and minimisation |
| A13 | 3 | (no lawful basis named for any purpose) | `[?]` | Brief silent on Art. 6 basis and on a privacy notice |
| A14 | 4, n8n | "no EU region is specified" | `[EU]` `[?]` | n8n holds everything, including execution history with CV text. Cloud or self-hosted, and where? |
| A15 | 4, OpenAI | "CV text, GitHub data ... generated report draft" · US | `[EU]` | Largest flow of candidate data, to the US |
| A16 | 4, Tavily | "Search query created from the company and job details" · US | `[EU]` `[?]` | Probably no personal data, unless the job description carries a recruiter name |
| A17 | 4, GNews | Location "Not documented" | `[EU]` `[?]` | Company name only; probably no personal data |
| A18 | 4, GitHub REST API | Username sent · US | `[EU]` | GitHub is the source here and acts as its own controller |
| A19 | 4, Notion | "Invalid submission details" · US | `[EU]` | See A9 |
| A20 | 4, Browser / hosting | "Deployment-dependent" | `[EU]` `[?]` | Hosting provider and region unknown |
| A21 | 4 | "does not document formal data-processing agreements or retention settings" | `[?]` | No DPAs, no retention: confirms the gap |
| A22 | 4 | "form and execution logs may still retain operational records" | `[?]` | Reports are not stored on purpose, but copies may persist in logs |
| A23 | 5 | "does not automatically approve, reject or rank the person" | | No decision with legal or similar effect: Art. 22 not triggered |

## Summary of tags

- **Personal data:** 11 categories; the CV (A1) and the generated report (A7) carry the most.
- **Special category:** possible in CVs and repeated in reports (A1, A7); nothing in the brief filters it.
- **Non-EU flows:** OpenAI, Tavily, GitHub and Notion in the US; n8n, GNews and hosting not documented.
- **Purpose concerns:** Notion logging of rejected submissions (A9, A12) and use of GitHub profiles that may not be the user's own (A11).
- **Open questions:** feed the Phase 3 log ([03_clarifying_questions.md](03_clarifying_questions.md)).
