# Phase 1: annotated reading of the Menohelp brief

**Input:** [reconstructed brief B0-B7](menohelp-reconstructed-processing-brief.md). First pass: identify the service and end-to-end flow. Second pass: the annotation register below. These are analytical annotations of an auditor-created brief, not annotations received from the builder. No builder discussion or self-audit was available.

Legend: **PD** personal data; **SC** special-category data; **?** unresolved fact; **X** possible external/non-EEA route; **P!** purpose-reuse concern. X is the text equivalent of underlining, and ? of circling. Locations refer to brief paragraphs so that Phase 2 can be checked from the brief alone.

| Brief | Annotation | Interpretation / provisional position |
|---|---|---|
| B1 | ? Operator, jurisdiction, actual users, deployment | Audit conservatively assumes a professional EEA-facing service; educational/local execution alone is not an exemption. No live deployment established. |
| B2 | PD + SC: cycle dates, lengths, flow | Reproductive health information relating to a person; summaries retain sensitivity. |
| B2 | PD: age and user ID | Ordinary identifiers in isolation; links to a health record make the combined record sensitive. A user-supplied ID can itself be an email or name. |
| B2 | PD + SC: uploaded PDF, name/DOB, analytes, ranges, draw dates, derived age | Parsing identifiers out is a useful minimisation control; the server still initially processes the full PDF. Birth date can influence retained age. |
| B2 | SC + ?: symptoms, hormone/surgery context, free text | Health and potentially sex-life information; text may name the user or another person. Character limits do not anonymise it. |
| B3 | X + PD/SC: OpenAI generation and embedding | Two external routes. The concern is used for retrieval as well as report generation. Regions and logging are unknown. |
| B3 | X + ?: Supabase vectors and selectors | Reference corpus is not a patient database, but patient-derived queries and request metadata require assessment. Vectors are not automatically anonymous. |
| B4 | PD + SC + X: report, chart, email address, Resend and mailbox | Email reconnects the health narrative to a direct identifier. App memory limits do not erase vendor/mailbox copies. |
| B4 | P! + ?: public real-data showcase | Private reporting does not by itself authorise public publication. README claim requires provenance/permission verification; no actual breach is concluded. |
| B5 | ?: retention and access | One-hour threshold is lazy expiry; unknown session/export/vendor lifetimes and API access boundaries. |
| B6 | PD + X + ?: network/account metadata and vendors | Metadata can identify an operator or link requests. Identify legal entities and actual destinations before selecting a Chapter V mechanism. |
| B7 | ?: legal basis, consent, notice, DPIA, DPAs and rights | Missing evidence becomes a question and a release gate, not an invented builder answer. |

**Purpose boundary:** P1/P2 support the requested report; P3 optional email must be separately explained and selected. P4 public demonstrations, training, marketing or research require their own assessment and any necessary permission. No patient-training workflow is asserted.
