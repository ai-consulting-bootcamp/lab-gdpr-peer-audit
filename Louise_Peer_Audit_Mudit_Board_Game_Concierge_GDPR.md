# Peer Audit — GDPR — Board Game Concierge

**Auditor:** Louise Plessis  
**Teammate / Builder:** Mudit  
**Project audited:** Board Game Concierge  
**Lab:** Audit your teammate's project — GDPR lens  
**Date:** 19 August 2026

---

# Phase 1 — Read and annotate

## Data-processing summary

Board Game Concierge is a Telegram conversational application that processes user messages in order to answer board-game questions, maintain conversational context, provide recommendations, and retrieve strategy information.

Mudit clarified that the application processes:
- Message text and follow-up questions.
- Telegram user ID/chat ID.
- Username/display name if present.
- Stated game preferences and constraints.
- Short-lived conversation context and pending intent.

Conversation context is stored in memory only for the active session.

The system also uses external services including OpenAI and search APIs. Mudit clarified that raw messages are not directly passed to Pinecone, SerpApi, Serper, or Tavily. Instead, messages are processed to identify their core meaning or keywords, which may then be supplied to external APIs as query parameters.

## Personal-data annotations

### Personal data clearly or potentially processed
- Telegram message content.
- Follow-up questions.
- Telegram user ID / chat ID.
- Username / display name if present.
- Game preferences and constraints.
- Short-lived conversation context.
- Derived search queries/keywords.
- Technical or vendor logs where applicable.

### Special-category data

No special-category data are required for the service.

Because the product accepts free-text messages, users could incidentally disclose Article 9 information. This is possible but not an intended processing purpose.

### International-transfer observations

The project uses several external technology providers. The precise transfer position remains incomplete because the exact processing locations, vendor payloads, contractual entities, and vendor retention/reuse policies are not fully documented.

A transfer analysis is therefore required for services actually receiving personal data.

### Purpose-limitation observations

The core purposes are clear:
- answering users' questions;
- recommending games;
- maintaining short-lived conversational context;
- supporting retrieval.

No incompatible secondary use is documented, but vendor reuse of prompts or queries remains unclear.

---

# Phase 2 — Personal data and role map

## Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Message text | Telegram user | Answer questions | Cannot fully determine | Normally no; free text could contain sensitive data |
| Follow-up questions | User | Conversation continuity | Cannot determine | Same caveat |
| Telegram user/chat ID | Telegram | Routing/session handling | Cannot determine | No |
| Username/display name | Telegram | User/session identification | Cannot determine | No |
| Game preferences/constraints | User | Recommendations | Cannot determine | Normally no |
| Conversation context | User interaction | Maintain active conversation | Cannot determine | Could reflect sensitive information if voluntarily disclosed |
| Derived search keyword/query | Backend | Retrieve strategy information | Potentially, depending on provider/location | Normally no |
| Rulebook embeddings | Rulebooks | Retrieval | Pinecone infrastructure | Not personal data on current facts |

## Role map

| Entity | Provisional role | Processing activity | DPA needed? |
|---|---|---|---|
| Board Game Concierge operator / owner | Controller | Determines purposes and means of the service | N/A |
| Builder / Mudit | Same controller activity if also operating the service; otherwise role depends on client relationship | Development/operation | Depends on actual arrangement |
| n8n | Potential processor | Workflow/orchestration of user messages | Yes, if acting as processor |
| OpenAI | Potential processor or other recipient depending on contractual setup | AI inference / synthesis | Yes if acting as processor |
| Telegram | Requires activity-specific assessment | Communication platform and transmission of user interactions | TBD |
| Pinecone | Potential processor only if personal data are processed there | Rulebook vector storage/retrieval | Only if personal data are processed |
| SerpApi / Serper / Tavily | Potential processors or other recipients | External strategy-search queries | TBD based on actual payload and role |

## International transfer position

For every vendor receiving personal data, the controller must determine:
- where processing occurs;
- which legal entity provides the service;
- whether an adequacy mechanism applies;
- or whether another Chapter V transfer mechanism is required.

**Current assessment:** Cannot fully determine from available information.

---

# Phase 3 — Clarifying questions log

## Question 1 — Personal-data flow

**What I needed to know:**  
Exactly which Telegram data are sent through Telegram → n8n → FastAPI → OpenAI?

**Why it matters:**  
This determines the personal-data map, data minimisation assessment, recipients, and privacy-notice requirements.

**My provisional assumption:**  
Message content and some identifier necessary to route conversations were likely processed.

**Mudit's answer:**  
The system processes message text, follow-up questions, Telegram user ID/chat ID, username/display name if present, user-stated game preferences/constraints, and short-lived conversation context/pending intent.

