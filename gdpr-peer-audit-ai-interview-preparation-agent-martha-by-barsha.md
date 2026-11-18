# GDPR Peer Audit - AI Interview Preparation Agent (Martha's Project 3)

**Auditor:** Barsha Mishra
**Builder / client:** Martha
**System audited:** AI Interview Preparation Agent (n8n workflow, Ironhack Project 3)
**Information received:** Martha's *Data Processing Brief - Project 3 AI Interview Preparation Agent*, received 17 November 2026. **Only the brief was exchanged.** I did not see Martha's lawful bases, DPIA analysis, findings or memo before writing this audit. Martha received only my data processing brief.
**Date:** 17 November 2026

---

## Phase 1 - Read and annotate

Key:
- **[PD]** = personal data category (special-category status noted)
- **[UNCLEAR]** = needs confirmation
- **[NON-EU]** = flow to a non-EU vendor or possible transfer outside the EEA
- **[PURPOSE?]** = purpose possibly incompatible with the original collection

| # | Element in the brief | Mark | Note |
|---|---|---|---|
| 1 | "a CV, potentially containing a name, contact details, employment and education history, dates, skills and achievements" | [PD] | Core personal data. **Dates** can reveal **age**, which is not special category but is a discrimination risk. |
| 2 | "A CV could incidentally contain a photo or sensitive personal information" | [PD] **Special category possible** | Health, disability or religion in a CV is **Art. 9 data**. A photo can reveal ethnic origin or religion (e.g. religious clothing). |
| 3 | "The submitted job description may include recruiter contact details" | [PD] [PURPOSE?] | **Third-party personal data.** The recruiter gave their details to advertise a job, not to be processed by an AI tool and sent to US vendors. |
| 4 | "Generated reports may include inferred strengths, experience gaps and draft professional examples about the candidate" | [PD] | **Inferred data and an evaluation** of the candidate's work-related suitability. This is relevant to the DPIA criteria and to accuracy (Art. 5(1)(d)). |
| 5 | "requests the user's permission before starting the CV check; the precise consent text, enforcement and logging have not yet been verified" | [UNCLEAR] | Is this consent valid (Art. 7)? What happens on refusal? Is it recorded? |
| 6 | "OpenAI GPT-4o-mini generates personalised interview guidance" | [NON-EU] | OpenAI is US-based. Full CV text likely goes there. |
| 7 | "Tavily and NewsAPI provide external company/job context" | [NON-EU] [UNCLEAR] | Probably only company names are sent, but this is not confirmed. |
| 8 | "Pinecone supports retrieval-augmented generation (RAG)" | [NON-EU] [UNCLEAR] | **What is stored in Pinecone?** Company documents only, or CV embeddings too? |
| 9 | "the report is saved or delivered through Notion" | [NON-EU] [UNCLEAR] | Notion is US-based. "Saved or delivered" suggests reports may be **stored**, not just delivered (to verify). If stored, who can access them? |
| 10 | "n8n and connected services may retain execution metadata and logs, depending on settings" | [UNCLEAR] | Retention is unknown. Logs may contain full CV text. |
| 11 | "The exact fields transmitted to each service have not been confirmed" | [UNCLEAR] | It is not possible to check data minimisation without this. |
| 12 | "the production controller/operator arrangement is not specified" | [UNCLEAR] | Without it, controller and processor roles cannot be fixed. |
| 13 | "Hosting regions … contractual terms, and subprocessors have not been confirmed" | [NON-EU] [UNCLEAR] | There is no evidence of DPAs or transfer mechanisms. |
| 14 | "A recovered sample report includes proposed STAR achievements whose accuracy … is not independently verified" | [UNCLEAR] [PURPOSE?] | Was this sample built from a real person's CV? If so, keeping it as a project sample is a new purpose. |
| 15 | "There is no verified model-training or secondary-use purpose for submitted CVs" | Positive | No intended reuse. But "not verified" is not the same as "excluded by contract", so vendor terms still need checking. |

---

## Phase 2 - Personal data and role map

*Completed from the brief alone. Gaps in the brief are noted.*

