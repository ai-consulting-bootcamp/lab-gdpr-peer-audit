# CompanyScope remediation plan

**Priority finding:** unresolved vendor processing and international-transfer safeguards  
**Related audit finding:** Finding 2 in `companyscope_gdpr_audit_report.md`

## Remediation objective

Prevent the CompanyScope workflow from sending live personal data to OpenRegister, Tavily, OpenAI, n8n or any subprocessor until the controller can identify each recipient, confirm the role and contract, and document where the data is processed.

## Plan

| Requirement | Plan |
|---|---|
| Artifact that closes the gap | A signed data-flow/vendor register; Article 28 DPA or equivalent processor terms for each processor; subprocessor list; retention and model-use settings; and an Article 46 SCC/transfer-impact-assessment package where a non-EEA transfer is confirmed. |
| Owner | Deploying controller owns the decision; procurement owns contract collection; DPO/privacy lead and legal counsel review the role, transfer and TIA analysis. Sean supplies the technical data-flow and configuration evidence. |
| Timeline | Freeze live personal-data testing immediately. Produce the technical inventory within 2 business days; complete vendor and transfer review within 10 business days; obtain approvals before production or external report sharing. |
| Evidence for a regulator | Versioned data-flow diagram; field-level vendor matrix; signed agreements and SCC annexes; destination/subprocessor list; documented TIA and supplementary measures; screenshots or export of retention/model settings; deletion test; and controller approval record. |

Until this evidence exists, use synthetic or demonstrably non-personal data and keep reports in a controlled test environment.
