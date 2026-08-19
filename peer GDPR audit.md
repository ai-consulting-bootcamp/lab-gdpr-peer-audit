# GDPR Peer Audit – AI Entrepreneur Coach

## Read and Annotate

### Personal Data Identified

| Data category                             | Source       | Purpose(s)                                      | Crosses EU border?             | Special category?                     |
| ----------------------------------------- | ------------ | ----------------------------------------------- | ------------------------------ | ------------------------------------- |
| LinkedIn PDF / CV                         | User upload  | Extract skills, education, experience, industry | Yes (OpenAI, Cohere, Pinecone) | No                                    |
| Personality questionnaire (TIPI Big Five) | User         | Personality profiling for recommendations       | Yes                            | No (but sensitive inference possible) |
| Budget                                    | User         | Recommendation filtering                        | Yes                            | No                                    |
| Time available                            | User         | Recommendation filtering                        | Yes                            | No                                    |
| Generated entrepreneur profile            | AI-generated | Recommendation explanation                      | Yes                            | No                                    |
| Career fit score                          | AI-generated | Ranking recommendations                         | Yes                            | No                                    |
| Selected business idea                    | User         | Generate 90-day roadmap                         | Yes                            | No                                    |


### Initial observations

The system processes substantially more personal data than a conventional chatbot. It combines professional history, personality assessment, financial constraints, and inferred behavioural characteristics to produce personalized recommendations. These data flows cross EU borders through multiple AI service providers.

Purpose limitation appears clear from the documentation; all collected information supports entrepreneurial recommendations.

---
---

## Personal Data and Role Map

### Personal Data Summary

| Data category                | Source | Purpose(s)                       | Crosses EU border? | Special category?            |
| ---------------------------- | ------ | -------------------------------- | ------------------ | ---------------------------- |
| CV / LinkedIn export         | User   | Extract professional profile     | Yes                | No                           |
| Personality responses (TIPI) | User   | Determine entrepreneurial traits | Yes                | No (psychological profiling) |
| Budget & available time      | User   | Filter recommendations           | Yes                | No                           |
| Generated profile summary    | AI     | Explain recommendations          | Yes                | No                           |
| Career fit percentage        | AI     | Rank business ideas              | Yes                | No                           |


### Role Map

