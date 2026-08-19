# GDPR Audit Report — TenderAI Assistant

**Auditor:** Akansha Verma
**System audited:** TenderAI (Project 3, built by teammate Vincent)
**Basis for review:** Teammate's data processing brief only, exchanged per lab kick-off rules — no access to Vincent's lawful basis assessments, DPIA analysis, findings, or memo before this audit was written or the debrief occurred.
**Date:** 19 August 2026

## Confirmation of exchange: 
This audit was conducted against the "TenderAI Assistant — GDPR Data Processing Brief" (dated 19 August 2026, status "[pre_audit_inventory](pre_audit_inventory.md)") only. No architecture diagram beyond the data-flow sequence embedded in the brief itself was provided. *

### Ground rules
Ground rules were respected — this report was drafted independently until Phase 4 based on data processing brief, before any discussion with Vincent. The clarifying questions arising from the brief's unresolved points are documented in Phase 3.

---

## Phase 1: Read and Annotate

*First-pass annotation of the brief, completed before drafting any table or finding. This is the evidence base for everything below.*

### Personal data / special-category annotations
- Identification/contact information — name, professional email, business phone, other contact details (Section 3). Not special category.
- Professional information — job title, employer/affiliation, employment history, qualifications, certifications, project responsibilities, professional biography (Section 3). Not special category, but a professional biography or CV could incidentally narrate something that touches Article 9 (e.g., a career gap tied to a disclosed health event) — flagged as a residual inference risk, not a confirmed one.
- Free-text content written by or about an identifiable person (Section 3) — this is the widest and least controllable category, since the brief itself says this "could include text written by an identifiable person or information describing an identifiable person" without further bounding.
- AI-generated/derived information — extracted text, chunks, embeddings, retrieved passages, assessments, evidence summaries, draft responses (Section 3). The brief itself correctly flags that these "must be assessed to determine whether they contain or remain linked to personal data" — a mature observation for a self-authored brief to include, treated as a live open question below rather than assumed resolved.
- Special-category data (Section 11): the brief explicitly lists the full Article 9 category set as a possibility in production documents (health, disability, ethnic origin, religious belief, trade union, political opinion, sexual orientation, biometric) and does not rule any of them out — status is self-marked **TBD — legal review**, treated here as an honest and appropriately unresolved answer rather than a gap in the brief's reasoning.

### Unclear points / information requiring confirmation
- The client organisation's "exact GDPR role must be confirmed for each deployment" (Section 6) — the brief doesn't commit to controller status being fixed across all client deployments.
- OpenAI's and Pinecone's "precise contractual role, applicable service terms, data-processing terms, retention settings, and processing locations" are all separately marked TBD (Section 6) — five distinct open sub-questions bundled into one TBD.
- Whether TenderAI is offered as a hosted service or self-hosted deployment is not addressed anywhere in the brief — this is a gap in the brief itself, not just an item the brief flags as TBD, and it directly affects whether Vincent's own entity has a processing role.

### EU-border / non-EU vendor flow annotations
- OpenAI and Pinecone are both named as external cloud services (Section 8); the brief explicitly states geographic processing/storage locations "have not yet been documented in this project" and that it is "not currently possible to conclude... whether all personal-data processing remains within the EEA."
- Section 9 names the specific Chapter V mechanisms that would need to be identified (adequacy decision, SCCs, other) rather than just flagging "transfers may occur" — a well-scoped TBD.

### Purpose-limitation annotations
- Section 5 explicitly names purpose limitation as a live, unresolved question: "The system should not assume that information uploaded for one business purpose can automatically be reused for unrelated AI processing," marked **TBD — legal review for production deployments.** The brief does not claim purpose limitation is respected; it correctly declines to claim that.
- Six distinct purposes are listed (ingestion, KB creation, requirement analysis, evidence retrieval, response generation, reporting). Purpose limitation needs to be assessed per purpose, not once for the whole system — noted for Phase 2.

