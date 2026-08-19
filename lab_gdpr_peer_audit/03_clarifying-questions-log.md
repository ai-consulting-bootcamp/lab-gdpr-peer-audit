# Phase 3 — Clarifying questions log: Platform Risk Research Agent (GDPR)

Information requested from client (Nelly) on 2026-08-19. Logged before finalizing the audit, per lab ground rules — though see the process log for a note on the sequencing issue in this round.

---

### Question 1 — Whose data is the "buyer context data," exactly?
**What I need to know:** When a user types internal team or role names into the context field, are those colleagues aware their names are being submitted, and did the submitting user have any authority or basis to submit that data on their behalf?
**Why it matters:** This affects whether the submitting user's colleagues are separate data subjects the builder has obligations toward (transparency under Article 13/14, and a question of whether the buyer company or the builder is the controller for that specific slice of data), not just the account holder.
**Provisional assumption:** I'm assuming this is typically limited to role titles or first names in passing, not full profiles, and that no separate notice currently reaches those colleagues — worth confirming rather than assuming it's negligible.

### Question 2 — Is the buyer company a controller, a joint controller, or simply a data source?
**What I need to know:** Does the buyer company make any of its own determinations about how the submitted data or resulting report is used downstream, or is the builder the sole controller for the full processing chain?
**Why it matters:** This determines whether a controller-to-controller relationship (with its own Article 26 joint-controller considerations, or separate independent-controller documentation) exists, versus a straightforward controller-processor relationship where DPAs are the only mechanism needed.
**Provisional assumption:** I'm assuming the builder is the sole controller for now, and the buyer is best characterized as the data source plus the report's recipient, since the brief describes no downstream decision-making role for the buyer over how their submitted data is processed.

### Question 3 — What lawful basis applies to each of the three processing purposes?
**What I need to know:** Specifically: is account data processed under contract (Article 6(1)(b)), and is vendor research data (including the incidentally-collected third-party data) processed under legitimate interests (Article 6(1)(f))? Has a Legitimate Interests Assessment been documented for the latter?
**Why it matters:** The brief doesn't state a lawful basis anywhere. Legitimate interests is the most plausible basis for the vendor research function, but it requires a documented three-part test (purpose, necessity, balancing), especially given it affects third parties who never interacted with the platform.
**Provisional assumption:** I'm assuming account/context data relies on contract (necessary to provide the requested service) and vendor research data relies on legitimate interests, with no formal LIA yet on record.

### Question 4 — Has a DPIA been assessed or conducted?
**What I need to know:** Has the team run the EDPB's nine-criteria screening test against this processing, and if the answer is yes on two or more criteria, has a full DPIA been completed?
**Why it matters:** At minimum, "new technology" (an AI/LLM-based research and scoring pipeline) and "data processed about vulnerable data subjects or those with no relationship to the controller" (the individuals named in breach disclosures) both look like plausible matches from the brief alone, which would trigger the DPIA requirement under Article 35.
**Provisional assumption:** I'm assuming no DPIA has been conducted yet, since the brief makes no mention of one, and I'd treat this as an open, unresolved risk rather than assume the threshold isn't met.

### Question 5 — How are Article 14 transparency and data subject rights operationalized for individuals named in web research?
**What I need to know:** Is there any mechanism for someone to find out their name appeared in a report, request a copy, or ask for erasure or rectification — or is a disproportionate-effort exemption (Article 14(5)(b)) being relied on instead?
**Why it matters:** These are the data subjects with the weakest position in this whole system — no relationship with the controller, no notice, and (per the brief) currently no defined process to locate or act on their data. This is a live obligation gap, not a hypothetical.
**Provisional assumption:** I'm assuming no mechanism currently exists, since none is described, and that no formal reliance on the Article 14(5) exemption has been documented either.
