# Phase 5: Debrief and joint closing note - Model Intake Brief

## How this debrief was run (disclosure)

- **Order kept:** I finished and committed `01`-`03` (commit `2bc787f`) **before** opening Sergii's self-audit (`model-intake-gdpr-assessment.md`, `model-intake-compliance-memo.md`, commit `89b0b5c` of his repo).
- **No live session.** Sergii wasn't available. In step 2, every builder response is either **[written]**, meaning taken from his self-audit, or **[simulated]**, meaning my guess at what he would say. The closing note is written by me, drawing his side from his written work.

## Step 1 - Auditor presents

My report in one breath: a low-risk, non-sensitive B2B tool with **one blocking gap**. Vendors are receiving page text that can hold personal data, and no DPA is verified (F1). There are three significant gaps: transfers, an undocumented lawful basis, no privacy notice. Two minor ones: no redaction, no retention rule. No DPIA needed, Art 22 not triggered. Position: **do not proceed with live mode until F1 is closed**; offline mode can continue.

## Step 2 - Builder responds

| Point | Builder's context |
|---|---|
| "Processors *already* receive personal data" | **[written]** The synthetic probe was **intercepted locally**: "no personal information was transmitted during the test". The live demo ran on corporate model cards. **Effect on my report:** my F1 wording overstates the evidence. Transmission of personal data is *possible*, not *shown*. |
| Jina and Hugging Face have no contract | **[written]** Agrees: "public keyless access does not establish suitable processor terms". He treats Hugging Face and source sites as **independent controllers** of their own access logs, which is more precise than my "processor or controller". |
| Redaction is "Minor" | **[written]** He makes it **gap G1, first priority**, because it is the cheapest control and shrinks every other risk. |
| Code-level controls | **[written]** Adds G6, which I didn't find: the Hugging Face route reads pages **without an allowed-domain list**, and link checking **follows redirects before checking the destination**. |
| Client deployment | **[simulated]** "There is no client yet; I didn't want to invent roles." This explains why his role map leaves the future roles conditional, while mine assumes a hosted service. |

## Step 3 - Compare lawful basis (primary purpose P2: LLM assessment of documentation)

| | Me | Sergii |
|---|---|---|
| **Basis** | Art 6(1)(f) legitimate interests | Art 6(1)(f), **candidate only, TBD - legal review** |
| **LIA outcome** | Conditional pass: interest ✅, necessity only in part, balancing ✅. **Conditional on redaction.** | Necessity **fails for the current unredacted flow** (his probe shows an unnecessary contact in the payload). Doesn't rely on LI until redaction exists. |

**Which is stronger?** **His.** We agree on the basis and on the fix, but he states the *current* result honestly: as built, the LIA fails. A "conditional pass" reads as a pass to a busy client. **Agreed wording:** "LI fails necessity today; passes once identifiers are removed before dispatch."

## Step 4 - Compare DPIA conclusions

**Agreement: no mandatory DPIA.** Both screens find **one** criterion (innovative technology).

| Point | Resolution |
|---|---|
| Sensitive data | He marks it **contingent/unknown**; I said "not expected". Same substance. |
| "One criterion can be enough" | He adds that one criterion can be enough if the risk is high, so the threshold isn't mechanical. I agree; it doesn't change the result here. |
| National list | He requires a check of the national mandatory list (the German DSK list). I missed that step. |
| Lab wording | He corrects the lab's ninth criterion ("cross-border transfer preventing rights exercise"). The EDPB criterion is about processing that **prevents the exercise of a right or the use of a service**. I used the correct wording too. |

## Step 5 - Compare gap lists

| | Gaps |
|---|---|
| **Both found** | DPAs and roles unverified (my F1 / his G2) · transfer mechanism (F2 / G2) · no LIA (F3 / G3) · no notice, Art 14 indirect collection (F4 / G3) · no redaction before OpenAI (F5 / G1) · no retention or rights process (F6 / G4) · DPIA screening not recorded (G5) |
| **Self-audit only** | **G6:** domain and redirect control gaps, found by reading code · telemetry and browser persistence · identifying URL query parameters · the Streamlit "recent models" list as stored run history · Art 3 territorial scope · a **tested** probe instead of an assumption |
| **Peer audit only** | **Reviewer data as employee data** in a client deployment (§26 BDSG, works council) · harvested contact emails reused for **supplier outreach** as a new purpose · the **licensed-software option** in which Sergii has no GDPR role at all · a **severity call**: an unverified DPA for a processor is Blocking under the lab's guide |

**Overall positions:** **his "proceed with conditions"** vs **my "do not proceed with live mode"**. The two labels differ, but the operations are the same: both say continue offline, hold live personal-data flows, and close contracts and redaction first. After step 2, I'd keep my label only for runs on **unscreened** live sources.

**What's unusual about this pair:** here the **self-audit was the deeper review**. Sergii had the code and tested it; I had a one-page brief. The external audit added *framing*, not *facts*: who the controller would be, which purposes are new, and how severe a gap is.

## Step 6 - Joint closing note

> Self-assessment is strongest where the builder can test: Sergii's audit found code-level gaps no brief would show, and mine of Menohelp found things only the builder knew, such as the real data behind a showcase report. The gaps hardest to catch in your own work are the ones that sit *outside* the code: what role you'd play for a client, who else's data your design quietly collects, and how severe a gap you've lived with looks to someone else. A builder's honesty about gaps doesn't replace an outsider's judgement on how much they matter.

*(Written by Ben; Sergii's side drawn from his written self-audit and peer audit. Not yet confirmed by him.)*

---

## Reinforce

### Questions Sergii logged about *my* system (his GDPR peer audit of Menohelp)

| His question | Can I answer it from the project docs alone? |
|---|---|
| Q1 Who operates it; was the "real data" showcase permitted? | **No.** The README says "real data" and nothing about whose, or with what permission. |
| Q2 Vendor entities, DPAs, regions, transfer tools | **No.** Nothing is documented. |
| Q3 Who relies on the output, at what scale; DPIA? | **Partly.** `gtm_future_sprints.md` gives the audience and scale; no DPIA. |
| Q4 Consent, notice, withdrawal, rights across all copies | **No.** Only UI captions. |
| Q5 Is the API reachable; what binds a dataset ID to its user? | **Partly.** README says it runs locally; `store.py` shows the TTL; there is no access model. |

**What it suggests:** my docs describe the **code** well and the **data's legal life** not at all: where it came from, under what permission, with whom it is shared. That matches my own accountability check (0 of 15 documents complete). Sergii's Q1 is the same issue as my self-audit's red flag C, found independently from the outside.

### One finding I disagreed with as builder

His **Finding 7** rates Article 22 on Menohelp as a **Significant** "assessment gap". My self-audit says Art 22 simply doesn't apply, because the report decides nothing. After the debrief, **I still disagree with the severity, but not the point.** Art 22 needs a *decision*, and an information report a woman reads herself isn't one. His real point, though, is that I never **recorded the intended use**. Without that record, nothing stops a coach from using the report to accept clients or choose a programme, which *would* be a decision. So the gap is a missing intended-use statement: Minor today, and a gate before coach use. A disclaimer is not a safeguard. I'd add one line to my self-audit's memo: write the intended use down before Sprint 2.
