# GDPR Peer Audit — AI Search Visibility Agent

**Independent auditor:** Martha  
**Project owner:** Barsha Mishra  
**Source:** Barsha's Project 3 data processing brief (received for peer audit).  
**Scope:** Independent review of the brief only; technical settings, contracts and execution evidence have not been verified.  
**Status:** Phases 1–4 completed as a brief-based audit; Phase 5 updated following written peer debrief on 18 November 2026. Implementation and contractual evidence remain unverified.

## Phase 1 — Read and annotate

**Personal data identified:** report requester's email address; names and professional information in news/search/AI outputs; names of freelancers or other individuals treated as brands; possible IP addresses, timestamps and technical logs; personal information repeated in generated reports.

**Article 9:** No intentional special-category processing is described. However, retrieved news text or personal-brand content could incidentally reveal protected characteristics. This requires testing and a handling policy, not an assumption that such data is absent.

**International data flows:** The brief describes OpenAI, Serper, NewsAPI, Render, Google/Gmail and QuickChart as US-based or US-hosted. Exact recipients, regions, transfers and legal mechanisms are unverified. Barsha subsequently confirmed that the workflow runs on n8n Cloud; the actual hosting/processing region still needs confirmation. Pinecone reportedly holds public guidelines only, but its region is not configured for the EU.

**Unclear points:** Who operates the service and determines purposes? Which data reaches each vendor? Are URLs or email addresses sent to QuickChart? How long are execution records retained? Is the personal Gmail account appropriate for real clients? What safeguards apply to personal-brand requests?

**Potential purpose mismatch:** The brief does not establish incompatible reuse, but storing request data for future weekly tracking or Google Sheets history would introduce an additional purpose requiring separate assessment before implementation.

## Phase 2 — Personal data and role map

### Personal data summary

| Data category | Source | Purpose(s) | Crosses EEA border? | Special category? |
|---|---|---|---|---|
| Requester's email address | User form | Deliver report; possibly execution troubleshooting | Possible: Gmail/Google and n8n; verify routing | No, ordinarily |
| Individual names and professional details | Serper, NewsAPI, OpenAI outputs | Research, visibility analysis, report generation and fact-checking | Possible/likely given stated vendor stack; exact transfers TBD | Not inherently; possible incidental disclosure |
| Personal-brand name or competitor | User form | Brand visibility analysis, LLM report | Possible across search/LLM vendors | Context-dependent |
| IP addresses, timestamps and logs | Form host, n8n, QuickChart or email-image delivery | Service delivery, troubleshooting and image retrieval | Unknown; verify each host | Ordinarily no |
| Report content containing identifiable people | Generated output | Deliver and store report | Possible via OpenAI, Render, Gmail and recipient | Context-dependent |

### Role map — provisional

| Entity | Likely role | Processing activity | DPA needed? |
|---|---|---|---|
| Service operator / commissioning client (not named) | Controller, subject to confirmation | Determines report purpose and means | Processor contracts required where applicable |
| Barsha / project team | Could be controller for self-operated demo or processor for client; TBD | Builds, operates and troubleshoots workflow | Depends on actual relationship |
| n8n Cloud (confirmed by Barsha during debrief) | Likely processor | Workflow execution and logs; hosting region unverified | Verify Article 28 agreement |
| OpenAI and Render | Role depends on service terms and purposes | LLM generation and hosted fact-checking | Verify roles, contracts and sub-processors |
| Serper and NewsAPI | Role depends on terms and actual data | Search and news requests | Verify classification and terms |
| Google/Gmail | Role depends on account/service | Email delivery and possible logs | Verify contractual position; personal account is a concern |
| QuickChart | Role depends on delivery and logging | Chart generation/image retrieval | Verify whether personal data reaches it and applicable terms |
| Pinecone | Reportedly public guideline documents only | Knowledge base | No GDPR processor relationship for this flow if genuinely no personal data; verify |

**Transfer review:** Confirm actual processing regions and data sent to each vendor. For any restricted transfer, check an applicable adequacy decision (including any relevant certified EU–US Data Privacy Framework participation) or SCCs with the required assessment and supplementary measures. A vendor's US headquarters alone does not prove a restricted transfer.

## Phase 3 — Clarifying questions log

