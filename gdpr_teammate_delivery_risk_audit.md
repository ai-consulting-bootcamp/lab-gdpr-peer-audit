# GDPR Audit — AI Delivery Risk Assistant

**Audited project:** `delivery-risk-assistant`
**Teammate / Project owner:** Akansha Verma
**Auditor:** Vincent de Paul
**Date:** 19 August 2026
**Audit type:** Independent GDPR peer audit

> **Scope note:** This audit is based on the data processing brief provided by the project owner. The audit is intentionally independent of the teammate's self-audit findings. Where the brief does not provide enough information to reach a conclusion, the assessment will state **TBD — legal review** or **Cannot determine from brief** rather than making assumptions.

---

# Phase 1 — Read and Annotate

## 1. Personal Data Identified

### Directly Identifiable Personal Data

* Full names of team members, stakeholders and external partners.
* Professional roles and employer context.
* Workplace communications authored by identifiable individuals.
* Standup transcript content.
* Slack messages.
* Retrospective comments.
* Status emails.
* Stakeholder and executive emails.

### Derived / Inferred Personal Data

* Workload strain.
* Capacity.
* Morale.
* Attrition / retention signals.
* Individual responsibility for blocked work.
* Individual ownership of remediation tickets.
* Contradictions between an individual's status claim and underlying evidence.
* Other performance-adjacent signals derived from workplace communications.

### Special-Category Data

**Cannot determine from brief.**

The brief does not identify any explicit Article 9 special-category data such as health, racial or ethnic origin, political opinions, religious beliefs, trade-union membership, sexual orientation or biometric data.

However, workplace communications may potentially contain or allow sensitive information to be inferred. This requires further confirmation before production processing.

---

## 2. Data Sources Identified

The current project documentation states that the repository's demo corpus is synthetic/fabricated.

Potential production sources include:

* Jira / ticket systems.
* Slack exports.
* Email.
* Sprint reports.
* Standup transcripts.
* Retrospective notes.
* Stakeholder communications.
* Executive communications.
* Other project-management artefacts uploaded through the application.

**Important distinction:** The current demo data is synthetic, but the architecture is designed for live client data.

---

## 3. Processing Activities Identified

The brief identifies the following processing activities:

1. Ingestion of project artefacts.
2. Chunking of source documents/text.
3. Vectorisation and embedding generation.
4. Storage of embedded chunks.
5. Semantic retrieval.
6. Evidence reranking.
7. LLM-based extraction of delivery risks.
8. Extraction of individual-related signals such as workload, morale and attrition.
9. Severity classification.
10. Human review of high-severity or contradictory findings.
11. Generation of leadership-facing reports.
12. Distribution through Markdown, Notion and Telegram.
13. Scheduled processing through n8n.

---

## 4. Third-Party Processing Identified

The brief identifies:

| Provider / service | Apparent function                  | Personal-data processing? |
| ------------------ | ---------------------------------- | ------------------------- |
| OpenAI             | Embeddings and LLM risk extraction | Potentially yes           |
| Pinecone           | Vector database                    | Potentially yes           |
| Cohere             | Evidence reranking                 | Potentially yes           |
| Telegram           | Human-review alerts                | Potentially yes           |
| Notion             | Report destination                 | Potentially yes           |
| n8n                | Workflow orchestration             | Potentially yes           |
| Render             | Application/API hosting            | Potentially yes           |

**Transfer status:** Cannot determine from brief.

The brief explicitly states that processing locations and regions are not confirmed.

---

## 5. Cross-Border Data Flow

**Status: Cannot determine from brief.**

The brief states that OpenAI, Pinecone, Cohere, Telegram, Notion, n8n and Render may process or host personal data, but the relevant processing/storage locations are not documented.

Therefore, it is not currently possible to establish:

* Whether data leaves the EEA.
* Which vendors process data outside the EEA.
* Whether an adequacy decision applies.
* Whether Standard Contractual Clauses (SCCs) are required.
* Whether any additional transfer safeguards are necessary.

---

## 6. Purpose-Limitation Flag

**Potentially significant issue identified.**

The source information is workplace/project information originally generated for operational purposes such as project management, communication and delivery coordination.

The proposed Tender/Risk Assistant-style processing uses that information to infer:

* workload,
* morale,
* capacity,
* attrition risk,
* performance-adjacent signals.

The compatibility between the original collection purposes and these new AI-based risk-analysis purposes cannot be determined from the brief alone.

**Provisional assessment: TBD — legal review.**

