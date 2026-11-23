# Debrief and remediation plan: Application Prep Agent

Auditor: Friedrich Tschoepke · Builder: Nicolò Marseu

## Phase 5: Debrief (to complete with Nicolò)

| Step | Auditor (Friedrich) | Builder (Nicolò) | Agreed reading |
|---|---|---|---|
| Lawful basis, primary purpose | Contract (6(1)(b)) for self-use; client's own basis for coach submissions | | |
| DPIA required? | Yes: scoring, innovative technology, likely sensitive data | | |
| Self-audit caught, external missed | | | |
| External caught, self-audit missed | | | |

**Builder's context (5 minutes):**

**Joint closing note** *(required: what kinds of gaps are hardest to catch in your own work?)*:

## Reinforce: reflection on my own system

To complete after reading Nicolò's questions about my AI Use Case Identifier: which questions I cannot answer from my documentation, and one finding I first disagreed with.

## Stretch: remediation plan for Finding 1 (processor contracts and transfers)

| | |
|---|---|
| **Artifact** | (1) Email delivery switched from personal Gmail to a transactional email service with an EU data processing agreement. (2) A data processing agreement with the n8n host, or migration to a host that offers one (n8n Cloud or self-hosted in the EU). (3) Archived acceptance of OpenAI's DPA with a note on its transfer mechanism. (4) A one-page vendor register: vendor, role, data received, location, contract, transfer mechanism. |
| **Owner** | Nicolò as controller. A data protection adviser reviews the vendor register once. |
| **Timeline** | Email switch and OpenAI DPA: 2–3 days. Hosting decision with Ironhack: 1–2 weeks. Vendor register: 1 day. All before the sprint 1 pilot. |
| **Evidence a regulator would accept** | Signed or accepted DPAs with dates; the vendor register; screenshots of the new email configuration and n8n data-retention settings; a test run showing no data in the run history after the deletion period. |
