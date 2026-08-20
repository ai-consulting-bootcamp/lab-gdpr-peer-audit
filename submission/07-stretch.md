# Stretch: Remediation Plan

**Finding addressed:** Finding 2 — International transfer mechanism unconfirmed ahead of Germany go-live (Significant, Blocking once Germany launches if unresolved)

Selected over Finding 1 (purpose limitation) because it has a harder deadline attached — Germany go-live is a known future event, not an open-ended judgment call, which makes it the better candidate for a concrete, timeline-bound plan.

**What specific artifact closes this gap:** A documented Transfer Impact Assessment (TIA) confirming the actual processing region for OpenAI API calls and Google Workspace/Sheets tenancy, plus Standard Contractual Clauses (SCCs) executed with either vendor if processing occurs outside the EEA. If both vendors confirm EU-region processing, the artifact is instead a short written confirmation citing each vendor's own data residency documentation — no SCCs needed in that case, but the confirmation itself must still exist as a record.

**Who would own it:** Anand, working with his father (as the current controller for the India deployment) and whoever will operate the Germany deployment (controller for that entity) — with external legal counsel engaged specifically to confirm SCC execution is done correctly, since this isn't a mechanical task once non-EEA processing is confirmed.

**Realistic timeline:** Should be resolved before the Germany deployment accepts its first live school order — not after. Given this is currently just a confirmation-and-documentation task (checking existing vendor settings, not building anything new), a 1-2 week timeline is realistic if prioritized ahead of go-live, assuming no SCC negotiation is required (most cloud vendors offer standard SCC addenda that just need to be executed, not negotiated from scratch).

**What evidence would confirm to a regulator that the gap is closed:** A written record showing (1) the confirmed processing region for each vendor (screenshot or written confirmation from OpenAI/Google's own account settings or support), and (2) if applicable, signed SCCs on file, dated before the Germany deployment's first live processing activity — not retroactively executed after the fact.
