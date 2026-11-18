# CompanyScope debrief

**Participants:** Jedrzej and Sean Langsdorf (builder)  
**Project:** CompanyScope  
**Date:** 17 November 2026


## 1. Auditor presents — uninterrupted report walkthrough

The auditor presented the report in this order:

1. CompanyScope is a research-briefing workflow, not an intended automated decision-maker.
2. The workflow can nevertheless process personal data in public web content, queries, prompts and reports.
3. The most urgent gaps are: no evidenced lawful basis or Article 9 approach; unresolved vendor roles, DPAs and transfers; no evidenced DPIA screening; no evidenced AI-aware notice or rights process; and non-enforced accuracy, retention and release controls.
4. The ambiguous-match stop and the expected professional source review are useful safeguards, but they do not prove compliance or prevent all downstream misuse.
5. The recommendation is not to use live personal data or share production reports until the blocking conditions are closed.

## 2. Builder responds — five-minute context

**Builder response:** Sean explains that the prototype is intended for a professional researcher to prepare for a meeting or initial counterparty review, not to score people or make a decision about them. He says the intended inputs are company facts, that public websites were treated as lower risk, and that the professional is expected to open sources and correct the output. He also says he assumed the model and search services' standard terms would cover the integration and had not yet mapped vendor locations, query logs, or a rights-request process.

**Audit response:** Those design intentions are helpful scope constraints, but they do not answer whether person-level data enters the workflow or establish a lawful basis, Article 14 notice, DPA, transfer safeguard or retention rule. A warning to review output is weaker than an enforced release gate, especially when the brief acknowledges unsupported claims may pass the structural checks.

## 3. Compare lawful-basis selections

| Topic | Self-audit position | Independent-audit position | Debrief result |
|---|---|---|---|
| Primary research purpose | Legitimate interests of the research client or law firm, because targeted company research supports a business/legal purpose | Legitimate interests is plausible, but the brief does not document necessity, balancing, affected people, reasonable expectations or safeguards | Keep legitimate interests as the working candidate only after a documented LIA and purpose definition. |
| Authenticated query and operational logs | Possibly necessary to provide the service or protect the workflow; not analysed separately | Must be separated from the research purpose and assessed based on what is actually logged and retained | Inventory the fields and select a basis per log purpose; do not assume the research basis covers all telemetry. |
| Vendor prompts and report sharing | Assumed to be covered by the primary research purpose | Could be a compatible processor operation only if instructed, minimised and transparently disclosed; separate sharing or reuse may need its own analysis | Add each disclosure/recipient to the purpose and vendor matrix; do not rely on “public data” as permission. |

**Agreed lawful-basis finding:** The audits do not genuinely disagree on the likely candidate. They disagree on whether naming “legitimate interests” is enough. It is not: the controller must document the specific interest, necessity, balancing, safeguards and transparency, and it must address any special-category data separately.

## 4. Compare DPIA conclusions

**Builder conclusion:** No DPIA is required because CompanyScope does not make automated decisions and is aimed at company research rather than individual profiling.

**Independent-audit conclusion:** Article 22 and Article 35 ask different questions. The stated scope may avoid Article 22, but the use of novel AI, combined registry/web datasets and possible person-level analytical observations can create high-risk indicators. Scale, recurring monitoring, special-category content and downstream use are still unknown.

**Joint resolution:** Both parties agree to complete and retain a DPIA screening before any production use. They will complete a full DPIA if the screening confirms likely high risk, including where multiple EDPB criteria apply, or if the workflow expands into recurring monitoring, profiling, sensitive data or decisions about people. Until then, the prototype is restricted to synthetic/non-personal testing or controlled review under the conditions in the audit report.

## 5. Compare gap lists

| What the self-audit caught | What the independent review added | What the external review could not know from the brief |
|---|---|---|
| Ambiguous company matches stop rather than being guessed; source references are checked; the design expects a professional to verify findings; no intended Article 22 decision | A company query can reveal a person's research activity; public data is not automatically reusable; person-level web content changes the Article 6/9/14 analysis; vendor roles, DPAs, locations and transfers need evidence; rights and retention need operating owners | Actual n8n hosting mode, API configurations, vendor contract terms, retention/training settings, scale, real users, logs, access controls and whether any special-category data has actually appeared |
| The intended company-focused scope limits risk | The report can still contain unsupported or inferred claims about named people, and “human review advised” is not an enforceable control | Whether the product technically blocks release without review, redacts irrelevant people or records corrections |

## 6. Joint closing note

Self-assessment tends to follow the intended user and the happy path, so it can miss personal data about other people entering through public sources, search queries, prompts, logs and downstream sharing. Independent review is especially useful for testing assumptions such as “public means permitted,” “no automated decision means no DPIA,” and “the vendor's standard terms are sufficient,” and for turning those assumptions into evidence requests.

## Findings surfaced by the debrief

1. **Scope drift:** “Company research” can become person-level processing when web results, inferences or search metadata identify people.
2. **Lawful-basis shorthand:** The phrase “legitimate interests” is a starting hypothesis, not a completed assessment.
3. **DPIA misconception:** Avoiding Article 22 decisions does not remove the need to screen for Article 35 high-risk processing.
4. **Documentation is a control:** Without a vendor/data-flow inventory, the team cannot reliably answer who receives prompts, where data goes or how deletion and rights requests work.
5. **Human review needs enforcement:** A recommendation to review sources is valuable, but a release gate, correction record and restricted downstream use are stronger controls.

## Agreed actions

| Action | Owner | Evidence of completion | Target |
|---|---|---|---|
| Build a field-level data-flow and vendor register | Sean / product owner with controller | Diagram showing inputs, prompts, outputs, logs, recipients, locations and subprocessors | Before any live-data test |
| Document purposes, lawful bases and the legitimate-interest assessment | Controller with DPO/legal support | Signed purpose matrix and LIA; Article 9 decision recorded | Before production design approval |
| Complete DPIA screening and, if triggered, the full DPIA | Controller/DPO | Screening record and approved DPIA with mitigations | Before production use |
| Confirm DPAs, transfer tools, retention and model-use settings | Controller/procurement/legal | Executed contracts, SCC/TIA where needed, vendor settings and retention schedule | Before vendor receives personal data |
| Add notice, rights, redaction, source-review and release controls | Product owner/controller | Privacy notice, rights SOP, test cases and release/audit logs | Before reports are shared externally |
