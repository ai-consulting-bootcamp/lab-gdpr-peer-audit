# Independent GDPR Peer Audit — Intellectus

**Auditor:** Marija Kavaliauskaite
**Teammate:** Paola Hintze
**Project:** Intellectus
**Status:** Phases 1–4 complete from the permitted brief; Phase 5 pending.

## Evidence received

- Paola Hintze's Intellectus Kick-off data-processing brief, received 20 August 2026.
- Official lab instructions and rubric (method only).
- Separate architecture/data-flow diagram: **NOT RECEIVED**.

## Evidence limitations

The Intellectus brief is the sole substantive source. No teammate GDPR conclusions or previous EU AI Act audit were consulted. Exact legal entities, user location, scale, production hosting, n8n deployment, vendors, logs, retention, processing countries, security controls, privacy notice, contracts, and rights procedures are not established. For those matters: **Cannot determine from brief.**

Prospective private-document processing, hosted external AI, production case-file storage, and person-level scoring are not treated as active MVP functions.

## Phase 1 — Read and annotate

### Personal data identified

- Intake: organisation name, website, country and research window; plus names, professional roles, business contact information, and free-text narratives concerning identifiable people where entered.
- Public research: names, professional roles, quotations, public contact details, and statements written by or about employees, volunteers, leaders, or other identifiable people.
- Workflow metadata: URLs, search results, run identifiers and timestamps where linked to a consultant, user, or named person.
- Controlled repository material: fixtures and retained public-source evidence; the brief states that the public repository has no credentials or private client data.
- **FUTURE / NOT ACTIVE:** employee/volunteer records, donor/beneficiary information, case narratives, performance comments, inferred attributes, and private-document contents.

### Potential Article 9 data

The demonstrated MVP does not intentionally process a stated Article 9 category. However, free-text narratives and public-web statements could incidentally reveal or support inferences about health, disability, political or religious beliefs, ethnicity, trade-union membership, or other sensitive matters. **Cannot determine from brief** whether filtering, redaction, suppression, or an Article 9 condition exists.

The future private-document pilot could contain Article 9 data directly; it is **FUTURE / NOT ACTIVE** and requires a separate Article 6/9 assessment before activation.

### Unclear information and annotations

- Legal controller(s), processor(s), instructions and essential means: **Cannot determine from brief**.
- Lawful basis per purpose, Article 9 condition, privacy notice and LIA: **Cannot determine from brief**.
- Scale/frequency of public research and whether people are systematically monitored or profiled: **Cannot determine from brief**.
- Production n8n hosting, logs, vendors, countries, retention, deletion and rights-search capability: **Cannot determine from brief**.
- Selected file references exist in the interface, but document contents stay session-only; private upload is not active.

### Purpose-limitation flags

The stated purposes are organisational context, bounded cited public research, diagnostic drafting, consultant quality review, and limited security/troubleshooting records. Reusing public statements or contact details for person-level evaluation, outreach, ranking, or unrelated client purposes would require a compatibility/new-purpose assessment and is not demonstrated. “Limited” troubleshooting must be defined so full narratives or unnecessary personal data do not enter logs.

### Possible international transfers

No transfer is demonstrated. Production hosting, n8n deployment, vendor identities, processing/support/backup countries, and external AI are unestablished. Any restricted EEA transfer is therefore a verification item, not a fact.

### Demonstrated MVP versus prospective functionality

| Demonstrated MVP | FUTURE / NOT ACTIVE |
| --- | --- |
| React intake; JSON to n8n; child workflow; bounded public-web research; local retrieval; draft organisational diagnostic; consultant review; limited security/troubleshooting records | Private-document ingestion; secure server-side uploads; hosted external AI; production case-file storage; person-level scoring/ranking/flagging; consequential individual decisions; additional hosting/logging/support vendors |

### CFU 1 — Recognize

- **Personal data:** intake identities/contact details/narratives, public-web identities/quotations/contact details/statements, and linkable workflow metadata.
- **Potential Article 9:** incidental revelation or inference in MVP free text/public research; direct sensitive content is especially foreseeable in the future private-document pilot.
- **Possible EU-border flow:** possible through future or unverified production hosting, n8n, logs, support, storage, search, or AI providers; no actual destination is evidenced.

### CFU 2 — Probe

The three most consequential questions are: (1) who determines purposes and essential means; (2) what Article 6 basis applies to each purpose and how incidental Article 9 data is prevented/handled; and (3) where n8n, logs, storage and any subprocessors operate. Pending answers, the provisional positions are that roles are unresolved, legitimate interests is only a candidate requiring an LIA for bounded public research/security, and no international transfer may be asserted.

### CFU 3 — Map roles