---

## 7. Automated Decision-Making / Human Review

The system assists in identifying and classifying delivery risks and individual-related signals.

The brief states that severity-1 findings and contradictory findings are routed to a human reviewer through Telegram before appearing in the report.

This is an important safeguard.

However, the brief does not establish whether the resulting reports are subsequently used to make decisions about identifiable employees, such as performance management, disciplinary action, promotion, dismissal or other similarly significant decisions.

**Article 22 assessment: Cannot determine from brief — further clarification required.**

---

# Phase 1 — Initial Auditor Observations

### Observation 1 — Personal data is clearly present

The system is not limited to anonymous operational project data. It processes names, workplace communications and derived individual-level signals.

### Observation 2 — Sensitive inferences create additional risk

The system explicitly derives morale, workload, capacity and attrition-related signals from communications attributable to identifiable individuals.

### Observation 3 — Production transfer architecture is unclear

The brief identifies multiple external providers but does not establish their processing locations or applicable international-transfer mechanisms.

### Observation 4 — Purpose compatibility requires investigation

The original operational purpose of workplace communications may differ from the purpose of AI-based employee-related risk analysis.

### Observation 5 — Human review is present but its legal significance requires clarification

The code-enforced human-in-the-loop mechanism is relevant, but the downstream use of the generated risk reports must be understood before reaching an Article 22 conclusion.

---

# Phase 1 — Questions to Carry Forward

The following issues must be investigated in Phases 2–4:

1. What is the client's lawful basis for analysing employee communications for delivery and individual-related risk?
2. Are employees informed that their communications may be analysed by an AI system for workload, morale or attrition signals?
3. Are any Article 9 special-category data or sensitive attributes processed or inferred?
4. Where are OpenAI, Pinecone, Cohere, Telegram, Notion, n8n and Render processing/storing the data?
5. What contractual safeguards and DPAs exist with each processor?
6. Are AI-generated risk reports used to make employment-related decisions about individuals?
7. Has a DPIA been conducted?

**Phase 1 status: Initial review complete — proceed to Phase 2.**
# Phase 2 — Personal Data and Role Map

## 2.1 Personal Data Summary

| Data category                                       | Source                                                              | Purpose(s)                                                                    | Crosses EU border?              | Special category?                                            |
| --------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------ |
| Names and professional roles                        | Sprint reports, standups, Slack, emails and other project artefacts | Identification, evidence retrieval, risk analysis and reporting               | **Cannot determine from brief** | **No confirmed Article 9 data**                              |
| Workplace communications                            | Slack threads, standup transcripts, retrospectives and emails       | Semantic retrieval, evidence ranking and AI risk extraction                   | **Cannot determine from brief** | **Cannot determine from brief**                              |
| Workload and capacity information                   | Project communications and project artefacts                        | Delivery-risk analysis and risk reporting                                     | **Cannot determine from brief** | **Potentially sensitive, but not automatically Article 9**   |
| Morale-related information                          | Workplace communications authored by identifiable individuals       | Delivery-risk analysis and risk reporting                                     | **Cannot determine from brief** | **Cannot determine from brief**                              |
| Attrition / retention signals                       | Statements in workplace communications                              | Identify potential delivery risks associated with staff retention or capacity | **Cannot determine from brief** | **No confirmed Article 9 data; further assessment required** |
| Performance-adjacent information                    | Tickets, status reports and workplace communications                | Risk detection, severity classification and leadership reporting              | **Cannot determine from brief** | **No confirmed Article 9 data**                              |
| AI-derived risk assessments                         | LLM analysis of source material                                     | Delivery-risk classification and leadership reporting                         | **Cannot determine from brief** | **Cannot determine from brief**                              |
| Vector embeddings                                   | Text extracted from source documents                                | Semantic retrieval and evidence ranking                                       | **Cannot determine from brief** | **Potentially linked to personal data**                      |
| Retrieved evidence passages                         | Vector database and retrieval system                                | Provide evidence to the LLM for risk analysis                                 | **Cannot determine from brief** | **Cannot determine from brief**                              |
| Risk reports containing individual-related findings | AI-generated reports                                                | Leadership review and delivery-risk management                                | **Cannot determine from brief** | **Cannot determine from brief**                              |

### Personal Data Assessment

The brief provides sufficient evidence to conclude that the system processes personal data.

The data is not limited to names and identifiers. It includes the **content of communications written by identifiable individuals and information inferred about those individuals**, including workload, morale, capacity and potential attrition.

