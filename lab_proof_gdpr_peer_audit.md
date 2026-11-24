# GDPR peer audit — Green Warehouse Network

**Auditor:** Sabrina Urriola  
**Builder / teammate:** Fatma Meray 
**Assessment date:** 24 November 2026  
**Evidence reviewed for the independent assessment:** `GreenWarehouse_gdpr_brief.md`. The project README/architecture summary was used only to understand named components. Fatma’s conclusions are compared in Phase 5, after the independent findings.

## Phase 1: Read and annotate

- **Potential personal data:** customer ID/name or label, precise latitude/longitude, and annual demand; planner chat and clarification text; assignments, scenario history, maps, and report content linked to a customer. These are personal data only if they identify or can reasonably be linked to a natural person. The brief does not establish whether customer records refer only to companies or include sole traders/individuals.
- **Special-category data:** none is described or intended. Free-text chat could contain sensitive details accidentally; no control is evidenced.
- **Cross-border/vendor flows:** user text and selected scenario/results go to OpenAI; customer/site coordinates go to OpenRouteService during a one-time refresh. Regions, subprocessors, onward access, and transfer mechanisms are unspecified. Climatiq receives factor queries/metadata; personal data in that payload is not established.
- **Purpose question:** customer planning records may have been collected for ordinary logistics/customer management and are reused for optimization, LLM explanations, and reports. Original collection purposes are not described, so compatibility cannot be confirmed.
- **MVP boundary:** static project data, no live operational-system connection, planner review, and no automatic operational changes are described. The actual sample values, deployment host, and production scale were not verified.

## Phase 2: Personal data and role map

### Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Customer ID/name/label, coordinates, annual demand — potentially personal if linked to an individual/sole trader | Customer CSV or planner-added scenario | Assignment, capacity, cost/emissions, distance, maps, and failure analysis | OpenAI receives selected scenario/results; OpenRouteService receives coordinates at refresh. Location and transfer mechanism unknown. | No such data described; not intended |
| Planner chat/clarification text | Dashboard user | Scenario interpretation, clarification, explanations/report writing | Sent to OpenAI; processing location/retention unknown | Not intended; incidental sensitive text possible |
| Derived assignment, scenario history, metrics, maps, report | Local optimizer/session; derived from customer data | Display, comparison, explanation, optional downloadable report | Selected results/session events sent to OpenAI; report may be downloaded locally. Exact payload and destination unknown. | No such data described; linked output could relate to a person |
| Planner account/session/log data, if collected by host | Streamlit/hosting configuration not specified | Access, security, troubleshooting | Unknown; hosting and telemetry locations not given | Not established |

### Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Client / deploying logistics organization | No current client established; future client likely **controller** for its planning purpose and customer data | Supplies data and decides how planning outputs are used | If a vendor processes personal data on its instructions, Article 28 terms are required. No client is identified. |
| Builder / project team | Current MVP: likely controller for any personal data it selects and processes for its own course/testing purposes; future processor if operating solely on client instructions | Builds/runs application, selects prompts and outputs, manages local files | Future client DPA needed if acting as processor. None evidenced. |
| OpenAI | Role depends on terms and actual purposes; potentially processor for prompt content and separate controller for account/service data | Receives user text and selected scenario/results | Confirm applicable DPA, instructions, retention, subprocessors, and terms before any personal data is sent. |
| OpenRouteService | Role depends on terms and actual use; potential processor/independent controller | Receives coordinates for one-time distance refresh | Confirm data role and terms if coordinates identify people. No DPA evidenced. |
| Streamlit host / Climatiq | Host role unknown; Climatiq receives emissions queries/metadata, with no personal data established | Host may process sessions/logs; Climatiq supports factor refresh | Identify actual host and payloads; obtain Article 28 terms where a processor relationship exists. |

No third-country transfer is confirmed. For any personal-data transfer outside the EEA, identify destination/recipient and document an applicable adequacy decision or Article 46 safeguard (such as SCCs) and any required transfer assessment. The brief supplies no evidence of a mechanism. GDPR roles and DPA duties depend on actual purposes, instructions, vendor terms, and personal-data flows; they cannot be assigned from vendor names alone. ([GDPR Articles 28, 44–46](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/))

## Phase 3: Clarifying questions log

| Question | Why it matters | Provisional assumption |
|---|---|---|
| 1. Do any current or planned customer names, IDs, locations, or demand records identify a natural person, sole trader, or home business? | Establishes GDPR scope and data-subject impact under Articles 4 and 5. | The brief does not establish this; treat as potentially identifying until sample data are checked. |
| 2. What are the original collection purposes and notices for customer data, and what exact fields are sent to OpenAI/ORS? | Determines Article 6 basis, Articles 5(1)(b)/(c) purpose limitation/minimization, Articles 13/14 notice, and compatibility under Article 6(4). | No original purpose/notice or complete payload is evidenced; do not send identifiable data pending review. |
| 3. Who will control the production use, and what DPAs, regions, subprocessors, retention settings, and transfer safeguards apply to OpenAI, hosting, and ORS? | Determines controller/processor roles under Articles 4/28 and lawful international transfers under Chapter V. | Future client likely controller; vendor locations and terms remain unknown. |
| 4. At what scale and with what consequences will assignments be used; can a planner meaningfully override them? | Informs DPIA screening under Article 35 and whether Article 22 could apply to significant decisions about people. | Course MVP is limited, human-reviewed planning; no significant individual effect is described. |
| 5. What retention, access, privacy-notice, and rights-request processes exist for sessions, prompts, logs, reports, and downloads? | Tests storage limitation, security, Articles 12–14 and rights handling; supports accountability. | No end-to-end controls or schedules are evidenced in the brief. |