**Updated conclusion:**  
These data categories should all appear in the formal processing map.

## Question 2 — Storage and retention

**What I needed to know:**  
What user/conversation data are persisted anywhere in the system, including application session memory, n8n execution history, OpenAI/vendor logs, and for how long?

**Why it matters:**  
This determines storage limitation and affects deletion and rights processes.

**My provisional assumption:**  
Application session state was transient/in-memory, while n8n and third-party retention were unknown.

**Mudit's answer:**  
Conversation context is in-memory only for the active session.

**Updated conclusion:**  
Application-level retention is relatively limited, but full storage-limitation compliance cannot yet be verified because n8n execution history and vendor-side retention remain unclear.

## Question 3 — Pinecone and external providers

**What I needed to know:**  
Do user messages or other user-derived personal data enter Pinecone, SerpApi, Serper, or Tavily?

**Why it matters:**  
This affects the processor/recipient map and international-transfer assessment.

**My provisional assumption:**  
Pinecone contains only rulebook chunks, while search providers may receive user-derived queries.

**Mudit's answer:**  
Not directly. Messages are reviewed and broken down to identify the core message, extract keywords, and then sent as query parameters within API requests.

**Updated conclusion:**  
This reduces unnecessary disclosure but does not automatically make the derived query non-personal data. Actual payloads should still be inspected.

## Question 4 — Lawful basis

**What I needed to know:**  
Which Article 6 lawful basis was selected for processing user messages and conversation context?

**Why it matters:**  
Every processing purpose requires a lawful basis.

**My provisional position:**  
Article 6(1)(b) could potentially apply if processing is necessary to deliver a service under a genuine contractual relationship.

**Mudit's answer:**  
Article 6(1)(f) legitimate interests for answering user questions, recommending games, maintaining short-lived chat context, and storing vectors/embeddings for retrieval.

**Updated conclusion:**  
Article 6(1)(f) is the stronger provisional basis on the currently documented facts because no contractual relationship with users has been established. However, the legitimate interest, necessity, and balancing against users' rights should be documented in a Legitimate Interests Assessment.

## Question 5 — DPIA

**What I needed to know:**  
Did the self-audit conclude that a DPIA is required?

**Why it matters:**  
The lab requires comparison of independent and self-audit DPIA conclusions.

**My provisional conclusion:**  
A mandatory DPIA did not appear required on the current MVP facts.

**Mudit's answer:**  
No firm conclusion that a DPIA is required. He would tighten the wording to: "not clearly mandatory yet, but strong candidate for escalation once vendor retention and transfer details are confirmed."

**Updated conclusion:**  
A DPIA is not clearly mandatory on the presently documented processing, but the screening should remain open and be reassessed once vendor retention, transfers, scale, and any secondary processing are fully known.

---

# Phase 4 — GDPR audit report

## Section 1 — System summary

Board Game Concierge processes Telegram messages and related identifiers to provide conversational board-game assistance. Personal data include message content, follow-up questions, Telegram user/chat IDs, usernames/display names where present, preferences, and short-lived session context. OpenAI and other external services contribute to response generation and information retrieval. Conversation context itself is held in-memory for the active session.

## Section 2 — Data and role map

The Board Game Concierge operator is provisionally the **controller**.

n8n, OpenAI, and other service providers may act as processors or other recipients depending on their factual role and contract.

Pinecone appears to store rulebook material rather than user conversations.

External search services receive extracted queries/keywords instead of full messages.

International-transfer status cannot yet be fully verified because vendor locations, retention, and contractual mechanisms remain insufficiently documented.

## Section 3 — Compliance findings

### Finding 1 — Legitimate-interest basis needs documentation

**Severity:** Significant

**Description:**  
Mudit selected Article 6(1)(f) legitimate interests for the primary processing purposes.

This is plausible for the current recreational use, but the justification itself is not enough. The controller should establish the legitimate interest pursued, demonstrate necessity, and balance that interest against users' rights and reasonable expectations.

**Recommended action:**  
Create a documented Legitimate Interests Assessment for the relevant purposes. Keep separate any purpose that is not necessary for operating the service, such as future analytics or model improvement.

**Escalation needed?**  
Yes — privacy/legal review.

### Finding 2 — Privacy notice absent

**Severity:** Significant

**Description:**  
Mudit confirmed that his self-audit identified no privacy notice.

Users currently do not have an evidenced notice explaining processing purposes, lawful basis, recipients, retention, transfers, or rights.

**Recommended action:**  
Create a concise Telegram-accessible privacy notice covering the actual processing.