**Personal data summary**

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Identity and contact data (name, email, phone, address) | User, via CV upload | Intake, generation, delivery | **Likely** (OpenAI, Notion are US). *Brief: regions not confirmed.* | No |
| Employment and education history, skills, achievements, dates | CV | CV-to-role comparison, STAR examples | Likely (OpenAI) | No. *Dates can reveal age.* |
| Photo and sensitive details (health, disability, religion) | CV (incidental) | Not intended, but processed if present | Likely (OpenAI, Notion) | **Yes, possible (Art. 9)** |
| Recruiter contact details | Job description (third party) | Not needed for any stated purpose | Likely (OpenAI) | No |
| Permission / consent response | Form | Intake (pre-check) | Unknown (n8n region not stated) | No |
| Inferred strengths, experience gaps | Generated by OpenAI | Interview guidance | Yes (generated in the US) | No, but it is an **evaluation of a person** |
| Draft STAR examples about the candidate | Generated by OpenAI | Interview guidance | Yes | No. **Accuracy risk** |
| Reports stored in Notion | Generated | Delivery and storage | Likely (Notion, US) | Possible, if sensitive CV data is copied in |
| Execution logs and metadata (may include CV text, IP, timestamps) | n8n and services | Operations | **Gap:** depends on settings and region | Possible |
| Names in company news (executives) | Tavily, NewsAPI | Company research | Likely | No |
| *Pinecone vectors* | **Gap:** the brief does not say whether CV content is embedded | RAG | Likely (US) | Unknown |

