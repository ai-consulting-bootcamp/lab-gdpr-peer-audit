# GDPR Peer Audit Proof

**Auditee:** Ayhan Demir  
**Project:** Fix My Process (Kleinanzeigen Ironhack Project 3)  
**Evidence reviewed:** `FixMyProcess_data_processing_brief_AyhanDemir.md`  
**Exchange scope:** Teammate's data processing brief only

## Phase 1: Read and annotate

- **Personal data:** Free-text problem descriptions; names and customer details; department, tools, frequency; chat messages; feedback; IP addresses and request metadata; timestamps and case metadata; Board decision metadata; and error-message fragments.
- **Potential special-category data:** Not explicitly identified. Special-category data may be inferred or voluntarily disclosed in free text, for example an employee's health-related reason or a colleague's or customer's sensitive information. A worker's opinions are not necessarily special-category data, but no content review or redaction control is described.
- **EU-border data flows:** OpenAI (US), Cohere (US infrastructure), Pinecone (US), Tavily (US), OpenAlex (US), Airtable (US), Notion (US), and Slack (US). Render has Frankfurt as its only EU region, but the configured region is undocumented. n8n, GNews, and the region of any n8n or GNews processing are undocumented.
- **Potential purpose-compatibility issues:** Using problem text for AI research/reporting, policy flags, quality scoring, Board review, error diagnosis, internal summaries, and planned department summaries may extend beyond the employee's apparent purpose of obtaining a fix report.
- **Clarifications needed:** Lawful bases, internal AI/privacy notice, retention, regional configuration, DPA status, employee-access controls, record of decisions, and actual use of free-text data for employee evaluation.

## Phase 2: Personal data and role map

### Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Free-text problem description; possible names, customer details, colleague details | Employee | Fix report, research, policy flag, summaries, quality scoring, error diagnosis, Board review | Yes, sent to US-based vendors | No confirmed special category; may be inferred/disclosed |
| Department, tools and frequency | Employee | Use-case reporting, report generation | Yes, sent to AI and workflow services | No |
| Chat messages (up to 10) | Employee | Session context | Yes, sent to OpenAI | Unknown; may include sensitive information |
| Feedback and attitude to tools | Employee | Adoption measurement | Yes, through Airtable/Notion and possibly Slack | No confirmed special category |
| Inferred reports, flags, ratings, confidence and impact | AI system | Policy flagging, report delivery, Board/quality workflow | Yes, with vendor and case/database processing | Could repeat special-category information from source text |
| Case metadata and timestamps | System | Status lookup, reporting, error monitoring | Yes | No |
| Board decision and Slack identity of Board member | Board member / Slack | Review and pipeline status | Yes | No |
| Error records with input fragments | System | Troubleshooting | Yes | Unknown; fragments may contain personal or sensitive data |
| IP address and request metadata | Render and hosting/workflow logs | Hosting, security, diagnostics | EU or US status not documented | No confirmed special category |

### Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Kleinanzeigen / relevant client organization | Likely controller | Determines employee-facing purpose and receives reports and summaries | DPA is needed with its processors |
| Builder / AI enablement team | Likely controller or joint-controller participant; role must be confirmed | Builds and operates system, supplies internal documents, receives use-case summaries | DPA required for processor relationships if contracted to process on behalf of the controller |
| n8n hosted by Ironhack | Processor or processor sub-contractor, role to be confirmed | Orchestrates every step and retains execution history | Yes |
| OpenAI | Processor/AI provider | Research, report generation and quality check | Yes |
| Cohere | Processor/service provider | Ranks search results | Yes |
| Pinecone | Processor/service provider | Hosts embeddings and internal document passages | Yes |
| Tavily | Processor/service provider | Web search | Yes |
| GNews | Processor/service provider | News search | Yes |
| OpenAlex | Processor/service provider | Research-paper search | Yes |
| Airtable | Processor/service provider | Stores case and error records | Yes |
| Notion | Processor/service provider | Stores use-case summaries | Yes |
| Slack | Processor/service provider | Board notices and operational alerts | Yes |
| Render | Processor/service provider | Hosts web page and logs requests | Yes |

**Transfer mechanism:** The brief provides no evidence of adequacy decisions, Standard Contractual Clauses, or another Article 46 mechanism for any non-EU provider. It does not establish whether all are covered by a valid Article 45 transfer mechanism or documented supplementary measures.

## Phase 3: Clarifying questions log

