# GDPR peer audit of the Editorial Research Agent

**Auditor:** Sandra Obregón. **Builder:** Jaime Garate Marquerie.

| Lab phase | Evidence |
|---|---|
| 1 and 2 | [Source annotations, data inventory and role map](audit_notes.md) |
| 3 | [Clarifying questions and builder responses](clarifying_questions.md) |
| 4 | [Audit report](audit_report.md) |
| 5 | [Debrief and approved joint note](debrief.md). Sandra confirmed both approvals on 18 November 2026. |

## Code and workflow

[Workflow export](workflow.md) and [source code reviewed at commit 3939562](https://github.com/jaimegmarquerie-ui/proyecto3-agente-editorial/tree/3939562dec432c07f804a5412cf4a8c02dfdccd3/editorial_agent).

## Observed run

- **Input:** The bookseller searched for works by a named author using the La Insumisa profile. The separate author field was empty at the start. See the [input and evidence extract](evidence/run_evidence.md).
- **Evidence:** Run ID `6d2c924b`, 11 November 2026. The first search found zero books. A rewritten query found ten, all judged useful for the shop.
- **Final output:** [Editorial dossier extract](evidence/editorial_dossier_extract.md), with the original dossier ID and status.
- **Limitation:** The initial author-less query produced no books. The system inferred the author and used its second search attempt. This was an existing saved run reviewed for the audit.
- **Evidence minimisation:** The evidence and output extracts keep the operational facts and remove unnecessary personal material, raw provider text and local paths.