## Phase 4: Audit report

### Section 1: System summary

Green Warehouse Network helps logistics planners compare warehouse networks in Germany. It calculates primary/backup assignments and related distance, capacity, cost, emissions, and failure-scenario metrics from customer and warehouse inputs. A deterministic optimizer performs the calculations; an LLM interprets requests, explains results, and may write an HTML report. A planner reviews outputs, and the system does not automatically change operations.

### Section 2: Data and role map

Customer labels, IDs, precise locations, demand, chat, and linked outputs may be personal data if they identify a natural person; no Article 9 data is intended. The future client is likely controller; the project team likely controls its prototype and could be a processor in a client deployment. OpenAI receives text/results and ORS receives refresh coordinates; vendor roles, locations, and transfer safeguards are unknown. No third-country personal-data transfer is confirmed.

### Section 3: Compliance findings

> **Finding 1 — Lawful basis, purpose limitation, and minimization**  
> **Severity:** Significant before any live personal-data use  
> **Description:** Identifiability, source purposes, necessity of names/precise coordinates, and the controller’s Article 6 basis are unconfirmed. Chat/results go to OpenAI and coordinates to ORS. No incompatible reuse is proven, but compatibility and minimization are unverified.  
> **Recommended action:** Validate fields and source purposes, minimize/pseudonymize inputs, and document the Article 6 basis and any Article 6(4) compatibility assessment before live use. Article 6(1)(f) is only a candidate after a complete LIA.  
> **Escalation needed?** Yes — controller privacy lead/DPO or counsel before a live personal-data pilot.

> **Finding 2 — Processor terms and international transfers**  
> **Severity:** Significant before vendors receive personal data  
> **Description:** Vendor roles, locations, retention, subprocessors, DPAs, and Chapter V safeguards are not established for potentially identifying payloads. This is an evidence gap; an unlawful transfer is not confirmed.  
> **Recommended action:** Map payloads and entities, establish Article 28 terms where applicable, and document a valid transfer mechanism/assessment if data leaves the EEA.  
> **Escalation needed?** Yes — procurement/privacy counsel and vendor owners.

> **Finding 3 — DPIA screening and possible effects on people**  
> **Severity:** Minor for the described MVP; reassess before deployment  
> **Description:** No screening/DPIA record is supplied. Large-scale processing, profiling, or significant individual decisions are not established; data combination and LLM use alone do not prove a DPIA is required.  
> **Recommended action:** Document Article 35 screening for actual data/scale and national rules; complete a DPIA if processing is likely to create high risk. Reassess Article 22 if outputs significantly affect people.  
> **Escalation needed?** Yes — controller privacy lead/DPO; consult counsel if high risk or Article 22 use is identified.

> **Finding 4 — Transparency, retention, and rights operations**  
> **Severity:** Significant before live use; current status cannot be determined  
> **Description:** No notice, retention schedule, access controls, or rights-request workflow is evidenced for chats, prompts, logs, outputs, and downloads. Data discovery/deletion across these copies may be difficult.  
> **Recommended action:** Define applicable Article 13/14 notices, retention/deletion, least-privilege access, and a rights process covering local files and vendors.  
> **Escalation needed?** Yes — controller privacy lead/DPO; technical owner for implementation.

### Section 4: Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each purpose | **Cannot determine from brief** | No basis is selected; assess each personal-data purpose before live use. |
| Purpose limitation respected | **Cannot determine from brief** | Original collection purpose/notices are unknown; AI/report reuse needs assessment. |
| Data minimisation | **Cannot determine from brief** | Names, precise coordinates, and free text may exceed what is needed; test minimized payloads. |
| Controller/processor roles mapped and DPAs in place | **Gap identified** | Likely roles can be hypothesized, but actual deployment, vendor roles, and DPAs are not evidenced. |
| International transfer mechanism documented | **Cannot determine from brief** | No transfer confirmed; vendor locations and safeguards are unknown. |
| DPIA conducted if required | **Cannot determine from brief** | No screening/DPIA evidence; current brief alone does not show that a DPIA is mandatory. |
| Article 22 safeguard if automated decisions affect people | **Appears met** | No significant decision about a person is described; human planner review is stated. Reassess if use changes. |
| Privacy notice covers AI processing | **Cannot determine from brief** | No privacy notice is described; Article 13/14 applicability depends on personal data and source. |
| Data-subject rights can be operationalised within deadlines | **Cannot determine from brief** | No data discovery, correction, erasure, objection, or response workflow is evidenced. |