**Role map**

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| **Client / operator** *(brief: "not specified")* | **Controller.** Assumed to be the organisation offering the tool to job seekers. In the prototype, this is Martha. | Decides purposes and means: CV analysis and report generation | — (the controller signs DPAs with processors) |
| **Builder (Martha)** | **Controller** today, since she runs the prototype. If she operates the tool for a client (e.g. a career coach), she becomes a **processor** | Builds and runs the n8n workflow | **Yes**, with the client if Martha operates it for them |
| **Job seeker** | **Data subject** (not a controller, because uploading one's own CV is personal use) | Supplies the CV and reads the report | — |
| **OpenAI** | **Processor / sub-processor** | Generates guidance from CV text | **Yes**. *Brief: no evidence* |
| **Notion** | **Processor / sub-processor** | Stores and delivers reports | **Yes**. *Brief: no evidence* |
| **n8n (cloud or self-hosted, not stated)** | **Processor** if cloud-hosted | Runs the workflow and keeps logs | **Yes, if cloud**. *Brief: not stated* |
| **Pinecone** | **Processor**, if any personal data is stored | Vector storage for RAG | **Yes, if CV data is stored.** Otherwise not needed. *Brief: gap* |
| **Tavily, NewsAPI** | **Probably not processors of candidate data**, if only company names are sent | Company research | **Likely not**. Confirm which fields are sent. |

**International transfers:** OpenAI, Notion and Pinecone are US-based, and Tavily and NewsAPI are likely outside the EU. Each transfer needs either the **EU-US Data Privacy Framework** (if the vendor is certified) or **Standard Contractual Clauses plus a transfer impact assessment**. **The brief provides no evidence that any mechanism is in place.** It explicitly says contractual terms and regions are "not confirmed".

---

## Phase 3 - Clarifying questions log

*Sent to the client (Martha) in writing on 17 November 2026. Written answers received on 17 November 2026.*

| # | What I need to know | Why it matters (GDPR obligation) | Provisional assumption | Martha's answer (17 Nov) | Effect on audit |
|---|---|---|---|---|---|
| 1 | What is the exact permission / consent text, what happens if the user refuses, and is the answer recorded? | **Lawful basis** (Art. 6), **conditions for consent** (Art. 7: freely given, specific, informed, demonstrable), **explicit consent** for special-category data (Art. 9(2)(a)) | Not logged, and refusal may not stop processing, so consent is **not demonstrable**. **Contract (Art. 6(1)(b))** is the realistic basis. | A permission request exists, but the wording, whether refusal stops processing, and whether the answer is recorded are **not verified**. | **Not verified, so treated as a gap until checked.** Finding 1 stays **Blocking** for real CVs; it would drop if the consent flow and an Art. 9 approach are verified. |
| 2 | Which CV fields are sent to each service, in which regions? Are CVs embedded in Pinecone? | **Data minimisation** (Art. 5(1)(c)), **processor contracts** (Art. 28), **transfers** (Chapter V) | Full CV to OpenAI, report to Notion, both in the US. CV embeddings *may* be in Pinecone. | The services are confirmed (OpenAI, Pinecone, Tavily, NewsAPI, Notion). The fields sent, Pinecone CV storage and regions are **not verified**, and Martha calls them documentation gaps. | **Not verified, so treated as a gap until checked.** Finding 2 stays **Blocking** for real CVs. Minimisation remains **cannot determine**. |
| 3 | Retention of CVs, reports, logs and vectors? Notion access and share links? | **Storage limitation** (Art. 5(1)(e)), **security** (Art. 32), **erasure** (Art. 17) | No retention period, Notion reports kept indefinitely | **No verified retention periods.** Notion permissions and shared-link access are **not confirmed**. | **Not verified, so treated as a gap until checked.** Finding 3 stays **Significant**. |
| 4 | Can users upload someone else's CV, or job descriptions with recruiter contacts? Is this prevented or warned against? | **Lawful basis for third-party data** (Art. 6), **Art. 14 information**, **purpose limitation** | No check | **Not verified** whether the system prevents or warns about third-party uploads. | **Not verified, so treated as a gap until checked.** Finding 5 stays **Significant**. |
| 5 | Who is the production operator? Was the sample report made from real personal data? | **Controller responsibility** (Art. 24), **Art. 28**, **purpose limitation** | Martha is controller. The sample is assumed synthetic. | The agent is a bootcamp project, **currently inactive**, with **no production operator**. A recovered **Siemens test report** exists, and Martha **cannot confirm whether the source CV contained real personal data**. Its STAR achievements are unverified against the CV. | **Martha is the controller** for all past processing. The sample report is a **possible retention of real personal data** for a new purpose, so Finding 5 is strengthened. Because the agent is inactive, "do not proceed" does not stop a live service. |

---

## Phase 4 - Audit report

### Section 1 - System summary

The AI Interview Preparation Agent is an n8n workflow that helps job seekers prepare for interviews. The user uploads a CV and a job description through a form and gives a pre-check permission. The workflow researches the company (Tavily, NewsAPI, Pinecone) and sends the information to OpenAI GPT-4o-mini. The model then produces a personalised report with CV-to-role comparisons, interview questions, inferred strengths and gaps, and suggested STAR answers. The report is saved and delivered through Notion. The main personal data is the candidate's CV, which can include sensitive details. It is processed by several services, most of them likely US-based.

### Section 2 - Data and role map

- **Personal data:**
  - CV identity, contact and career data
  - possible **special-category data** (photo, health, religion) included incidentally in CVs
  - **third-party data** (recruiter contacts in job descriptions)
  - **inferred evaluations** of the candidate (strengths, gaps)
  - generated content about the candidate
  - logs
- **Roles:** the operator (Martha in the prototype) is the **controller**. OpenAI, Notion, n8n (if cloud) and Pinecone (if it stores CV data) are **processors**. Tavily and NewsAPI likely receive no candidate data.
- **Transfers:** CV data very likely reaches the US (OpenAI, Notion). The brief gives **no evidence of DPAs or transfer mechanisms**, and states that regions and contracts are unconfirmed.

### Section 3 - Compliance findings

**Finding 1 - Lawful basis and Article 9 condition not established**
**Severity: Blocking** (for real CVs)
- **Description:** every purpose needs an Art. 6 basis, and any special-category data in a CV needs an Art. 9 condition. The brief describes a "permission" step, but its text, its effect on refusal and its logging are unverified, so consent cannot be **demonstrated** (Art. 7(1)). Health, religion or photos in CVs would be sent to OpenAI with **no Art. 9 condition**.
- **Recommended action:**
  1. Use **contract (Art. 6(1)(b))** as the basis for generating the report the user requests.
  2. Either **exclude sensitive data**, by telling users not to include it and stripping photos and sensitive sections before the OpenAI call, or collect **explicit, logged consent** for it.
  3. Make refusal stop the workflow.
- **Escalation needed?** **Yes, to a DPO or privacy lawyer**, for the Art. 9 approach.

**Finding 2 - Processor contracts and international transfers undocumented**
**Severity: Blocking** (for real CVs)
- **Description:** every processor that handles personal data needs an Art. 28 DPA. Transfers to the US need DPF certification or SCCs. The brief confirms neither for OpenAI, Notion, n8n or Pinecone.
- **Recommended action:**
  1. List every service and the exact fields it receives.
  2. Accept or sign the DPAs of OpenAI, Notion, n8n and Pinecone (if applicable).
  3. Check each vendor's DPF certification, or put SCCs and a transfer impact assessment in place.
  4. Use EU regions where available.
  5. Confirm in the contracts that vendors cannot use the data to train their models.
- **Escalation needed?** **Yes, to the DPO or legal counsel**, for the transfer assessment.

**Finding 3 - Storage limitation and access to stored reports**
**Severity: Significant**
- **Description:** according to the brief, reports are saved or delivered through Notion, and logs and vectors *may* also keep CV data (not verified). No retention periods or access controls are confirmed, which goes against storage limitation (Art. 5(1)(e)) and security (Art. 32). It also makes erasure requests (Art. 17) hard to fulfil.
- **Recommended action:**
  1. Set a retention schedule (e.g. CV deleted right after generation, reports deleted after 30 days, logs after 14 days, no CV vectors).
  2. Restrict Notion access and disable public sharing links.
  3. Document an erasure procedure that covers all services.
- **Escalation needed?** **No.**

**Finding 4 - DPIA likely required but not conducted**
**Severity: Significant** (becomes Blocking if the DPO confirms a DPIA is required before launch)
- **Description:** at least two EDPB criteria appear to apply:
  - **evaluation of a person** (inferred strengths and gaps about work-related suitability)
  - **innovative technology** (an LLM generating content about individuals)

  Possible **sensitive data** in CVs and job seekers' dependent position add to the risk. The brief mentions no DPIA.
- **Recommended action:** run a DPIA screening now, and a full DPIA before processing real CVs at scale.
- **Escalation needed?** **Yes, to the DPO.**

**Finding 5 - Purpose limitation and third-party data**
**Severity: Significant**
- **Description:** recruiter contact details in job descriptions, and possibly CVs uploaded by someone other than the candidate, bring in third-party data with no clear basis and no Art. 14 information. Martha confirmed she **cannot verify whether the recovered Siemens test report was generated from a real person's CV**. If it was, keeping it as a project sample is storage of personal data for a new purpose with no basis or retention limit.
- **Recommended action:**
  1. Strip contact details from job descriptions before processing.
  2. Add an "I am uploading my own CV" confirmation.
  3. Check the Siemens test report: if its origin can't be confirmed as synthetic, **delete it** (and any copies in Notion and n8n), and use only clearly synthetic CVs for future testing.
- **Escalation needed?** **No.**

**Finding 6 - Accuracy of generated content about the candidate**
**Severity: Minor**
- **Description:** STAR examples and inferred gaps are personal data about the candidate, and the accuracy principle (Art. 5(1)(d)) applies. The brief notes that the accuracy of the sample STAR achievements was not verified. Because the candidate reviews the output, the impact is limited.
- **Recommended action:** label suggestions clearly as drafts to check against the CV, and test whether the model invents achievements.
- **Escalation needed?** **No.**

### Section 4 - Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | **Gap identified** | Only a "permission" step is described, and it is unverified. There is no Art. 9 condition for sensitive CV data. |
| Purpose limitation respected (no incompatible reuse) | **Gap identified** | Recruiter contacts and possible third-party CVs. The sample report's origin is unclear. |
| Data minimisation (only necessary data collected) | **Cannot determine from brief** | The fields sent to each service are not confirmed. Photos and contacts are probably not needed. |
| Controller/processor roles mapped and DPAs in place | **Gap identified** | The production controller is unspecified, and no DPAs are confirmed. |
| International transfer mechanism documented | **Gap identified** | Regions and mechanisms are not confirmed for the US vendors. |
| DPIA conducted if required | **Gap identified** | A DPIA is likely required (evaluation + innovative technology), and none is mentioned. |
| Article 22 safeguard in place if automated decisions affect people | **Appears met (not applicable)** | The tool gives advice to the candidate and makes no decisions about them. The candidate decides how to use it. |
| Privacy notice covers AI processing | **Cannot determine from brief** | Only a permission step is mentioned. No privacy notice is described. |
| Data subject rights can be operationalised within deadlines | **Gap identified** | No retention or erasure procedure across n8n, Notion, OpenAI and Pinecone. |

### Section 5 - Overall recommendation

**Do not proceed with real CVs. Prototype testing with clearly synthetic data can continue.** Martha confirmed that the agent is currently inactive with no production operator, so this recommendation sets the conditions for any future launch.

Two **blocking** findings must be resolved before any real candidate's personal data is processed:
1. **No demonstrable lawful basis or Art. 9 condition** for CV data that may include sensitive information (Finding 1).
2. **No confirmed DPAs or transfer mechanisms** for the US vendors that would receive full CVs (Finding 2).

Once these are fixed, the significant findings (retention and Notion access, the DPIA, third-party data) should be completed before go-live. At that point the system could realistically move to **proceed with conditions**. The tool's purpose, helping candidates prepare, is legitimate and low-impact on decisions, so these gaps are fixable.

### Section 6 - What this report is not

This report is an independent first-pass review based only on the builder's data processing brief. It is **not a legal opinion, not a DPIA, and not a certification of compliance**. The client should obtain legal review, and involve a data protection officer, before relying on this assessment or processing real applicants' data.

---

## Phase 5 - Debrief conversation (with Martha, 17–18 November 2026, held in writing)

**1. Auditor presents:** I sent Martha this full audit report (findings, severities, lawful basis, DPIA conclusion, recommendation) on 18 November 2026.

**2. Builder responds:** Martha added context that the brief did not contain:
- The agent is a bootcamp project, **currently inactive**, with no production operator.
- She deliberately treated the workflow's **permission step as separate from valid GDPR consent**, because its wording, refusal handling and logging are not verified.
- She has **no lawful basis for model training or improvement**, and none is intended.

**3. Compare lawful basis selections (primary purpose: analysing the CV to generate the requested report)**

| | Lawful basis |
|---|---|
| Martha's self-audit | **Contract (Art. 6(1)(b))** for CV analysis and the report. **Legitimate interests (Art. 6(1)(f))**, with an LIA, for security and troubleshooting logs. No basis for model training. |
| My peer audit | **Contract (Art. 6(1)(b))** for the report, plus **exclusion of sensitive data or explicit consent (Art. 9(2)(a))** for special-category CV content |
| Which is stronger and why | **We agree on the primary basis (contract)**, and we both rejected the unverified permission step as GDPR consent. The strongest position **combines both audits**. Martha's version covers a purpose I left open (**logs, under legitimate interests**). Mine adds the **Article 9 condition**, which is required because no Art. 6 basis alone allows processing of health or religion details in a CV. |

**4. Compare DPIA conclusions**

| | DPIA required? |
|---|---|
| Martha's self-audit | A **documented DPIA screening is necessary** before deployment. A full DPIA is **not yet established as mandatory**, because it depends on scale, data categories and safeguards. |
| My peer audit | **Likely required** (evaluation of a person + innovative technology, plus possible sensitive data) |
| Agreement or specific ambiguity | We worked through the EDPB criteria. We agree that **innovative technology** applies and that **sensitive data** is possible but incidental. Scale is unknown, because the agent is inactive. **The specific ambiguity is criterion 1 (evaluation or scoring)**: does a CV-to-role comparison count when the candidate requests it for their own benefit and no one else uses it? **Agreed position:** document a DPIA screening now, and do a **full DPIA before any processing of real CVs** as a **precautionary approach**, because two criteria are arguably met and the EDPB says that generally triggers a DPIA. We both acknowledge that whether it is **legally mandatory** still depends on the risk assessment (scale, data categories, safeguards). |

**5. Compare gap lists**

| Martha's self-audit findings | My peer audit findings | Caught by only one of us |
|---|---|---|
| 1. Data exposure to vendors (fields, regions, contracts)<br>2. Retention and deletion<br>3. Sensitive data and minimisation (photos, contacts)<br>4. Consent and transparency<br>5. AI-generated inaccuracies (Siemens report) | 1. Lawful basis and Art. 9 condition (Blocking)<br>2. DPAs and US transfers (Blocking)<br>3. Retention and Notion access (Significant)<br>4. DPIA (Significant)<br>5. Third-party data and purpose limitation (Significant)<br>6. Accuracy (Minor) | **Only the external audit (me):**<br>- **third-party personal data**: recruiter contacts in job descriptions, and no check that the CV belongs to the uploader<br>- the **Siemens test report as a possible purpose-change and retention problem** (Martha saw it only as an accuracy issue)<br>- an explicit **Art. 9 condition**<br>- **Notion share links**<br><br>**Only the self-audit (Martha):**<br>- a **lawful basis for logs**<br>- **no basis for model training**<br>- **combining CV and job-description data** as a DPIA criterion<br>- the internal fact that the **permission step is unverified in the workflow export** |

**Blocking vs significant:** Martha recommended *proceed with conditions, using synthetic data*. I recommended *do not proceed with real CVs*. We agreed that these are the **same practical outcome**: no real CVs until the safeguards are verified. Under the lab's severity guide, a missing lawful basis or a missing DPA for a processor that handles personal data counts as **Blocking for live processing**, so we agreed to label Findings 1 and 2 as Blocking.

**6. Joint closing note (written together):**
Self-assessment is strongest on what we built and weakest on what we never thought of as data. Martha saw her Siemens test report as an accuracy problem, while an outside reviewer saw stored personal data with a new purpose. In the same way, recruiter contacts inside job descriptions were invisible to the builder because they arrive inside user uploads. The hardest GDPR gaps to catch in your own work sit between components: third-party data inside inputs, test outputs kept "just in case", and vendor terms you assumed rather than checked.

**Debrief sign-off (18 November 2026):** Martha confirmed she agrees with this comparison, the DPIA approach and the joint closing note. We also agreed to mark details that are **not yet verified** as open points rather than confirmed facts (see the Phase 3 log). I corrected the wording of my audit accordingly and removed a duplicated table in Phase 3.

---

## Reinforce

**Martha's audit of my AI Search Visibility Agent - my response**

Martha found five Significant issues:
1. DPAs and controller/processor roles not verified
2. Transfers not documented
3. No retention for n8n logs and reports
4. Lawful bases, transparency and personal-brand processing need clarification
5. Personal Gmail and QuickChart IP exposure

Her recommendation was **proceed with conditions for a limited demonstration**. On the DPIA, she concluded that a screening is advisable but a full DPIA is not automatically required. **I agree with all five findings and with her recommendation**, and our DPIA conclusions are the same. My clarifications:
- n8n runs on **n8n Cloud** (n8n GmbH, Germany).
- Sending from a personal Gmail account is confirmed. I will move to a business email service with a DPA.
- I propose **excluding personal brands** from the tool's intended use, rather than assessing them.

**Questions I could not answer from my own documentation:** the n8n Cloud hosting region, each US vendor's DPF certification status, and whether Render logs request bodies. My README explains *how* the agent works, but nothing documents *where* data goes or *on what terms*.

**A finding I initially disagreed with:** Martha marked "lawful bases need clarification", and at first I felt my self-audit had already assessed them, including a full LIA. After the debrief I agree with her. She could only see my brief, and my project documentation contains no LIA, privacy notice or record of processing. A lawful basis that exists only in a lab document, and not in the project, cannot be shown to a regulator. That is exactly the accountability gap my self-audit's Verify section found.

---

## Stretch - Remediation plan for Finding 2 (processor contracts and transfers)

- **Artifact that closes the gap:** a **vendor and transfer register**, which is a one-page table listing each service, the data fields it receives, its region, DPA status, transfer mechanism (DPF or SCCs) and training opt-out. It comes with the signed or accepted DPAs and a short transfer impact assessment for OpenAI and Notion.
- **Owner:** Martha, as controller and operator, prepares the register and accepts the vendor DPAs. The **DPO or external counsel** reviews the transfer impact assessment.
- **Timeline:** about 1–2 weeks:
  - Days 1–3: map the fields per service from the n8n workflow export.
  - Days 4–7: accept the DPAs, check DPF certifications, and switch to EU regions where available.
  - Week 2: the transfer impact assessment and legal review.
- **Evidence for a regulator:**
  - the completed register
  - copies of the accepted DPAs with dates
  - screenshots of each vendor's DPF certification entry or the signed SCCs
  - the transfer impact assessment
  - an n8n workflow export showing that only the listed fields are sent