The brief supports functional actors, not conclusive legal roles. The client/client representative appears likely to determine why its organisation is assessed; the consultant may act as an independent controller, joint controller, or processor depending on mandate and discretion; and the Intellectus team/n8n may process on instructions or determine essential means. **Cannot determine from brief.** A DPA is required wherever an entity processes personal data on a controller's behalf; joint-controller allocation is required if purposes and essential means are jointly determined.

### CFU 4 — Find the gaps

- **Lawful basis:** no purpose-by-purpose Article 6 record; candidate bases are assessed below, not confirmed.
- **Purpose limitation/minimisation:** bounded research and human review help, but intake fields, public-person evidence, metadata and logging necessity are not documented.
- **Processor/DPA governance:** legal roles, instructions, contracts and subprocessors are unestablished.
- **Transfers:** no transfer is evidenced; production countries/mechanisms are unestablished.
- **DPIA:** current MVP trigger cannot be concluded without scale/systematic-monitoring and deployment facts; future sensitive/person-level functions materially change the result.
- **Article 22:** does not appear applicable to the demonstrated MVP because output concerns organisations, does not make consequential individual decisions, and requires consultant review.
- **Transparency, retention/deletion and rights:** procedures and notices cannot be determined from the brief.

## Phase 2 — Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
| --- | --- | --- | --- | --- |
| Organisation/contact intake information: organisation, website, country, research window | Consultant/client representative | Context and bounded research | Cannot determine from brief | Normally no; context may link to an individual representative |
| Names, professional roles and business contact information | Intake; public web | Context, evidence and diagnostic draft | Cannot determine from brief | Normally no |
| Free-text narratives concerning identifiable people | Consultant/client representative | Describe challenge; support diagnosis/review | Cannot determine from brief | Possible incidental Article 9 revelation/inference |
| Public names, roles, quotations, contact details and statements | Public websites/search results | Bounded cited research; diagnostic draft/review | Cannot determine from brief | Possible incidental Article 9 revelation/inference |
| URLs, search results, run IDs and timestamps linked to people | Public web; workflow | Evidence provenance, security and troubleshooting | Cannot determine from brief | Normally no; context may reveal sensitive information |
| Controlled fixtures and retained public-source evidence | Public repository/public web | Controlled testing and evidentiary support | Cannot determine from brief | Cannot determine from brief; repository reportedly excludes private client data |
| **FUTURE / NOT ACTIVE:** employee/volunteer, donor/beneficiary, case and performance records; inferred attributes | Future client documents | Prospective private-document diagnostic | Cannot determine; architecture not established | Yes or likely possible, including listed Article 9 categories |

## Phase 2 — Role map

| Entity | Role supported by brief | Processing activity | DPA needed? |
| --- | --- | --- | --- |
| Client/client representative | Likely controller for its organisational diagnostic, but legal allocation cannot be concluded | Supplies intake and may supply personal narratives | If another entity processes on its behalf: **Yes**; actual contract cannot be determined |
| Consultant | Controller, joint controller or processor depending on mandate/discretion — **Cannot determine from brief** | Enters intake; reviews evidence, inferences and recommendations | Required if acting as processor; joint-controller arrangement if applicable |
| Intellectus application/team | Functional system operator/builder; legal role **Cannot determine from brief** | Receives intake; orchestrates research/retrieval; structures diagnostic | Required if processing on controller instructions; existence not asserted |
| n8n deployment | Workflow technology/provider role depends on deployment — **Cannot determine from brief** | Webhook, child workflow and orchestration | Required if a separate entity processes personal data for a controller |
| Public-web sources | Data sources, not shown to be processors | Supply public names, roles, quotations, contacts and statements | Not ordinarily a DPA relationship on evidence provided |
| Local retrieval corpus | Internal data source/component; operator unknown | Supplies local knowledge for retrieval | Depends on operator and whether it processes personal data on instructions |
| Prospective hosting/storage/external-AI/logging/support vendors | **FUTURE / UNESTABLISHED** processors/subprocessors if engaged | Prospective hosting, storage, inference, logs or support | Yes if processing personal data for a controller; vendor DPAs/subprocessor terms needed |

### International-transfer assessment

No EEA-to-third-country transfer can be identified from the brief. Before production, verify every hosting, n8n, search, logging, storage, backup, support and AI provider; contracting entity; processing/access country; onward subprocessor; and remote-support location. If a restricted transfer occurs, assess an Article 45 adequacy decision or an Article 46 safeguard (such as SCCs), conduct the necessary transfer-impact assessment, adopt supplementary technical/organisational measures where required, document onward transfers, and update transparency records. No mechanism is assumed to exist.

## Phase 3 — Clarifying questions log