**Escalation needed?**  
Yes — privacy owner.

### Finding 3 — Processor/DPA evidence absent

**Severity:** Significant

**Description:**  
Mudit's self-audit identified no evidence of DPAs for the relevant processors.

Because services including n8n and potentially OpenAI process user-derived information, processor relationships need to be identified and Article 28 arrangements confirmed where applicable.

**Recommended action:**  
Create a vendor register, assign GDPR roles, and retain DPA evidence for processors.

**Escalation needed?**  
Yes — privacy/legal owner.

### Finding 4 — International transfer position incomplete

**Severity:** Significant

**Description:**  
The exact vendor payloads, processing locations, and transfer mechanisms remain under-specified.

The fact that raw messages are transformed before reaching external search providers reduces disclosure but does not settle whether personal data are transferred.

**Recommended action:**  
Inspect actual API payloads and vendor configurations. Determine which vendors receive personal data and document the applicable transfer mechanism where necessary.

**Escalation needed?**  
Yes — privacy/legal review.

### Finding 5 — Retention schedule and deletion workflow absent

**Severity:** Significant

**Description:**  
Application conversation context is short-lived and stored in memory only, which reduces persistence.

However, Mudit's self-audit identified:
- no retention schedule;
- no documented deletion workflow for chat history, embeddings, or logs.

n8n and external-vendor retention also remain unclear.

**Recommended action:**  
Create a retention schedule covering each system and vendor, with deletion procedures and owners.

**Escalation needed?**  
Yes — controller/privacy owner.

### Finding 6 — Data-subject-rights workflow absent

**Severity:** Significant

**Description:**  
Mudit identified no documented process for handling access, erasure, or other rights requests.

**Recommended action:**  
Create a simple rights-request process identifying where data can be located, exported, corrected, or deleted across the stack.

**Escalation needed?**  
Yes — privacy owner.

### Finding 7 — RoPA absent

**Severity:** Minor / scale-dependent

**Description:**  
Mudit's self-audit identified no Record of Processing Activities.

**Recommended action:**  
Maintain a processing record capturing purposes, categories, recipients, retention, and transfer information where Article 30 applies, and in any case use the same structure as a practical accountability artifact.

**Escalation needed?**  
No immediate escalation for the prototype; verify Article 30 applicability before scaling.

### Finding 8 — Incident-response process absent

**Severity:** Minor for current prototype / Significant before scale

**Description:**  
Mudit's self-audit found no documented incident-response procedure.

**Recommended action:**  
Define how suspected personal-data breaches are identified, escalated, documented, and assessed.

**Escalation needed?**  
Not immediately for the prototype, but assign an owner before broader use.

## Section 4 — Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | **Appears partially met** | Article 6(1)(f) selected; LIA evidence still needed |
| Purpose limitation respected | **Cannot fully determine from brief** | Core purpose clear; vendor reuse of prompts/queries unknown |
| Data minimisation | **Appears partially met** | Search queries are reduced to core terms, but actual vendor payloads need inspection |
| Controller/processor roles mapped and DPAs in place | **Gap identified** | No DPA evidence |
| International transfer mechanism documented | **Gap identified** | Vendor locations/mechanisms incomplete |
| DPIA conducted if required | **Cannot yet determine** | Not clearly mandatory on current facts; reassess after vendor/scale clarification |
| Article 22 safeguard in place if automated decisions affect people | **Appears not applicable** | Outputs do not appear to create legal or similarly significant effects |
| Privacy notice covers AI processing | **Gap identified** | No privacy notice |
| Data subject rights can be operationalised within deadlines | **Gap identified** | No documented workflow |

## DPIA conclusion

**Final position after debrief: Not clearly mandatory yet — reassess as the processing picture becomes complete.**

The system currently appears recreational, relatively low-consequence, and does not appear to make significant automated decisions about individuals.

However, vendor retention, transfers, actual processing scale, and secondary uses remain incomplete.

Therefore, rather than concluding definitively that no DPIA is required, the appropriate position is to document the screening and reassess it when those facts are known.

## Article 22 conclusion

Article 22 does not appear applicable on the current facts.

The assistant provides board-game recommendations and informational responses rather than decisions creating legal or similarly significant effects.

## Section 5 — Overall recommendation

### PROCEED WITH CONDITIONS

The GDPR audit does not identify a reason to redesign the core Board Game Concierge functionality.

However, the privacy governance surrounding the product is incomplete.