### Automated decision-making annotation
- The brief's own data-flow diagram (Section 7) shows **"Human review by client team"** as an explicit step positioned before "Optional report generation." This is more specific than "human review is part of the workflow" — it's placed in the data flow itself, between AI output and any downstream business use.
- The brief's own conclusion: "No current Article 22 use case identified in the MVP... TBD — reassess if later extended to make decisions about identifiable individuals." Treated as correct in Phase 4, with one caveat: TenderAI's outputs are about tender/bid readiness (a business decision), not decisions "about" an individual data subject, so Article 22 is unlikely to apply even at production scale — but the brief is right not to close this off permanently.

---

## 2. Probe

The probe step tests the initial observations from the brief by asking what is known, what is uncertain, and what evidence would be needed before reaching a compliance conclusion.

### Probe 1 — Personal data and special-category data

**What the brief establishes:**  
Tender documents and company knowledge-base material may contain names, professional contact details, employment history, qualifications, biographies, and free-text content.

**What remains uncertain:**  
The brief does not establish whether production documents contain special-category personal data under Article 9 GDPR.

**Evidence needed:**  
A representative production-data inventory or documented data classification showing whether Article 9 data can occur.

**Provisional conclusion:**  
Do not assume special-category data is absent. Treat its presence as a residual risk requiring confirmation before production use.

### Probe 2 — Processing purposes

**What the brief establishes:**  
The system is used for tender analysis, bid-readiness assessment, retrieval, evidence extraction, and generation of draft response material.

**What remains uncertain:**  
The brief does not fully establish whether all proposed uses of uploaded material are compatible with the purposes for which the information was originally collected.

**Evidence needed:**  
A documented purpose inventory and compatibility/lawful-basis assessment for each material processing purpose.

**Provisional conclusion:**  
Purpose limitation cannot be confirmed from the brief alone.

### Probe 3 — Roles and deployment model

**What the brief establishes:**  
The system uses OpenAI and Pinecone as external services, while the precise role of the TenderAI operator is not fully documented.

**What remains uncertain:**  
Whether TenderAI is operated as a hosted service or distributed as self-hosted software.

**Evidence needed:**  
A confirmed deployment architecture and contractual role map.

**Provisional conclusion:**  
The builder/operator role cannot be conclusively determined from the brief alone.

### Probe 4 — International transfers and vendors

**What the brief establishes:**  
OpenAI and Pinecone are external cloud services.

**What remains uncertain:**  
Processing/storage locations, applicable transfer mechanisms, retention settings, and vendor terms are not fully documented.

**Evidence needed:**  
Current vendor DPAs, processing locations, transfer safeguards, retention configuration, and training-use settings.

**Provisional conclusion:**  
International-transfer compliance cannot be confirmed from the brief alone.

### Probe 5 — Automated decision-making and human review

**What the brief establishes:**  
The system produces bid-readiness assessments and draft response material, with human review in the workflow.

**What remains uncertain:**  
The brief does not fully document whether any output could become a decision producing legal or similarly significant effects on an individual.

**Evidence needed:**  
A documented decision-flow description showing the role of human review and whether outputs directly determine decisions about individuals.

**Provisional conclusion:**  
Article 22 risk appears limited by human review, but the final assessment depends on the actual production workflow.

### Probe-to-question traceability

The probe findings above generated the Phase 3 clarifying-questions log. Each unresolved point was converted into a question specifying:

1. what information is needed;
2. why the information matters under GDPR; and
3. the provisional assumption used until the point is confirmed.

See **Phase 3: Clarifying Questions Log** for the resulting five questions.

---

## Phase 2: Personal Data and Role Map

### Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Identification/contact data (name, professional email, business phone, other contact details) | Client-uploaded PDF documents (company profiles, project references, tender docs, certifications) | Purposes 1–6: ingestion, KB creation, requirement analysis, evidence retrieval, response generation, reporting | **Gap in brief** — not confirmed; OpenAI/Pinecone processing locations undocumented (Section 8) | No |
| Professional information (job title, employer, employment history, qualifications, certifications, project responsibilities, biography) | Same as above | Same as above — primarily Purposes 2–5 | Same gap | No — but see residual inference risk noted in Phase 1 |
| Free-text content written by or about an identifiable person | Client-uploaded documents, unbounded by document type per the brief | Same as above | Same gap | **Gap in brief** — cannot be ruled out; brief itself lists full Art. 9 category set as possible (Section 11) |
| AI-generated/derived information (extracted text, chunks, embeddings, retrieved passages, assessments, draft responses) | Generated internally by TenderAI from the above | Purposes 2, 4, 5, 6 | Same gap — embeddings stored in Pinecone, location undocumented | Inherits status of source data; not separately assessed by the brief |