| # | What we need to know | GDPR relevance | Provisional assumption |
| --- | --- | --- | --- |
| 1 | Which legal entities decide each purpose and essential means, what instructions govern the consultant/Intellectus team, and who contracts with the client? | Articles 24–28: controller, joint-controller and processor allocation; accountability; DPA responsibility. | Roles remain unresolved; do not represent a DPA or Article 26 arrangement as complete. |
| 2 | What Article 6 basis is proposed separately for intake/service delivery, public-person research, diagnostic drafting, and security/troubleshooting; if legitimate interests is used, what necessity/balancing evidence exists? | Articles 5(1)(b), 6, 13/14 and 21; purpose-specific basis, transparency, LIA and objection rights. | Contract may cover necessary service data about the contracting person; legitimate interests is only a candidate for bounded public research/security and needs an LIA; consent is not assumed. |
| 3 | Where are n8n, webhook data, logs, local corpus, backups and support operated; which vendors/subprocessors can access them; what countries and contractual safeguards apply? | Article 28, security/accountability, and Chapter V restricted-transfer compliance. | No vendor, DPA, country or international transfer is assumed. |
| 4 | What retention periods, deletion triggers, log minimisation, backup deletion and rights-search/export/correction/objection workflows apply to each data category? | Articles 5(1)(c)/(e), 12–22 and 30; storage limitation and operational rights. | No retention schedule or rights procedure is evidenced; treat them as production-readiness gaps. |
| 5 | At what scale/frequency is public research run, are individuals tracked across sources, and how are incidental Article 9 data/inferences filtered or suppressed? | Articles 9 and 35; minimisation, systematic monitoring, high-risk screening and potential DPIA triggers. | MVP is treated as bounded, organisation-level and human-reviewed, but scale and sensitive-data controls cannot be determined. |

## Phase 4 — Audit report

### A. System summary

Intellectus is a consultant-facing tool that accepts organisational context and sends it as JSON to an n8n workflow. The demonstrated MVP conducts bounded public-web research and local retrieval, structures evidence and preliminary findings, and returns an organisation-level diagnostic draft for consultant review. Personal data may appear in intake narratives, public evidence and linkable workflow metadata. Private documents, hosted external AI, production case-file storage and person-level consequential decisions are prospective, not active MVP functions.

### B. Data and role map summary

The MVP may process ordinary professional/contact data, statements and quotations, free-text information about identifiable people, and linkable technical metadata; incidental sensitive information may be revealed or inferred. The client, consultant, Intellectus team and n8n participate, but their legal controller/processor allocation cannot be concluded from the brief. No international transfer is demonstrated because production vendors, countries and deployment are unestablished.

### C. Compliance findings

#### Finding 1 — Lawfulness, fairness and purpose-specific accountability
**Severity:** Significant
**Description:** The stated diagnostic, research, review and security purposes have no recorded Article 6 basis in the brief. Contract might cover necessary service data about a contracting person, but not automatically third-party public data. Legitimate interests is only a candidate after an LIA. This is a documentation gap, not proof that no basis exists.
**Recommended action:** Record each purpose, data/source, Article 6 basis, necessity, notice route and retention; complete an LIA before using Article 6(1)(f).
**Escalation needed: Yes — controller and privacy counsel/DPO.**

#### Finding 2 — Role allocation and processor governance
**Severity:** Significant
**Description:** The legal entity deciding purposes/essential means and the status of the consultant, Intellectus team and n8n are unestablished. Article 28 or subprocessor terms are not evidenced; this is not treated as proof that a required DPA is missing.
**Recommended action:** Map decision rights and entities; execute Article 28 terms for instructed processing or an Article 26 arrangement for joint determination; register subprocessors.
**Escalation needed: Yes — contracting client/controller, Intellectus owner and privacy counsel.**

#### Finding 3 — Minimisation and incidental Article 9 handling
**Severity:** Significant
**Description:** Free text and public sources may expose unnecessary sensitive information. Filters, redaction, an Article 9 condition and a sensitive-inference policy are not evidenced. Future private documents are not active.
**Recommended action:** Constrain intake; suppress unnecessary person-level/sensitive content; document redaction and prohibit sensitive inference by default. Obtain approved Articles 6/9 grounds before intentional Article 9 processing.
**Escalation needed: Yes — product owner, controller and privacy counsel/DPO.**

#### Finding 4 — Retention, transparency and data-subject-rights operations
**Severity:** Significant
**Description:** Retention/deletion, Articles 13/14 notices and procedures to locate, correct, erase, restrict or export linked intake, evidence, metadata and logs are not established.
**Recommended action:** Create a retention schedule and deletion tests; map identifiers; publish direct/indirect collection notices; document rights-request ownership and deadlines.
**Escalation needed: Yes — controller, product/operations owner and privacy counsel/DPO.**

