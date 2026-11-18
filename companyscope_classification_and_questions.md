# CompanyScope classification, annotations and questions

**Audited teammate:** Sean Langsdorf  
**Project:** CompanyScope  
**Audit date:** 17 November 2026

## Scope and independence note

This document was prepared from `companyscope_system_brief.md` only. Sean's self-audit, lawful-basis assessment, DPIA analysis and gap findings were not available during the independent review. “Cannot determine” means the brief does not provide evidence; it does not by itself prove that a control is absent.

## Phase 1 — Read and annotate

| Brief evidence | Personal-data classification | GDPR question or risk to carry into the audit |
|---|---|---|
| User enters a company name and optionally a commercial-register identifier | Usually company information, but it can identify a sole trader or be linked to an identifiable requester. The query can reveal which company a person or firm is researching. | Treat the query and any linked account/request metadata as potentially personal data; confirm logging, access and retention. |
| Registered name, court, number, legal form, address, business purpose and status | Mostly legal-entity information. A registered address, name or business purpose may be personal data where it points to a natural person, such as a sole trader. | Data-minimisation and accuracy controls need to distinguish company-only fields from information about people. |
| Tavily web results may contain names, professional contact details or other information about identifiable people | Personal data is expressly in scope. No special-category data is identified, but public pages could contain or allow inferences about it. | Public availability is not a lawful basis by itself. Confirm filtering, Article 9 handling, purpose compatibility and transparency. |
| OpenAI receives selected registry and web evidence plus local research-method notes | The prompt can contain personal data from the registry or web results; the generated report can create or repeat personal-data claims and inferences. | Identify the controller/processor relationship, vendor retention and training terms, transfer locations and human review. |
| The local reference collection contains method notes, not company facts | No personal data is identified in the brief. | Confirm that the collection is actually free of case-specific or person-specific data. |
| The output is saved as a Markdown report and browser results page | The output may contain personal data and may be shared outside the research team. | Define recipients, retention, correction/deletion handling and controls against unsupported claims. |
| The workflow can run through an authenticated endpoint or manually in n8n | Authentication and workflow logs may identify operators or firms, although the brief does not describe those fields. | Confirm what is logged, where it is stored, who can access it and whether those logs are included in the privacy notice. |
| The brief names OpenRegister, Tavily, OpenAI and n8n, but does not state their hosting locations or subprocessors | International transfer status is unresolved. | Obtain vendor locations and data-flow details; use an adequacy decision or an Article 46 safeguard such as current EU SCCs plus a transfer impact assessment where required. |
| The system combines registry data and web evidence and produces analytical observations | The new report purpose may go beyond the purpose for which an individual originally published information. | Test purpose compatibility, necessity, legitimate interests and Article 14 transparency before production use. |
| The system stops if it cannot identify one registry match; a professional is expected to check sources and correct or omit unsupported statements | These are useful accuracy and human-review controls, but they are described as advice rather than enforced workflow gates. | Confirm whether the product can prevent publication or downstream use without review. |

## Phase 2 — Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Company name and optional register identifier; possibly linked requester or firm information | Browser form, authenticated endpoint or manual n8n run | Find one company and provide a research briefing | Cannot determine; logs and endpoint hosting are not described | Not inherently; research activity may still be personal data when linked to a person |
| Registered name, court, register number, legal form, address, business purpose and status | OpenRegister | Company profile and entity verification | Cannot determine from the brief | Generally no; address/name/business-purpose fields may identify a natural person |
| Names, professional contact details and other information about identifiable people | Public websites reached through Tavily | Public findings, analysis and follow-up research | Cannot determine; search-provider and source-site locations are not stated | Not identified, but possible or inferable from public content; Article 9 handling is not described |
| Selected registry/web evidence, model prompt, analytical observations and report | Derived inside the workflow; prompt sent to OpenAI | Draft and render the report | Cannot determine; OpenAI processing location and onward transfers are not stated | Could reproduce or infer special-category data if it enters from a source |
| Research-method notes | Local reference collection | Guide research method and model output structure | Not indicated | No personal data identified in the brief |

