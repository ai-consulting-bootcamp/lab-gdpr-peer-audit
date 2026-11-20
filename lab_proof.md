# Lab Proof: GDPR Peer Audit of a Teammate's Project (Interview Prep Report)

**Auditor:** Ayhan Demir · Ironhack AI Consulting & Integration Bootcamp · 20 Nov 2026
**Teammate and project audited:** Julia Antunes, Interview Prep Report (her Project 3)
**My project, audited by Julia:** Fix My Process (my Project 3)
**Result in one line:** **do not proceed** with real candidate data until processor contracts are in place (the only Blocking finding), then **proceed with conditions**. The debrief showed that self-assessment misses documentation gaps most.

## Start here

| Phase | File | Outcome |
|---|---|---|
| Input | [00_julia_brief.md](00_julia_brief.md) | Julia's data processing brief, the only document received before the audit |
| Input (copy) | [Data_Processing_Brief_Interview_Prep_Report_julia.md](Data_Processing_Brief_Interview_Prep_Report_julia.md) | The brief as received, identical to `00` |
| 1. Read and annotate | [01_annotations.md](01_annotations.md) | 23 tagged annotations. Special-category data is possible in CVs and repeated in reports. OpenAI, Tavily, GitHub and Notion are in the US; the n8n, GNews and hosting locations are not documented. Two purpose concerns: the Notion error log, and GitHub profiles that may not be the submitter's own |
| 2. Data and role map | [02_data_and_role_map.md](02_data_and_role_map.md) | 10 data categories. Julia is the controller (assumed); n8n, OpenAI, Tavily, Notion and the host are processors with no DPAs; GitHub and GNews are independent controllers. US transfers need the Data Privacy Framework or SCCs |
| 3. Clarifying questions | [03_clarifying_questions.md](03_clarifying_questions.md) | 5 questions, each with the GDPR article it affects and a provisional assumption |
| 4. Audit report | [04_audit_report.md](04_audit_report.md) | 6 findings: 1 Blocking (Art. 28 DPAs) and 5 Significant. 2 escalations: legal counsel on transfers, a data protection adviser on the DPIA. Checklist: 4 gaps, 2 appear met, 3 cannot be determined. All six required sections, including the disclaimer |
| 5. Debrief | [This file, below](#phase-5-debrief) | Lawful basis and DPIA compared for both systems; joint closing note |

## Top three actions for Julia's system

1. Sign DPAs with OpenAI, the n8n host, Notion and Tavily before any real CV is processed (Finding 1).
2. Record a lawful basis for each purpose and show a privacy notice before upload (Finding 2).
3. Remove contact details, date of birth and referees from the CV before the LLM call, and confirm that the CV and profile belong to the submitter (Finding 3).

## Phase 5: Debrief

Each of us audited the other's system from the brief alone, then we compared the audits with our self-audits.

| Step | Record |
|---|---|
| 1. Auditor presents | I presented [04_audit_report.md](04_audit_report.md). Julia presented her audit of Fix My Process |
| 2. Builder responds | **TO ADD:** Julia's context on her own system. Mine: I had already decided the lawful basis (legitimate interests) and that outputs judge processes rather than people, but neither is stated in my brief |
| 3. Lawful basis | See the first table below |
| 4. DPIA | See the second table below |
| 5. Gap lists | See "What independent review surfaced" below |
| 6. Joint closing note | See below |

**Lawful basis for the primary purpose**

| System | Builder's self-audit | Peer audit |
|---|---|---|
| Interview Prep Report (Julia) | **TO ADD:** Julia's basis from her self-audit | Contract, Art. 6(1)(b), for purposes (1) to (4) and (7): the candidate asks for the report, and it cannot be produced without their CV. Legitimate interests for (5) and (6). The brief names no basis (Finding 2) |
| Fix My Process (mine) | Legitimate interests, Art. 6(1)(f), for all 9 purposes; consent ruled out in an employment setting | The brief states no basis. Julia could not credit a basis that was decided but never written down |

**DPIA conclusion**

| System | Builder's self-audit | Peer audit |
|---|---|---|
| Interview Prep Report (Julia) | **TO ADD:** Julia's DPIA conclusion from her self-audit | Two EDPB indicators apply: evaluation or scoring, and innovative technology. A full DPIA may not be needed because the report serves the candidate and decides nothing about them, but the screening must be documented (Finding 6, Significant) |
| Fix My Process (mine) | Required before the pilot, on two EDPB criteria: employees as vulnerable data subjects, and innovative technology | No DPIA is evidenced in the brief. Julia rated two of the three documentation gaps (lawful basis, DPIA, human-review boundaries) Blocking; I had rated none Blocking |

**What independent review surfaced**

- **On my system, Julia caught what my self-audit softened:**
  - my brief never states the lawful basis, never evidences a DPIA and never draws human-review boundaries, although my self-audit covered all three;
  - the planned department summaries and employee evaluation are a present risk, because the design does not technically prevent them. My self-audit called them a future risk and concluded "proceed with conditions".
- **On Julia's system:** my external audit raised the missing DPAs, the full CV going to OpenAI, CV copies in n8n and Notion logs, and the lack of an ownership check on the CV and GitHub profile. **TO ADD:** which of these Julia's self-audit had already caught, and what it caught that I missed.

### Joint closing note

> Julia’s debrief shows that the hardest GDPR gaps to catch in your own work are documentation gaps, not design gaps. I knew which lawful basis I intended (legitimate interests) and that the outputs judge processes rather than people, so I filled those in as answers. Julia could only see that the brief never stated a basis, never evidenced a DPIA and never drew human-review boundaries, so she rated two of them Blocking where I had rated none. Self-assessment also softens severity and function creep: I graded the department summaries and employee evaluation as a “planned, future” risk and concluded “proceed with conditions”, while an outside reader treats anything the design doesn’t technically prevent as a present risk.

## Method

- Received only Julia's data processing brief, not her lawful basis assessment, DPIA analysis, memo or findings. The git history shows the brief committed alone (`9efd088`, 17 Nov 18:07) before any audit file (`d9da311`, 18:14).
- Worked independently until the debrief. Unclear points went into the questions log as Q1 to Q5, each with a stated assumption, rather than being asked.
- GDPR lens only. Severity follows the guide in [instructions.md](instructions.md).

## Limitations

- The audit is based on the brief alone; Julia's repository and workflow export were not reviewed.
- The controller role is assumed (Q1). An answer from Julia that contradicts any assumption in Q1 to Q5 changes the related finding.
- The Data Privacy Framework certification of each US vendor was not verified.

## Assumptions

- Julia runs the tool for the public with real candidate CVs, not only demo data.
- Law as of 17 Nov 2026.
- This is a course assessment, not a legal opinion, DPIA or certification.
