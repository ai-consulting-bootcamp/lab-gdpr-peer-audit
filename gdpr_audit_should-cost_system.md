# GDPR Audit — Should-Cost Estimation System (Teammate's Project 3)

**Auditor:** Anand Narasipuram
**System audited:** LangGraph/n8n should-cost estimation pipeline (part cost, freight, overhead calculator)
**Source document:** Teammate's Kick-off data processing brief (dated as received)

---

## Phase 2 — Personal Data & Role Map

### Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Free-text part description | User input at request time | Classification / cost estimation | Depends on requester location — not stated | No |
| Material description | User input | Cost estimation | Not stated | No |
| Part weight | User input | Cost calculation | Not stated | No |
| Stock utilization fraction | User input | Cost calculation | Not stated | No |
| Source/destination **business** addresses | User input | Geocoding → freight distance (via OpenCage) | Likely yes (OpenCage; jurisdiction not stated) | No — *but see Finding 1: could be inferable if address string includes a sole trader's name* |
| Annual production quantity | User input | Cost calculation | Not stated | No |
| Boolean feature flags | User input | Cost calculation | Not stated | No |
| **Not addressed in brief:** requester identity/authentication, IP address, request timestamps/logs | Infrastructure layer (n8n, OpenAI, Pinecone, Google, Notion access logs) | Unknown | Unknown (all four named vendors are US-based) | Unknown |

### Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Client (end user of the should-cost tool) | Controller (assumed — not confirmed in brief) | Submits part spec, receives estimate | N/A (controller) |
| Builder (teammate's team) | Processor *or* Controller — **undocumented**, see Finding 4 | Runs pipeline, orchestrates all vendor calls | Depends on role determination |
| OpenAI | Sub-processor | LLM classification + narrative generation | Yes — not confirmed in brief |
| Pinecone | Sub-processor | Vector storage/retrieval (RAG corpus) | Yes — not confirmed in brief |
| CommodityPriceAPI | Sub-processor | Live material pricing lookup | Likely low-risk (no personal data in this call), but Yes in principle |
| OpenCage | Sub-processor | Geocoding of business addresses | Yes — not confirmed; jurisdiction also not stated |
| Google Sheets API | Sub-processor | Report delivery | Yes — not confirmed |
| Notion API | Sub-processor | Report delivery | Yes — not confirmed |

**International transfer note:** OpenAI, Pinecone, Google, and Notion are confirmed US-based. No transfer mechanism (SCCs, EU-US Data Privacy Framework certification) is documented for any of them. OpenCage's jurisdiction isn't stated at all.

---

## Phase 3 — Clarifying Questions Log

1. **What identifies the "user" who submits a request?** (name/email/login, or fully anonymous form submission?)
   *Why it matters:* Determines whether any personal data enters the pipeline at all — this is the load-bearing question for the entire "no personal data" conclusion.
   *Provisional assumption:* Treating this as unknown/unconfirmed rather than assuming anonymity, since the brief doesn't say either way.

2. **Are IP addresses, timestamps, or other request metadata logged** by n8n, OpenAI, Pinecone, or the hosting infrastructure?
   *Why it matters:* IP addresses are personal data under GDPR (Breyer, CJEU 2016) regardless of whether the business payload is personal. If logged and retained, this alone brings the system into scope.
   *Provisional assumption:* Standard infrastructure logging is occurring by default, since nothing indicates it has been disabled or anonymized.

3. **Could a source/destination "business address" ever resolve to a named individual** (e.g., a sole proprietorship or freelance machine shop operating under a person's name)?
   *Why it matters:* GDPR applies to data *relating to* a natural person — a business address that functions as a sole trader's identifier can be personal data even though it's labeled "business."
   *Provisional assumption:* Low likelihood given the industrial/manufacturing context, but not ruled out by the brief.

4. **Is the Builder operating this tool for its own internal procurement, or on behalf of a client company?**
   *Why it matters:* This determines controller vs. processor status for the Builder itself, which determines who signs DPAs with the six vendors and who bears primary Article 5/28 obligations.
   *Provisional assumption:* Treating the Builder as the controller, since the brief describes the tool being used by "a human buyer" without naming a separate client entity.

5. **Do DPAs exist with OpenAI, Pinecone, CommodityPriceAPI, OpenCage, Google, and Notion**, and do any of them cover an EU-US transfer mechanism (DPF certification or SCCs)?
   *Why it matters:* Required under Article 28 the moment any personal data (per Q1–Q3) flows to these vendors; currently unconfirmed for all six.
   *Provisional assumption:* Assuming standard vendor terms only (no bespoke DPA) until confirmed otherwise, since none is mentioned in the brief.

---

## Audit Report

### Section 1 — System summary

The system takes a free-text part specification (description, material, weight, stock utilization, business origin/destination addresses, production volume, and process flags) and produces a should-cost estimate — material, labor/process, freight, and overhead — delivered as a report and live spreadsheet. It's used by a human buyer as one input into a supplier negotiation and doesn't score, rank, or make determinations about any individual. Six external services support the pipeline: OpenAI (LLM), Pinecone (vector RAG), CommodityPriceAPI (pricing), OpenCage (geocoding), and Google Sheets/Notion (delivery) — four of which are confirmed US-based.

### Section 2 — Data and role map

Covered above in Phase 2. Headline: the *primary payload* (part specs, business addresses, quantities) is plausibly non-personal, but the brief's "explicit confirmation" of zero personal data doesn't address the infrastructure layer — authentication, IP logging, or request metadata — where personal data typically lives even in business-to-business tools. The controller/processor split between the Builder and its client (if any) is also undocumented, as are DPAs with all six vendors.

### Section 3 — Compliance findings

**Finding 1 — Personal-data scope determination is incomplete**
Severity: **Significant**
Description: The brief concludes "this system does not process personal data" based on a walkthrough of the business payload fields, but doesn't address (a) who the requesting "user" is and whether they're identified, (b) infrastructure-level logging (IP, timestamps) across n8n/OpenAI/Pinecone, or (c) whether a business address could resolve to a named sole trader. The conclusion is well-argued for the fields it covers, but it closes the question before covering the whole system.
Recommended action: Confirm the three open items in Clarifying Questions 1–3 before treating "no personal data" as final.
Escalation needed? Yes — to the system owner, since it's the premise the rest of the compliance posture rests on.

**Finding 2 — International transfer mechanism undocumented**
Severity: **Significant**
Description: OpenAI, Pinecone, Google, and Notion are confirmed US-based; OpenCage's jurisdiction isn't stated. If Finding 1 surfaces any personal data, no SCCs or DPF certification are documented for any of these vendors.
Recommended action: Document each vendor's transfer basis (DPF certification status or SCCs within the DPA) and confirm OpenCage's location, contingent on Finding 1.
Escalation needed? Yes, if Finding 1 confirms personal data reaches these vendors.

**Finding 3 — Processor agreements (DPAs) not confirmed**
Severity: **Blocking**, conditional on Finding 1
Description: Article 28 requires a DPA with each processor handling personal data on the controller's behalf. Six vendors are named; none has a confirmed DPA in the brief.
Recommended action: Confirm or obtain DPAs with OpenAI, Pinecone, CommodityPriceAPI, OpenCage, Google, and Notion before any personal data (per Finding 1) is processed through them.
Escalation needed? Yes.

**Finding 4 — Builder's own controller/processor role undocumented**
Severity: **Minor**
Description: The brief doesn't state whether the Builder operates this tool as controller (own procurement use) or processor (on behalf of a separate client), which determines who bears primary Article 5/28 obligations.
Recommended action: State this explicitly in the data processing brief.
Escalation needed? No — resolve before final sign-off.

**Finding 5 — Retention period undefined**
Severity: **Minor**
Description: No retention period is stated for stored part specs, generated reports, or Pinecone embeddings. Low risk if Finding 1 confirms no personal data, but still a gap in data minimisation practice.
Recommended action: Define and document a retention/deletion schedule.
Escalation needed? No.

### Section 4 — GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | Cannot determine from brief | Brief assumes no personal data, so lawful basis isn't addressed at all |
| Purpose limitation respected | Appears met | Single stated purpose (cost estimation); no reuse described |
| Data minimisation | Appears met | Payload fields are narrow and purpose-specific |
| Controller/processor roles mapped and DPAs in place | Gap identified | Six vendors named, zero DPAs confirmed; Builder's own role undocumented |
| International transfer mechanism documented | Gap identified | Four confirmed US vendors, no SCCs/DPF stated |
| DPIA conducted if required | Cannot determine | Contingent entirely on resolving Finding 1 |
| Article 22 safeguard in place if automated decisions affect people | Appears met (N/A) | Output estimates a part's cost, not a person; no automated decision on an individual identified |
| Privacy notice covers AI processing | Cannot determine | No privacy notice mentioned in the brief |
| Data subject rights can be operationalised within deadlines | Cannot determine | No process described; moot if Finding 1 confirms no personal data |

### Section 5 — Overall recommendation

**Proceed with conditions.** The primary payload — part specs, material, weight, business addresses, quantities — is plausibly non-personal, and the brief's reasoning for that payload is sound. But the "no personal data" conclusion is stated as settled when it hasn't been tested against the infrastructure layer (user identity, request logs) or against the six named vendors' DPA/transfer status. Conditions before go-live: resolve Clarifying Questions 1–3 definitively; if any personal data is confirmed, obtain DPAs and document transfer mechanisms for all US-based vendors (Finding 2, Finding 3) before that data reaches them.

### Section 6 — What this report is not

This report is not a legal opinion, not a DPIA, and not a certification of compliance. The client should obtain legal review before relying on this assessment.

---

## Joint Closing Note (to complete together in Phase 5)

*[Fill in after the debrief conversation with your teammate.]*