*Gap noted across the board: the brief does not state a retention period for any category, does not confirm whether personal data is deliberately filtered out of any ingestion step, and does not confirm document-level provenance beyond "client-uploaded."*

### Role map

> The following tables were completed solely from Vincent's data processing brief; where the brief is silent, the gap is explicitly recorded.

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Client organisation | Controller (per brief Section 6) — though the brief notes this "must be confirmed for each deployment," so treated here as the working assumption rather than a settled fact | Supplies enterprise documents; determines business purpose for using TenderAI | N/A — client is the controller |
| TenderAI application / Vincent (builder) | **Cannot determine from brief** — describes what the application *does* but never states whether it's operated as a hosted service (processor) or distributed as self-hosted software (no ongoing processing role) | Runs the pipeline described in Section 6/7 | **Cannot determine** — depends on the hosted-vs-self-hosted question, which is a gap in the brief itself |
| OpenAI | Processor (sub-processor) — role stated in brief, but "precise contractual role... must be verified" (Section 6) | Text embeddings; LLM processing of client documents and retrieved evidence | **TBD per brief** — needs to be confirmed/executed before production use |
| Pinecone | Processor (sub-processor) — same caveat as OpenAI | Stores document embeddings and associated metadata; retrieval infrastructure | **TBD per brief** — needs to be confirmed/executed before production use |

*International transfer note: the brief's own Section 9 correctly identifies transfer status as unresolved and correctly names the applicable Chapter V mechanisms. This audit agrees with that self-assessment and folds it into Finding 2 below rather than raising it separately.*

---

## Phase 3: Clarifying Questions Log

> Five clarifying questions are recorded below; each includes the information needed, the GDPR obligation affected, and a provisional assumption.

**1. Will TenderAI be deployed as a hosted service (Vincent processes client data on his own infrastructure) or as self-hosted software (the client runs it within their own environment)?**
- *Why it matters:* This is the single fact the brief never addresses, and it determines whether Vincent's entity is a processor at all — which in turn determines whether a builder–client DPA is required.
- *Provisional assumption:* Assuming a hosted-service model, since that's the higher-risk assumption to plan around and the more common MVP-to-pilot path.

**2. Section 5 lists six distinct processing purposes but marks purpose limitation as one single TBD. Is compatibility expected to be assessed once for the whole pipeline, or per purpose?**
- *Why it matters:* Purpose limitation is assessed against the *original* collection purpose for each data category, and one source document may feed multiple purposes each a different distance from why it was originally created.
- *Provisional assumption:* Assuming each purpose needs its own compatibility check, with Purposes 3–5 (requirement analysis, evidence retrieval, response generation) most likely to diverge from a document's original purpose.

**3. Does "Human review by client team" (Section 7) correspond to a mandatory, logged gate in the software, or is it a description of intended client behaviour the software doesn't currently enforce?**
- *Why it matters:* Affects how confidently "Appears met" can be claimed for the Article 22 safeguard row below, and matters separately for AI Act human-oversight-design obligations.
- *Provisional assumption:* Assuming this is currently a described workflow expectation rather than a technically enforced gate, based on the brief's own MVP-stage framing.

**4. Has either vendor's default data-retention or model-training-use configuration been reviewed for this specific use case?**
- *Why it matters:* A DPA alone doesn't resolve whether a vendor's default settings (e.g., using submitted content for model training) are compatible with purpose limitation and data minimisation.
- *Provisional assumption:* Assuming this has not yet been reviewed, since the brief bundles it into the same TBD as the DPA question rather than addressing it separately.

