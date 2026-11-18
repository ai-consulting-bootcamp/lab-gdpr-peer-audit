# Independent GDPR Peer Audit — RCSA Evidence & Challenge Agent

**Audit date:** 17 November 2026  
**Source:** *GDPR Audit — Data Processing Brief: RCSA Evidence & Challenge Agent* (2 pages)  
**Review type:** Independent peer assessment based on the data processing brief; no access to the builder's self-audit or production environment.  
**Scope:** Current synthetic-data MVP versus a proposed production deployment in an EEA bank. The EEA context is an assumption for this assessment, not a fact established by the brief.

**Evidence convention:** **Confirmed** = explicitly stated in the brief; **Provisional** = audit inference requiring validation; **Unknown** = not established by the brief.

## Phase 1 — Read and Annotate

| Annotation | Evidence in the brief | GDPR interpretation / open issue |
| --- | --- | --- |
| Personal data — people and contact details | Process owner/assessor names, roles, departments and possibly business emails; reporter and involved-employee names (sections 1–2). | Identifiable employee data under Article 4(1). Whether all these fields reach the AI API is unknown. |
| Personal data — responses and records | Owner-linked RCSA answers and justifications, historical RCSAs, customer/account references, incident amounts and dates (sections 1–2). | Personal data when linked to an identifiable owner, employee or customer; historic and new records may be combined. |
| Personal data — AI outputs | Challenge flags linked to named owners, plus potentially attributable assessment text (sections 1 and 6). | AI-generated information can itself be personal data; inaccurate flags could affect individuals. |
| Potential Article 9 data | Free-text loss narratives may mention workplace injuries or health conditions (section 1). | Health information is special-category data; an Article 9(2) condition would be needed if processed, in addition to an Article 6 lawful basis. |
| Potential Article 10 data | Narratives may describe suspected internal fraud by an employee (section 1). | Allegations relating to criminal offences may trigger Article 10, **not** Article 9; relevant EU/member-state legal authority and safeguards must be assessed. |
| Usually non-personal data | Aggregated KRI counts, rates and volumes; generic risk taxonomy (sections 1–2). | Normally outside GDPR if genuinely non-identifying. Small groups or combinations may enable re-identification. |
| Possible international transfer | Owner answers, process descriptions and relevant loss-event text are sent to the OpenAI API; provider is US-based (sections 4–5). | A non-EEA transfer **cannot be ruled out**, but actual hosting, remote access, onward transfers and safeguards are unverified. |
| Potential incompatible reuse | The stated purpose is operational-risk assessment, **not** employee performance evaluation (sections 3 and 6). | Using named challenge flags for HR discipline or performance ranking could constitute a new, incompatible purpose; prevent and assess such reuse. |
| Material unknowns | No real-data retention/deletion policy, formal access control, enforced or logged final approval, verified API contract or transfer settings (sections 5–6). | These are production-readiness gaps, not proof that the synthetic MVP currently violates GDPR. |

**Phase 1 conclusion:** The MVP is described as using only synthetic data. A production version would process at least employee-related data and possibly customer data, including sensitive free text. The highest-risk boundary is the transfer of selected internal narratives/answers to an external AI API, followed by generating flags that are attributable to employees.

## Phase 2 — Personal Data and Role Map

### 2.1 Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
| --- | --- | --- | --- | --- |
| Owner/assessor name, role, department, possible business email | Process owner / RCSA records | Link answers and reports to responsible persons | **Possible** if included in API input; unverified | No |
| RCSA answers, justifications and control descriptions linked to an owner | Owner input; previous bank RCSA | Risk identification; contradiction checks; ratings/report | **Potentially** — current answers sent to API; destination unverified | Not ordinarily; free text may contain sensitive details |
| Reporter and involved-employee identities | Internal loss/near-miss database | Compare assessments with incident evidence | **Possible** within selected narrative text; payload fields unknown | Not ordinarily |
| Customer/account references, incident amounts and dates | Internal loss/near-miss database | Evidence-based challenges and risk reporting | **Possible** within selected loss-event text; unverified | Not ordinarily; financial data is still potentially sensitive in the everyday sense |
| Workplace injury/health references in narratives | Internal free-text loss reports | Incident evidence, if not filtered | **Possible** if included in API prompts | **Yes — Article 9** (health) |
| Suspected employee fraud / offence allegations | Internal free-text loss reports | Incident evidence, if not filtered | **Possible** if included in API prompts | **Article 10 may apply**; distinct from Article 9 |
| AI challenge flags and reports attributable to named owners | System-generated outputs | Challenge, ratings and second-line reporting | Outputs stored locally; external generation uses API; exact output flow unknown | Usually no; may reproduce sensitive source data |
| Aggregated KRIs | Bank KRI reporting | Risk signals and calibration | No specific KRI-to-API transfer documented | Normally not personal data, unless re-identification is possible |

