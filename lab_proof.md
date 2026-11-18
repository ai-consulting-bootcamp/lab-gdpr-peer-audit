# Lab proof — Audit your teammate's project (GDPR lens)

**Auditor:** Pieter Albrecht
**Teammate:** Elif Yurdakul
**Project audited:** Elif's Project 3, the **Unioptt university programme fact-checker** (checks programme facts and compares them with a Turkish student's profile)

This is the entry point for the reviewer. Each section below links to the supporting file.

## 1. Workflow

```
Elif's brief (only input; no self-audit findings, per lab rules)
        │
        ▼
Phase 1  Annotate  ([PD] data · [?] unclear · [X] cross-border · [P] purpose risk)
        │
        ▼
Phase 2  Personal data summary + role map + transfers
        │
        ▼
Phase 3  Clarifying questions log (5 questions + provisional assumptions)
        │
        ▼
Phase 4  Audit report (summary · map · 6 findings · obligations checklist · recommendation · disclaimer)
        │
        ▼
Phase 5  Debrief with Elif ──► joint closing note      Stretch: DPIA remediation plan
```

## 2. One run: input → evidence → output

**Input:** Elif's one-page brief. The key passages: *"student profile: grades, language test scores, budget, citizenship … often a minor's"* and *"n8n, Telegram and Airtable for delivery and logging."*

**Evidence produced:**
- 16 annotated passages ([annotations](brief_annotations_GDPR_Elif_Unioptt.md)).
- The data and role map ([map + log](data_role_map_and_questions_log.md)):

| Check | Result |
|---|---|
| Personal data | Children's academic records, family budget, citizenship, Telegram identity, met/gap evaluation (profiling) |
| Special category | None by design; possible via scholarship checks |
| Cross-border | Airtable (US), Telegram (non-EU), OpenAI (US, if profile in prompts) |
| DPIA | Required: 3–4 EDPB criteria |
| Art. 22 | Not triggered: no decision made |

**Final output:** [audit report](GDPR_audit_report_Unioptt_programme_checker.md). **Do not proceed with real student data** until the 2 Blocking findings (DPIA, lawful basis for minors) are resolved. The synthetic MVP can continue. Plus 3 Significant findings (transfers and DPAs, privacy notice, purpose limitation) and 1 Minor (retention and rights).

## 3. Failure / limitation I hit

- **Wrong input document.** The lab expects Elif's GDPR *data processing brief*; I audited from her AI Act *system brief* because that is what I had. It covers data, sources and vendors, but not storage locations or retention. The data processing brief has been requested.
- **Same system, two lenses, two verdicts.** My AI Act audit said "proceed with conditions" (consumer version not high-risk); this GDPR audit says "do not proceed with real data". They don't contradict each other: the AI Act risk sits in the *use case*, the GDPR risk in the *data* (children) and *vendors*.
- **Unverifiable from the brief:** what Airtable logs, whether the profile reaches OpenAI, where Unioptt is established. All logged as questions with stated assumptions.

## 4. Supporting files

- [brief_annotations_GDPR_Elif_Unioptt.md](brief_annotations_GDPR_Elif_Unioptt.md) — Phase 1: annotated brief
- [data_role_map_and_questions_log.md](data_role_map_and_questions_log.md) — Phases 2–3: data summary, role map, transfers, questions log
- [GDPR_audit_report_Unioptt_programme_checker.md](GDPR_audit_report_Unioptt_programme_checker.md) — Phase 4: audit report
- [debrief_GDPR_with_Elif.md](debrief_GDPR_with_Elif.md) — Phase 5: debrief, joint closing note, Reinforce
- [stretch_remediation_plan_DPIA.md](stretch_remediation_plan_DPIA.md) — Stretch: remediation plan for Finding 1
- [instructions.md](instructions.md) — Stretch: provided instrunctions markdown
- [rubric.md](srubric.md) — Stretch: provided rubric markdown filej