**5. Section 4 states production data may arrive indirectly through documents the client originally collected from employees, consultants, suppliers, or other third parties. Does the client have a lawful basis for the *original* collection that plausibly extends to this new AI-processing use?**
- *Why it matters:* TenderAI's own lawful-basis position depends in part on whether the client's original collection from third parties was itself compatible with feeding an AI RAG pipeline — an upstream gap becomes a downstream problem.
- *Provisional assumption:* Assuming this has not been assessed by the client, since the brief gives no indication it's been considered at the client-relationship level.

---

## Phase 4: Audit Report

### Section 1: System Summary

TenderAI is an enterprise RAG assistant that helps organisations analyse tenders and prepare evidence-based tender responses. Enterprise documents are ingested, extracted, chunked, embedded via OpenAI, and stored in Pinecone. When a user submits a tender requirement, the system retrieves relevant evidence via semantic search and uses an LLM to generate an assessment (supported / partially supported / insufficient) or a draft tender response. Per the brief's own data-flow diagram, outputs pass through human review by the client team before an optional report is generated. The current MVP is tested exclusively on synthetic company documents; the brief is explicit and self-aware that production deployment would involve real client documents likely to contain personal data, and marks most of the resulting GDPR questions as TBD rather than assuming them resolved.

### Section 2: Data and Role Map

The brief identifies four broad personal-data categories that could appear in production documents — identification/contact data, professional information, unbounded free-text content, and AI-derived/generated information — while correctly noting the current synthetic MVP does not intentionally contain any of them. The client organisation is treated as the controller, though the brief itself flags that this role "must be confirmed for each deployment." OpenAI and Pinecone are named sub-processors of document content and embeddings respectively; both are external cloud services with undocumented processing/storage locations, so international transfer status is correctly self-marked TBD. The most significant gap this audit adds beyond what the brief itself flags is that **the builder's (Vincent's) own role is never addressed at all** — the brief describes the client and both vendors in detail but is silent on whether TenderAI is a hosted service or self-hosted software, which is the fact the entire role map depends on.

### Section 3: Compliance Findings

**Finding 1 — Lawful basis and purpose-limitation assessment deferred across six distinct purposes**

*Severity:* Significant

*Description:* Section 5 lists six processing purposes and marks purpose-limitation compatibility as a single TBD, without a stated plan for assessing each purpose separately. No lawful basis is proposed anywhere in the brief for any purpose.

*Recommended action:* Complete a per-purpose lawful-basis and compatibility assessment before onboarding the first real client, giving particular attention to Purposes 3–5, which are furthest from a source document's likely original collection purpose.

*Escalation needed?* No — but must be resolved before production go-live, not treated as a "later" task.

**Finding 2 — No DPA/SCCs or vendor configuration confirmed for OpenAI or Pinecone**

*Severity:* Blocking (for production; not blocking for continued MVP/synthetic-data work)

*Description:* Both vendors are named sub-processors of document content and embeddings. The brief marks their contractual role, service terms, retention settings, and processing locations as TBD (Section 6), and separately marks international transfer mechanism as TBD (Section 9). Without a signed DPA, confirmed retention/training-use settings, and a valid Art. 46 transfer mechanism, this is a hard blocker for any real-client pilot.

*Recommended action:* Confirm DPAs/SCCs are executed, confirm EU-region processing configuration for both vendors, and review default data-retention/training-use settings before any non-synthetic document is processed.

*Escalation needed?* Yes — to whoever owns vendor contracts, before any real client document is ingested.

**Finding 3 — No data retention or erasure mechanism documented for any personal data category**

*Severity:* Significant

*Description:* Retention/deletion is listed as an open risk area (Section 12, item 7) but no lifecycle policy for source documents, chunks, or Pinecone embeddings is described. Embeddings are difficult to map back to and delete for a specific data subject once generated, complicating Art. 17 compliance.

*Recommended action:* Define retention periods per data category and a deletion procedure — including embedding-level deletion in Pinecone — before production use.

*Escalation needed?* No, but should be resolved alongside Finding 2.

**Finding 4 — Builder's (Vincent's) controller/processor role is entirely unaddressed in the brief**

*Severity:* Significant