**Data flow established by the brief:** Bank RCSA records, owner input, loss records and KRIs feed the local Python/LangGraph workflow. The OpenAI API receives process descriptions, owner answers and relevant loss-event text; the local MVP stores inputs and generated reports as files. There is no vector database or external search API receiving bank data in the described design.

### 2.2 Controller/processor role map

| Entity | Role | Processing activity | DPA needed? |
| --- | --- | --- | --- |
| Bank (future client) | **Provisional controller** | Defines RCSA objectives, categories, access, retention and downstream use | **No** DPA with itself; responsible for Article 28 contracts with processors |
| Builder / development team | **Conditional processor** if it processes real bank data on the bank's behalf; otherwise a developer outside this processing chain | Build, support, hosting or troubleshooting **only if** given access to real records | **Yes if** processing bank personal data as processor; **not applicable** for purely synthetic development without personal data |
| OpenAI API provider | **Provisional processor**, subject to the actual service contract and purposes | Processes submitted descriptions, owner answers and loss narratives to generate risks, challenges and reports | **Yes**, an Article 28-compliant DPA where processing personal data on controller instructions; confirm contractual chain and subprocessors |
| Local Python/LangGraph software | **Not a separate legal entity** | Orchestrates processing on the local machine | No standalone DPA; access by any external host/support provider would require separate role analysis |

### 2.3 International transfer assessment

- **Known:** API processing by a US-based provider; the specific processing location, retention settings and contractual safeguards have **not** been verified.
- **Not established:** That any actual EEA-to-US transfer has already occurred, or that the contracted API service/entity is covered by a particular transfer mechanism.
- **Required before real-data use:** Map data locations, remote access and subprocessors; verify whether a relevant EU–US Data Privacy Framework adequacy decision covers the **specific certified recipient and service**, or implement an appropriate Article 46 mechanism such as Standard Contractual Clauses (and a transfer impact assessment / supplementary measures where required). An Article 28 DPA and a Chapter V transfer mechanism address **different** obligations.

## Phase 3 — Clarifying Questions Log

| Priority and question | Why this matters | Provisional assumption without an answer |
| --- | --- | --- |
| **1. Exactly which fields enter each OpenAI request? Are owner names, customer/account identifiers, health details and fraud allegations removed before transmission?** | Articles 5(1)(c), 9, 10, 25 and 32: minimisation, sensitive/offence data and security. | Free-text narratives may contain these details; no documented filtering or redaction is evident. |
| **2. What is the bank's Article 6 lawful basis for each purpose, and what specific Article 9/10 authority exists if sensitive/offence data are retained? Is HR reuse explicitly prohibited?** | Articles 5(1)(b), 6, 9 and 10: lawfulness and purpose limitation. | No basis or additional condition is documented. Article 6(1)(c) may apply only if a specific legal obligation covers the processing; Article 6(1)(f) would require a defensible legitimate-interests assessment where applicable. Neither is presumed valid. |
| **3. Which OpenAI contracting entity, service settings, processing regions, retention periods, subprocessors, DPA and Chapter V transfer mechanism apply?** | Articles 28, 32 and 44–46: processor governance, security and third-country transfers. | Processing geography and contractual safeguards are not verified, as the brief explicitly says. |
| **4. Can named flags affect performance reviews, disciplinary action or other decisions about employees? Is independent human approval mandatory, meaningful and logged?** | Articles 5(1)(b), 22 and 25: downstream purpose, automated individual decisions and protective design. | The system is intended to rate processes rather than people, but approval is not enforced and misuse remains possible. Article 22 applicability is not established. |
| **5. Who can access local files and reports, how long are they retained, how are data-subject requests handled, and has a documented DPIA screening assessed production scale and impact?** | Articles 5(1)(e), 12–22, 32 and 35: storage limitation, rights, security and DPIA. | No formal real-data deletion/access framework or DPIA evidence is provided; bank-level controls may exist but were not described. |