| Question | Why it matters | Provisional position pending answer |
|---|---|---|
| 1. Who is the controller/operator, and is this a demo or a service for clients? | Articles 4, 24 and 28: accountability and processor roles | Roles and DPA responsibilities are unverified |
| 2. Exactly which form fields, search queries, report text and identifiers are transmitted to each vendor, and in which region? | Articles 5, 28 and Chapter V: minimisation and transfers | International transfer assessment cannot be completed |
| 3. What are n8n log, report and email retention settings, and can records be deleted on request? | Articles 5(1)(e), 15–17: storage limitation and rights | Default log saving with no stated retention is a material gap |
| 4. Does QuickChart receive only non-personal brand scores, or personal-brand labels and requester identifiers? Does it log viewer IPs? | Articles 5, 6, 13 and vendor obligations | Potential personal-data exposure requires verification |
| 5. How are personal-brand requests, sensitive news content, email delivery and planned recurring history controlled? | Purpose limitation, transparency, security and possible Article 9 data | Restrict to company brands or add safeguards before expanding |

## Phase 4 — Independent audit report

### 1. System summary

The AI Search Visibility Agent accepts brand-related questions and a report-recipient email address, collects search/news information and AI answers, then produces a brand-visibility report. It uses n8n, OpenAI, Serper, NewsAPI, Render, Gmail, QuickChart and a Pinecone knowledge base of public guidance. Although its primary subject is companies, the workflow also processes identifiable email addresses and sometimes information about people appearing in search results or personal brands. It does not appear to make employment, credit or other legally significant decisions about individuals.

### 2. Data and roles

Personal data may enter through the user form, public search/news results, technical logs and the report itself. The operator/controller is not established, and vendor roles and contracts are not evidenced in the brief. Multiple vendors may process information outside the EEA; exact data flows and transfer safeguards remain unknown.

### 3. Compliance findings

**Finding 1 — Controller/processor accountability and contracts. Severity: Significant (potentially Blocking before live personal-data processing).** The brief names multiple services but does not establish the controller, vendor roles or Article 28 agreements. **Action:** Name the operator/controller; map each vendor; verify and execute required DPAs before using processors for live personal data. **Escalation:** Yes — operator, DPO/legal.

**Finding 2 — International transfers. Severity: Significant (potentially Blocking if an unlawful transfer is confirmed).** The brief suggests US-based processing, but actual transfer paths and Chapter V mechanisms are undocumented. **Action:** Create a vendor-by-vendor transfer inventory and verify adequacy/DPF or SCCs and any needed assessment. **Escalation:** Yes — DPO/legal and vendor owners.

**Finding 3 — Storage limitation and rights. Severity: Significant.** Default n8n execution saving and no stated retention schedule create unnecessary persistence and complicate erasure/access requests. **Action:** Define short, purpose-specific retention; configure deletion; document report storage and rights handling. **Escalation:** Yes — operator and technical owner.

**Finding 4 — Lawful basis, transparency and personal-brand edge cases. Severity: Significant.** The brief does not identify Article 6 bases or privacy notices for form email/logs and research involving individuals. **Action:** Document a lawful basis per purpose (e.g., contract may be plausible for requested report delivery; legitimate interests requires an LIA for other processing), publish a privacy notice, and restrict or assess personal-brand processing. **Escalation:** Yes — DPO/legal.

**Finding 5 — Personal Gmail and chart-image data exposure. Severity: Significant.** The brief describes a personal Gmail account for delivery, and QuickChart may receive viewer IPs and possibly personal-brand labels. During the debrief Barsha said she **plans** to replace personal Gmail with a business email covered by a DPA; this is not yet verified as implemented. **Action:** Verify account security, access and vendor terms; implement and validate an organisation-controlled delivery account with appropriate contractual coverage; minimise chart payloads and assess remote image retrieval. **Escalation:** Yes — operator/technical owner.