The AI-derived information remains relevant to GDPR analysis because personal data can include information generated or inferred about an identifiable person.

---

## 2.2 Special-Category Data Assessment

**Assessment: Cannot determine from brief.**

No confirmed Article 9 category is identified in the brief.

However, the system analyses free-text workplace communications and creates inferences concerning workload strain and morale. If the processing begins to infer or reveal information concerning an individual's physical or mental health, another Article 9 category could potentially become relevant.

The client should therefore establish whether source material or model outputs contain or infer Article 9 data before production deployment.

---

## 2.3 Role Map

| Entity                      | Role                                                           | Processing activity                                                                                    | DPA needed?                                                         |
| --------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Client organisation         | **Controller — provisional**                                   | Determines the purpose of analysing project artefacts and using AI-generated delivery-risk information | **Not with itself; controller responsibilities must be documented** |
| Teammate / development team | **Processor — provisional**                                    | Operates the application and processes client project artefacts according to client instructions       | **Yes, if acting as processor under Article 28**                    |
| OpenAI                      | **Processor / service provider — role to be confirmed**        | Generates embeddings and performs LLM-based risk extraction                                            | **Yes if processor; contractual role and terms must be verified**   |
| Pinecone                    | **Processor / service provider — role to be confirmed**        | Stores and retrieves vector embeddings and associated metadata                                         | **Yes if processor; contractual terms must be verified**            |
| Cohere                      | **Processor / service provider — role to be confirmed**        | Reranks candidate evidence                                                                             | **Yes if processor; contractual terms must be verified**            |
| Telegram                    | **Third-party service — role to be confirmed**                 | Delivers human-in-the-loop approval alerts                                                             | **Role, processing terms and DPA status require verification**      |
| Notion                      | **Processor / service provider — role to be confirmed**        | Receives/stores leadership-facing reports                                                              | **Yes if processing personal data as a processor**                  |
| n8n                         | **Processor / infrastructure service — role to be confirmed**  | Executes scheduled workflow and orchestrates report delivery                                           | **Yes if processing personal data as a processor**                  |
| Render                      | **Processor / infrastructure provider — role to be confirmed** | Hosts the live FastAPI backend                                                                         | **Yes if processing personal data as a processor**                  |

---

## 2.4 Controller / Processor Analysis

The **client organisation is provisionally the controller** because it determines why the project data is analysed and how the resulting risk information is used.

The development team would provisionally be a **processor** if it operates the system solely on behalf of the client and according to documented instructions.

The external vendors may also act as processors where they process personal data on behalf of the controller/processor chain. However, the brief does not provide sufficient contractual information to conclusively establish each vendor's GDPR role.

**Important:** Roles cannot be determined solely from the names of the services. The actual contractual arrangements, purposes and means of processing must be reviewed.

---

## 2.5 Data Processing Agreement Assessment

A DPA would generally be required for each relationship where an entity qualifies as a processor processing personal data on behalf of a controller.

Based solely on the brief, the following relationships require verification:

* Client → development team
* Development team/client → OpenAI
* Development team/client → Pinecone
* Development team/client → Cohere
* Development team/client → Telegram
* Development team/client → Notion
* Development team/client → n8n
* Development team/client → Render

**Current status: Cannot determine from brief whether appropriate DPAs are in place.**

The audit therefore cannot treat the processor relationships as compliant merely because the vendors are named.

---

## 2.6 International Transfer Assessment

The brief explicitly states that processing locations are not confirmed.

Therefore:

**International transfer status: Cannot determine from brief.**

Before production processing, the organisation should identify:

1. The country/region where each vendor processes personal data.
2. The country/region where data is stored.
3. Relevant subprocessors.
4. Whether any processing involves a transfer outside the EEA.
5. Whether an adequacy decision applies.
6. If not, whether Standard Contractual Clauses or another valid Chapter V mechanism applies.
7. Whether supplementary safeguards are required.

No specific transfer mechanism should be asserted until these facts are verified.

---

## 2.7 Phase 2 Findings

### Finding P2-01 — Extensive personal-data processing

The system processes identifiable employee communications and derives individual-related information such as morale, workload and attrition signals.

**Status: Confirmed from brief.**

### Finding P2-02 — Vendor role allocation is incomplete

The brief identifies numerous external services, but their exact GDPR roles and contractual relationships cannot be determined from the brief.

**Status: Gap identified.**

### Finding P2-03 — DPA status cannot be confirmed

