# Menohelp: independent GDPR audit report

**Auditor:** Sergii Rostovskyi. **Builder:** Ben Mayer. **Date:** 17 November 2026. **Scope:** reconstructed brief B0-B7, snapshot `89940e85b3f86`. No builder brief/self-audit or interview was supplied. Findings are provisional; missing evidence is not proof of an actual violation. The PDF is the authoritative two-page layout. Supporting analysis is separate.

## 1. System summary

Menohelp turns cycle records, optional blood-test PDFs and symptoms into an individual explanatory report. Local code calculates statistics and parses selected laboratory values, while OpenAI supports retrieval and report generation. Supabase handles reference retrieval and Resend can email the report and chart. The repository describes local operation and includes a showcase labelled as based on real data; actual user history and permission for publication remain unknown.

## 2. Data and role map

Health inputs, derived findings and free-text concerns remain sensitive even after names are removed. IDs, ages, recipient addresses and service metadata can link them to people. Provisionally, the operator is controller; Ben is a processor only for a separate client's instructed processing. OpenAI, Supabase and Resend require activity-specific role/contract checks. External flows are established, but processing regions and Chapter V mechanisms are unverified. See B2-B6 and the separate data/role tables.

## 3. Compliance findings

### Finding 1 - Lawfulness and special-category data (Arts. 6, 7, 9)

**Severity:** Blocking for real-health-data use until resolved.
**Description:** B2/B7 establish health processing but no evidenced Article 6 basis plus Article 9 condition. Uploading alone does not establish explicit consent.
**Recommended action:** Approve purpose-specific grounds; for this optional consumer service, assess explicit consent and implement it before collection, with withdrawal.
**Escalation needed?** Yes - controller and privacy counsel.

### Finding 2 - DPIA before likely high-risk processing (Arts. 35/36)

**Severity:** Blocking for intended real-user operation pending resolution.
**Description:** B2-B3 combine health evaluation, several data sources and innovative technology; a DPIA is likely required. Completion is unknown, not proven absent.
**Recommended action:** Complete DPIA/national-list review or document a defensible contrary screen. Consult the authority if residual risk remains high.
**Escalation needed?** Yes - controller and DPO/privacy adviser.

### Finding 3 - Processors and transfers (Arts. 28, 44-49)

**Severity:** Significant; unresolved contracts/transfers remain release gates.
**Description:** B3/B4/B6 identify vendors but no accepted DPAs, destinations or transfer tools. Standard terms may contain a DPA; absence is not established.
**Recommended action:** Verify entities, accepted terms, subprocessors, regions and safeguards for generation, embeddings, query processing and email. Stop affected flows if required arrangements are absent.
**Escalation needed?** Yes - controller, procurement and counsel.

### Finding 4 - Minimisation and purpose limitation (Art. 5)

**Severity:** Significant.
**Description:** B3 retains user IDs and unrestricted concerns in derived payloads; B4 describes a potentially real-data public showcase. Private reporting does not establish permission for publication.
**Recommended action:** Remove unnecessary identifiers before all outbound routes; prefer structured symptoms. Verify showcase provenance and replace personal examples with synthetic ones unless separately justified.
**Escalation needed?** Yes - controller and builder; counsel for publication.

### Finding 5 - Confidentiality and access (Arts. 25/32)

**Severity:** Significant for local prototype; release gate for shared access.
**Description:** B5 shows an optional shared UI gate but no evident API ownership checks. This is not evidence of an internet-exposed endpoint or successful attack.
**Recommended action:** Keep API isolated; enforce authentication and dataset/lab ownership before shared use, test cross-user denial, and control email recipients and logs.
**Escalation needed?** Yes - builder/security owner.

### Finding 6 - Transparency, retention and rights (Arts. 5, 12-21)

**Severity:** Significant.
**Description:** B5/B7 do not demonstrate an AI privacy notice or end-to-end rights process. Lazy one-hour expiry does not cover sessions, exports, vendors or mailboxes.
**Recommended action:** Publish notice, assign a rights contact, define retention and test access/correction/deletion within one calendar month, subject to lawful extensions.
**Escalation needed?** Yes - controller and builder.

### Finding 7 - Automated effects assessment (Art. 22)

**Severity:** Significant assessment gap.
**Description:** B1 describes information, not a proven significant automated decision; actual reliance is unknown. A disclaimer or code checker is not human intervention.
**Recommended action:** Record intended/actual use. If significant solely automated decisions arise, establish a lawful exception, special-category restrictions and applicable intervention/contest safeguards before use.
**Escalation needed?** Yes - controller and counsel if consequential use is planned.

## 4. Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | Cannot determine from brief | F1: no purpose-specific record supplied |
| Purpose limitation respected (no incompatible reuse) | Cannot determine from brief | F4: showcase permission unresolved |
| Data minimisation (only necessary data collected) | Gap identified | F4: IDs/free text survive derived processing |
| Controller/processor roles mapped and DPAs in place | Cannot determine from brief | F3: provisional roles, contracts unverified |
| International transfer mechanism documented | Cannot determine from brief | F3: destination and safeguards unknown |
| DPIA conducted if required | Cannot determine from brief | F2: likely trigger, no completion evidence |
| Article 22 safeguard in place if automated decisions affect people | Cannot determine from brief | F7: significant effects not established |
| Privacy notice covers AI processing | Cannot determine from brief | F6: notice not supplied |
| Data subject rights can be operationalised within deadlines | Cannot determine from brief | F6: full process not demonstrated |

## 5. Overall recommendation

**Do not proceed** with real-person health-data collection, external processing, shared deployment or publication until F1/F2 are resolved and the relevant contract, transfer, security and rights gates are evidenced. This is a precautionary release decision, not a claim that unlawful live processing occurred. Continue only genuinely synthetic local exercises under controlled service accounts; separately assess operator metadata. Existing minimisation, PDF filtering and numeric checks are useful but do not establish legal authority or erase downstream copies.

## 6. What this report is not

This report is not a legal opinion, not a DPIA and not a certification of compliance. The client should obtain legal review before relying on this assessment. Basis: brief B0-B7; GDPR Articles cited above and EDPB DPIA guidance, linked in the accompanying evidence register. A simulated debrief does not constitute builder confirmation.