#### Finding 5 — Production vendors and international-transfer readiness
**Severity:** Significant
**Description:** No transfer is demonstrated, but production n8n hosting, storage, logging, support/AI vendors and countries are unestablished; deployment could create undocumented processor or transfer exposure.
**Recommended action:** Gate go-live on vendor/country diligence and DPAs. For restricted transfers, document adequacy or Article 46 safeguards, transfer risk and supplementary measures.
**Escalation needed: Yes — procurement/security, controller and privacy counsel/DPO.**

### D. GDPR obligations checklist

| Obligation | Assessment | Note |
| --- | --- | --- |
| Lawful basis identified for each processing purpose | Gap identified | Purposes are stated; Article 6 bases and any LIA are not. |
| Purpose limitation respected (no incompatible reuse) | Appears met | MVP purposes are bounded and organisation-level; future/person-level reuse requires fresh assessment. |
| Data minimisation (only necessary data collected) | Gap identified | Free text/public research may capture unnecessary person-level or sensitive content; controls not evidenced. |
| Controller/processor roles mapped and DPAs in place | Cannot determine from brief | Functional actors are named; legal allocation/contracts are not. |
| International transfer mechanism documented | Cannot determine from brief | No transfer is demonstrated; production countries/vendors are unestablished. |
| DPIA conducted if required | Cannot determine from brief | Scale/systematic-monitoring facts and DPIA screening are absent. |
| Article 22 safeguard in place if automated decisions affect people | Appears met | MVP makes organisation-level hypotheses, no consequential individual decisions, and requires consultant review; Article 22 does not appear engaged. |
| Privacy notice covers AI processing | Cannot determine from brief | Notice and final production AI architecture are not provided. |
| Data-subject rights can be operationalised within deadlines | Cannot determine from brief | Rights-search, correction, deletion, restriction and objection procedures are not evidenced. |

### E. Overall recommendation

**Proceed with conditions.** The bounded, organisation-focused, consultant-reviewed MVP supports no Blocking finding or Article 22 conclusion. Before production or scale-up, document lawful bases, settle roles/contracts, control sensitive data, operationalise notices/retention/rights, and complete vendor/country diligence. Keep private documents, hosted external AI, production case files and person-level features disabled until separately assessed.

### DPIA position

For the MVP, an Article 35 requirement **cannot be determined from the brief** because scale, systematic tracking, vulnerable persons, sensitive-data controls and deployment are unknown. Retain a DPIA screening before production. Future private records, Article 9 data, systematic monitoring or person-level scoring could require a DPIA before activation.

### Article 22 position

Article 22 does **not appear to apply** to the demonstrated MVP: it produces hypotheses and recommendations about an organisation, does not make hiring, eligibility, service-access, credit or other consequential individual decisions, and requires consultant review. Reassess if future person-level scoring, ranking, flagging or nominal human review is introduced.

### F. What this report is not

This report is not a legal opinion, not a DPIA, and not a certification of GDPR compliance. It is an independent educational audit based only on the supplied brief and should receive appropriate review by qualified privacy counsel or a DPO before reliance.

## Phase 5 — Debrief

**Status: PENDING — real debrief with teammate required.**

- Auditor presentation: `PENDING — real debrief with teammate required`
- Builder response: `PENDING — real debrief with teammate required`
- Comparison with Paola's self-audit: `PENDING — real debrief with teammate required`
- Lawful-basis comparison: `PENDING — real debrief with teammate required`
- DPIA comparison: `PENDING — real debrief with teammate required`
- Gap-list comparison: `PENDING — real debrief with teammate required`
- Joint closing note: `PENDING — real debrief with teammate required`

No response, agreement, disagreement, comparison or joint conclusion has been fabricated.

## Reinforce

**Status: PENDING — Phase 5 inputs required.** Paola's questions about Marija's project and Paola's independent report have not been reviewed. Documentation-gap reflection and any response to a disputed finding require the real debrief.

## Stretch remediation plan

### Priority finding

Finding 1 — purpose-specific lawful basis and accountability.

- **Artifact needed:** a controller-approved processing-purpose register plus completed LIA for any public-person research or security purpose relying on Article 6(1)(f). Include purpose, data/source, necessity, reasonable expectations, impact, safeguards, balancing outcome, notice route, objection handling and review date.
- **Owner:** accountable controller, supported by the Intellectus product owner and privacy counsel/DPO.
- **Timeline:** draft within 10 business days; legal/DPO review and approval before production personal-data processing or expansion.
- **Regulator-facing closure evidence:** approved dated register/LIA, version history, linked privacy-notice text, implemented objection/minimisation controls, training/decision record, and evidence that production configuration matches the documented purposes.

This plan does not assert that legitimate interests is the final lawful basis; it creates the evidence needed to test that proposal.