*Description:* The brief documents the client's role and both vendors' roles in detail but never states whether TenderAI is operated as a hosted service or self-hosted software — the fact this entire role map depends on.

*Recommended action:* Decide and document the deployment model explicitly in the next revision of the data processing brief.

*Escalation needed?* No, but raised directly in the Phase 5 debrief as this audit's top clarifying question.

**Finding 5 — Privacy notice and data subject rights operationalisation not addressed**

*Severity:* Minor (at MVP stage) / Significant (at production stage)

*Description:* Data-subject rights are named as an open risk area (Section 12) but no privacy notice covering AI/RAG processing or access/erasure-handling process is described.

*Recommended action:* Draft a privacy notice addendum for AI processing and a lightweight rights-handling procedure ahead of any real-client pilot, informed by the retention work in Finding 3.

*Escalation needed?* No.

**Finding 6 — Upstream lawful basis for indirectly-collected third-party data is unconfirmed**

*Severity:* Minor (flagged for awareness; not yet confirmed as a live issue)

*Description:* Section 4 acknowledges production data may arrive indirectly through documents the client originally collected from employees, consultants, suppliers, or other third parties. Whether the client's *original* collection was compatible with this new AI-processing use is a layered question the brief doesn't address at the client-relationship level.

*Recommended action:* Raise this explicitly with each client during onboarding rather than assuming TenderAI's own lawful-basis work automatically covers it.

*Escalation needed?* No — but raised explicitly in the Phase 5 debrief.

### Section 4: GDPR Obligations Checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | Gap identified | Not proposed for any of the six purposes; correctly deferred per brief Section 5, but no assessment exists yet |
| Purpose limitation respected (no incompatible reuse) | Gap identified | Brief itself marks this TBD (Section 5); needs per-purpose assessment, not a single check |
| Data minimisation (only necessary data collected) | Cannot determine from brief | MVP uses synthetic data only; production minimisation approach is not described |
| Controller/processor roles mapped and DPAs in place | Gap identified | Client role stated but caveated; builder's role entirely unaddressed (Finding 4); vendor DPAs unconfirmed (Finding 2) |
| International transfer mechanism documented | Gap identified | Brief's own Section 9 correctly self-identifies this as TBD |
| DPIA conducted if required | Cannot determine from brief | Not assessed; likely not required at current MVP/synthetic-data scale, but no formal trigger analysis exists yet |
| Article 22 safeguard in place if automated decisions affect people | Appears met | Data-flow diagram shows an explicit human-review step before reporting; brief's own conclusion (no current Art. 22 use case) is reasonable |
| Privacy notice covers AI processing | Gap identified | Not described anywhere in the brief |
| Data subject rights can be operationalised within deadlines | Gap identified | No retention/deletion or person-indexed lookup mechanism described |

### Section 5: Overall Recommendation

**Overall recommendation: Proceed with conditions**

**Proceed with conditions.** The MVP itself, built and tested exclusively on synthetic data, has no blocking findings and can continue in its current form. It should not move to a real-client pilot until: (1) DPAs, region configuration, and retention/training-use settings with OpenAI and Pinecone are confirmed (Finding 2); (2) a retention and deletion policy for source documents and embeddings exists (Finding 3); and (3) the builder's own controller/processor role is explicitly documented (Finding 4). None of these are large lifts individually, but all three sit upstream of processing a single real client document, and the third — the builder's own role — is the most foundational, since it determines who owns closing the other two.

### Section 6: What This Report Is Not

This report is not a legal opinion, not a DPIA, and not a certification of compliance. The client should obtain legal review before relying on this assessment.

---

## Phase 5: Debrief Conversation

*Completed jointly with Vincent following the six-step sequence in the lab instructions.*

**Step 1 — Auditor presents** 

