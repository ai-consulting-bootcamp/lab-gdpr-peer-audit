# GDPR Peer Audit Report — School Book Order Bot
**Auditor:** Jay Ramamoorthi
**System audited:** School Book Order Bot (Anand Narasipuram, Project 3)
**Material reviewed:** Data processing brief only, per lab ground rules

---

## Section 1: System Summary

This is an order-intake automation for a school textbook distribution business, operating via Telegram and WhatsApp. Schools submit book orders as text or photo messages; the system parses, matches, and fulfills these against a catalogue, and separately supports order-status lookups, publisher-level order consolidation, and a conversational Q&A layer over historical order data for the business operator. The system currently runs live in India, with a second deployment planned for Germany. Personal data processed includes chat identifiers, order content tied to an identifiable school contact, and incidental content that may appear in handwritten order photos.

## Section 2: Data and Role Map Summary

Three personal data categories are present: chat identifiers, order content linked to an identifiable sender, and possible incidental personal content in photo uploads (assessed by the brief itself as a low-but-nonzero risk, not ruled out). No special-category data is intentionally collected. The controller is the operating business (India currently; Germany once live); OpenAI, Google Sheets/Workspace, n8n, and Telegram/WhatsApp all act as processors. The builder's own role (processor, joint controller, or neither, post-handover) could not be determined from the brief alone. The most significant open question is international transfer: the India deployment does not currently trigger GDPR's territorial scope, but the Germany deployment will, the moment it goes live — and the processing region for OpenAI and Google Workspace has not yet been confirmed.

## Section 3: Compliance Findings

**Finding 1 — Purpose limitation: conversational Q&A over historical order data (self-identified by the builder)**
**Severity: Significant**
**Description:** Order data was originally collected for parsing, matching, consolidation, and status-reply purposes. Purpose (e) — an LLM-driven Q&A layer letting the operator query historical order data conversationally — was not part of the original design and was not contemplated at the time this data was first collected. The brief itself flags this rather than asserting compatibility, which is the correct instinct, but it remains an unresolved gap. Article 5(1)(b) requires new purposes to be compatible with the original collection purpose, or to have their own independent lawful basis.
**Recommended action:** Determine whether purpose (e) can be justified as compatible with the original purposes (e.g., under a purpose-compatibility assessment considering the link between purposes, context, and reasonable expectations), or whether it needs its own lawful basis and, likely, updated notice to schools. Do not treat operator convenience alone as sufficient justification.
**Escalation needed?** Yes — to legal counsel, given this is a genuine purpose-compatibility judgment call, not a mechanical fix.

**Finding 2 — International transfer mechanism unconfirmed ahead of Germany go-live**
**Severity: Significant (Blocking once Germany goes live, if unresolved)**
**Description:** The brief correctly identifies that OpenAI and Google Workspace processing regions are unconfirmed. This is currently a documentation gap, not yet a live violation, since the India deployment doesn't trigger GDPR scope. However, this becomes Blocking the moment Germany-based schools' data starts flowing through the system without a confirmed lawful transfer mechanism in place.
**Recommended action:** Confirm processing region for both OpenAI and Google Workspace before Germany go-live. If either processes outside the EEA, establish Standard Contractual Clauses (or confirm another valid mechanism) before any German school's data is processed — this needs to be resolved *before* launch, not remediated after.
**Escalation needed?** Yes — to legal counsel, specifically ahead of the Germany launch date, not as a general to-do.

**Finding 3 — DPAs not confirmed with any processor**
**Severity: Significant**
**Description:** The brief lists four processors (OpenAI, Google Sheets/Workspace, n8n, Telegram/WhatsApp) but does not confirm DPAs are in place with any of them. Given that real personal data (chat identifiers, order content tied to identifiable schools) already flows through all four in the live India deployment, this is a present-tense gap, not a future one.
**Recommended action:** Confirm and document DPA status with each processor individually. Particular attention to OpenAI, given the incidental personal-data risk in photo processing (Finding 4) — a general-purpose DPA may not adequately address image content specifically.
**Escalation needed?** No — this is a standard, mechanical documentation task, not a judgment call requiring legal interpretation (though legal review of DPA terms themselves is good practice).

**Finding 4 — Incidental personal data in photo uploads**
**Severity: Minor**
**Description:** The brief honestly assesses this as a low-but-nonzero risk — handwritten order photos may incidentally contain names, phone numbers, or other personal content beyond the book list, processed transiently by the vision model. This is not a data category the system intentionally collects, but "transient processing" is not itself a GDPR exemption — the data is still processed the moment it's parsed, however briefly.
**Recommended action:** Confirm technically what happens to the image after parsing (see Clarifying Question 4) — if images are not retained, document this explicitly as a mitigating design choice rather than leaving it implicit. If they are retained anywhere (including platform-level message history outside the system's direct control), note this honestly in the privacy notice.
**Escalation needed?** No, unless retention is confirmed and found to be significant, in which case revisit severity.

**Finding 5 — Human review status of the "mark fulfilled" auto-step**
**Severity: Minor**
**Description:** The brief correctly notes this doesn't constitute an Article 22 issue, since it's an operational step, not a decision about a person. It's included here as a data-accuracy and operational-integrity finding, not a compliance-blocking one.
**Recommended action:** Confirm whether human review exists at this step; if not, consider adding a lightweight confirmation step given that fulfillment records tied to identifiable schools could matter in a future dispute.
**Escalation needed?** No.

## Section 4: Specific GDPR Obligations Checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | Cannot determine from brief | Brief lists purposes clearly but does not state a proposed lawful basis for any of them — this wasn't part of what was shared, per lab ground rules, so absence here doesn't necessarily mean it's missing from Anand's own analysis |
| Purpose limitation respected (no incompatible reuse) | Gap identified | Finding 1 — purpose (e) self-flagged as a live concern |
| Data minimisation (only necessary data collected) | Appears met | No evidence of excessive data collection; incidental photo content is a byproduct, not a deliberate collection choice |
| Controller/processor roles mapped and DPAs in place | Gap identified | Roles are mappable from the brief, but DPA status is unconfirmed for all four processors (Finding 3) |
| International transfer mechanism documented | Gap identified | Finding 2 — self-flagged by the brief as unconfirmed |
| DPIA conducted if required | Cannot determine from brief | Not addressed in the brief; this system plausibly meets DPIA triggers (systematic processing of order data linked to identifiable contacts, at meaningful scale across many schools) — worth checking directly |
| Article 22 safeguard in place if automated decisions affect people | Appears met (not applicable) | Correctly assessed by the brief as not applicable — no decision with legal/significant effect on a person occurs |
| Privacy notice covers AI processing | Cannot determine from brief | Not addressed |
| Data subject rights can be operationalised within deadlines | Cannot determine from brief | Not addressed — worth a direct question given data is spread across Sheets, chat platforms, and n8n |

## Section 5: Overall Recommendation

**Proceed with conditions.** No finding in this audit is severe enough to demand an immediate stop to the live India deployment as currently scoped, but two Significant findings (purpose limitation on the Q&A feature, and the international transfer question) must be resolved — the second one specifically *before* the Germany deployment goes live, not after. The DPA documentation gap (Finding 3) should also be closed promptly given real personal data is already flowing through all four processors today. The two minor findings are good-practice items, not blockers.

## Section 6: What This Report Is Not

This report is a first-pass, independent compliance review conducted by a peer without legal training, based solely on the data processing brief provided, per this lab's ground rules. It is not a legal opinion, not a DPIA, and not a certification of compliance. The client should obtain legal review before relying on this assessment, particularly given the genuine judgment calls involved in Findings 1 and 2.
