# Phase 3: Clarifying Questions Log

**Audited system:** Interview Prep Report (Julia Antunes) · **Input:** [00_julia_brief.md](00_julia_brief.md) · **Evidence:** [01_annotations.md](01_annotations.md), [02_data_and_role_map.md](02_data_and_role_map.md) · **Date:** 17 Nov 2026

| # | What I need to know | Why it matters (GDPR obligation) | Provisional assumption |
|---|---|---|---|
| Q1 | Who runs the tool and for whom: Julia for the public, or an organisation (bootcamp, career service) as its client? | Decides who is controller and who signs DPAs (Art. 4(7), 24, 28) | Julia runs it for the public, so she is the controller |
| Q2 | Which lawful basis does each purpose rely on, and does the form show a privacy notice before upload? | Art. 6(1) basis for each purpose; Art. 13 information at collection, including that an AI processes the CV | Purposes (1) to (4) and (7) rely on the user's request (contract, Art. 6(1)(b)); (5) and (6) on legitimate interests; no privacy notice exists |
| Q3 | Does the system check that the CV and GitHub profile belong to the person submitting, and is anything removed from the CV (photo, date of birth, contact details, referees) before it goes to OpenAI? | Data minimisation (Art. 5(1)(c)), special category (Art. 9), information to people whose data is obtained indirectly (Art. 14) | No ownership check; the full CV text goes to OpenAI |
| Q4 | Where is n8n deployed, how long is execution history kept, and what exactly is "related submission data" in the Notion log? | Storage limitation (Art. 5(1)(e)), transfers (Art. 44), security (Art. 32) | n8n keeps full executions, including CV text, by default; Notion stores the full rejected submission; location unknown |
| Q5 | Which accounts and plans are used for OpenAI, Tavily, Notion and n8n, and has any vendor DPA been accepted? | Processor contracts (Art. 28); transfer mechanism (Art. 44 to 46) | Free or trial plans, no DPA accepted, no transfer mechanism in place |

These assumptions are used in the audit report ([04_audit_report.md](04_audit_report.md)). Any answer from Julia that contradicts one changes the related finding.