Akansha walked through the report above without interruption, emphasising Finding 4 (the builder's-role gap) as the item this audit treats as most foundational, since it determines who owns closing Findings 2 and 3.

**Step 2 — Builder responds** 

Vincent confirmed the intended model for the MVP-to-pilot stage is a **hosted service** — Vincent's own infrastructure would run TenderAI on behalf of each pilot client, at least until a client specifically requests self-hosting. This resolves Clarifying Question 1 in favour of the audit's working assumption and confirms Finding 4's Significant severity was appropriate. Vincent also confirmed the "Human review by client team" step (Clarifying Question 3) is currently a described workflow expectation communicated to pilot users, not yet a technically enforced gate in the Streamlit interface — matching this audit's cautious assumption.

**Step 3 — Compare lawful basis selections**
- Akansha's position: Did not propose a specific basis, per the lab's independence rules, but noted legitimate interest or contract performance (on behalf of the client-controller) as the likely fit for most purposes.
- Vincent's position (self-audit): Legitimate interests, for the client-controller's processing of their own enterprise documents, with the caveat that Vincent's own hosted-service role as processor does not itself require a separate lawful basis — a processor acts on the controller's instructions rather than needing its own Art. 6 basis.
- Which is stronger and why: Vincent's framing is more precise — it correctly distinguishes the controller's lawful basis from the processor's separate obligations (DPA, security, sub-processor management), which this audit's report did not fully separate out. Agreed as the stronger position.

**Step 4 — Compare DPIA conclusions**
- Akansha's position: Cannot determine from brief; likely not required at current MVP/synthetic-data scale, but no formal trigger analysis was possible from the brief alone.
- Vincent's position: Also concluded a DPIA is not currently required at MVP stage, but flagged that production-scale deployment across multiple pilot clients would very plausibly trigger "large-scale processing" and "matching/combining datasets" (tender requirements cross-referenced against KB evidence) under the EDPB's nine criteria.
- Agreement reached: both audits converge on "not required yet, likely required at production/multi-client scale" — no disagreement to work through further.

**Step 5 — Compare gap lists**
- What the self-audit caught that this external audit missed: Vincent's self-audit had already identified the controller/processor lawful-basis distinction noted in step 3, which sharpens this audit's Finding 1.
- What this external audit caught that the self-audit missed: Vincent's self-audit had not explicitly named the builder's own hosted-vs-self-hosted role as an open question in the *brief itself* — Vincent knew the answer but hadn't recognised that the brief, as written, doesn't state it.

**Step 6 — Joint closing note**
Independent review caught a documentation gap the builder didn't know was a gap — Vincent knew TenderAI's deployment model but hadn't realised the brief never said so, because that answer felt too obvious to a builder to need writing down. Self-assessment is weakest exactly where a builder's own tacit knowledge quietly stands in for something that was never actually documented; a reader with no access to that tacit knowledge is what surfaces it.

---

## Reinforce

**Finding I initially disagreed with, post-debrief:** Vincent's self-audit initially treated Finding 4 (the builder's role) as a Minor item, on the reasoning that he personally knew the answer and didn't see it as a real compliance gap. After the debrief, I still think Significant is the right severity, not Minor — the point of documentation is that it survives beyond what's currently in the builder's head, and a new team member, an investor, or a future auditor reading only the brief would hit exactly the same gap this audit did. Vincent agreed with this reasoning during the debrief and revised the severity in his own tracking, so this is now a resolved rather than an open disagreement.

---

## Stretch

**Remediation plan for the most significant finding (Finding 2 — No DPA/SCCs or vendor configuration confirmed for OpenAI or Pinecone):**

- **Artifact that closes the gap:** Executed DPAs (or confirmed acceptance of standard DPA terms) with OpenAI and Pinecone, EU-region processing configuration confirmed for both, and a short internal memo documenting each vendor's data-retention/training-use settings as reviewed and accepted for this use case.
- **Owner:** Vincent, as the operator of the hosted service (confirmed in the Phase 5 debrief), owns execution; a DPO or external counsel should review before any real client document is processed.
- **Realistic timeline:** 1–2 weeks — both OpenAI and Pinecone offer standard, self-service DPA acceptance and EU-region configuration for most account tiers, so this is largely an administrative and configuration task rather than a negotiated contract.
- **Evidence that would confirm closure to a regulator:** Signed/accepted DPA documentation from both vendors, a screenshot or export confirming EU-region configuration, and the internal memo noting retention/training-use settings reviewed, with the date each step was completed and by whom.