### 4. GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis for each purpose | Cannot determine from brief | No Article 6 assessment supplied (appropriately omitted for independent review) |
| Purpose limitation | Cannot determine from brief | Planned weekly tracking/history is not yet built |
| Data minimisation | Cannot determine from brief | Brand-focused design helps, but field-level sharing unknown |
| Roles and DPAs | Cannot determine from brief | Vendors named; agreements not evidenced |
| International transfer mechanism | Cannot determine from brief | US processing described; safeguards not documented |
| DPIA if required | Cannot determine from brief | Likely not automatically required for ordinary company-brand reporting; reassess scale and personal-brand profiling |
| Article 22 safeguards if applicable | Appears not applicable on described facts | Brand scoring, no significant automated decisions about people |
| Privacy notice for AI processing | Cannot determine from brief | No notice supplied |
| Rights requests within deadlines | Cannot determine from brief | Logs and report deletion mechanisms unknown |

### 5. Overall recommendation

**Proceed with conditions for a limited, controlled demonstration; do not launch processing of real users' personal data until the operator has verified lawful bases, controller/processor roles and required contracts, international transfer safeguards, a privacy notice, and retention/access controls.** The brief does not establish that every identified concern is a violation; it establishes that compliance cannot yet be demonstrated. Personal-brand requests and planned scheduled history should remain disabled pending a separate review. A DPIA screening should be documented and revisited if processing scope expands.

### 6. Limitations

This is a preliminary independent assessment based solely on the teammate's brief, not a legal opinion, completed DPIA or compliance certification. Technical configuration, contractual terms, consent/notice text and live execution evidence have not been inspected. Obtain qualified legal review before deployment.

## Phase 5 — Joint debrief (written exchange, 18 November 2026)

### 1. Independent audit presented and builder response

Martha shared her independent audit of Barsha's **AI Search Visibility Agent**. Barsha responded in writing: **“I agree with all five of your findings on my agent and with ‘proceed with conditions’.”** This confirms agreement with the five audit themes and the conditional recommendation; it does **not** establish that any remediation has already been implemented.

**Clarifications from Barsha:**

| Topic | Barsha's response | Effect on audit / outstanding evidence |
|---|---|---|
| n8n hosting | Workflow runs on **n8n Cloud** | Hosting model confirmed; region, execution-retention settings and DPA still need verification |
| Email delivery | Will replace **personal Gmail** with a **business email that has a DPA** | Planned mitigation only; verify provider, agreement and implementation before treating as closed |
| Personal brands | Will **exclude personal brands** from the tool | Agreed scope restriction; enforce and test the exclusion in form validation and downstream processing |
| Overall recommendation | Agrees with **proceed with conditions** | Conditional demo may continue; live personal-data processing must wait for required safeguards |

### 2. Lawful-basis comparison

The written debrief also compared Barsha's peer audit of **Martha's AI Interview Preparation Agent** with Martha's self-audit:

| Processing / question | Martha's self-audit position | Barsha's peer-audit position | Agreed conclusion / qualification |
|---|---|---|---|
| Candidate-requested CV analysis and interview report | **Article 6(1)(b)** may apply if necessary to provide the requested service under a contract | **Article 6(1)(b)** proposed for the main purpose | Agreement in principle; verify actual contractual relationship and necessity |
| Necessary security / troubleshooting logs | **Article 6(1)(f)** provisionally, subject to legitimate-interests assessment | Recognises need to establish appropriate basis and safeguards | Document purpose, necessity, balancing test, minimisation and retention before relying on Art. 6(1)(f) |
| Special-category CV information | Exclude unnecessary sensitive content or establish a valid Article 9 condition | Exclude such data or consider **explicit consent under Article 9(2)(a)** | Article 9 is an **additional condition**, not a substitute for an Article 6 lawful basis; mere presence of a photograph does not automatically make it special-category data |

**For Barsha's AI Search Visibility Agent:** Martha's independent audit identified possible Art. 6(1)(b) for requested report delivery, and potentially Art. 6(1)(f) for justified ancillary processing, subject to purpose-specific assessment. Barsha agreed with the five findings; she did not provide a complete purpose-by-purpose lawful-basis register for her agent during this exchange.

### 3. DPIA comparison and decision

| | Position |
|---|---|
| Martha's self-audit of the interview agent | Conduct a **documented DPIA screening**; a full DPIA is required if the processing is likely to result in high risk, but mandatory status had not been established from the brief alone |
| Barsha's peer audit of the interview agent | A full DPIA is **likely required**, citing evaluation of a person and innovative AI technology as risk criteria |
| Written debrief agreement | **Screen now and complete a full DPIA before processing any real CVs**, as a cautious project decision |

