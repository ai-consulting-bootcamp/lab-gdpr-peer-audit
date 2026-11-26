# Audit your teammate's project — GDPR lens

**Track:** Module 7 — GDPR · **When:** Week 7, Day 3 · **Status:** Required

This repository contains everything you need for this lab.

## Files

- [`instructions.md`](./instructions.md) — the lab instructions
- [`rubric.md`](./rubric.md) — how your submission is graded; this is what the AI reviewer checks your PR against

## Submission map (Ben Mayer)

**Teammate:** Sergii Rostovskyi
**Project audited:** *Model Intake Brief*, a LangGraph agent that checks a third-party AI model's public documentation against an 18-item checklist ([project snapshot `e384f3a`](https://github.com/s-rostovskyi/model-intake-brief/tree/e384f3a41b5c74119786f55865ebe4e7e6cfb73c)). Brief received: [`model-intake-data-processing-brief.md`](https://github.com/s-rostovskyi/lab-gdpr-self-audit/blob/89b0b5cf0a0022fc122e49c1cdcfbf14ce8582ad/model-intake-data-processing-brief.md).

| File | Lab step |
|---|---|
| [`01-model-intake-gdpr-brief-annotations.md`](./01-model-intake-gdpr-brief-annotations.md) | Exchange log (ground rules), Phase 1 annotations, CFU 1 Recognize |
| [`02-data-role-map-and-clarifying-questions.md`](./02-data-role-map-and-clarifying-questions.md) | Phase 2 data summary + role map + transfers, CFU 2 Probe, Phase 3 questions log |
| [`03-gdpr-peer-audit-report-model-intake.md`](./03-gdpr-peer-audit-report-model-intake.md) | Phase 4 audit report (6 sections, 6 findings, obligations checklist) |
| [`04-debrief-and-joint-closing-note.md`](./04-debrief-and-joint-closing-note.md) | Phase 5 six-step debrief, joint closing note, Reinforce |
| [`05-stretch-remediation-plan-processor-contracts.md`](./05-stretch-remediation-plan-processor-contracts.md) | Stretch: plan for the blocking finding |

**Result:** one blocking finding (Art 28 processor contracts unverified), three significant, two minor. No DPIA needed, Art 22 not triggered. Recommendation: **do not proceed with live mode until processor contracts are verified; offline mode can continue.** Sergii's self-audit says "proceed with conditions", which is the same operational position under a different label.

**Independence and simulation:**
- **Read before the report:** only the brief, the project README and the two sample reports. `01`-`03` were committed (`2bc787f`) before I opened his self-audit.
- **Simulated:** there was no live debrief. Builder responses are marked *[written]* (from his self-audit) or *[simulated]*. I wrote the closing note alone; see the disclosure in `04`.

**Legal baseline:** GDPR as in force (proposed Digital Omnibus GDPR changes not relied on). Not legal advice. ⚖️ = needs counsel.

## How to complete this lab

1. **Fork** this repository.
2. Do the work described in `instructions.md`, committing to your fork.
3. Open a **pull request** back into this repository.
4. You'll receive **AI feedback** on your PR based on `rubric.md`. Address any blocking feedback and push updates to the same PR.

## Submission hygiene

- Keep this repository scoped to this lab only — no unrelated projects or personal files.
- Use clear, descriptive filenames.
- Remove secrets, API keys, and tokens before committing.
