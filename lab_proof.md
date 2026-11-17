# Lab proof · Audit your teammate's project: GDPR lens

**Start here.** Peer GDPR audit of **Friedrich's Project 3, the *AI Use Case Identifier***: a Python/LangGraph agent that researches a company from public sources (website, job ads, news, commercial registers) and writes an AI use-case brief for a consultant.

## Result in one line

**Do not proceed with real companies until two blocking findings are closed:** (1) no processor contracts or transfer mechanism for OpenAI and Tavily; (2) the legitimate interests basis fails on necessity while names, years of birth and home towns are sent to the model. **Then proceed with conditions.** Both fixes take about a week.

## The run: input → evidence → output

**Input.** Friedrich's data processing brief for the AI Use Case Identifier, received 17 Nov 2026, 16:30. The system's code and workflow were not shared, so the review is document-based: the brief stands in for the workflow export.

**Evidence produced**

- [`01_annotated_brief_ai_use_case_identifier.md`](01_annotated_brief_ai_use_case_identifier.md): Phase 1 annotations (personal data, special-category flags, unclear points, EU-border flows, purpose-compatibility flags)
- [`02_data_and_role_map_ai_use_case_identifier.md`](02_data_and_role_map_ai_use_case_identifier.md): CFU 1 and 3, Phase 2 data summary, role map, transfer mechanisms
- [`03_clarifying_questions_log.md`](03_clarifying_questions_log.md): CFU 2, Phase 3: five questions with provisional assumptions

**Final output**

- [`04_gdpr_audit_report_ai_use_case_identifier.md`](04_gdpr_audit_report_ai_use_case_identifier.md): CFU 4, Phase 4 audit report: 8 findings (2 Blocking, 4 Significant, 2 Minor), obligations checklist, recommendation
- [`05_debrief_prep_and_joint_closing_note.md`](05_debrief_prep_and_joint_closing_note.md): Phase 5 comparison with Friedrich's self-audit, plus the joint closing note
- [`06_stretch_remediation_plan_processor_contracts.md`](06_stretch_remediation_plan_processor_contracts.md): Stretch remediation plan for Finding 1

## One failure / limitation I hit

**Independence was compromised at the hand-over.** The lab specifies exchanging the data processing brief only, but I received Friedrich's **full self-audit**, including his lawful bases, DPIA view and memo. I built the audit on the brief section and logged it in the audit trail (file 01). Because I saw his conclusions first, agreement between our audits is weaker evidence than it would otherwise be. The divergences I document (severity of the legitimate interests failure, DPAs ranked above the README, Tavily's mixed role, Art. 14 timing for leads) are where the independent value remains.

A second limitation: with no code shared, facts such as Pinecone query content, the image prompt and existing real-company outputs are **assumed** (file 03), not verified.