The brief does not provide evidence that appropriate Article 28 agreements exist with relevant processors.

**Status: Cannot determine from brief.**

### Finding P2-04 — International transfers are unresolved

The processing locations of the external providers are not documented.

**Status: Significant information gap.**

### Finding P2-05 — Embeddings cannot automatically be treated as anonymous

The system stores vectorised representations of source material that may contain identifiable employee information.

**Status: Further technical and legal assessment required.**

---

## Phase 2 Conclusion

The AI Delivery Risk Assistant processes substantially more than ordinary operational project data. Its pipeline processes identifiable workplace communications and creates additional individual-level inferences.

The client should provisionally be treated as the controller, with the development team and relevant technology providers potentially acting as processors, subject to contractual verification.

The principal unresolved Phase 2 issues are:

* processor/controller role confirmation,
* DPA status,
* international transfer mechanisms,
* vendor/subprocessor mapping,
* and the treatment of personal data contained in embeddings and derived risk information.

**Phase 2 status: Complete — proceed to Phase 3.**
# Phase 3 — Clarifying Questions Log

The following questions must be answered before a final GDPR compliance opinion can be issued. They focus on information that is material to the assessment but cannot be established from the data processing brief.

## Question 1 — What is the lawful basis for analysing employee communications?

### What we need to know

What lawful basis does the client rely on to process Slack messages, emails, standup transcripts, retrospective comments, ticket information and other workplace communications for AI-based delivery-risk analysis?

The client should also explain whether the same lawful basis covers the generation of individual-level signals such as workload, morale and potential attrition.

### Why it matters

GDPR Article 6 requires a lawful basis for each processing purpose. The purpose of analysing operational project information may not automatically justify using employee communications to infer morale, capacity or likelihood of leaving the organisation.

If legitimate interests is proposed, the client would need to complete the three-part Legitimate Interests Assessment:

1. **Purpose:** What concrete legitimate business interest is being pursued?
2. **Necessity:** Is analysing individual workplace communications necessary to achieve that purpose, or is there a less intrusive alternative?
3. **Balancing:** Do the interests or fundamental rights and freedoms of employees override the client's interest?

### Provisional assumption

**TBD — legal review.**

No lawful basis can be confirmed from the brief alone.

---

## Question 2 — Were employees informed that their communications would be analysed by AI?

### What we need to know

Were employees informed that workplace communications from Slack, email, meetings, standups or retrospectives could be processed by an AI system to identify delivery risks and derive signals concerning workload, morale, capacity or attrition?

We also need to know whether the client's privacy notice or employee information notice specifically covers this processing.

### Why it matters

This affects transparency obligations, purpose limitation and fairness under GDPR.

Employees may reasonably expect workplace communications to be used for ordinary project coordination without necessarily expecting those communications to be analysed by an AI system for individual-related risk signals.

The compatibility between the original purpose of the communications and the new AI-analysis purpose therefore needs to be established.

### Provisional assumption

**Cannot determine from brief.**

For audit purposes, we assume that the required transparency documentation has **not yet been demonstrated**.

---

## Question 3 — Can AI-generated risk findings affect employment decisions?

### What we need to know

When the system identifies an individual-related risk such as workload strain, morale concerns, performance-adjacent behaviour or attrition risk, can the resulting report influence:

* performance management,
* promotion,
* dismissal,
* disciplinary action,
* compensation,
* staffing decisions,
* HR investigations,
* or other decisions with significant effects on the individual?

We also need to understand exactly what the human reviewer can approve, reject or modify.

### Why it matters

This is directly relevant to GDPR Article 22 and to the assessment of the significance of profiling.

A human-in-the-loop mechanism is important, but the existence of a human reviewer does not by itself resolve every Article 22 question. The nature and significance of the downstream decision must be understood.

### Provisional assumption

The system is currently advisory and does not itself take automated employment action.

**Article 22 status: Cannot determine from brief.**

---

## Question 4 — Where do the vendors process and store personal data?

### What we need to know

For each external service, confirm:

* processing country/region,
* storage country/region,
* relevant subprocessors,
* applicable contractual data-processing terms,
* and international transfer mechanism where applicable.

The services identified are:

* OpenAI
* Pinecone
* Cohere
* Telegram
* Notion
* n8n
* Render

### Why it matters

If personal data leaves the EEA, GDPR Chapter V requirements apply.

The organisation must establish whether an adequacy decision, Standard Contractual Clauses (SCCs), or another valid transfer mechanism applies.

### Provisional assumption