| Entity                                 | Role                                       | Processing activity                         | DPA needed?                        |
| -------------------------------------- | ------------------------------------------ | ------------------------------------------- | ---------------------------------- |
| Client operating AI Entrepreneur Coach | Controller                                 | Determines purposes and means of processing | N/A                                |
| Builder / Development team             | Processor (during development) or Provider | Development and maintenance                 | Yes (if acting on client's behalf) |
| OpenAI                                 | Processor                                  | Profile extraction and report generation    | Yes                                |
| Cohere                                 | Processor                                  | Embeddings                                  | Yes                                |
| Pinecone                               | Processor                                  | Vector database                             | Yes                                |


### International transfers

The project documentation does not specify hosting locations for OpenAI, Cohere or Pinecone. Since these services may process personal information outside the EEA, an appropriate transfer mechanism (Standard Contractual Clauses, adequacy decision, or EU-US Data Privacy Framework participation) should be verified before deployment.

---
---

## Clarifying Questions Log

### Question 1

What happens to uploaded CVs after recommendation generation?

Why it matters

This affects storage limitation, retention schedules, and the right to erasure (Articles 5 and 17 GDPR).

Provisional assumption

Uploaded documents are deleted after the session, as suggested in the project risk assessment, but this is not explicitly documented as a technical control.

### Question 2

Are uploaded CVs or personality responses used to improve AI models?

Why it matters

Purpose limitation, processor agreements, transparency obligations, and lawful basis depend on whether third-party vendors reuse submitted content.

Provisional assumption

The system relies on standard API processing only and does not intentionally use customer data for model training, although this should be contractually verified.

### Question 3

How are users informed that personality profiling is being performed?

Why it matters

Transparency obligations require users to understand how their information influences recommendations.

Provisional assumption

No dedicated privacy notice currently exists.

### Question 4

Is the fit percentage fully deterministic or partly generated by the LLM?

Why it matters

Transparency and explainability depend on whether scores are reproducible.

Provisional assumption

Documentation states the percentage is calculated algorithmically rather than invented by the LLM.

---
---

## Audit Report

### Section 1 – System Summary

AI Entrepreneur Coach recommends business ideas based on a user's professional background, personality profile, budget, and available time. Users upload a LinkedIn PDF or CV, complete a Big Five personality questionnaire, and receive a ranked list of business ideas with explanations and a personalized 90-day roadmap. Recommendations are grounded in a curated business idea knowledge base rather than being generated solely by an LLM.

### Section 2 – Data and Role Map

The application processes identifiable personal information, including employment history, education, skills, personality assessment responses, financial constraints, and AI-generated behavioural summaries.

The client acts as the controller, while OpenAI, Cohere, and Pinecone function as processors. Because these vendors may process data outside the EEA, appropriate international transfer safeguards should be implemented.

### Section 3 – Compliance Findings

Finding 1 — **Data Processing Agreements**

Severity: Blocking

Description

The documentation identifies several third-party processors but provides no evidence that Article 28 Data Processing Agreements exist.

Recommended action

Execute DPAs with OpenAI, Cohere, and Pinecone before processing production user data.

Escalation needed?

Yes — Legal Counsel.

Finding 2 — **International Transfers**

Severity: Significant

Description

Personal data may leave the European Economic Area, but no transfer mechanism is documented.

Recommended action

Verify Standard Contractual Clauses, adequacy decisions, or Data Privacy Framework participation for each vendor.

Escalation needed?

Yes — Data Protection Officer.

Finding 3 — **Transparency**

Severity: Significant

Description

Users provide personality data and receive AI-generated recommendations, but no transparency notice describing profiling, third-party processing, or retention is documented.

Recommended action

Publish a GDPR-compliant privacy notice explaining AI processing, profiling, third-party providers, retention, and user rights.

Escalation needed?

No.

Finding 4 — **Retention Policy**

Severity: Minor

Description

The documentation states that uploaded files are not persisted beyond the session but does not describe technical enforcement.

Recommended action

Publish a documented retention schedule and implement automatic deletion controls.

Escalation needed?

No.

Section 4 – **GDPR Obligations Checklist**

| Obligation                                  | Assessment           | Note                                                            |
| ------------------------------------------- | -------------------- | --------------------------------------------------------------- |
| Lawful basis identified                     | **Gap identified**   | Not documented                                                  |
| Purpose limitation respected                | **Appears met**      | Data used consistently for recommendations                      |
| Data minimisation                           | **Appears met**      | Inputs appear proportionate                                     |
| Controller/processor roles mapped and DPAs  | **Gap identified**   | Vendors identified, DPAs not documented                         |
| International transfer mechanism documented | **Gap identified**   | No evidence provided                                            |
| DPIA conducted if required                  | **Cannot determine** | Profiling may justify one                                       |
| Article 22 safeguards                       | **Appears met**      | Recommendations only; no automated decisions with legal effects |
| Privacy notice covers AI processing         | **Gap identified**   | Not documented                                                  |
| Data subject rights operationalised         | **Cannot determine** | No documented procedure                                         |


Section 5 – **Overall Recommendation**

Proceed with conditions

The project demonstrates a thoughtful approach to explainable AI by grounding recommendations in retrieved knowledge and avoiding automated decisions with legal effects. However, several GDPR governance measures are missing, particularly around third-party processor agreements, international transfers, and transparency documentation.

Before deployment, the project should establish Data Processing Agreements with all AI vendors, document international transfer safeguards, publish a comprehensive privacy notice, and formalise retention policies. These measures would substantially improve accountability while preserving the system's existing privacy-conscious architecture.

Section 6 – **What This Report Is Not**

This report represents an independent GDPR compliance review based solely on the supplied project documentation. It is not legal advice, not a Data Protection Impact Assessment, and not evidence of GDPR certification. Production deployment should include review by qualified legal counsel and, where appropriate, a Data Protection Officer.

---
---

### Debrief Conversation

1. Auditor Presentation

The audit concluded that the project demonstrates good technical design with respect to explainable recommendations and purpose limitation. The primary concerns relate to governance rather than the recommendation algorithm itself, particularly third-party processor agreements, international data transfers, transparency, and retention documentation.

2. Builder Response

The builder explained that uploaded files are intended to exist only during the active session and are not stored permanently. They also confirmed that recommendation scores are calculated algorithmically rather than generated by the LLM.

3. Lawful Basis Comparison

Both audits considered Article 6(1)(b) GDPR (performance of a contract) to be the strongest lawful basis for generating recommendations requested directly by the user. Legitimate interests may apply only to operational analytics and system monitoring.

4. DPIA Comparison

Both reviews acknowledged that a DPIA may become necessary if persistent user accounts, longitudinal profiling, or large-scale deployment are introduced. For the current MVP, the documentation alone does not provide sufficient evidence to conclude that a mandatory DPIA is triggered.

5. Gap Comparison

The builder focused primarily on technical privacy protections, while the independent audit placed greater emphasis on organisational accountability, particularly contractual arrangements with processors and international transfer documentation. The external review also highlighted the need for a formal transparency notice.

6. Joint Closing Note

The debrief demonstrated that self-audits often focus on technical implementation, whereas an independent reviewer is more likely to identify missing governance documentation and contractual obligations. It also highlighted how project documentation influences GDPR assessments: when retention, transparency, or processor relationships are not explicitly documented, auditors must assume additional compliance risk even if appropriate practices exist in implementation.

---
---

## Reinforce

### Documentation Review

The current project documentation provides strong technical explanations but does not fully answer several GDPR governance questions.

Missing or incomplete documentation includes:

Data Processing Agreements with vendors
Privacy Notice
Records of Processing Activities (RoPA)
Retention Schedule
Lawful Basis Assessment
Legitimate Interests Assessment (where applicable)

These omissions suggest that the project documentation is stronger from a software engineering perspective than from a compliance perspective.

### Reflection

Initially, the builder may disagree that a DPIA should even be considered because the application does not make legally significant decisions. After the audit, however, it becomes clear that extensive personality profiling and AI-generated recommendations increase regulatory attention, even if Article 22 GDPR is not triggered. The discussion therefore shifts from whether the project is "high risk" to whether sufficient governance documentation exists to demonstrate accountability.

---
---

## Stretch

### Remediation Plan – Third-Party Processor Governance

**Gap**

No documented Data Processing Agreements (DPAs) exist with OpenAI, Cohere, or Pinecone.

**Required artifact**

Signed Article 28 GDPR Data Processing Agreements together with documentation of international transfer safeguards (Standard Contractual Clauses or equivalent).

**Owner**

Client (Controller), Legal Counsel, and Data Protection Officer.

**Timeline**

Before any production deployment involving real user data.

**Evidence for a regulator**

Executed DPAs with each processor.
Documentation of transfer mechanisms.
Vendor security documentation.
Updated privacy notice identifying each processor and describing its processing activities.