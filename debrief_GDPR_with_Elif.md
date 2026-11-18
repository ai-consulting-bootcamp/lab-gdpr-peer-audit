# Phase 5 — GDPR debrief with Elif Yurdakul

*To complete together after sharing the audit report. Fill in each section with what actually happens.*

**Date:** _…_ · **Present:** Pieter Albrecht (auditor), Elif Yurdakul (builder)

## 1. Auditor presents
Walked Elif through [the audit report](GDPR_audit_report_Unioptt_programme_checker.md): 6 findings (2 Blocking, 3 Significant, 1 Minor) and "do not proceed with real student data".

## 2. Builder responds (5 minutes)
Context Elif gave that wasn't in the brief, incl. answers to Q1–Q5 in the [questions log](data_role_map_and_questions_log.md):
- _…_

## 3. Compare lawful basis for the primary purpose (the report for the student)

| | Lawful basis | Reasoning |
|---|---|---|
| Elif's self-audit | _…_ | _…_ |
| My audit | Contract (Art. 6(1)(b)), with a parent or guardian for users under the applicable age | The student asks for the report; consent is fragile for minors and withdrawable |

Which is stronger, and why? _…_

## 4. Compare DPIA conclusions

| | DPIA required? | EDPB criteria counted |
|---|---|---|
| Elif's self-audit | _…_ | _…_ |
| My audit | Yes | Evaluation, vulnerable subjects (minors), innovative tech, + arguably combining datasets |

Agreement reached, or the specific ambiguity: _…_

## 5. Compare gap lists
- **What Elif's self-audit caught that I missed:** _…_
- **What my audit caught that Elif missed:** _…_

## 6. Joint closing note (required)

Elif’s design work showed in the parts she built deliberately: rules rather than AI decide each fact’s status, the tool makes no score or decision, and the student profile asks only for what the comparison needs. The external audit found its gaps in the parts that felt like plumbing: Telegram and Airtable carrying minors’ grades, budgets and evaluations to non-EU vendors, logs kept for no stated purpose, and no plan for parental involvement once real students replace the synthetic profiles. Self-assessment checks what the system is designed to do, so the gaps hardest to catch in your own work are the data flows around the core feature and the obligations that only begin when an MVP goes live.

> _…_

---

## Reinforce (after the debrief)

**Elif's questions about my Vendor DD Agent that I can't answer from my documentation, and what that says:**
_…_

**One finding from Elif's audit of my project I initially disagreed with. Reflection after the debrief (one paragraph):**
_…_