**Cannot determine from brief.**

No international transfer mechanism should be assumed to exist until provider documentation and the actual production configuration are reviewed.

---

## Question 5 — What happens to the source data, embeddings and generated reports after processing?

### What we need to know

What are the retention periods and deletion mechanisms for:

* uploaded documents,
* extracted text,
* chunks,
* vector embeddings,
* metadata,
* retrieved passages,
* LLM inputs,
* AI-generated risk assessments,
* Telegram alerts,
* Notion reports,
* and logs?

We also need to know whether employees can exercise access or erasure rights across these different storage locations.

### Why it matters

GDPR requires purpose limitation and storage limitation and provides data subjects with rights including access and, where applicable, erasure.

A system with multiple copies and derived representations may create operational difficulties when responding to an access or deletion request.

### Provisional assumption

**Cannot determine from brief.**

The audit will treat retention and deletion controls as **unverified until supporting documentation is provided**.

---

# Phase 3 — Question Summary

| # | Clarification required                                                                  | GDPR relevance                                              | Provisional position            |
| - | --------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------- |
| 1 | Lawful basis for analysing employee communications and deriving individual risk signals | Article 6; legitimate interests assessment if applicable    | **TBD — legal review**          |
| 2 | Whether employees were informed about AI analysis and profiling                         | Transparency, fairness, purpose limitation                  | **Cannot determine from brief** |
| 3 | Whether AI-generated findings can influence employment decisions                        | Article 22; profiling; fairness                             | **Cannot determine from brief** |
| 4 | Vendor processing/storage locations and transfer mechanisms                             | GDPR Chapter V international transfers                      | **Cannot determine from brief** |
| 5 | Retention/deletion of source data, embeddings and outputs                               | Storage limitation; purpose limitation; data-subject rights | **Cannot determine from brief** |

## Phase 3 Conclusion

The data processing brief is sufficiently detailed to establish that the system processes personal data and involves significant AI-assisted profiling. However, several facts required for a final compliance assessment are not documented.

The most important unresolved questions concern **lawful basis, employee transparency, downstream employment decisions, international transfers, and retention/deletion controls**.

These questions will form the evidence gaps considered in Phase 4.

**Phase 3 status: Complete — proceed to Phase 4.**
# Phase 4 — Audit Report

## Section 1 — System Summary

The AI Delivery Risk Assistant analyses project-management and workplace communications to identify delivery risks. The system ingests sprint reports, ticket exports, standup transcripts, Slack threads, retrospective notes and stakeholder or executive emails, then uses embeddings, semantic retrieval, reranking and an LLM to identify and classify risks. The processing includes personal data because the source material contains names, roles and communications attributable to identifiable individuals, while the system also derives information concerning workload, capacity, morale and potential attrition. High-severity or contradictory findings are routed to a human reviewer before inclusion in the final leadership-facing report.

The current repository uses synthetic demo data, but the architecture is designed for production processing of real client workplace data.

---

# Section 2 — Data and Role Map

### Personal Data

The system processes:

* Names and professional roles.
* Workplace communications.
* Project and ticket information associated with individuals.
* Performance-adjacent information.
* Workload and capacity signals.
* Morale-related information.
* Attrition/retention signals.
* AI-generated risk assessments.
* Embeddings, metadata and retrieved passages that may remain linked to identifiable individuals.

No specific Article 9 category is confirmed by the brief. However, free-text processing creates a possibility that sensitive information could be present or inferred.

### Controller / Processor

The client organisation is provisionally the **controller** because it determines why employee/project information is analysed.

The development team is provisionally a **processor** if it operates the system on the client's documented instructions.

OpenAI, Pinecone, Cohere, Telegram, Notion, n8n and Render may also act as processors or service providers processing personal data. Their precise GDPR roles and contractual arrangements cannot be established from the brief alone.

### International Transfers

International transfer status **cannot be determined from the brief**. Processing/storage locations and applicable transfer mechanisms for the external providers have not been documented.

---

# Section 3 — Compliance Findings

## Finding 1 — Lawful Basis for AI-Based Employee Profiling

**Severity: Blocking**

**Description:** The system processes identifiable employee communications and derives individual-related signals including workload, morale and attrition risk. The brief does not identify a lawful basis for these processing activities. Without establishing an appropriate Article 6 lawful basis for each purpose, production processing cannot safely begin.

If legitimate interests is proposed, the client must complete the three-part LIA: legitimate purpose, necessity, and balancing against employees' rights and freedoms.

