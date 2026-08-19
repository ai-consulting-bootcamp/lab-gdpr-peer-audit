# Debrief — Nelly Pourmehr & Kimia Asgari
Project: RegGuard-Mini

## Auditor presents
Nelly walked through the audit report: one Blocking finding (LLM sub-processor DPA missing), two Significant findings (transfer mechanism, works-council monitoring risk), one Significant finding on free-text data minimisation, one Minor finding (retention undefined). Overall position: do not proceed on the LLM data flow until the Blocking and transfer findings close.

## Builder responds
Kimia's self-audit memo landed on "proceed with conditions" overall, not "do not proceed." Same underlying facts, different label. Worth resolving: does a missing DPA for a processor already handling personal data count as a condition to satisfy, or a blocker? Rubric says Blocking. Flag this as the point to align on.

## Lawful basis comparison
Nelly's audit: could not determine a lawful basis from the brief. Marked "cannot determine."
Kimia's self-audit: memo does not state a chosen lawful basis either.
Result: neither audit reached a lawful basis conclusion. This is unresolved, not a disagreement. Needs a live answer from the client, likely legitimate interest for identity/attribution and consent or contract for typed questions and handoff data — to be confirmed, not assumed.

## DPIA conclusion comparison
Nelly's audit: "cannot determine from brief" — flagged the confidence-scoring feature as relevant but didn't reach a conclusion.
Kimia's self-audit: raises the same feature under works-council risk, does not state a DPIA conclusion.
Result: both audits stop short of a DPIA call. Ambiguity to work through: does confidence-scored assessment of a person's work meet the EDPB "evaluation or scoring" trigger, even without an automated decision that affects the designer directly?

## Gap list comparison

**Caught by self-audit, missed by external audit:**
- Handoff colleague never receives a privacy notice and has no direct relationship with the tool. Kimia flagged this as a residual risk. Nelly's report didn't raise it as a distinct finding.
- Foreign government data-access exposure if the LLM provider sits outside the EU — a DPA reduces this risk but doesn't remove it. Kimia's memo names this explicitly; Nelly's report treats it as folded into the transfer-mechanism finding.

**Caught by external audit, missed by self-audit:**
- Free-text input risk: designer questions could incidentally include special category data, with no filtering described. Kimia's memo doesn't mention this.
- Formal severity rating (Blocking/Significant/Minor) with escalation owners. Kimia's memo lists actions but doesn't rate them by severity, which is part of why the two overall positions diverge.

## Joint closing note (required deliverable)
Both audits converged on the same two core gaps — the LLM provider's identity/DPA and the works-council question — which confirms these are real risks, not artifacts of one person's reading. But each audit caught something the other missed: the builder's insider knowledge surfaced the handoff privacy-notice gap and the foreign-access exposure, while the external, brief-only read surfaced the free-text data-minimisation risk that familiarity with the system had made invisible to the builder. Self-assessment blind spots come from knowing too much about intent; independent-review blind spots come from knowing too little about context — and the two together cover more ground than either alone.