| # | Question | Why it matters | Provisional assumption |
|---|---|---|---|
| 1 | What lawful basis and purpose are specified for each processing activity, and has a documented legitimate-interest assessment or other basis been completed where relied on? | Articles 5(1)(a)-(b) and 6 require a lawful basis and purpose definition for every processing purpose. | Assume no lawful basis is documented and treat the brief as insufficient to establish Article 6 compliance. |
| 2 | Has a DPIA been conducted, and were the contents, intended uses and foreseeable risks of the employee text, AI outputs and possible employee evaluation assessed? | Article 35 may apply due to systematic/large-scale AI profiling or evaluation-like use; the employee-evaluation risk makes this especially unclear. | Assume a DPIA is required and has not been conducted. |
| 3 | Which entities are controller(s), processor(s) and sub-processors, and are DPAs available for n8n and every listed vendor? | Article 28 requires a compliant contract for processor relationships. | Assume no valid DPAs are in place, as the brief expressly states. |
| 4 | What regions hold the data and what Article 45 or 46 transfer mechanism applies to every non-EU processor? | Chapter V governs transfers; storage and subprocessors must be mapped, with transfer tools and supplementary measures documented. | Assume Chapter V safeguards are absent pending evidence. |
| 5 | What retention and deletion schedule applies, and can case records, Slack data, logs, embeddings and generated reports be deleted and searched for individual-rights requests? | Storage limitation and rights obligations under Articles 5(1)(e), 15-22, and 17-22 require clear periods and operational procedures. | Assume no retention limits or rights workflows are documented. |

## Phase 4: Audit report

### Section 1: System summary

Fix My Process is an internal employee workflow assistant that collects free-text task descriptions and context, sends it to several AI and search providers, and generates a report and compliance flags. It stores case records and use-case summaries, posts red cases to a governance Board, and records feedback and technical logs. The brief shows personal data can be entered voluntarily, may include names or customer details, and can be retained across multiple US-based services. Because the system may identify employees and their tool preferences in small departments, downstream reporting could indirectly affect teams or individuals. The brief also indicates no retention schedule or processor agreements are in place.

### Section 2: Data and role map

The relevant data includes employee text, workplace context, chat history, feedback, inferred AI fields, case metadata, Board decisions and technical logs. The organization is provisionally the controller, while the builder, n8n and service vendors appear to support processing; the exact role split is not documented. Free text is the primary identification and special-category-data risk because content controls are limited to an on-screen warning.

Personal data or data derived from personal data is sent to OpenAI, Cohere, Pinecone, Tavily, OpenAlex, Airtable, Notion, Slack and Render, and likely n8n and GNews. The brief does not document adequacy decisions or Article 46 transfer tools. It expressly says no DPA exists and no retention period is configured.

### Section 3: Compliance findings

**Finding 1 — Article 28 processor contracts**  
**Severity:** Blocking  
**Description:** The brief expressly states that no DPAs are in place while n8n and numerous vendors process personal data. This includes data that is stored or sent to US vendors.  
**Recommended action:** Pause personal-data processing with these processors until each relationship is identified and a GDPR Article 28-compliant DPA is signed; document subprocessors and deletion requirements.  
**Escalation needed?** Yes — to the controller's DPO/legal team and each service owner/procurement lead.

**Finding 2 — Lawful basis and purpose limitation**  
**Severity:** Blocking  
**Description:** The brief lists many purposes and uses but does not identify the lawful basis for each. It also shows possible expansion from obtaining a fix report into quality scoring, adoption feedback, Board review, department summaries and employee evaluation.  
**Recommended action:** Document an Article 6 basis for each purpose, conduct an Article 5(1)(b) purpose test, and document or abandon incompatible reuse. Where employee consent is not genuine or freely given in an employment context, consider whether legitimate interests are appropriate and complete a documented balancing assessment.  
**Escalation needed?** Yes — to the DPO/legal team and system owner.

**Finding 3 — DPIA**  
**Severity:** Blocking  
**Description:** The system uses AI-generated outputs, systematic free-text processing and possible evaluation-like employee context. The brief does not evidence a DPIA or EDPB-style threshold assessment.  
**Recommended action:** Conduct a DPIA before processing continues, including data minimisation, sensitive-data controls, vendor risks, employee impact and governance.  
**Escalation needed?** Yes — to the DPO and AI governance/legal team.

