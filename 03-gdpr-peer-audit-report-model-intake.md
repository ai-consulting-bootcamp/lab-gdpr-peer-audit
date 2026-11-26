# GDPR audit report - Model Intake Brief

**Builder:** Sergii Rostovskyi · **Auditor:** Ben Mayer · **Date:** 26 Nov 2026 · **Basis:** data processing brief (commit `89b0b5c`) and project README at `e384f3a` only. Assumptions from the questions log (`02`) apply.

## 1. System summary

Model Intake Brief helps a governance reviewer check whether a third-party AI model is documented well enough to integrate. Given a model ID, it searches the web and Hugging Face for public documentation, extracts the text, and asks an OpenAI model to rate 18 evidence criteria with a source and a verified quote. It then renders a Markdown report for a human reviewer. The system is about *models*, not people, but the public pages it reads contain names, handles and email addresses of individuals, and every run exposes the operator's IP and account data to five external services. Today it is a local educational prototype with one user. I also assess an assumed hosted deployment for an EU client.

## 2. Data and role map

- **Personal data:** third-party identity and contact data, collected indirectly from public docs (Art 14). Operator metadata. In a client deployment, reviewer data. **No special-category data** is targeted, but it can't be ruled out in arbitrary web text.
- **Roles:** today Sergii is the **controller**. In the assumed deployment, the **client is controller**, Sergii **processor**, and OpenAI, Tavily, Jina, Hugging Face and Pinecone **sub-processors**. Source websites are independent controllers.
- **Transfers:** at least four US vendors, **no documented mechanism** and no chosen regions. The brief says so itself.

## 3. Compliance findings

> **Finding 1 - Processor contracts (Art 28)**
> **Severity:** Blocking (for live mode on real sources)
> **Description:** Processors already receive personal data: his own probe shows contact details reach OpenAI. DPA acceptance is unverified, and Jina Reader and the Hugging Face Hub are used without an account, so probably without any contract.
> **Recommended action:** Accept and file each vendor's DPA. For keyless services, either sign up for a contracted plan, assess whether the vendor acts as an independent controller ⚖️, or replace them. Until then, use offline mode.
> **Escalation needed?** Yes, to the client's DPO before a client deployment.

> **Finding 2 - International transfers (Chapter V)**
> **Severity:** Significant
> **Description:** US processing with no DPF check, no SCCs and no transfer impact assessment. `store: false` doesn't remove OpenAI's abuse-monitoring retention.
> **Recommended action:** Check each vendor on the active DPF list. Otherwise rely on the SCCs in the DPA plus a short TIA. Prefer OpenAI EU data residency with zero data retention, and EU regions for Pinecone.
> **Escalation needed?** Yes, DPO or privacy counsel for the TIA.

> **Finding 3 - Lawful basis undocumented (Art 6)**
> **Severity:** Significant
> **Description:** No basis is stated for any purpose. The data is incidental, so **legitimate interests (6(1)(f))** fits P1-P4. My LIA: (1) the *interest* is real: due diligence before integrating a model; (2) it is *necessary* only in part, because names and emails aren't needed to judge documentation; (3) *balancing* passes, because people published this information professionally, for others to evaluate their model, and the impact is low. **Conditional on minimisation (Finding 5).** Employee data of reviewers: 6(1)(f), or §26 BDSG ⚖️.
> **Recommended action:** Write the LIA down (one page), per purpose.
> **Escalation needed?** No.

> **Finding 4 - Transparency (Art 13-14)**
> **Severity:** Significant
> **Description:** No privacy notice. People named in docs are never told (Art 14). The **disproportionate-effort exemption (Art 14(5)(b))** likely applies, but it must be documented, and the information must still be made public. Reviewers in a client deployment need an Art 13 notice that explains the AI processing and vendors.
> **Recommended action:** Publish a short notice covering both groups; record the Art 14(5)(b) reasoning in the LIA.
> **Escalation needed?** No.

> **Finding 5 - Data minimisation (Art 5(1)(c), 25)**
> **Severity:** Minor
> **Description:** Up to 3,500 characters per source go to OpenAI unfiltered; emails and personal names aren't needed to rate documentation.
> **Recommended action:** Redact email addresses and phone numbers before the LLM call and in quotes. This one step shrinks Findings 1-4.
> **Escalation needed?** No.

> **Finding 6 - Retention and sharing of reports (Art 5(1)(e), 6(4))**
> **Severity:** Minor
> **Description:** No retention rule, no deletion of exported reports. Publishing reports for "educational demonstration" could carry individuals' names to a public audience. Today's two samples contain none.
> **Recommended action:** Set a retention period (e.g. the integration decision plus 2 years). Run the redaction check before any report is published.
> **Escalation needed?** No.

**Not findings:** **Art 22** doesn't apply, because no decision concerns a person. **DPIA:** only **1** EDPB criterion clearly applies (innovative technology). There is no scoring of people, no sensitive data, no large scale, no vulnerable subjects. **A DPIA is not required**; record the screening.

## 4. Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | **Gap identified** | Purposes P1-P4 are well defined; no basis stated (F3) |
| Purpose limitation respected (no incompatible reuse) | **Appears met** | P1-P2 compatible with why docs are published; watch P3 publication (F6) |
| Data minimisation (only necessary data collected) | **Gap identified** | No redaction before OpenAI (F5) |
| Controller/processor roles mapped and DPAs in place | **Gap identified** | Roles open for deployment; DPAs unverified (F1) |
| International transfer mechanism documented | **Gap identified** | None (F2) |
| DPIA conducted if required | **Appears met** | Not required (1 criterion); screening not yet recorded |
| Article 22 safeguard in place if automated decisions affect people | **Appears met** | N/A: decisions concern models |
| Privacy notice covers AI processing | **Gap identified** | No notice (F4) |
| Data subject rights can be operationalised within deadlines | **Cannot determine from brief** | No run store, so access is easy; reports outside the app can't be searched or erased (F6) |

## 5. Overall recommendation

**Do not proceed with live mode on real sources until Finding 1 is closed; offline mode can continue.** The only blocking issue is paperwork, not design: vendors are already receiving personal data without a verified contract. That is likely a one-day fix for OpenAI, Tavily and Pinecone, and a decision for Jina and Hugging Face. Once it is closed, the position becomes **proceed with conditions**: transfers documented (F2), LIA and privacy notice written (F3-F4) before any client deployment, and redaction (F5) and a retention rule (F6) soon after. The underlying risk is low. This is a low-volume, non-sensitive, B2B tool, and the brief is unusually honest about its own gaps.

## 6. What this report is not

This report is not a legal opinion, not a DPIA, and not a certification of compliance. It is based on a one-page brief and public project documentation. The client should obtain legal review before relying on this assessment.
