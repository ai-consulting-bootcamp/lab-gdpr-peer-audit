# GDPR peer audit: Virtual Coffee Chat Bot

**Auditor:** Gordan · **Provider audited:** John Adams · **System:** Virtual Coffee Chat Bot (Project 3)
**Date:** 19 August 2026 · **Status:** Advisory. Not a legal opinion. See Section 6.

## Audit trail and independence statement

Recorded first, because it qualifies everything below.

| Item | Detail |
|---|---|
| Evidence used to form this audit | John's published Project 3 documentation: workflow descriptions, tool and API table, setup notes, and his own written limitations section. |
| Data processing brief | Not received as a standalone document. The lab intends this to be the primary input; it was not available, so the project documentation was used instead and the gaps are logged in Section 5. |
| John's GDPR self audit | Received from John on 19 August 2026 at `github.com/jp92672/johna-lab-week7-day3-gdpr-self-audit`. The lab ground rules exclude it from the exchange. **It was not read until after Sections 1 to 6 below were complete.** The comparison against it is held separately in `debrief_note_gdpr.md` and forms no part of the findings here. |
| Key fact supplied by the provider | The system is currently demo only and not publicly reachable. This audit is written on that basis. |

## Section 1: System summary

A conversational agent that stands in for John Adams in a first contact with a recruiter. It answers questions about his work history, skills and projects from a retrieval layer holding his CV, CliftonStrengths results and narrative career material, and it takes actions: checking Calendly availability, booking a call, and sending email. Every conversational turn, together with thumbs up or down feedback, is written to a persistent `chat_log` table. It runs on self hosted n8n over OpenAI, Pinecone, Cohere, Calendly and Resend, exposed through a Cloudflare tunnel behind Basic Auth. The personal data it processes falls into two very different groups: John's own, which he supplied about himself, and that of anyone who talks to it, which is captured as a side effect of the conversation.

## Section 2: Data and role map

### 2.1 Personal data summary

| Data category | Source | Purpose | Crosses EU border? | Special category? |
|---|---|---|---|---|
| John's CV, employment history, project narrative | Supplied by John about himself | Answer recruiter questions | Yes. Embedded to OpenAI, stored in Pinecone, reranked by Cohere | No |
| CliftonStrengths results | Supplied by John about himself | Same | Yes | Not Article 9. Psychometric profiling data is sensitive in effect but is not a listed category unless it reveals health, which these do not |
| End user name and email | Conversation input, Calendly booking form | Booking a call, sending email | Yes. Calendly and Resend are US established | No |
| Full conversation transcripts | `chat_log`, every turn | Operation, and quality review via thumbs feedback | Yes, in transit through OpenAI | Possible by volunteering. A recruiter may disclose health, union membership or other Article 9 data unprompted, and the system stores whatever is typed |
| Thumbs up or down feedback | End user | Quality review | Stored locally | No |
| Error payloads | `error_log` plus alert email to John | Debugging | Yes, via Resend | Inherits whatever conversation content is in the payload |
| Meeting metadata and technical data | Calendly, Cloudflare tunnel, browser | Booking, transport | Yes | No |
| Third parties named in `kb/narrative/` | John's writing | Answering questions | Yes | Unknown. Cannot determine from the documentation |

### 2.2 Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| John Adams | Controller | Determines purposes and means for all processing. Also the data subject for one of the two data groups | Not applicable |
| End users (recruiters) | Data subjects | Conversation, booking, email | Not applicable |
| OpenAI | Processor | Embedding generation, chat completion. Conversation content passes through | Yes |
| Pinecone | Processor | Vector storage of John's own data only | Yes |
| Cohere | Processor | Reranking retrieved chunks | Yes |
| Calendly | Processor for booking data, independent controller for its own account and platform data | Availability and booking | Yes, and the dual role should be documented |
| Resend | Processor | Outbound mail delivery | Yes |
| Cloudflare | Processor | Tunnel transport, IP addresses | Yes |
| n8n | Not a processor | Self hosted. The software vendor processes nothing. If the host is a third party server, that host is a processor | Only if hosted by a third party |