## Phase 4 — Independent Audit Report

### Section 1 — System summary

The Python/LangGraph agent supports bank Risk and Control Self-Assessments (RCSAs). It combines process descriptions, prior RCSAs, loss events and KRIs to suggest risks, challenge owner answers and produce indicative ratings and reports. OpenAI processes descriptions, answers and selected loss-event text. The MVP uses synthetic data; production could expose employee/customer identifiers and potentially sensitive narratives. Second-line human approval is intended but not enforced or logged.

### Section 2 — Data and role map

The bank is the **provisional controller**. The builder is a processor only if handling real data for the bank; OpenAI's role and contracting chain need verification. Owner-linked responses, incident text and AI flags may be personal data. Non-EEA API transfers are **possible, not confirmed**; the MVP itself is described as synthetic-only.

### Section 3 — Compliance findings

**Finding 1 — Lawful basis and purpose limitation**  
**Severity:** Blocking for production.  
**Description:** No Article 6 basis is documented; risk-management obligations do not automatically justify every AI input or HR reuse.  
**Recommended action:** Document a valid basis per purpose and prohibit incompatible employee assessment.  
**Escalation needed?** Yes — DPO/legal and risk owner.

**Finding 2 — Health and offence-related narratives**  
**Severity:** Blocking if processed without the required legal conditions.  
**Description:** Incident text may include Article 9 health data and Article 10 offence allegations; no exception/authorisation or exclusion control is evidenced.  
**Recommended action:** Redact/exclude where possible; otherwise establish specific conditions and safeguards.  
**Escalation needed?** Yes — DPO/legal.

**Finding 3 — Processor agreements**  
**Severity:** Blocking before any processor receives real data without an appropriate DPA.  
**Description:** Article 28 terms with the API provider and any real-data-handling builder are unverified.  
**Recommended action:** Confirm roles, agreements, instructions, subprocessors and retention terms.  
**Escalation needed?** Yes — DPO, procurement and legal.

**Finding 4 — International transfers**  
**Severity:** Significant; a real transfer without a Chapter V mechanism would block deployment.  
**Description:** API location, remote access and DPF/SCC coverage are unknown.  
**Recommended action:** Verify actual flows and recipient; document applicable DPF coverage or SCCs and any necessary transfer assessment.  
**Escalation needed?** Yes — DPO/vendor manager.

**Finding 5 — DPIA assessment**  
**Severity:** Significant; Blocking if a mandatory DPIA is omitted.  
**Description:** AI, possibly sensitive narratives, linked employee flags and multiple data sources indicate potential high risk, but no screening is supplied. AI use alone does not automatically mandate a DPIA.  
**Recommended action:** Document Article 35 screening and complete a DPIA before processing if required.  
**Escalation needed?** Yes — DPO/risk owner.

**Finding 6 — Security, retention and rights**  
**Severity:** Significant.  
**Description:** Local files lack a formal real-data retention policy or application access controls; notices and data-subject-rights workflows are unaddressed.  
**Recommended action:** Define deletion, access, appropriate security/logging, privacy information and rights handling.  
**Escalation needed?** Yes — IT security/DPO.

**Finding 7 — Human oversight and downstream misuse**  
**Severity:** Significant.  
**Description:** Named challenge flags could influence employee assessments. Human sign-off is not enforced or logged. Article 22 is **not established** because consequential solely automated decisions about people are not described.  
**Recommended action:** Restrict HR reuse, log meaningful approval and reassess Article 22 if individual decisions are introduced.  
**Escalation needed?** Yes — risk management/HR governance/DPO.

### Section 4 — Specific GDPR obligations checklist

| Obligation | Assessment | Note |
| --- | --- | --- |
| Lawful basis for each purpose | **Gap identified** | No basis documented. |
| Purpose limitation | **Cannot determine from brief** | HR reuse risk; no restriction evidenced. |
| Data minimisation | **Cannot determine from brief** | API filtering unknown. |
| Roles and DPAs | **Gap identified** | Agreements unverified. |
| International transfer mechanism | **Gap identified** | Safeguards unverified. |
| DPIA if required | **Cannot determine from brief** | Screening/DPIA not supplied. |
| Article 22 safeguard if applicable | **Cannot determine from brief** | Article 22 trigger unclear; approval unenforced. |
| Privacy notice covering AI | **Cannot determine from brief** | Not described. |
| Data-subject rights within deadlines | **Cannot determine from brief** | No process described. |

