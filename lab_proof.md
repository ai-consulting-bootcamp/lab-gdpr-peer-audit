# Lab proof: Menohelp GDPR peer audit

**Reviewer entry point.** Auditor: Sergii Rostovskyi. Teammate/builder: **Ben Mayer**. Audited project: **Menohelp / Project Menopause Insights** ([source](https://github.com/benmayer/proj-menopause-insights)), snapshot `89940e85b3f869b888e247a5b9651020b8d6c865`. Assessment: 17 November 2026.

**Outcome:** provisional **Do not proceed with real-health-data use** until the report's release gates close. Continue only genuinely synthetic local exercises with separate attention to operator metadata. This is an educational audit, not a compliance certification.

**Integrity limitation:** no colleague-written brief or GDPR self-audit was available. The brief is reconstructed and the debrief is simulated with the student's explicit authorisation. No discussion, peer approval, reciprocal audit or joint authorship is claimed. Literal requirements for real exchange and debrief remain unmet unless the instructor accepts the disclosed simulation or a real follow-up completes them. No commit, push or PR is part of this local delivery.

## Workflow export and final outputs

1. Reconstruct a descriptive [one-page brief](menohelp-reconstructed-processing-brief.pdf) from a pinned functional source snapshot, keeping unknowns explicit. [Editable brief](menohelp-reconstructed-processing-brief.md).
2. Apply [Phase 1 annotations](menohelp-brief-annotations.md), then complete [Phase 2 data/role maps and risk analysis](menohelp-data-roles-and-risk-analysis.md) from B0-B7.
3. Record [five clarifying questions](menohelp-clarifying-questions.md), with Q1-Q3 prioritised and all provisional assumptions retained.
4. Form the independent [two-page audit report](menohelp-gdpr-audit-report.pdf), containing all six required sections, seven findings, nine checklist rows, recommendation and disclaimer. [Editable report](menohelp-gdpr-audit-report.md).
5. Use the [six-step simulated debrief and proposed joint closing note](menohelp-simulated-debrief-and-closing-note.md). It also covers the reinforce exercise without inventing a real disagreement.
6. Follow the optional [half-page remediation plan](menohelp-remediation-plan.pdf). [Editable plan](menohelp-remediation-plan.md).

The [evidence/source register](menohelp-evidence-and-sources.md) provides pinned source links, legal references, reconstruction methodology and course-material reconciliation.

## One reproducible run: synthetic outbound-data probe

**Question:** do a user identifier and an identifying free-text concern survive into report-generation and retrieval inputs, despite the design's avoidance of raw cycle rows?

**Input:** invented user ID `audit.person@example.invalid`, age 46, six cycles with mean length 32, sleep severity 3, and the artificial concern `Synthetic case only: I am Alex Audit, alex.audit@example.invalid, with night sweats.` These describe no real person. Both addresses use the reserved `.invalid` domain.

**Code/workflow:** [menohelp-offline-privacy-probe.py](evidence/menohelp-offline-privacy-probe.py). Python 3.10+ standard library and Git. Use a separate checkout of the source at the exact commit, then run from this audit repository:

```text
python evidence/menohelp-offline-privacy-probe.py --source "PATH_TO_PEER_CHECKOUT" --output evidence/menohelp-offline-privacy-probe-result.json
```

The script checks the commit and rejects local changes in its four input source files. It executes selected actual source functions and literal constants, replacing vendor clients with offline spies. It never imports the full app, reads `.env`, sends emails or calls a vendor. Empty lab helper results isolate this fixture; this is not a complete application run.

**Recorded evidence:** [JSON result](evidence/menohelp-offline-privacy-probe-result.json), including exact fixture, captured generation message, captured embedding input, mocked RPC/selector calls, source hashes and function-line locators.

| Observation | Recorded result | Interpretation |
|---|---|---|
| User ID remains in generation message | True | Derived statistics do not guarantee removal of identifiers |
| Free-text identity remains in generation message | True | A length limit is not redaction |
| Same concern reaches embedding-client spy | True | Retrieval is another route to include in the data map |
| Mock query vector reaches Supabase RPC spy | True | Downstream retrieval is part of the flow; fixture vector does not prove real-vector identifiability |
| Symptom title selector reaches Supabase spy | True | The reference store also receives patient-derived query context |

**Actual run result:** 5/5 observations reproduced. These are successful reproductions of privacy-relevant behaviour, **not five passing privacy controls**. No synthetic input was transmitted to real vendors. The findings inform F4 and the completeness of F3; they do not establish an actual unlawful disclosure.

**Failure/limitation encountered:** the real builder brief and self-audit were unavailable, so strict exchange/debrief requirements cannot be proved. Technically, the probe cannot determine live destinations, contracts, consent validity, API exposure or end-to-end deletion. A source-level data-flow reproduction cannot certify compliance.

## Rubric coverage

| # | Rubric objective / criterion | Evidence | Honest completion status |
|---|---|---|---|
| 1 | Independent audit of another system | Brief provenance, report, evidence register | Analysis prepared; source-reconstruction departure disclosed |
| 2 | Structured report and recommendations | Two-page report, remediation plan | Prepared |
| 3 | Structured debrief reveals self-assessment blind spots | Debrief steps 3-6 | Simulated; real comparison unavailable |
| 4 | Only teammate's brief exchanged; ground rules | B0 and evidence-boundary disclosure | Not literally satisfied: no teammate brief exchange |
| 5 | Data and role tables from brief, gaps noted | Phase 2 tables with B references | Prepared from reconstructed brief |
| 6 | Questions: what/why/assumption | Q1-Q5 log | Prepared, no answers invented |
| 7 | Report sections/checklist/recommendation/disclaimer | Report sections 1-6 | Prepared |
| 8 | Six-step debrief, basis/DPIA comparison, joint note | Simulated debrief and proposed closing note | Method demonstrated; real discussion/joint approval outstanding |
| 9 | Phase 1 annotations | Annotation register | Prepared |
| 10 | Phase 2 maps | Data/role/risk analysis | Prepared |
| 11 | Phase 3 questions | Questions log | Prepared |
| 12 | Phase 4 report | Two-page PDF and Markdown | Prepared |
| 13 | Phase 5 conversation | Six-step simulation | Simulation only |

No grade or instructor approval is claimed. If a real debrief is mandatory, use the minimum-participation instructions at the end of the simulation and disclose that strict independence may require a fresh brief-based review.

## Submission state

Submission repository: [s-rostovskyi/lab-gdpr-peer-audit](https://github.com/s-rostovskyi/lab-gdpr-peer-audit). This link identifies the intended submission location, not evidence that these files have been published. Review the local deliverables first. Commit, push and PR require the user's separate confirmation; any eventual PR must retain the simulation disclosure.
