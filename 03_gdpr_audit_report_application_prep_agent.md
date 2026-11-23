# GDPR audit report: Application Prep Agent

Auditor: Friedrich Tschoepke · Builder: Nicolò Marseu · 23 November 2026 · Based on the system brief, the public repository and the provisional assumptions in the questions log.

## 1. System summary

The Application Prep Agent is an n8n workflow that takes a CV, a job posting and an email address through a public web form. It sends the full CV text to OpenAI to score the person's fit for the job from 0 to 100 and to write CV edits, a cover letter and interview notes, and emails the result through Gmail. Below a score of 50 it automatically sends a short note instead of the full pack. It is live as a free demo and is meant to be sold to career services, later with stored candidate profiles and a partner dashboard showing scores.

## 2. Data and role map

Complete CVs, free text, email addresses and an inferred fit score, with special-category data likely present in CVs. Nicolò is controller for the demo and will be processor for each paying client. OpenAI is a processor; the Ironhack n8n host is an undocumented processor; the personal Gmail account cannot serve as one. Data reaches the US through OpenAI's group and Google; no transfer mechanism is documented.

## 3. Compliance findings

**Finding 1 — Processor contracts (Article 28) and transfers (Article 44)**
**Severity:** Blocking
**Description:** Every CV passes through the Ironhack n8n instance and every report through a personal Gmail account. Neither relationship has a processor contract, and consumer Gmail offers none. OpenAI's DPA exists but its acceptance is not documented.
**Recommended action:** Restrict the live form to the fictional demo CV now. Replace Gmail with an email service offering an EU DPA; obtain a DPA from Ironhack or move to hosting with one; archive OpenAI's DPA.
**Escalation needed?** Yes, Ironhack (as host) and a data protection adviser.

**Finding 2 — DPIA required, not conducted (Article 35)**
**Severity:** Blocking (before real candidate data or the pilot)
**Description:** EDPB criteria met: evaluation or scoring of people, innovative technology, likely sensitive data, and partly automated decisions and denial of a service. In sprint 3, vulnerable data subjects (laid-off employees) and larger scale are added.
**Recommended action:** Conduct a DPIA focused on the fit score before the pilot.
**Escalation needed?** Yes, data protection adviser.

**Finding 3 — Transparency and storage limitation (Articles 5, 13, 14)**
**Severity:** Significant
**Description:** "Nothing you submit is stored" is contradicted by n8n run history, the Gmail sent folder and OpenAI's 30-day logs. No privacy notice exists. Candidates whose coaches upload their CV are not informed.
**Recommended action:** Switch off n8n run history or delete after seven days; state exactly what is kept where; publish a notice; give coaches a candidate notice.
**Escalation needed?** No.

**Finding 4 — Lawful basis and special categories (Articles 6, 9)**
**Severity:** Significant
**Description:** No basis is documented. For self-use, contract (6(1)(b)) fits. For coach submissions the client institution needs its own basis. No Article 9 condition covers scoring special-category data.
**Recommended action:** Document the basis per purpose; strip photo, date of birth, nationality and address before scoring.
**Escalation needed?** Yes, legal review for coach submissions.

**Finding 5 — Automated decision (Article 22) and planned score reuse**
**Severity:** Significant
**Description:** The gate below 50 is a solely automated outcome of profiling. Limited effect in self-use; significant once partners rely on scores (CJEU C-634/21, SCHUFA). Sprint 3 reuses scores for a new purpose.
**Recommended action:** Let users request the full pack anyway, explain the score logic, and bar partners from deciding on scores without human review.
**Escalation needed?** Yes, before sprint 3.

**Finding 6 — Third-party content on the landing page (ePrivacy, § 25 TDDDG)**
**Severity:** Minor
**Description:** Google Fonts loaded from Google servers without consent.
**Recommended action:** Host fonts locally.
**Escalation needed?** No.

## 4. GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis per processing purpose | Gap identified | None documented. |
| Purpose limitation | Gap identified | Coach uploads; planned profiles and score dashboard. |
| Data minimisation | Gap identified | Full CV incl. photo text, age, nationality goes to the model. |
| Roles mapped, DPAs in place | Gap identified | Ironhack and Gmail without DPA. |
| International transfer mechanism documented | Gap identified | Not documented for OpenAI or Google. |
| DPIA if required | Gap identified | Required, not done. |
| Article 22 safeguard | Gap identified | No override, no explanation. |
| Privacy notice covers AI processing | Gap identified | No notice at all. |
| Rights operational within deadlines | Cannot determine from brief | Depends on where copies are; no procedure known. |

## 5. Overall recommendation

**Do not proceed with real candidate data.** Two blocking findings apply: processors without contracts already sit in the data path, and the required DPIA has not been done. The fictional demo can stay online if the form is limited to the sample CV or clearly marked as a test. Once Findings 1 and 2 are closed, the system moves to proceed with conditions, with Findings 3 to 5 to be fixed before the pilot starts. None of this calls the product into question; the fixes are contractual and configuration work.

## 6. What this report is not

This report is not a legal opinion, not a DPIA and not a certification of compliance. It rests on a system brief, public repository files and provisional assumptions. The client should obtain legal review before relying on this assessment.