## Phase 2 — Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Deploying client / law-firm or business research team | Likely controller for its research purposes, including deciding what to search, why to use the report and whom to share it with | Collects query data, commissions the research, reviews and shares the report | No DPA with itself; it must appoint processors under Article 28 where applicable |
| Sean / builder team | Builder rather than automatically a controller or processor. If the team only created the prototype and never handles live client data, its role may end there. If it operates, hosts or accesses data for the client, it is likely a processor; joint-controller risk would need separate facts. | Configuration, workflow maintenance, possible hosting, support or access | Conditional: yes if it processes personal data on the client's documented instructions |
| OpenRegister | Registry source/API. Independent-controller versus processor status cannot be determined from the brief or service terms. | Receives a company query and returns registry fields | Conditional: Article 28 terms if it processes personal data as a processor; otherwise review its independent-controller terms and source lawfulness |
| Tavily | Search/API vendor; likely a processor for an instructed search, but its own use of queries and results could change the analysis | Runs the web search and returns selected results | Conditional: DPA and subprocessor/transfer review if it processes on the client's behalf |
| OpenAI | Model/API vendor; likely a processor or subprocessor for the prompt, subject to the contract and service configuration | Receives selected evidence and method notes and generates analysis | Conditional: Article 28 terms, retention/training settings and transfer safeguards must be confirmed |
| n8n or its hosting provider | Workflow processor if cloud-hosted or if it stores prompts, credentials, logs or reports; a self-hosted installation may shift the relevant vendor to the infrastructure provider | Orchestrates calls, stores or transmits workflow data and may save results | Conditional: DPA and subprocessor review where it handles personal data |
| Public websites / source publishers | Usually separate controllers for their own publication; the brief does not establish a processor relationship | Publish source content that the workflow retrieves | Usually no client DPA, but source terms, lawful reuse, notice and purpose compatibility still require review |

## International-transfer note

The brief identifies external services but does not state where they, their subprocessors or the relevant data stores are located. I therefore cannot conclude that a transfer occurs, but I also cannot clear the flow. If personal data leaves the EEA, the controller needs an applicable adequacy decision or an appropriate safeguard under Article 46, normally with a documented transfer assessment and any supplementary measures needed for the actual destination and access risks. The current EU Standard Contractual Clauses are one possible tool, not automatic proof of compliance.

## Phase 3 — Clarifying questions log

| Question | What I need to know | Why it matters | Provisional assumption if unanswered |
|---|---|---|---|
| 1. What personal data is allowed to enter, and how are special-category data, allegations and irrelevant person-level content filtered? | Field-level input/output rules, source filters, prompt filters and whether sole-trader or residential-address records are in scope | Articles 5(1)(c), 5(1)(d), 9 and 25; special-category processing needs an additional Article 9 condition and a higher-risk assessment | No special-category data should be intentionally processed; the workflow should stop, redact or exclude it until a documented rule exists. |
| 2. Who is the controller, what are the separate purposes, and what lawful basis has been selected for each? | Controller identity; basis for research, query logging, vendor prompts, report storage and sharing; any legitimate-interest assessment | Article 6 requires a lawful basis for each purpose, and Article 5 requires purpose limitation and fairness | Legitimate interests may be the most plausible basis for targeted business research, but processing should not proceed on that label alone: a necessity/balancing assessment is required. |
| 3. Which vendors and subprocessors receive which fields, where are they located, how long do they retain them, and do they use them for their own model or service purposes? | Data-flow diagram, locations, subprocessors, retention/training settings, DPAs and transfer documents | Articles 28 and 44–46; this determines processor duties, international-transfer safeguards and whether data can be put into prompts | Assume external processing and a possible non-EEA transfer; do not send live personal data until contracts and transfer safeguards are evidenced. |
| 4. What is the scale and operating pattern, and can the output influence decisions about people? | Number of users and reports, recurring monitoring, profiling or scoring, categories of affected people, and whether reports are used in hiring, credit, client acceptance or transactions | Article 22 and Article 35; no automated decision in the brief is helpful, but it does not answer whether processing is high risk or whether downstream use changes the assessment | Run a documented DPIA screening. Treat a full DPIA as a precondition for production if the combined-data/novel-AI processing is high risk. |
| 5. What notice, rights, retention and correction workflow exists for people whose data appears in sources or reports? | Article 14 notice, rights intake and response process, report retention/deletion, correction and publication controls | Articles 5(1)(e), 12–15 and 17–21; third-party collection makes transparency and rights operationalisation especially important | Assume the controls are not yet evidenced. Require an AI-aware Article 14 notice, a correction/deletion route and a defined retention schedule before sharing reports beyond controlled review. |

## Primary sources used

- [GDPR Regulation (EU) 2016/679 — EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/), especially Articles 5, 6, 9, 13–14, 22, 28, 35 and 44–46.
- [EDPB DPIA requirements and criteria](https://www.edpb.europa.eu/sme-be-compliant/be-compliant_en), including the guidance that two or more high-risk criteria generally warrant DPIA assessment.
- [European Commission: standard contractual clauses](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en).
