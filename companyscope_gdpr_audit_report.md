# CompanyScope GDPR audit report

**Audited teammate:** Sean Langsdorf  
**Project:** CompanyScope  
**Evidence reviewed:** `companyscope_system_brief.md` only  
**Audit date:** 17 November 2026

## 1. System summary

CompanyScope produces a first research briefing about a German-registered company from an entered company name and optional register identifier. It checks OpenRegister, searches a limited set of public web results through Tavily, and sends selected evidence and research-method notes to an OpenAI model for a Markdown report and browser results page. The brief says the system is not intended to decide hiring, credit, client acceptance or transaction approval, and expects a professional to verify sources and correct or omit unsupported claims. The workflow nevertheless may process names, professional contact details and other information about identifiable people, and the search itself may reveal the company a person or firm is researching.

## 2. Data and role map

The main company-profile fields are usually information about a legal entity, but names, addresses and business-purpose fields can become personal data when they identify a sole trader or another natural person. Public web evidence may contain personal data and could contain or permit inferences about special-category data; the brief does not describe a filter. Query data, authentication/log data, prompts and saved reports may also be personal data.

The deploying law firm or research team is the likely controller for its purposes. Sean is only a builder if he does not handle live data; if he hosts or accesses it for the client, he is likely a processor. OpenRegister, Tavily, OpenAI and n8n/hosting providers are external data-flow participants whose exact role, DPA status, retention and subprocessor chain are not established. Their hosting locations are also not given, so an international transfer cannot be cleared from this brief.

## 3. Compliance findings

### Finding 1 — Lawful basis and special-category control

**Severity:** Blocking for live personal-data processing  
**Description:** The brief identifies likely personal data but does not identify a lawful basis for research, query logging, vendor prompts, report storage or sharing. Public availability is not, by itself, a lawful basis. If web content includes special-category data, an Article 9 condition and stronger safeguards are also required.  
**Recommended action:** Build a purpose/data-field matrix; select and document an Article 6 basis for each purpose; if relying on legitimate interests, complete a necessity and balancing assessment; exclude or redact special-category data unless a documented Article 9 condition and safeguards apply.  
**Escalation needed?** Yes — controller, DPO or privacy lead and legal counsel.

### Finding 2 — Vendor roles, DPAs and international transfers

**Severity:** Blocking for any vendor flow that handles personal data without the required safeguards  
**Description:** The workflow names OpenRegister, Tavily, OpenAI and n8n, but does not show whether each is a processor, what data each receives, where it is processed, or whether a DPA and transfer mechanism are in place. If personal data is transferred outside the EEA, an adequacy decision or appropriate Article 46 safeguard is needed; current SCCs may be relevant, but they do not replace a destination and access-risk assessment.  
**Recommended action:** Create a vendor/data-flow register; verify roles, DPAs, subprocessors, retention and model-use settings; minimize prompts; record hosting countries; and complete SCC/TIA and supplementary-measure documentation where required.  
**Escalation needed?** Yes — controller, procurement, DPO and legal counsel.

### Finding 3 — DPIA screening and AI governance

**Severity:** Significant pending screening; blocking if a required DPIA is not completed  
**Description:** The stated use does not describe an Article 22 automated decision because the report is not intended to decide matters with legal or similarly significant effects. That does not settle Article 35. The system uses a novel AI workflow, combines registry and web datasets, and may produce person-level analytical observations. The brief provides no documented DPIA screening or DPIA.  
**Recommended action:** Complete and retain a DPIA screening now. Complete a full DPIA before production if the scale, recurring monitoring, profiling, sensitive data, combined datasets or other facts make the processing likely high risk. Enforce human review, prohibit decision use, and log corrections rather than relying on an advisory warning.  
**Escalation needed?** Yes — DPO/privacy lead; consult legal counsel if the screening is borderline.

### Finding 4 — Purpose limitation, transparency and data-subject rights

**Severity:** Significant  
**Description:** Collecting public web material, combining it with registry data, generating inferences and sharing a report may not be compatible with the original publication context. The brief does not evidence an Article 13/14 privacy notice covering AI processing, sources, recipients, transfers, retention and rights, or a process for access, correction, deletion and objection.  
**Recommended action:** Define the research purpose and permitted recipients; perform and record a compatibility analysis; publish an AI-aware notice for third-party data; provide a rights channel with ownership and deadlines; and add correction, objection and deletion handling before reports are shared outside controlled review.  
**Escalation needed?** Yes — controller/privacy lead; legal review of the notice and rights exceptions.

### Finding 5 — Accuracy, minimisation and retention

**Severity:** Significant  
**Description:** The ambiguous-match stop, source-reference checks and expected professional review are positive controls. They do not prove that a source supports a claim, that a model inference is accurate, that irrelevant person-level data is excluded, or that reports and prompts are deleted when no longer needed. A false claim about a named person could cause material harm.  
**Recommended action:** Limit collection to fields needed for the defined purpose; redact irrelevant people; require source-to-claim review and an approval gate before release; label inferences; provide correction/versioning; and set retention and deletion periods for prompts, logs and reports.  
**Escalation needed?** Yes — product owner and controller/privacy lead; legal review for high-impact person-level claims.

## 4. Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | **Gap identified** | No basis is stated for research, queries, prompts, storage or sharing. |
| Purpose limitation respected (no incompatible reuse) | **Gap identified** | Compatibility of public-source collection, AI inference and report sharing is not demonstrated. |
| Data minimisation (only necessary data collected) | **Cannot determine from brief** | The brief says the web search is limited, but gives no field/filter or person-level exclusion rules. |
| Controller/processor roles mapped and DPAs in place | **Gap identified** | Roles and contracts for OpenRegister, Tavily, OpenAI and n8n are not evidenced. |
| International transfer mechanism documented | **Cannot determine from brief** | Vendor locations, subprocessors and transfer documents are absent. |
| DPIA conducted if required | **Cannot determine from brief** | DPIA screening is required; the brief gives no screening or DPIA. |
| Article 22 safeguard in place if automated decisions affect people | **Appears met** | The stated prototype does not make such decisions. The product must still prevent downstream decision use. |
| Privacy notice covers AI processing | **Cannot determine from brief** | No notice or Article 14 process is described. |
| Data subject rights can be operationalised within deadlines | **Cannot determine from brief** | No intake, ownership, search, correction, deletion or response process is described. |

## 5. Overall recommendation

**Do not proceed with live personal-data processing or production sharing until the blocking conditions are resolved.** The prototype may be tested with synthetic or demonstrably non-personal data while the team documents its purposes and lawful bases, confirms vendor roles and transfer safeguards, completes DPIA screening, and implements notice, rights, accuracy and retention controls. The absence of an Article 22 decision is a useful scope limitation, but it does not cure the unresolved Article 6, Article 28/44–46, Article 35 or transparency issues.

## 6. What this report is not

This report is not a legal opinion, not a DPIA, and not a certification of compliance. The client should obtain legal review before relying on this assessment.

## Primary sources

- [GDPR Regulation (EU) 2016/679 — EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/)
- [EDPB DPIA requirements and criteria](https://www.edpb.europa.eu/sme-be-compliant/be-compliant_en)
- [European Commission: standard contractual clauses](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en)
