# GDPR Peer Audit — AI Search Visibility Agent

**Lab:** Audit your teammate's project — GDPR lens  
**Auditor:** Martha  
**Project owner / audit partner:** Barsha Mishra  
**Project audited:** AI Search Visibility Agent (Ironhack Project 3)  
**Status:** Independent review and written peer debrief documented; technical and contractual remediation not verified.

## Purpose

This repository documents an independent, brief-based GDPR peer audit of Barsha's AI Search Visibility Agent. The tool researches brand visibility using search, news and AI services, generates a report, and delivers it by email. The audit considers incidental personal data, vendor roles, potential international transfers, retention, lawful bases, transparency and privacy risks.

The audit is a training exercise, **not** a legal opinion, a completed DPIA or a GDPR compliance certification.

## Files

| File | Purpose |
|---|---|
| [`gdpr_peer_audit_barsha_data_processing_brief.md`](gdpr_peer_audit_barsha_data_processing_brief.md) | Barsha's original data processing brief, shared for independent review. Keep the source content unchanged. |
| [`gdpr_peer_audit_ai_search_visibility.md`](gdpr_peer_audit_ai_search_visibility.md) | Martha's audit: Phase 1 annotations, Phase 2 data/role maps, Phase 3 clarification questions, Phase 4 findings and recommendation, and Phase 5 written debrief. |
| [`lab_proof.md`](lab_proof.md) | Evidence index, documented peer exchange, audit outputs, limitations and remaining proof to collect. |

> **Filename check:** If the original brief has not yet been copied into this repository under the name above, add it before submission. The audit and proof files do not replace the source brief.

## Audit process

1. **Exchange:** Each partner shared only their own Project 3 data processing brief before independent assessment.
2. **Independent review:** Martha assessed Barsha's brief and mapped data, vendors, roles and unresolved issues.
3. **Clarification:** Questions and later written clarifications were recorded, distinguishing confirmed facts from plans and unknowns.
4. **Audit report:** Findings were rated and the recommendation was **Proceed with conditions**, not unconditional clearance for live personal-data processing.
5. **Debrief:** Both partners compared lawful bases, DPIA conclusions and findings; the written exchange and a proposed joint reflection are documented in the audit file.

## Key outcomes

Barsha confirmed that the workflow runs on **n8n Cloud**, plans to replace personal Gmail with a business email arrangement, and plans to exclude personal brands. Those last two changes are **planned, not verified as implemented**. The exact n8n hosting region, retention settings, vendor contracts and transfer arrangements remain to be checked.

The joint debrief also covered Martha's separate **AI Interview Preparation Agent** and the decision to screen for DPIA risk and complete a full DPIA before using real CVs as a precautionary project condition. That is not evidence that a DPIA has already been conducted.

## Submission

Review all Markdown links, include the unchanged partner brief, and commit the files to the lab-specific GitHub repository. Add screenshots or workflow evidence only if genuinely available; do not claim that unperformed tests, implemented fixes or vendor reviews have been completed.