**Recommended action:** Document the lawful basis separately for operational risk analysis, individual-level profiling and leadership reporting. Complete an LIA where legitimate interests is proposed.

**Escalation needed?** **Yes — DPO / legal counsel.**

---

## Finding 2 — Purpose Limitation and Employee Transparency

**Severity: Significant**

**Description:** Workplace communications may originally have been collected for communication, project coordination or operational purposes. The system subsequently analyses them to infer workload, morale and potential attrition. The brief does not establish whether this secondary use is compatible with the original purpose or whether employees were adequately informed.

**Recommended action:** Document the original collection purposes and compatibility assessment. Update employee privacy information where required and ensure employees are informed about AI-assisted analysis and profiling.

**Escalation needed?** **Yes — DPO / legal counsel.**

---

## Finding 3 — DPIA Requirement

**Severity: Blocking**

**Description:** The system involves evaluation or scoring of individuals, innovative AI technology and potentially large-scale processing of workplace information. It also creates individual-level inferences that could affect how employees are perceived or managed. These factors create a strong likelihood that the processing presents a high risk to individuals' rights and freedoms and therefore requires a DPIA before production deployment.

**Recommended action:** Conduct and document a DPIA before processing live employee data. The DPIA should specifically assess profiling, employee expectations, discrimination/bias, sensitive inference, human oversight, data minimisation, retention, security and downstream employment decisions.

**Escalation needed?** **Yes — DPO / privacy counsel.**

---

## Finding 4 — International Transfers and Vendor Governance

**Severity: Significant**

**Description:** Multiple external services participate in the processing chain, including OpenAI, Pinecone, Cohere, Telegram, Notion, n8n and Render. The brief does not establish their processing locations, subprocessors or applicable international-transfer mechanisms.

**Recommended action:** Build a complete vendor and subprocessor register. Confirm processing regions and contractual roles, establish required DPAs, and document the appropriate GDPR Chapter V mechanism for every transfer outside the EEA.

**Escalation needed?** **Yes — DPO / procurement / legal counsel.**

---

## Finding 5 — Retention and Data Subject Rights

**Severity: Significant**

**Description:** The architecture creates multiple representations of the same information: source documents, extracted text, chunks, embeddings, metadata, retrieved passages and generated reports. The brief does not establish retention periods or a deletion workflow across these layers.

This may make access and erasure requests difficult to fulfil within GDPR requirements.

**Recommended action:** Create a data retention and deletion schedule covering every processing layer. Build a documented workflow for access, erasure and objection requests and test whether deletion can be propagated across relevant systems.

**Escalation needed?** **Yes — DPO / technical privacy lead.**

---

## Finding 6 — Article 22 and Employment Decision-Making

**Severity: Significant**

**Description:** The brief states that high-severity and contradictory findings are subject to human approval. This is a positive safeguard, but the brief does not establish whether AI-generated findings subsequently influence employment decisions such as performance management, promotion, disciplinary action or dismissal.

Therefore, the Article 22 position cannot be conclusively determined.

**Recommended action:** Document all downstream uses of AI-generated findings and establish whether any decisions have legal or similarly significant effects. Ensure that any applicable Article 22 safeguards and meaningful human intervention requirements are implemented.

**Escalation needed?** **Yes — DPO / employment-law counsel.**

---

## Finding 7 — Special-Category Data

**Severity: Significant**

**Description:** No specific Article 9 category is confirmed in the brief. However, the system processes unrestricted workplace free text and generates inferences concerning morale and workload. Depending on the source material and model behaviour, sensitive information could potentially be exposed or inferred.

**Recommended action:** Test the production data pipeline for Article 9 data and sensitive inference. Establish filtering/minimisation controls and determine whether an Article 9(2) condition would be required if such data is processed.

**Escalation needed?** **Yes — DPO / legal counsel if Article 9 data is identified.**

---

# Section 4 — Specific GDPR Obligations Checklist

