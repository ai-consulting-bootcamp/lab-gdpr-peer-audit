# Phase 1: Read and annotate - Model Intake Brief (Sergii Rostovskyi), GDPR lens

## Exchange log (ground rules)

| Date | What | Notes |
|---|---|---|
| 26 Nov 2026 | **Received:** the teammate's data processing brief, [`model-intake-data-processing-brief.md`](https://github.com/s-rostovskyi/lab-gdpr-self-audit/blob/89b0b5cf0a0022fc122e49c1cdcfbf14ce8582ad/model-intake-data-processing-brief.md) (commit `89b0b5c`) | His self-audit repo keeps the brief in its own file. I opened **only that file**. |
| 26 Nov 2026 | **Received:** project documentation at the snapshot the brief names, [`e384f3a`](https://github.com/s-rostovskyi/model-intake-brief/tree/e384f3a41b5c74119786f55865ebe4e7e6cfb73c) | README (architecture diagram, tool table) and the two sample reports in `samples/`. These count as the "architecture or data flow diagrams" the lab allows. |
| Not opened before the debrief | `model-intake-gdpr-assessment.md`, `model-intake-compliance-memo.md`, `model-intake-accountability-and-design.md`, `model-intake-evidence-and-sources.md` | His lawful bases, DPIA screen, memo and gap findings. The evidence register (E1-E9, L1-L4) is cited by the brief, but it may hold conclusions, so I left it closed. I saw the filenames in a directory listing only. |
| 26 Nov 2026 | **Clarifying questions** logged in writing (see `02`) | No live contact before Phase 5. Answers in the debrief come from his written self-audit; anything beyond it is marked **simulated** (see `04`). |

**Context I can't unlearn:** I audited the same system for the EU AI Act two labs ago. I know the architecture well, so my independence is about *conclusions*, not about the system.

## Annotations

The brief was read once without notes, then annotated. **Key:** 🟪 **[PD]** = personal data category (+ special-category status) · 🟠 **[?]** = unclear, needs confirming (circle) · 🟦 **[EU]** = crosses an EU border or non-EU vendor (underline) · 🚩 **[PL]** = possible purpose-limitation issue.

| # | Brief text (excerpt) | Mark | Annotation |
|---|---|---|---|
| 1 | "local, individual educational use, public model documents only, no real client data and no other users" | 🟠 ? | Defines today's scope. Not covered by the household exemption (Art 2(2)(c)): the project is published and demonstrated. Sergii is the **controller** today. Is a client deployment planned? His AI Act brief assumed one. |
| 2 | "No privacy notice, retention rules, deliberately selected processing regions or DPA documentation has been arranged" | 🟠 ? | An honest statement of four gaps: Art 13/14, Art 5(1)(e), Chapter V and Art 28. |
| 3 | "Standard vendor terms may incorporate a DPA; acceptance is unverified" | 🟠 ? | **Key open fact.** Whether the processors already handling data are under contract decides whether this is a *blocking* finding. |
| 4 | "author names, identifiable repository handles, named business contacts and email addresses" | 🟪 PD | **Third-party personal data, collected indirectly** (Art 14). Ordinary data, not Art 9. Collected without the people knowing. |
| 5 | "source URLs and quotes can preserve them" | 🟪 PD · 🚩 PL | Names travel from the source into the **report**, which is kept and shared (P3). The data outlives its source. |
| 6 | "operator's IP address and account-linked request metadata" | 🟪 PD · 🟦 EU | The **operator's own** data, sent to every vendor. In a client deployment, the operator is an **employee**, which brings in employee-data rules (§26 BDSG in Germany ⚖️). |
| 7 | "A synthetic probe proves that contact details survive into the outgoing LLM payload" | 🟪 PD · 🟦 EU | Good evidence work: a tested fact, not a guess. It also shows **no redaction step** exists before OpenAI. |
| 8 | "P3: retain or share the report for human review and educational demonstration" | 🚩 PL · 🟠 ? | Two purposes in one line. Demonstration means publishing (`samples/` in a public repo). The two shipped samples contain no personal names or emails (I checked), but nothing *prevents* it. Who receives shared reports? |
| 9 | "P4: operate and troubleshoot … vendor service metadata" | 🟪 PD | Operator metadata. Legitimate interests is the natural basis. |
| 10 | "sends model queries to Tavily, URLs to Jina Reader, and model IDs to Hugging Face" | 🟦 EU · 🟪 PD | Model IDs can contain a **personal account handle** (`username/model`). Tavily and Hugging Face are US-based; Jina's processing location isn't stated. |
| 11 | "up to 3,500 characters per source go to OpenAI's assessment API" | 🟦 EU · 🟪 PD | The main transfer. US processing unless EU data residency is set up. |
| 12 | "link verification contacts source websites directly" | 🟦 EU | Exposes the operator's IP address to **arbitrary third-party sites**, anywhere in the world. Low risk, but those sites become independent controllers of that log entry. |
| 13 | "OpenAI embeddings and Pinecone handle the regulatory branch" | 🟦 EU | Non-personal regulatory text, so no transfer issue *if* the queries are fixed (they are: one per checklist item). Pinecone is US; region not stated. |
| 14 | "optionally to a downloaded file" | 🟠 ? · 🚩 PL | Once downloaded, no retention control exists. Where do exported reports live in a client setting? |
| 15 | "physical jurisdiction is unconfirmed" | 🟠 ? | Unusual but correct: a laptop's location matters for where processing happens. In practice it's the EU. |
| 16 | "`store: false` does not establish account-level zero retention" | 🟦 EU | Correct, and a detail most audits miss. OpenAI abuse-monitoring retention still applies unless ZDR is approved. |
| 17 | "neither approves deployments nor decides a person's employment, credit or benefits" | 🟠 ? | Points away from **Art 22**: the decisions concern models, not people. I accept it. Watch-out: a report could indirectly affect a named individual developer's reputation if it is shared widely. |
| 18 | "Human review is intended but not enforced" | 🟠 ? | Matters for accuracy (Art 5(1)(d)), not Art 22, because no person is the subject of a decision. |
| 19 | "future client/vendor roles depend on activities and contracts" | 🟠 ? | The brief leaves the role map open. This is my clarifying question 2. |

## CFU 1 - Recognize

| Question | Answer |
|---|---|
| **Personal data categories** | (1) **Third-party identity and contact data** in public documentation: author names, repository handles, business contacts, email addresses, carried into payloads, quotes, URLs and reports. (2) **Operator data**: IP address, API account, request metadata. (3) In a client deployment: **employee data** of reviewers (who ran which report). |
| **Special category (Art 9)?** | **Not expected and not targeted.** Model docs rarely contain health, political or similar data. It **can't be excluded**: arbitrary web text sometimes holds it (e.g. an author bio, or example rows in a dataset card). Nothing in the outputs *infers* special-category data about a person. |
| **Crosses an EU border?** | **Yes.** OpenAI (US), Tavily (US), Hugging Face (US-headquartered), Pinecone (US, region unstated), Jina Reader (location unstated), plus direct calls to source websites anywhere. **No transfer mechanism is documented** for any of them. |