The template row for a "client" does not apply. There is no client organisation: provider, controller and one of the two data subjects are the same natural person. That collapse is the single most important structural fact in this audit and is why an external review is worth more here than the system's size suggests.

### 2.3 International transfers

Every processor above is US established. Six transfer relationships, all requiring a Chapter V mechanism: either the vendor's EU US Data Privacy Framework certification or standard contractual clauses with a transfer impact assessment. The documentation evidences none of them. This is a paperwork gap rather than a design flaw, since each vendor publishes a DPA and most hold DPF certification; the work is to record which applies, not to negotiate anything.

## Section 3: Compliance findings

Severity is assessed against the system's current state, which the provider states is demo only. Where a finding would change severity on public exposure, that is noted. "Demo only" is a temporary condition, not a design property: the entire purpose of this system is to meet strangers.

> **Finding 1 — Lawful basis not identified for any processing purpose**
> **Severity: Significant now. Blocking on exposure.**
> **Description.** Article 6 requires a lawful basis per purpose. None is documented. Legitimate interests under Article 6(1)(f) is the right fit for operating the conversation and replying; it requires a documented balancing test that does not exist. Quality review from stored transcripts is a second, distinct purpose and needs its own basis and compatibility assessment under Article 6(4). Consent is a poor fit because the processing is not optional to the service.
> **Recommended action.** One page legitimate interests assessment covering both purposes. Half a day.
> **Escalation? No.**

> **Finding 2 — No processor agreements in place**
> **Severity: Significant now. Blocking on exposure.**
> **Description.** Article 28(3) requires a written contract with every processor before it handles personal data on the controller's behalf. Six processors, no agreements recorded. Today the only personal data flowing is John's own, which is why this is not yet blocking, but any demo given to a classmate, instructor or recruiter has already put a third party's data through all six.
> **Recommended action.** A processor register naming, for each vendor, the published DPA relied on and the date accepted. Two hours.
> **Escalation? No.**

> **Finding 3 — No Chapter V transfer mechanism documented**
> **Severity: Significant.**
> **Description.** Six US transfers, no DPF certification or SCC reference recorded, no transfer impact assessment. Applies equally to John's own data, so this one is live regardless of exposure.
> **Recommended action.** Add a transfer column to the processor register in Finding 2. Same exercise, no extra effort.
> **Escalation? No.**

> **Finding 4 — Security: the email tool is a personal data exfiltration path**
> **Severity: Significant now. Blocking on exposure.**
> **Description.** Article 32 requires security appropriate to the risk. The agent holds a send tool described as mailing "on the end user's behalf", behind a webhook, with no documented prompt injection defence. If the recipient address is agent selected from conversation input, an attacker can instruct the agent to mail the contents of retrieved context or prior conversation to an address they control. That is not an impersonation problem, it is an unauthorised disclosure of personal data under Article 32, and it would be a notifiable breach under Article 33. The provider's own documentation states that a tool reporting success on silently wrong output goes undetected, which removes the compensating control.
> **Recommended action.** Pin the recipient at the node rather than in the prompt. Full plan in `remediation_plan_email_tool.md`.
> **Escalation? Yes, to the provider before any demo to a third party.**

> **Finding 5 — No privacy notice**
> **Severity: Significant on exposure. Minor now.**
> **Description.** Article 13 requires notice at collection: controller identity, purposes, lawful basis and the legitimate interests relied on, recipients, transfers, retention, and rights including the Article 21 right to object. Nothing exists. Not yet biting because no third party is meant to be reaching it.
> **Recommended action.** Short notice linked from the chat interface. Two hours.
> **Escalation? No.**

> **Finding 6 — Retention undefined**
> **Severity: Significant.**
> **Description.** Article 5(1)(e) requires storage no longer than necessary. `chat_log` and `error_log` have no stated period and no deletion routine. Indefinite retention of conversation transcripts is the default state, and it is the hardest gap to close retroactively because the data accumulates while the policy does not exist.
> **Recommended action.** State a period, twelve months is defensible for a demonstration system, and implement deletion. Two hours.
> **Escalation? No.**