| Obligation                                                         | Assessment                      | Note                                                                                    |
| ------------------------------------------------------------------ | ------------------------------- | --------------------------------------------------------------------------------------- |
| Lawful basis identified for each processing purpose                | **Gap identified**              | No Article 6 basis is established in the brief.                                         |
| Purpose limitation respected                                       | **Gap identified**              | Compatibility between original workplace communications and AI profiling is unresolved. |
| Data minimisation                                                  | **Cannot determine from brief** | Need to establish whether all ingested communications are necessary.                    |
| Controller/processor roles mapped and DPAs in place                | **Gap identified**              | Roles are provisional and DPA evidence is absent from the brief.                        |
| International transfer mechanism documented                        | **Gap identified**              | Vendor regions and Chapter V mechanisms are not documented.                             |
| DPIA conducted if required                                         | **Gap identified**              | No DPIA is identified; processing presents multiple high-risk indicators.               |
| Article 22 safeguard in place if automated decisions affect people | **Cannot determine from brief** | Human review exists, but downstream employment decisions are unclear.                   |
| Privacy notice covers AI processing                                | **Cannot determine from brief** | Employee transparency documentation is not provided.                                    |
| Data subject rights can be operationalised within deadlines        | **Cannot determine from brief** | No access/erasure workflow across all processing layers is documented.                  |

---

# Section 5 — Overall Recommendation

## Proceed with Conditions

The AI Delivery Risk Assistant should **not process live employee personal data until the principal GDPR gaps are addressed**. The system has a legitimate potential business use, and the existing human-review mechanism is a positive control, but the current brief does not establish the lawful basis, DPIA, employee transparency, vendor/transfer safeguards or rights-management processes required for a defensible production deployment.

The conditions for proceeding are:

1. Establish and document the lawful basis for each processing purpose, including an LIA if legitimate interests is proposed.
2. Complete a DPIA before processing live employee data.
3. Establish purpose limitation and employee transparency controls.
4. Complete the processor/DPA and international-transfer assessment.
5. Define retention and deletion controls across the complete data pipeline.
6. Confirm whether AI-generated findings can influence employment decisions and implement any applicable Article 22 safeguards.

---

# Section 6 — What This Report Is Not

This report is a **first-pass educational GDPR assessment based on the data processing brief supplied for the peer-audit exercise**.

It is **not**:

* a legal opinion;
* a formal DPIA;
* a GDPR certification;
* a substitute for advice from qualified legal counsel or a Data Protection Officer.

The client should obtain appropriate legal and privacy review before relying on this assessment for production compliance decisions.

---

## Phase 4 Conclusion

The independent audit identifies several material gaps that cannot be resolved from the teammate's brief alone. The highest-priority issues are lawful basis, DPIA, purpose limitation/transparency, vendor and international-transfer governance, and the treatment of AI-generated employee-related risk information.

**Phase 4 status: Complete — proceed to Phase 5 only after the independent audit is finalised.**
# Phase 5 — Debrief

## 5.1 Independent Audit vs Self-Audit

The independent audit was conducted using only the teammate's Data Processing Brief, in accordance with the lab instructions.

The auditor did not use the teammate's lawful-basis assessment, DPIA analysis or compliance findings when forming the independent assessment.

The purpose of the debrief is therefore to compare the independent assessment with the project owner's own GDPR assessment and identify where an external reviewer identified risks or ambiguities that may be less visible to the system builder.

---

## 5.2 Auditor Findings to Present

The independent audit identified the following principal issues:

1. **Lawful basis for employee-related AI analysis**

   * The system processes workplace communications and derives workload, morale and attrition-related signals.
   * The lawful basis for this processing is not established in the brief.

2. **Purpose limitation and transparency**

   * Workplace communications may originally have been collected for operational/project purposes.
   * Their subsequent use for AI-based profiling and employee-related risk analysis requires a compatibility and transparency assessment.

3. **DPIA requirement**

   * The system evaluates individuals and creates individual-related risk signals using AI.
   * A DPIA appears highly relevant and should be completed before production processing of real employee data.

4. **International transfers**

   * Multiple external vendors participate in the processing chain.
   * Processing locations and applicable transfer mechanisms are not documented.

5. **Processor and DPA governance**

   * The roles of the development team and external vendors require contractual confirmation.
   * Appropriate DPAs and subprocessor arrangements have not been demonstrated.

6. **Retention and data-subject rights**

   * The architecture creates multiple representations of personal data, including source documents, chunks, embeddings and reports.
   * Retention and deletion mechanisms across these layers are not documented.

7. **Article 22 / employment decisions**

   * Human review exists for high-severity and contradictory findings.
   * However, the downstream use of those findings for employment-related decisions remains unclear.

8. **Potential special-category data**

   * No Article 9 category is confirmed.
   * However, unrestricted workplace free text may potentially contain or reveal sensitive information.

---

## 5.3 Comparison Table

The following table is to be completed during the debrief with the project owner.

