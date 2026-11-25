# Lab 6 — Independent GDPR Peer Audit

**Project selected:** Armin's Case 1 — AI-assisted industrial equipment quotation preparation.  
**Status:** Classroom scenario draft. The source case is real course material; details marked **Exercise assumption** are invented to complete the exercise and are not verified facts about Armin, a real client, or a real vendor.

## Constructed data-processing brief

**Exercise assumptions:** The client is “NordWerk Trading GmbH,” a fictional German industrial equipment trader with about 120 employees. Fifteen commercial and technical staff use a cloud quotation assistant for about 2,000 customer inquiries per year. The product compares customer requirements with supplier quotations and approved previous transactions, selected emails, and expert notes. It flags differences and drafts technical and commercial proposal text with references to source documents. An employee checks every draft, verifies claims and price, and sends the final proposal. The system cannot send a proposal or choose a supplier on its own.

Inputs may include names, work email addresses, job titles, and business phone numbers of customer and supplier contacts, plus employee names and email signatures in selected records. The system should not receive health, financial-account, or other special-category personal data. The client is assumed to be the controller. “QuoteAssist Cloud GmbH” is a fictional processor hosting the service in Frankfurt, Germany; “ModelWorks Ireland Ltd” is a fictional EEA sub-processor for text generation. Assume a signed data-processing agreement, no access from outside the EEA, and no use of customer data to train general models. The service deletes source documents after processing; prompts and drafts are kept for 30 days, security logs for 12 months, and backups for up to 90 days. The client keeps approved business proposals under its own six-year records schedule. These periods and safeguards are scenario assumptions only.

## Audit report (target: no more than two pages)

### 1. System summary

The fictional client uses software to compare customer inquiries with supplier quotations and selected historical records. The system flags differences and drafts technical and commercial proposals with source references. A staff expert checks every draft, confirms the supplier and price, and sends it. It cannot send proposals or make decisions about individual people. This review assesses the exercise assumptions above, not a live system.

### 2. Data and role map

| Data / people | Purpose | Provisional role / issue |
|---|---|---|
| Business contact names, work details, signatures | Prepare quotations | Client is assumed controller; collect only needed details. |
| Employee names and work emails in selected notes | Support quote preparation | Restrict access to authorized staff. |
| Source files, prompts, drafts | Compare documents and draft proposals | QuoteAssist is assumed processor; ModelWorks is assumed sub-processor. |
| Final proposal | Send to a named business customer | Client controls the final record and retention. |

Hosting and model processing are assumed to be in Germany and Ireland (EEA), with no third-country access. No sensitive data or significant decisions about people are expected. Verify these assumptions in a real deployment.

### 3. Compliance findings

**Finding 1 — Lawful basis and purpose (Significant; document).** Legitimate interests are assumed for necessary business-contact data. Record the purpose, necessity, and balancing assessment. Limit old emails and transaction records to relevant quote work; do not use them to train a general model. Escalate to the privacy lead before live use.

**Finding 2 — Vendors and transfers (Appears met only under assumptions; verify).** The client, QuoteAssist, and ModelWorks are assumed to have controller, processor, and sub-processor roles, with a DPA and EEA processing. Confirm the real provider list, contract, hosting and support locations, and any transfer terms before go-live.

**Finding 3 — Minimisation, retention, and rights (Significant; test).** Emails and notes may contain unnecessary personal details. The exercise assumes 30-day prompt/draft retention, 12-month security logs, and backups up to 90 days. Redact irrelevant details, document each period, and test access, correction, objection, and deletion across files, prompts, drafts, logs, and backups.

**Finding 4 — Human review (Control appears strong; verify).** Every draft is assumed to receive expert review, with evidence checks and a stop rule. Keep approval mandatory, require source references, and record corrections. This safety control does not replace privacy safeguards.

**Finding 5 — Articles 9 and 22; DPIA (No trigger expected; record screening).** The scenario has ordinary business-contact data and no significant decisions about people. Record a DPIA screen and revisit if the data, scale, or purpose changes; prevent accidental sensitive data where possible.

**Overall recommendation: Proceed with conditions.** Verify the DPA, providers, EEA locations, retention, and rights workflow; document the legitimate-interests assessment; test redaction and human approval. If an assumption is false, reassess before using live data. This is not legal advice, a DPIA, or a compliance certification.

### 4. Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis | Assumed; document | Legitimate interests and balancing assessment. |
| Purpose limitation | Appears met with condition | No general-model training; restrict old records. |
| Data minimisation | Partial | Redact irrelevant details. |
| Roles and DPA | Assumed met | Verify actual contracts and providers. |
| International transfers | No third-country transfer assumed | Verify support and access locations. |
| DPIA screening | Record and revisit | Reassess if risk changes. |
| Article 22 | Not triggered in scenario | No significant decision about a person. |
| Privacy notice / rights | Confirm | Test the request process. |

## Clarifying questions to ask the builder

1. Do the actual customer and supplier files contain only business contact details, or can they include personal or sensitive information in free text and attachments?
2. Are the actual vendor, model provider, hosting region, support-access locations, and sub-processors the ones assumed here? Can any data leave the EEA?
3. Is customer content used to train or improve a model, and can that setting be disabled contractually and technically?
4. Are the assumed 30-day, 12-month, 90-day, and six-year retention periods accurate? Can a user’s data be located and deleted across prompts, drafts, logs, and backups?
5. Does a qualified employee review every proposal and stop it when evidence is missing, or can any output be sent automatically?

## Simulated debrief worksheet

**This is a written classroom simulation, not a record of a real conversation.**

- **Where the two reviews agree:** The system handles business-contact information; an expert should check each proposal; provider and retention details need evidence.
- **Possible disagreement:** The builder may consider the existing business relationship enough to justify use of contact details. The reviewer still asks the client to document the lawful basis and explain the processing.
- **New fact assumed for the exercise:** The builder confirms that staff select approved records; the tool does not ingest every company email or send proposals automatically.
- **Change after debrief:** Keep the “Proceed with conditions” recommendation. Add an explicit ban on general-model training and test the vendor's deletion and human-approval controls.
- **Joint closing note:** Self-audits can miss how much personal information is hidden in ordinary business documents and email signatures. An outside reviewer can ask for proof of vendor settings, retention, and human review instead of relying only on the builder's intentions.

## Lab proof

**Manual review workflow:** Read the Case 1 brief; list its data sources, people, purposes, outputs, vendors, and human checks; mark missing details; create clearly labeled exercise assumptions; assess each GDPR obligation against those assumptions; write findings and questions; then simulate the debrief without claiming it happened.

**Input from the course case:** Customer inquiries/specifications, supplier technical and price documents, approved transaction records, reviewed emails, and expert notes. The brief says an expert checks the proposal, confirms supplier and price, and stops sending if an important claim lacks reliable support or a discrepancy remains unresolved.

**Evidence produced:** Constructed data-processing brief, role map, five findings, GDPR checklist, five clarifying questions, and simulated debrief note.

**Limitation:** Vendor names, locations, contract status, data volumes, retention periods, and debrief details in this document are invented for the classroom exercise. They are not verified facts. Replace assumptions with the teammate's real brief or label them as scenario assumptions in the submitted repository.

**File map:** This `lab_proof.md` is the entry point and contains the brief, audit report, checklist, questions, and simulated debrief.