Before broader deployment, the controller should:
1. Document the Article 6(1)(f) legitimate-interest assessment.
2. Publish a privacy notice.
3. Map processors/vendors and obtain required DPA evidence.
4. Verify international transfers and actual vendor payloads.
5. Establish retention/deletion rules.
6. Implement a data-subject-rights workflow.
7. Reassess the DPIA requirement once vendor and scale information is complete.

## Section 6 — What this report is not

This report is not a legal opinion, DPIA, or certification of GDPR compliance.

The assessment is based on the available project information and Mudit's clarifications and should be validated with qualified privacy/legal counsel before being relied upon for production use.

---

# Phase 5 — GDPR debrief

## 1. Auditor presents

My external audit initially identified lawful basis, vendor roles, international transfers, retention, privacy transparency, and rights management as the principal areas requiring clarification.

I initially considered Article 6(1)(b) as a possible lawful basis and considered a mandatory DPIA unlikely.

## 2. Builder responds

Mudit clarified the actual personal-data categories processed and confirmed that conversation context is in-memory only.

He also explained that external search providers receive extracted queries rather than full raw messages.

His self-audit selected Article 6(1)(f) legitimate interests and identified a broader set of governance gaps:
- No privacy notice.
- No retention schedule.
- No RoPA.
- No DPA evidence.
- No documented deletion workflow.
- No rights workflow.
- No incident-response process.
- No AI disclosure.

## 3. Compare lawful basis selections

**Auditor initial position:**  
Article 6(1)(b) might apply if a contractual/service relationship exists.

**Builder:**  
Article 6(1)(f) legitimate interests.

**Final position:**  
Article 6(1)(f) is the stronger provisional basis on the current facts because there is no demonstrated contractual relationship.

A documented Legitimate Interests Assessment should nevertheless validate this choice.

## 4. Compare DPIA conclusions

**Auditor initial conclusion:**  
Mandatory DPIA probably not required.

**Builder:**  
No firm conclusion that a DPIA is required; better phrased as not clearly mandatory yet but a strong candidate for escalation once vendor retention and transfer details are confirmed.

**Joint conclusion:**  
We agree that a DPIA is **not clearly mandatory on the presently documented MVP**, but the screening should remain open and be reassessed once processing scale, vendor retention, and transfer arrangements are fully understood.

## 5. Compare gap lists

The builder's self-audit identified several formal governance artifacts that my first-pass external audit did not foreground, particularly:
- RoPA.
- Incident-response process.
- Detailed deletion workflow.

The external audit concentrated more on uncertainties that an outsider cannot resolve from the implementation documentation:
- Exact vendor payloads.
- n8n execution-history retention.
- Possible vendor reuse of prompts/queries.
- FastAPI data handling that is evident architecturally but insufficiently documented.

This was the clearest difference between the two perspectives.

## 6. Joint closing note

The GDPR debrief showed that builders tend to know what the system is intended to do but can overlook formal governance artifacts because the technical flow feels obvious to them. An external reviewer is more likely to expose undocumented boundaries — especially what exactly leaves each component, what vendors retain or reuse, and which claims about minimisation, transfers, or deletion can actually be evidenced.

---

# Reinforce

The strongest lesson from the peer audit was that low-risk technical choices are not enough if they are not documented.

For example, the application uses short-lived in-memory conversation context, and the search flow reduces messages to extracted queries rather than sending complete conversations. These are useful privacy-preserving choices. However, an external reviewer still cannot determine the full privacy position without vendor payloads, logging information, retention terms, and evidence of the relevant agreements.

The gap is therefore partly product governance and documentation, not necessarily a flaw in the core application design.

---

# Stretch — Remediation plan

## Significant finding selected: Incomplete GDPR data-processing and vendor governance

**Specific artifact:**  
Create a GDPR Data Processing & Vendor Register, supported by a Legitimate Interests Assessment.

The register should cover:
- Telegram.
- n8n.
- FastAPI.
- OpenAI.
- Pinecone.
- SerpApi.
- Serper.
- Tavily.

For each, record:
- personal data received;
- purpose;
- lawful basis;
- controller/processor role;
- retention;
- processing location;
- DPA status;
- transfer mechanism;
- vendor reuse conditions;
- deletion mechanism.

**Owner:**  
Technical owner for factual system mapping.  
Controller/privacy owner for lawful basis and retention.  
Legal/DPO or external counsel for processor agreements and international transfers.

**Timeline:**  
2–3 working days for the technical/vendor inventory, followed by 1–2 working days for privacy/legal review.

**Evidence required to close:**  
The processing register matches the implemented architecture, actual API payloads have been checked, vendor roles and contracts are documented, retention and deletion periods are defined, applicable transfer safeguards are evidenced, and the Legitimate Interests Assessment has been completed.
