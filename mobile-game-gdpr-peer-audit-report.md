# Independent GDPR audit — Mobile Game Competitor Snapshot

**Reviewer** Sean Langsdorf · **Builder** Jędrzej Czarnota · **Scope** mk.III, hosted and client-managed modes · **Date** 17 November 2026

## 1. System summary

A studio employee submits a competitor name, delivery email and optionally an internal strategy PDF. The workflow gathers public studio, news and US storefront data and combines it with uploaded or fictional strategy material through OpenAI and Pinecone. It emails an AI-written briefing without prior human approval. Staff decide whether to act on its product and marketing suggestions.

## 2. Data and role map

Personal data can include requester emails, public names and roles, identifiable material in PDFs and report text. Game-level metrics alone are normally not personal data. The studio likely controls its research in both modes. The builder may process on its instructions in hosted mode and separately control its own sales activities. Recipient roles, hosting and transfer mechanisms remain unverified. See the [brief-only maps](mobile-game-brief-annotations-and-role-map.md) and [workflow evidence](mobile-game-workflow-audit-evidence.json).

## 3. Compliance findings

| Finding | Severity | Description | Recommended action | Escalation |
| --- | --- | --- | --- | --- |
| **1 · Isolation and disclosure** (Arts. 5, 25, 32) | **Blocking** | The reviewed export writes, clears and queries a fixed custom namespace on the same index and has an email fallback to a fixed mailbox. The brief describes autonomous delivery. In a hosted setup with overlapping jobs on that index, client material could be overwritten or misattributed. A missing address could route a report to an unintended mailbox. This is not a confirmed incident. | Disable live uploads and sending until per-request or per-tenant isolation is enforced and tested, a verified recipient is required, and missing or invalid recipients fail closed. | Yes · Engineering, security and DPO. |
| **2 · Roles and transfers** (Arts. 28, 44–46) | **Significant** | Vendor names and two operating modes are known. Actual contracts, recipient entities, access countries and mechanisms are not evidenced. | Document each leg, verify applicable processor terms and transfer safeguards, and block personal data flows where required terms or mechanisms cannot be shown. | Yes · Legal and procurement. |
| **3 · Basis, purpose and minimal inputs** (Arts. 5, 6, 9) | **Significant** | A delivery address can be necessary, but public names and full internal PDFs are not justified by default. No provision for sensitive data is evidenced. | Record purpose-specific necessity. Consider Art. 6(1)(b) only for necessary delivery when the individual is a contracting party, or document an Art. 6(1)(f) LIA. Prefer redacted company-only data and exclude Art. 9 data unless separately justified. | Yes · Controller and Legal. |
| **4 · DPIA, transparency and rights** (Arts. 12–22, 35) | **Significant** | No notice, rights workflow or DPIA is evidenced. Hosted, unrestricted uploads plus LLM retrieval and autonomous emailing are likely high risk if personal data can enter. No significant automated person decision appears on the described scope. | Screen both modes and complete a DPIA before any high-risk processing. Provide Art. 13/14 information as applicable, set retention, and test access, correction, erasure and objections across executions, vectors and mail. | Yes · DPO and operations. |

## 4. Specific obligations checklist

| Obligation | Assessment | Note |
| --- | --- | --- |
| Lawful basis per purpose | Cannot determine from brief | No basis recorded there. |
| Purpose limitation | Cannot determine from brief | Internal strategy may be reused externally. |
| Data minimisation | Gap identified | Whole PDFs accepted with no screening shown. |
| Roles and DPAs | Cannot determine from brief | No signed arrangements evidenced. |
| Transfer mechanism | Cannot determine from brief | Verify each deployment and vendor leg. |
| DPIA if required | Cannot determine from brief | Treat unrestricted hosted mode as likely high risk. |
| Art. 22 safeguard if triggered | Appears met | No significant solely automated person decision described. |
| AI privacy notice | Cannot determine from brief | Not provided. |
| Timely subject rights | Cannot determine from brief | No cross-store test or procedure evidenced. |

## 5. Overall recommendation

**Do not proceed with the reviewed hosted configuration on live personal data.** Resolve Finding 1 and confirm processor arrangements, transfer safeguards and the DPIA outcome before a live pilot. Restrict testing to fictional inputs and a mock outbox meanwhile. A segregated, client-managed deployment needs its own assessment, not automatic clearance.

## 6. What this report is not

This is not a legal opinion, DPIA or compliance certification. Obtain legal review before relying on it.
