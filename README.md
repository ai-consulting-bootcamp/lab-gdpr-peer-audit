# Audit your teammate's project — GDPR lens

**Track:** Module 7 — GDPR · **When:** Week 7, Day 3 · **Status:** Required

This repository contains everything you need for this lab.

## Files

- [`instructions.md`](./instructions.md) — the lab instructions
- [`rubric.md`](./rubric.md) — how your submission is graded; this is what the AI reviewer checks your PR against

## How to complete this lab

1. **Fork** this repository.
2. Do the work described in `instructions.md`, committing to your fork.
3. Open a **pull request** back into this repository.
4. You'll receive **AI feedback** on your PR based on `rubric.md`. Address any blocking feedback and push updates to the same PR.

## Submission hygiene

- Keep this repository scoped to this lab only — no unrelated projects or personal files.
- Use clear, descriptive filenames.
- Remove secrets, API keys, and tokens before committing.

---

## Submission contents (Ugo Ahukannah)

**Teammate:** Vittal Navale · **Project audited:** [Whizbiz — Messenger Accountant](https://github.com/vitcipher/W6_Project3-Whizbiz-Messenger-Accountant),
a chat-based bookkeeping bot for German solo business owners. This is the GDPR lens; the EU AI Act
peer audit of the same system is a separate lab.

| File | Contents |
|---|---|
| [`gdpr-peer-audit-whizbiz.md`](./gdpr-peer-audit-whizbiz.md) | The audit: Phase 1 read and annotate, Phase 2 personal data summary and role map, Phase 3 clarifying-questions log, Phase 4 audit report (system summary, data and role map, eight findings with severity, GDPR obligations checklist, overall recommendation, disclaimer) |
| [`questions-for-vittal-gdpr.md`](./questions-for-vittal-gdpr.md) | The clarifying questions as sent to my teammate, each naming the obligation it bears on — assumptions withheld so they could not lead his answers |
| [`debrief-and-joint-closing-note.md`](./debrief-and-joint-closing-note.md) | Phase 5: the six-step debrief, comparing lawful basis and DPIA conclusions, and the joint closing note |
| [`stretch-remediation-plan-article-28-dpa.md`](./stretch-remediation-plan-article-28-dpa.md) | Stretch: remediation plan for the blocking Article 28 finding — artifact, owner, timeline, and the evidence a regulator would accept |
| [`reinforce-audit-reflections.md`](./reinforce-audit-reflections.md) | Reinforce: documentation gaps in my own project, and what independent review revealed that self-assessment cannot |

**Working mode:** all exchange with my teammate is by markdown document — questions out, answers
back, report, then the debrief written into a shared file.

**Ground rules observed:** only Vittal's project materials were exchanged before the audit — no
self-audit findings, lawful-basis selections or DPIA conclusion — and clarifying questions were
logged in writing. **Verdict: do not proceed** to processing real subscribers' data until four
blocking findings are closed; the prototype run on the builder's own data is not condemned.
