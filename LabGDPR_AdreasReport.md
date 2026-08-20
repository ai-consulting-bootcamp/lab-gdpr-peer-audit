# GDPR Audit Report: Proactive Incident Agent

## Section 1: System summary

The Proactive Incident Agent is an AI-assisted decision-support system for cruise-company incident, claims, legal, risk and compliance teams. It processes incident and potentially medical information relating to passengers, staff, witnesses and other individuals, extracting structured information and identifying missing information. It then generates severity, claim-risk and customer-impact classifications, flags higher-risk cases and can produce weekly management reports. External services including Airtable, Notion and an LLM API may process or store the resulting data, while a human reviewer remains responsible for consequential decisions.

## Section 2: Data and role map

The system processes ordinary personal data such as names, locations, incident details, case status and evidence notes, together with potentially **special-category health data** contained in injury and doctor reports. It also generates inferred/profiling information including claim risk, severity, customer impact and high-risk flags.

The cruise company would **likely be the controller**, as it determines the purposes for which incident and claims information is processed. The builder and external technology providers would likely act as processors where they process data on the company's behalf. However, contractual arrangements are not provided, so the precise role allocation cannot yet be confirmed.

Airtable, Notion and the LLM provider may involve international processing, but the brief does not establish where processing occurs. Consequently, the existence of a restricted international transfer and the applicable Chapter V transfer mechanism cannot yet be determined. No evidence of SCCs, adequacy arrangements or other transfer safeguards is provided.

## Section 3: Compliance findings

### Finding 1 — Lawful basis for personal and health-data processing

**Severity:** **Blocking**

**Description:** The brief identifies extensive personal data and potentially Article 9 health data but does not identify an Article 6 lawful basis or an Article 9 condition for any processing purpose. This is particularly material because doctor reports and medical observations are expressly within scope.

**Recommended action:** Document the lawful basis for each distinct processing purpose and the applicable Article 9 condition for health data before production processing begins.

**Escalation needed?** **Yes — DPO/legal counsel.**

### Finding 2 — Processor roles and Article 28 arrangements

**Severity:** **Blocking**

**Description:** Airtable, the LLM provider and potentially Notion and the builder appear likely to process personal data on behalf of the cruise company. The brief states that DPAs need to be confirmed but provides no evidence that compliant processor agreements are in place.

**Recommended action:** Map all processors/subprocessors and execute appropriate Article 28 DPAs before they process real passenger or health data.

**Escalation needed?** **Yes — DPO/procurement/legal.**

### Finding 3 — International transfers

**Severity:** **Significant**

**Description:** The brief expressly acknowledges that vendors may process data outside the EEA but does not establish processing locations or a transfer mechanism. This prevents confirmation of GDPR Chapter V compliance.

**Recommended action:** Confirm all processing locations and transfer routes. Where required, implement SCCs or another valid Chapter V mechanism and conduct the necessary transfer assessment and supplementary safeguards.

**Escalation needed?** **Yes — DPO/legal.**

### Finding 4 — DPIA / high-risk processing assessment

**Severity:** **Blocking if a DPIA is required and absent; otherwise Significant**

**Description:** The system processes health data and generates classifications/profiles that may influence how individual claims are handled or escalated. The brief provides no evidence that a DPIA has been conducted. Given the nature and potential scale of the processing, a formal DPIA assessment is warranted before deployment.

**Recommended action:** Complete and document a DPIA screening and, if Article 35 criteria are met, a full DPIA before production processing. Include the LLM, profiling, health-data processing, vendors, international transfers and risks to affected individuals.

**Escalation needed?** **Yes — DPO.**

### Finding 5 — Purpose limitation, minimisation and secondary use

**Severity:** **Significant**

**Description:** Data collected for incident/claims handling are also used for weekly management reporting and LLM audit/cost-control logging. The brief does not establish whether these secondary uses are compatible with the original purposes or whether unnecessary personal/health information is included.

**Recommended action:** Define and document each purpose separately, minimise information included in management reports and LLM logs, and use aggregated or pseudonymised information wherever practical.

**Escalation needed?** **No**, unless the compatibility assessment identifies a new incompatible purpose.

### Finding 6 — Human review and Article 22

**Severity:** **Minor**

**Description:** The system does not make final claims decisions and requires a human reviewer to assess its outputs. This substantially reduces the likelihood that the current design constitutes a solely automated decision producing legal or similarly significant effects under Article 22. However, the brief does not document the reviewer's authority to override the AI or safeguards against excessive reliance on its classifications.

**Recommended action:** Document mandatory human review, reviewer authority to override outputs and procedures for challenging erroneous classifications.

**Escalation needed?** **No.**

## Section 4: Specific GDPR obligations checklist

| Obligation                                                         | Assessment                      | Note                                                             |
| ------------------------------------------------------------------ | ------------------------------- | ---------------------------------------------------------------- |
| Lawful basis identified for each processing purpose                | **Gap identified**              | No Article 6/9 bases stated                                      |
| Purpose limitation respected                                       | **Gap identified**              | Secondary reporting/logging purposes need assessment             |
| Data minimisation                                                  | **Cannot determine from brief** | Data categories are broad; necessity has not been demonstrated   |
| Controller/processor roles mapped and DPAs in place                | **Gap identified**              | Roles are inferable, but DPAs are not evidenced                  |
| International transfer mechanism documented                        | **Gap identified**              | Processing locations and mechanisms are unconfirmed              |
| DPIA conducted if required                                         | **Cannot determine from brief** | No DPIA evidence supplied                                        |
| Article 22 safeguard in place if automated decisions affect people | **Cannot determine from brief** | Human review is stated, but override controls are not documented |
| Privacy notice covers AI processing                                | **Cannot determine from brief** | No privacy notice is discussed                                   |
| Data subject rights can be operationalised within deadlines        | **Cannot determine from brief** | No rights-handling process is described                          |

## Section 5: Overall recommendation

**Do not proceed with production personal-data processing until the blocking conditions are resolved.** The MVP may continue using genuinely non-production/pseudonymised test data, but the brief does not establish a lawful basis for the processing of personal and health data or compliant processor arrangements for the external services that may receive that data. Before production go-live, the team should establish the Article 6 and Article 9 bases, complete the controller/processor and DPA mapping, conduct the required DPIA assessment, and resolve international-transfer requirements. Purpose limitation, minimisation, retention and human-oversight controls should then be documented as conditions of deployment.

## Section 6: What this report is not

This report is not a legal opinion, a DPIA, or a certification of compliance. It is a first-pass audit based solely on the supplied data processing brief. The client should obtain appropriate DPO and legal review before relying on this assessment or processing real personal data in production.