### Section 5: Overall recommendation

**Proceed with conditions.** The course MVP has no live-system connection, and the brief does not establish that current data identifies people. Before live personal-data use, validate fields and purposes, document the controller and lawful basis, minimize payloads, establish applicable vendor/transfer terms, and implement notice, retention, and rights processes. Record DPIA screening and complete a DPIA if the deployment is likely to result in high risk.

### Section 6: What this report is not

This is a first-pass peer review of the supplied brief, not a legal opinion, DPIA, or certification of compliance. Actual data, contracts, vendor settings, and deployment were not inspected. Obtain qualified privacy/legal review before relying on this assessment or processing live personal data.

**Sources:** [GDPR, Regulation (EU) 2016/679 — EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/); [EDPB: Data protection impact assessment](https://www.edpb.europa.eu/topics/accountability-and-compliance-tools/data-protection-impact-assessment_en).

## Phase 5: Debrief conversation 

1. **Auditor presents:** The key unresolved issue is whether customer records and locations identify natural persons. If they do, the controller needs a purpose-specific lawful basis, minimization and compatibility analysis, vendor/transfer review, and workable notice/rights/retention controls. The brief does not establish a DPIA trigger or Article 22 decision affecting a person, but the controller should document screening and revisit it for production scale or changed use.
2. **Builder responds:** “The project is a course MVP using static planning files, not connected to live logistics systems. We need to verify whether any sample names or locations identify individuals. The LLM receives user text and selected results, and ORS receives coordinates only during a distance refresh; we have not established vendor retention, locations, or transfer terms. No production DPA, approved lawful-basis decision, or DPIA is evidenced in the brief.”
3. **Compare lawful bases:** Fatma’s self-audit treated Article 6(1)(f) as a possible basis for planning if personal data is used, but left the LIA and final controller decision unresolved. The auditor’s procurement-risk agent audit also treated Article 6(1)(f) as a candidate for procurement analysis, while flagging public-source reuse and impacts on sole traders for legal review. The candidate basis is similar; the purpose, data subjects, necessity, expectations, and balancing analysis are different. Neither assessment should present legitimate interests as approved without the controller’s completed LIA.
4. **Compare DPIA conclusions:** Both the self-audit and peer review find that the brief alone does not demonstrate two clearly applicable high-risk criteria or establish a mandatory DPIA for the course MVP. Both call for a documented screen and production re-assessment. Scale, whether records identify people, and whether assignments materially affect an individual could change the result.
5. **Compare gap lists:** The audits align on uncertain identifiability, vendor/transfer facts, no evidenced lawful-basis decision, and missing retention/rights evidence. The external review emphasizes that the same location and assignment fields can become personal data in combination and separates “not evidenced” from proof of an unlawful transfer. The builder’s own audit has more detail about the actual intended workflow; independent review makes assumptions and missing evidence easier to spot.
6. **Joint closing note:** “GDPR self-assessment is especially vulnerable to assumptions about whether business records are personal data and whether a vendor receives only operational information. An outside reviewer traces identifiers through combined datasets, prompts, logs, and reports and asks for proof of purpose, lawful basis, and deletion. The comparison shows why data-flow evidence and source-purpose history matter as much as the model description.”

### Reinforce reflection 

A question for the auditor’s procurement-risk agent is: “Do supplier research prompts or report outputs contain identifiable supplier contacts, and can the team delete them from run files and published test fixtures?” The auditor’s existing assessment identifies possible names/contact details in public search results, a historical run record and test fixtures, plus unknown vendor retention and storage locations. Those points are documented as risks, but actual data-subject identifiability and deletion from repository history remain unresolved; that indicates a need for field-level payload and retention evidence.

For an initial disagreement, the builder questions whether customer coordinates are personal data because the tool plans business networks. After discussion, the builder accepts the **conditional** finding: coordinates are not automatically personal data, but can identify a sole trader or a home-based business when linked to a name, customer ID, or other accessible information. No evidence shows that Fatma’s current sample actually identifies a person, so the point remains a validation question rather than a claim that current data is personal.

## Stretch: Remediation plan — lawful basis and vendor flow validation

**Finding:** Significant — clarify whether personal data is sent to OpenAI/ORS and establish the legal/contractual basis before live use.

| Item | Plan |
|---|---|
| Deliverable | Controller-approved data-flow and purpose record; minimized payload specification; Article 6 decision and, if relying on Article 6(1)(f), completed LIA; vendor role/DPA and Chapter V transfer review where applicable. |
| Owner | Future controller’s privacy lead/DPO and procurement/legal counsel; project technical lead supplies payload maps and implements minimization. |
| Timeline | 2–3 weeks before any live personal-data pilot; pause those flows until the required decisions/terms are complete. |
| Closure evidence | Sample redacted payloads, approved flow diagram and purpose/basis record, signed applicable DPA, documented region/subprocessor/transfer assessment, and tests showing only necessary fields are sent. |

