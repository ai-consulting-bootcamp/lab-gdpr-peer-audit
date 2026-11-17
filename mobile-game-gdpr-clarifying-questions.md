# Clarifying questions — Mobile Game Competitor Snapshot

These questions were logged before discussion. The provisional positions below reflect uncertainty, not answers from the builder.

| # | What needs to be confirmed | GDPR consequence | Provisional position |
| --- | --- | --- | --- |
| 1 | In each mode, who decides why staff emails and playbooks are processed, who can access them, and what client/vendor agreements apply? Which service entities, host regions and support locations receive them? | Arts. 4, 26, 28, 30 and 44–46. Roles, processor commitments, accountability and transfers depend on each actual leg. | Treat hosted instructions as potential processor activity and own business purposes separately. Assume no DPA, adequacy coverage or SCCs are evidenced, not that none exist. |
| 2 | What can a real playbook contain, how are personal or sensitive details screened before embedding, and what proves that uploads, chunks and retrieval are isolated across client requests? | Arts. 5(1)(b), (c), (f), 6, 9, 25, 32 and 35. Purpose, necessity, access and high-risk screening turn on these controls. | Treat personal content as possible. Do not authorize real PDF use until field restrictions, isolation and deletion are evidenced. |
| 3 | How are email recipients verified, what happens on missing or mistyped addresses, and who can approve or halt delivery before the report leaves the system? | Arts. 5(1)(f), 25, 32 and 33–34. Disclosure can occur before anyone reads the report. | Treat the form as requesting a destination, not proving its authorization. Assume no pre-send human review and no proven address/domain control. |
| 4 | Which fields are sent to each API and retained in n8n, Gmail, Pinecone and backups? What deletion, correction and re-send procedures have been tested? | Arts. 5(1)(c), (e), 12–22, 25 and 28(3). The controller needs a way to find, correct, restrict and delete data and instruct processors. | Treat retention and rights compliance as unverified. Do not treat vectors, old report emails or attachments as automatically erased. |
| 5 | What lawful basis is used for delivery, public-source research, strategy tailoring and any service analytics? How do submitters and people named in sourced material get notice, and how often is the workflow used? | Arts. 5, 6, 13, 14, 21 and 35. Basis, reasonable expectations, transparency and DPIA threshold vary by purpose, scale and people affected. | A narrow Art. 6(1)(f) case may exist for necessary company-focused processing, subject to an LIA. Assume no blanket approval for real PDFs or person enrichment. Check Art. 14 case by case and no-scale claims against actual usage. |

## DPIA screen for the debrief

Check Art. 35 and the applicable national supervisory authority list per deployment. The EDPB criteria are a screening aid, not a numerical safe harbour.

| EDPB risk signal | Provisional assessment |
| --- | --- |
| Evaluation or scoring | Company/game scores, not known individual profiling. |
| Automated significant individual decision | Not on the described purpose. Email automation does not itself determine an individual's rights or access. |
| Systematic monitoring | Not evidenced. A user-initiated company snapshot is not continuous tracking of people. |
| Sensitive or highly personal information | Possible in arbitrary playbooks or snippets. Whether it is common is unknown. |
| Large scale | Number of clients, people and documents is not evidenced. |
| Matching or combining datasets | Public data is combined with internal context. Matching around identifiable people across contexts is possible but not shown as the design purpose. |
| Vulnerable data subjects | Not targeted. Uploaded staff material could include employees in an imbalanced relationship. Frequency and effects unknown. |
| Innovative technical/organizational use | Likely relevant for multi-vendor LLM synthesis and retrieval of uploaded business documents. |
| Prevents a right, service or contract | Not indicated. No natural-person gate is described. |

**Provisional result.** File and recheck the screen before live use. For hosted, multi-client processing of unconstrained PDFs that may contain personal data, treat the current design as likely high risk and complete a DPIA before release unless a documented controller assessment establishes otherwise. Consider sensitivity, access across clients, automated external disclosure, actual scale and reasonable expectations together. For a narrower, segregated workflow with no live PDFs, minimal professional data and verified delivery, reassess and record whether a DPIA is still required. Consult under Art. 36 if high residual risk remains despite mitigation.