> **Finding 7 — Data minimisation in error alerting**
> **Severity: Minor.**
> **Description.** Article 5(1)(c). Error alerts forward payloads that may contain conversation content into a second system and into an inbox. More processing than debugging requires.
> **Recommended action.** Truncate or hash user content in error payloads. One hour.
> **Escalation? No.**

> **Finding 8 — Data subject rights not operationalisable**
> **Severity: Minor now. Significant on exposure.**
> **Description.** Articles 15 to 22 carry a one month deadline. There is no contact route, and no indication that `chat_log` can be searched by data subject to fulfil an access or erasure request. Pinecone holds only John's own data, so the retrieval layer is not implicated.
> **Recommended action.** Contact address in the privacy notice, and confirm `chat_log` is queryable by session and by email address.
> **Escalation? No.**

> **Finding 9 — DPIA screening not recorded**
> **Severity: Minor.**
> **Description.** Article 35 requires a DPIA where processing is likely to result in high risk. Assessed against the EDPB criteria, this processing meets one, innovative use of technology. It does not involve systematic evaluation with legal effects, large scale processing, systematic monitoring of a public area, vulnerable data subjects, or matching of datasets. A DPIA is therefore not required. A screening that was performed and reasoned away is a stronger position than one never considered, and nothing records that it happened.
> **Recommended action.** Half a page recording the screening and its conclusion. Revisit if the system is offered to other job seekers or if the knowledge base expands to third parties.
> **Escalation? No.**

## Section 4: GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | Gap identified | Finding 1. Two distinct purposes, neither documented |
| Purpose limitation respected | Cannot determine from documentation | Transcript reuse for quality review is a second purpose. Probably compatible under Art 6(4), but the compatibility assessment does not exist |
| Data minimisation | Gap identified | Finding 7. Transcript logging itself is proportionate; error payload forwarding is not |
| Controller and processor roles mapped, DPAs in place | Gap identified | Finding 2. Roles are clear on analysis but were never mapped, and no agreements are recorded |
| International transfer mechanism documented | Gap identified | Finding 3. Six US processors, no mechanism recorded |
| DPIA conducted if required | Appears met in substance | Finding 9. Not required on the EDPB criteria, but the screening is unrecorded |
| Article 22 safeguard if automated decisions affect people | Not applicable | The system makes no decision producing legal or similarly significant effects about the end user. It answers questions and books a slot at the user's own request |
| Privacy notice covers AI processing | Gap identified | Finding 5. No notice of any kind, so no AI specific disclosure either |
| Data subject rights operationalisable within deadlines | Cannot determine from documentation | Finding 8. No route documented and no evidence `chat_log` is queryable by data subject |

## Section 5: Overall recommendation

**Proceed with conditions.**

On the provider's statement that the system is demo only, no blocking finding stands today: the personal data currently flowing through six US processors is almost entirely John's own, and a controller processing his own data with no contracts and no notice is exposed to nobody but himself. That is why this is not a "do not proceed".

It is also why the recommendation is fragile. Every one of Findings 1, 2, 4 and 8 converts from Significant to Blocking the moment a third party talks to the bot, and a system whose stated purpose is to meet recruiters will not stay demo only. Note also that any demo already given to a classmate, instructor or contact has already processed that person's data through all six processors with no lawful basis, no agreement, no notice and no transfer mechanism. "Demo only" is a description of intent, not a technical control; Basic Auth on the tunnel is the only thing actually enforcing it.

**Conditions, all before the system is shown to anyone other than John:** document the lawful basis (Finding 1), record the processor agreements and transfer bases (Findings 2 and 3), pin the email recipient (Finding 4), and publish a privacy notice with a stated retention period (Findings 5 and 6). Total effort is roughly one working day, and every item is documentation except one node configuration change.

If the provider intends to link the bot from a CV or LinkedIn profile without completing those four items, this recommendation becomes **do not proceed**.

## Section 6: What this report is not

This report is not a legal opinion, not a DPIA, and not a certification of compliance. It was prepared by a non lawyer from the information available at the time of writing, without access to the running system, its workflow definitions, or its data stores, and without a data processing brief. Its severity assessments depend on the provider's statement that the system is not publicly reachable; if that is inaccurate, several findings become blocking. The provider should obtain legal review before relying on this assessment.