**Finding 4 — International transfers**  
**Severity:** Significant  
**Description:** The brief identifies US processing and AWS US hosting, with additional infrastructure/region gaps. No transfer mechanism or supplementary-measure documentation is provided.  
**Recommended action:** Complete a transfer map, determine each transfer tool, add transfer clauses and assess third-country access where required; select EU/EEA processing regions where feasible.  
**Escalation needed?** Yes — to the DPO/legal team and procurement.

**Finding 5 — Article 22 and employee impact safeguards**  
**Severity:** Significant  
**Description:** Reports and flags assist with governance and tool decisions. Board decisions affect work processes and, according to the brief, may lead to individual or team evaluation if repurposed. The report is not presented as an automated decision solely affecting an employee, but safeguards and human-review boundaries are not documented.  
**Recommended action:** Document whether Article 22 applies, define human review, prohibit employment scoring until separately assessed, add meaningful explanations and accessible contest/challenge routes, and prevent department summaries from inferring individual performance.  
**Escalation needed?** Yes — to the DPO and HR/employee representatives if people are evaluated.

**Finding 6 — Retention and rights operations**  
**Severity:** Significant  
**Description:** The brief says there is no retention period and data remains in Airtable, Notion and Slack until deletion. Rights-search and deletion processes across vendors and logs are not described.  
**Recommended action:** Define retention periods by record type, implement deletion from databases, logs and generated records, and document procedures for access, erasure and objection requests.  
**Escalation needed?** Yes — to the system owner, DPO and each data store owner.

**Finding 7 — Data minimisation and special-category controls**  
**Severity:** Significant  
**Description:** Free text may include names and sensitive details, the only control described is an on-screen warning, and error logs retain input fragments.  
**Recommended action:** Replace the warning-only control with minimised prompts, optional-field review, redaction or masking, stricter log handling, and technical controls preventing unnecessary sensitive-data collection and disclosure.  
**Escalation needed?** Yes — to security, engineering and the DPO.

### Section 4: Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | Cannot determine from brief | No Article 6 basis or balancing assessment is documented. |
| Purpose limitation respected (no incompatible reuse) | Gap identified | Quality scoring, summaries, Board review and possible employee evaluation need a purpose compatibility assessment. |
| Data minimisation (only necessary data collected) | Gap identified | Free text and input fragments may be excessive or sensitive; the brief documents only an on-screen warning. |
| Controller/processor roles mapped and DPAs in place | Gap identified | Roles are only provisional and no DPAs are described. |
| International transfer mechanism documented | Gap identified | US and AWS US processing are identified; required transfer instruments are not evidenced. |
| DPIA conducted if required | Cannot determine from brief | AI/employee-impact characteristics suggest it may be required, but no DPIA evidence is provided. |
| Article 22 safeguard in place if automated decisions affect people | Cannot determine from brief | Outputs assist tool/process decisions and Board decisions; no Article 22 assessment or safeguards are described. |
| Privacy notice covers AI processing | Cannot determine from brief | No privacy notice is described. |
| Data subject rights can be operationalised within deadlines | Gap identified | No retention or deletion workflow is identified; this affects rights response and erasure. |

### Section 5: Overall recommendation

**Proceed with conditions — but personal-data processing should not expand or go live until Blocking findings are resolved.** The system can continue only after the organization confirms lawful bases and purposes, conducts and closes out an appropriate DPIA, and executes processor agreements. International-transfer documentation and Article 22/employee-impact safeguards must also be assessed. Until these conditions are met, the appropriate position is effectively **Do not proceed** for processing real personal data.

### Section 6: What this report is not

This report is not a legal opinion, not a DPIA, and not a certification of compliance. The client should obtain DPO and legal review before relying on this assessment.

## Phase 5: Debrief

The structured debrief has not been recorded in the evidence currently available. The following items must be completed together with Ayhan Demir and inserted here rather than inferred:

1. **Auditor presents:** Report walkthrough without interruption.
2. **Builder responds:** Five-minute context and clarification period.
3. **Lawful basis:** Compare the primary-purpose lawful bases selected by both audits and discuss the stronger assessment.
4. **DPIA:** Compare DPIA conclusions and apply the EDPB criteria until agreement or a documented ambiguity is reached.
5. **Gap comparison:** Compare self-audit and external-audit misses.
6. **Joint closing note:** Record 2-3 sentences on what the debrief reveals about GDPR self-assessment and which own-work gaps are hardest to see.

**Status:** Pending — no lawful-basis selections, DPIA conclusion, or joint closing note were supplied.