| Topic                      | Independent audit — Vincent                                                        | Self-audit — Akansha | Agreement / Divergence |
| -------------------------- | ---------------------------------------------------------------------------------- | -------------------- | ---------------------- |
| Lawful basis               | Not established from brief; requires assessment                                    | To be discussed      | Agreed                    |
| Purpose limitation         | Significant concern regarding reuse of workplace communications for AI profiling   | To be discussed      | Agreed                    |
| DPIA                       | Strongly indicated before production processing                                    | To be discussed      | Agreed                    |
| International transfers    | Cannot determine; vendor regions and mechanisms unresolved                         | To be discussed      | Agreed                    |
| DPA / processor governance | Roles and DPA status require verification                                          | To be discussed      | Agreed                    |
| Data minimisation          | Cannot determine from brief                                                        | To be discussed      | Agreed                    |
| Retention / deletion       | Cannot determine from brief                                                        | To be discussed      | Agreed                    |
| Article 22                 | Cannot determine; downstream employment use must be clarified                      | To be discussed      | No                    |
| Special-category data      | No confirmed Article 9 data, but potential sensitive inference requires assessment | To be discussed      | Agreed                    |
| Employee transparency      | Cannot determine from brief                                                        | To be discussed      | No                    |

---

## 5.4 What the Independent Review Surfaced

Even before the formal comparison with the self-audit, the independent review highlighted several areas that deserve particular attention.

### A. The distinction between operational risk and employee profiling

The system is presented as a delivery-risk assistant, but the source material and derived signals include information about identifiable employees.

The audit therefore treats the processing not merely as operational project analytics, but as processing that may involve profiling of individuals.

This distinction is important because the GDPR analysis changes when information about individual employees becomes part of the system's outputs.

### B. Human-in-the-loop does not automatically resolve every GDPR issue

The system contains a genuine human-review mechanism for high-severity and contradictory findings.

This is a positive control.

However, human review alone does not establish whether the processing is lawful, transparent, proportionate or compatible with the original purpose.

The downstream use of the AI-generated information must also be understood.

### C. Multiple representations of the same personal data

The audit identified a broader data lifecycle than the original source documents alone.

Personal information may exist as:

**Source document → extracted text → chunks → embeddings → retrieved evidence → LLM input → risk assessment → report → notification**

This creates additional questions around retention, deletion, access rights, security and processor governance.

### D. The vendor chain is larger than the application itself

The processing chain potentially includes OpenAI, Pinecone, Cohere, Telegram, Notion, n8n and Render.

An independent reviewer therefore needs to assess the complete processing chain rather than looking only at the application code.

---

## 5.5 Questions for the Debrief

During the meeting with Akansha, the following questions should be discussed:

1. What lawful basis did you select for the primary processing purpose? Legitimate interest assessment LIA
2. Did you treat the analysis of workload, morale and attrition as part of the same purpose or as separate processing purposes? yes
3. Did your DPIA assessment consider the individual-level profiling aspect of the system? Yes
4. Did you identify the same international-transfer uncertainty? yes
5. Did you identify the complete third-party processing chain? Yes
6. Did you consider embeddings and generated reports as part of the personal-data lifecycle? yes
7. Did you identify any potential Article 9/sensitive inference issue? yes
8. What retention and deletion mechanism did you identify? Define retention and deletion controls across the complete data pipeline.
9. What did the independent audit identify that was not obvious when reviewing the system from the builder's perspective? Retention & transfer EEA 

---

## 5.6 Debrief Outcome

### Areas of Agreement

To be completed during the debrief.

**Agreement 1:** Lawful bias ok

**Agreement 2:** Purpose bias ok

**Agreement 3:** DPIA ok

---

### Areas of Divergence

To be completed during the debrief.

No areas of divergence 

---

## 5.7 Joint Closing Note

The independent review demonstrates why GDPR self-assessment and peer review serve different purposes. A system builder naturally focuses on the intended function and technical safeguards of the system, whereas an external reviewer can more easily challenge assumptions about purpose, proportionality, downstream use and the complete data lifecycle.

The peer review also shows that AI systems can create GDPR risks not only through the original data they ingest, but through the inferences, embeddings, classifications and reports they generate from that data.

---

# Phase 5 Conclusion

The independent GDPR audit is complete.

The remaining activity is the structured debrief with the project owner, during which the independent findings should be compared with the owner's self-assessment.

No conclusions about the teammate's self-audit have been invented or assumed in this report.

**Phase 5 status: Independent audit complete — debrief comparison pending discussion with project owner.**