### Section 5 — Overall recommendation

**Do not proceed with production processing of real personal data.** The synthetic-only MVP may continue within its stated scope. Before real-data go-live, establish lawful bases and any Article 9/10 conditions; verify Article 28 contracts and any Chapter V transfers; implement retention, security, rights and enforced human review; and document DPIA screening and, if required, a DPIA. This is a **production readiness decision**, not evidence of an existing GDPR breach.

### Section 6 — What this report is not

This first-pass audit is **not** a legal opinion, a DPIA or a compliance certification. It relies only on the brief; the bank should obtain legal/DPO review and verify operational evidence.

## Phase 5 — Debrief Conversation and Joint Note

In refered project 3 all bootcamp members did only work on a MVP version. That's also the case for the RCSA audit tool and the career intelligence agent. Therefore, in both project assessments we were able to find compliance issues and risks. These risks were mostly based on the early stages of the projects and on the lack of focus regarding the data security and savety (GDPR). Still these are solvable issues, which do not inherently stop each partner from further development steps as long as significant findings in each report are handled.

Both projects are MVPs, so both audits found gaps, like no AI labels, unclear data transfers and no real human approval step. These are normal at this stage and can be fixed before real users or real data are involved.
The debrief showed a difference: as builders, we judged what we planned to build, so some things felt clear to us. As auditors, we could only judge what was written in the brief, so the same things became open questions. What is not written down is not a control. Self-audits know the system better, but external audits find the gaps.

Questions discussed:

**Q1 – Exactly which fields enter each OpenAI request? Are owner names, customer identifiers, health details and fraud allegations removed before transmission?**
The request contains the process steps, the owner's answers and justifications, and the relevant loss event descriptions and KRI values. **There is no redaction or pseudonymisation step yet**, so names or sensitive details in free text would be transmitted. With synthetic data this is not an issue today; for real data a redaction step is planned.

**Q2 – What is the bank's Art. 6 lawful basis per purpose, and what Art. 9/10 authority exists if sensitive or offence data are retained? Is HR reuse explicitly prohibited?**
No lawful basis has been documented yet; this would be the bank's decision as controller. My proposal is Art. 6(1)(f) legitimate interest (effective operational risk management) with a documented legitimate interest assessment, because Art. 6(1)(c) would require a specific legal obligation covering this exact processing. No Art. 9/10 condition is planned; instead, sensitive and offence data should be filtered out before processing. HR reuse is not yet explicitly prohibited in writing.

**Q3 – Which OpenAI entity, settings, regions, retention, subprocessors, DPA and Chapter V transfer mechanism apply?**
Not verified. The MVP uses a standard OpenAI API key. Contracting entity, DPA, regions, retention settings, subprocessors and the transfer mechanism are open items for vendor due diligence before real data is used.

**Q4 – Can named flags affect performance reviews or other decisions about employees? Is independent human approval mandatory, meaningful and logged?**
Not intended, but not technically prevented (see A-Q1). Human approval is not enforced or logged in the MVP (see A-Q2). The system takes no decisions about individuals; it produces proposals for discussion.

**Q5 – Who can access local files and reports, how long are they retained, how are data subject requests handled, and has a DPIA screening been done?**
The MVP runs on my local machine; only I have access. Reports are stored as local files with **no retention or deletion policy**. There is no process for data subject requests and **no DPIA or DPIA screening** has been done, because only synthetic data is used. A bank deployment would need all of these.

## Legal reference sources

- [GDPR — Regulation (EU) 2016/679 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/) — especially Articles 4–6, 9–10, 12–22, 25, 28, 32, 35 and 44–46.
- [EDPB — Data protection impact assessment](https://www.edpb.europa.eu/topics/accountability-and-compliance-tools/data-protection-impact-assessment_en) — documented high-risk assessment and DPIA framework.
- [EDPB — International data transfers](https://www.edpb.europa.eu/sme/be-compliant/international-data-transfers_en) — adequacy decisions, DPF participation, SCCs and transfer assessments.
- [EDPB — Automated decision-making and profiling](https://www.edpb.europa.eu/documents/guideline/automated-decision-making-and-profiling_en) — Article 22 scope and safeguards.