**Open question:** Does candidate-requested CV comparison amount to evaluation for DPIA screening? The answer may be yes even when requested by the candidate, but evaluation alone does not automatically establish a legal obligation to conduct a full DPIA. The documented risk assessment must consider processing context, scale, sensitive data, potential effects and safeguards. The agreed full DPIA is a **pre-live safeguard**, not a claim that the law has conclusively been shown to require one in every version of the prototype.

For the **AI Search Visibility Agent**, Martha's audit found that a full DPIA was not automatically established as necessary for company-focused brand reports. A screening and reassessment remain appropriate if the scope or risk changes, including personal-brand profiling or large-scale monitoring. Barsha's planned exclusion of personal brands reduces one potential risk, but must be implemented and tested.

### 4. Compare findings and severity

| Risk theme | Martha's self-audit of interview agent | Barsha's independent audit of interview agent | Debrief outcome |
|---|---|---|---|
| Lawful basis / special-category CV data | Permission implementation and sensitive-data safeguards need verification | **Blocking** for real CVs until Art. 6 basis and any necessary Art. 9 condition established | Agreed no real-CV processing until addressed |
| Processor agreements and transfers | Vendor data fields, regions, DPAs and safeguards unverified | **Blocking** for real CVs until agreements/transfers verified | Agreed no real-CV processing until addressed |
| Retention and access | CV, vector, log and Notion retention/access unverified | **Significant** | Remediation required before live use |
| DPIA | Screening needed; full DPIA dependent on high-risk assessment | **Significant**, likely full DPIA | Screen now; full DPIA before real CVs as agreed project safeguard |
| Third-party data / purpose limitation | Third-party CVs and recruiter contacts need safeguards | **Significant**; also flags uncertain origin of retained Siemens test report | Recognised as an easily missed input/output risk; verify source before treating sample as real personal data |
| Accuracy of generated STAR examples | Unverified claims in sample output | **Minor** accuracy finding | Label drafts and check outputs against source CV; no unverified achievements presented as facts |

**Additional distinction between the two projects:** Martha's audit of Barsha's agent flagged business-email delivery, QuickChart image/IP exposure and exclusion of personal brands. Barsha accepted all five findings. The comparison shows that different systems have different data subjects and processing risks; neither audit should be copied mechanically to the other.

**Blocking versus significant:** Barsha wrote that both auditors agreed on the same practical outcome: **no real CVs until the lawful-basis and DPA issues are resolved**, and these are **Blocking for live processing**. The interview agent is currently inactive. This severity agreement concerns the interview agent and should not be read as proof that every unknown vendor arrangement is unlawful.

### 5. Joint closing reflection

The following reflects Barsha's proposed closing note, with one factual qualification to avoid assuming the Siemens report contains confirmed real personal data:

> Self-assessment is strongest on what we built and weakest on what we never thought of as data. Martha saw her Siemens test report primarily as an accuracy problem, while an outside reviewer identified the possibility that it contained retained personal data being used for a new purpose. Similarly, recruiter contacts inside job descriptions can be overlooked because they arrive inside user uploads. The hardest GDPR gaps to catch in your own work sit between components: third-party data inside inputs, test outputs kept “just in case”, and vendor terms assumed rather than checked.

**Agreement status:** Barsha proposed the original closing note; Martha sent a message accepting the joint debrief and the note with the Siemens qualification. A separate reply explicitly accepting this exact revised wording has not been recorded. This note is suitable for the shared submission once both confirm the final wording.

### 6. Outstanding actions (not evidence of completion)

1. **Barsha:** Verify n8n Cloud processing region, execution-log retention and DPA; replace the personal Gmail setup and verify the business-email contractual terms.
2. **Barsha:** Implement and test exclusion of personal brands; verify QuickChart payloads and any IP-address disclosure.
3. **Both:** Keep controller/processor classifications, lawful bases, transfers, privacy notices and retention schedules as *unverified* until supported by settings, agreements or workflow evidence.
4. **Martha:** Before reactivating the interview agent for real CVs, resolve the blocking issues, perform DPIA screening and the agreed full DPIA, and investigate the origin and retention of the Siemens sample report.

**Scope note:** This debrief documents the written exchange and mutual recommendations; it is not proof that technical remediation, contractual review or a DPIA has been completed.
