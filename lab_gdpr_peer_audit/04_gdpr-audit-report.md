# GDPR Peer Compliance Audit Report: Platform Risk Research Agent

**Auditor:** Kimia Asgari
**System builder:** Nelly
**Date:** 2026-08-19
**Basis for this report:** Nelly's data processing brief only — rewritten after an earlier draft was found to have been influenced by prior exposure to her client memo. This version reasons only from facts stated or clearly inferable in the brief itself, and marks a claim as unconfirmed where the brief is simply silent, rather than treating silence as a confirmed absence.

---

## Section 1 — System summary

The Platform Risk Research Agent collects account data (name, email) at signup, buyer context data (company name, use case, internal context — potentially naming the buyer's colleagues) to scope a vendor check, and produces a risk report on a named AI vendor by researching public web sources. That research can incidentally surface personal data about named individuals unconnected to the platform — including, in rare cases, data that looks special-category if a source discloses health, criminal, or similarly sensitive status tied to a data breach. All processing (reasoning via DeepSeek/Vercel AI Gateway, embeddings via OpenAI, vector storage via Pinecone, hosting via Railway) runs through US-based vendors, with no EU-based storage, meaning personal data crosses the EU border on every use by an EU-based buyer.

## Section 2 — Data and role map

Three personal data categories are in play: account data, buyer context data, and incidentally-collected third-party data from public web research. None is intentionally special-category, but the third category carries a real, acknowledged risk of touching Article 9 data. The builder is the controller for all three; the four processing vendors (DeepSeek, OpenAI, Pinecone, Railway) are processors, all US-based, with no DPA or transfer mechanism confirmed in the brief. The full detail is in `02_personal-data-and-role-map.md`.

## Section 3 — Compliance findings

**Finding 1 — No confirmed DPA or international transfer mechanism with any of the four US processors**
**Severity:** Blocking
**Description:** The brief states plainly that data crosses the EU border on every EU-buyer use, that all four processors are US-based, and that no EU-based storage exists — but it names no DPA and no transfer mechanism (SCCs, adequacy reliance, or DPF certification) for any of the four. Per this lab's severity guide, a DPA missing for a processor that already handles personal data is Blocking, and that's the situation described here for all four vendors simultaneously.
**Recommended action:** Sign a DPA (Article 28) with each processor, and establish and document a transfer mechanism for each — most likely SCCs unless a given processor holds current EU–US Data Privacy Framework certification, which should be checked rather than assumed.
**Escalation needed?** Yes — to the DPO/legal counsel, before any further personal data is processed through these vendors.

**Finding 2 — No description of how third-party individuals incidentally captured in vendor research could exercise their rights**
**Severity:** Significant
**Description:** Individuals named in breach disclosures, news, or reviews about a researched vendor have no relationship with the platform and never consented to anything. The brief describes how this data enters the system but says nothing about any mechanism for these individuals to be identified, notified, or have their data corrected or removed — I'm treating that silence as an open gap to confirm, not as proof no such mechanism exists. This is a live Article 14 (information to be provided where data isn't obtained from the data subject) and Article 15/17 (access/erasure) question, compounded by the brief's own acknowledgment that some of this data could be special-category.
**Recommended action:** Confirm whether any rights-request mechanism exists for these individuals; if not, build one or document a defensible Article 14(5) disproportionate-effort exemption.
**Escalation needed?** Yes — to the DPO, since this touches both transparency obligations and the special-category risk together.

**Finding 3 — Lawful basis not documented for any processing purpose**
**Severity:** Significant
**Description:** The brief doesn't state a lawful basis anywhere. For the vendor-research function specifically, none of the individuals affected (the buyer, or the incidentally-named third parties) have given consent, so legitimate interests (Article 6(1)(f)) looks like the most plausible candidate on the facts described — but that's my inference from the shape of the processing, not something the brief confirms, and it requires its own documented three-part balancing test if it is in fact the basis being relied on.
**Recommended action:** Document the lawful basis for each processing purpose explicitly; if legitimate interests is the basis for vendor-research data, produce a formal LIA, given the processing affects people with no relationship to the controller.
**Escalation needed?** No — this is a documentation task, though the DPO should review the finished LIA.

**Finding 4 — DPIA status unclear against plausible EDPB trigger criteria**
**Severity:** Significant
**Description:** The brief gives no indication a DPIA has been run. On the facts described, at least two EDPB screening criteria look plausibly met: novel technology (an LLM-based research/scoring pipeline) and processing about people with no relationship to the controller (the incidentally-named individuals). Meeting two or more criteria is the EDPB's own rule of thumb for treating a DPIA as likely required.
**Recommended action:** Run the EDPB nine-criteria screening formally and document the outcome; if it confirms the requirement, conduct the DPIA before further scaling.
**Escalation needed?** Yes — to the DPO, since this determines a hard Article 35 obligation, not just a good-practice item.

**Finding 5 — No defined retention period for account data, reports, or embeddings**
**Severity:** Significant
**Description:** The brief describes what's collected and where it's stored but gives no retention period for any of it. Given that stored reports may contain incidentally-collected — potentially special-category-adjacent — third-party data, an undefined retention period here carries more weight than a typical low-risk retention gap.
**Recommended action:** Define and enforce (not just document) a retention period for account data, reports, and vector embeddings, with earlier deletion for anything flagged as touching special-category-adjacent content.
**Escalation needed?** No — but should be closed alongside Finding 2, since both concern the same stored report data.

## Section 4 — Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | Gap identified | Not stated in the brief for any of the three purposes — see Finding 3 |
| Purpose limitation respected (no incompatible reuse) | Cannot determine from brief | Fine for the user's own submitted data; unclear for third-party individuals whose public data is repurposed for vendor scoring — see the [PURPOSE] annotation in `01` |
| Data minimisation (only necessary data collected) | Appears met, with a caveat | Each of the three categories is tied to a clear, narrow purpose; the caveat is that incidental collection from public web search isn't really "minimised" by design, it's a side effect of how the research tool works |
| Controller/processor roles mapped and DPAs in place | Gap identified | Roles are mappable from the brief (see `02`), but no DPA is confirmed for any of the four processors — see Finding 1 |
| International transfer mechanism documented | Gap identified | See Finding 1 |
| DPIA conducted if required | Cannot determine from brief | See Finding 4 |
| Article 22 safeguard in place if automated decisions affect people | Appears met | The brief's own reasoning — vendor scoring, not a decision about a person — holds up on its face; no basis in the brief to dispute it |
| Privacy notice covers AI processing | Cannot determine from brief | Not addressed in the data processing brief at all |
| Data subject rights can be operationalised within deadlines | Cannot determine from brief | Clear for account holders (standard account-data rights); undescribed for incidentally-named third parties — see Finding 2 |

## Section 5 — Overall recommendation

**Proceed with conditions.** No single finding here is disputed on the facts as described — the brief itself is candid about most of the gaps (US-only storage, no defined retention, incidental data risk). The Blocking finding (Finding 1 — DPA/transfer mechanism) needs to close before any further personal data moves through the four processors, since data is described as already flowing through them today with no documented safeguard. The Significant findings (2–5) should be resolved on a near-term timeline, particularly Finding 2 and Finding 4, since both concern the individuals in the weakest position in this system — people who never interacted with the platform at all.

## Section 6 — What this report is not

This report is not a legal opinion, not a DPIA, and not a certification of compliance. It reflects an independent peer review for a course exercise, based solely on Nelly's written data processing brief. The client should obtain legal review, including of any DPAs and the LIA, before relying on this assessment.
