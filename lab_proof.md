# Lab Proof — GDPR Peer Audit

**Lab:** Audit your teammate's project — GDPR lens  
**Auditor:** Martha  
**Peer / project owner:** Barsha Mishra  
**Audited project:** AI Search Visibility Agent  
**Evidence status:** Document-based peer audit and written debrief; no independent technical execution or vendor-contract verification evidenced.

## 1. Entry points and evidence index

| Evidence item | Location | What it demonstrates | Status |
|---|---|---|---|
| Partner's original data processing brief | [`gdpr_peer_audit_barsha_data_processing_brief.md`](gdpr_peer_audit_barsha_data_processing_brief.md) | Input received for the independent audit | **Add/check file** in this repository |
| Independent audit (Phases 1–4) | [`gdpr_peer_audit_ai_search_visibility.md`](gdpr_peer_audit_ai_search_visibility.md) | Annotations, personal-data and role maps, clarification questions, findings, checklist and recommendation | Documented |
| Written debrief (Phase 5) | [Phase 5 in audit file](gdpr_peer_audit_ai_search_visibility.md) | Comparison of lawful basis, DPIA, findings, severity and closing reflection | Documented; final revised wording awaits explicit confirmation from both partners |
| Lab overview | [`README.md`](README.md) | Project description, file index and limitations | Documented |
| Optional architecture / workflow reference | [Barsha's project repository](https://github.com/barsha-mishra/ai-search-visibility-agent) | Public project context, if accessible | **Not independently verified** for this audit |

## 2. Input / example reviewed

**Input:** Barsha's written data processing brief for her AI Search Visibility Agent, rather than a live CV, email address or a workflow execution.

The brief describes user-provided brand/search information and a recipient email; Serper, NewsAPI and OpenAI research; report generation; n8n execution; Render-hosted fact-checking; QuickChart images; email delivery; and a Pinecone knowledge base said to contain public guidelines only.

**Review performed:** Classified possible personal data, flagged unclear flows and created a provisional vendor/role and transfer map. Findings and assumptions are recorded in Phases 1–4 of the audit file.

## 3. Output / result

**Final output:** [`gdpr_peer_audit_ai_search_visibility.md`](gdpr_peer_audit_ai_search_visibility.md).

**Audit recommendation:** **Proceed with conditions** for the described controlled/demo scope; verify and implement appropriate safeguards before live processing of personal data. Barsha agreed with the five findings and the conditional recommendation in her written response.

**Clarifications received from Barsha:**

- The workflow uses **n8n Cloud**; processing region and execution-data retention still need verification.
- She **plans** to replace personal Gmail with a business email arrangement that has an appropriate DPA; this has not been evidenced as complete.
- She **plans** to exclude personal brands; enforcement/testing has not been evidenced.

## 4. Peer exchange and debrief evidence

The written exchange described in the audit includes:

1. The partners' initial exchange of **data processing briefs only**, before sharing audit conclusions.
2. Martha's independent audit and questions about Barsha's agent.
3. Barsha's response agreeing with all five findings and **Proceed with conditions**.
4. Comparison of lawful bases, DPIA conclusions and **Blocking** versus **Significant** issues, including Barsha's independent review of Martha's interview-preparation project.
5. Barsha's proposed joint closing note, with a qualification that the Siemens sample report's real-person data origin remains **unverified**.

**Optional supporting proof to add, if available:** screenshots or exported messages showing the initial brief exchange, clarification responses, report exchange and agreement on the final closing note. Do not upload personal CVs or private data as proof.

## 5. Workflow / execution proof

**Workflow/code export:** Not included in this submission. Barsha's public project repository is listed as optional context, **not** as evidence that Martha independently inspected or ran the workflow.

**Live run / screenshots:** None supplied or independently verified for this audit. The assessed input was the written data processing brief. No live execution, vendor payload inspection, chart request capture or retention-setting test is claimed.

**Final output evidence:** The Markdown audit file itself, containing the GDPR analysis and written debrief.

## 6. Limitations and open verification items

- The exact data sent to each vendor and the actual processing regions have not been independently verified.
- Controller/processor roles, DPAs, international transfer mechanisms and privacy notices remain subject to verification.
- n8n Cloud retention settings and QuickChart's potential handling of viewer IP addresses remain untested.
- The proposed business-email replacement and personal-brand exclusion are **planned changes**, not confirmed fixes.
- The written debrief records a proposed joint closing reflection; explicit confirmation of the exact revised wording is not documented.

**Boundary:** This is a first-pass GDPR peer audit of a supplied brief, not a completed DPIA, legal advice, compliance certification or technical penetration test.

## 7. Before GitHub submission — checklist

- [ ] Confirm the unchanged original Barsha brief is saved under `gdpr_peer_audit_barsha_data_processing_brief.md`.
- [x] Save the independent audit with Phases 1–5 as `gdpr_peer_audit_ai_search_visibility.md`.
- [x] Add `README.md` and `lab_proof.md`.
- [ ] Confirm final wording of the joint closing note with Barsha if required by the instructor.
- [ ] Review Markdown links and remove any personal/sensitive information not needed for the lab.
- [ ] Commit and push the lab-specific repository; add the actual repository URL to the submission platform.
