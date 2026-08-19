# Phase 2 — Personal data and role map: Platform Risk Research Agent

## Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Account data (name, email) | Submitted directly by the user | Login and product access | Yes — stored on Railway, US region | No |
| Buyer context data (company name, use case, internal context; may include names/roles of the user's colleagues) | Submitted directly by the user | Scoping the vendor risk report | Yes — stored on Railway, US region | No, but potentially identifies people other than the submitting user — see Clarifying Question 1 |
| Vendor research / incidental data (named individuals appearing in breach disclosures, news, reviews) | Pulled from public web sources by the research tools | Producing the vendor risk report | Yes — processed via DeepSeek/Vercel AI Gateway and OpenAI (both US), stored as embeddings in Pinecone (US) | Not intentionally, but the brief itself acknowledges health/criminal status could be inferable from breach-disclosure sources — treat as a live Article 9 risk, not a remote one |

## Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Buyer company / signed-up user | Likely an independent controller for its own decision to use the report and for the internal context data it chooses to submit (including any colleague names it types in) — **not fully resolved from the brief; see Clarifying Question 2** | Submits account and context data; receives and acts on the report | N/A between buyer and builder unless the relationship is later characterized as joint controllership |
| Builder (Platform Risk Research Agent / Nelly) | Controller — determines the purposes and means of processing account data, buyer context data, and vendor research data | Runs the FastAPI backend and LangGraph pipeline; orchestrates all downstream processing | — |
| DeepSeek (via Vercel AI Gateway) | Processor | Reasoning calls on submitted/researched data | **Yes — not confirmed as in place** |
| OpenAI | Processor | Generates embeddings (`text-embedding-3-small`) | **Yes — not confirmed as in place** |
| Pinecone | Processor | Vector storage of the RAG corpus | **Yes — not confirmed as in place** |
| Railway | Processor | Hosts the backend service; stores report and account data | **Yes — not confirmed as in place** |
| Named individuals in breach disclosures / news / reviews | Data subjects with no direct relationship to the platform | Their personal data is incidentally processed as part of vendor research | Not applicable — but their Article 14/15 rights are a live open question, not a DPA question |

## International transfer

All four processors are US-based, and the brief states personal data crosses the EU border on every use where the buyer is in the EU. The brief provides no evidence of a transfer mechanism in place. The most likely applicable mechanisms would be Standard Contractual Clauses with each processor, or reliance on a processor's own EU–US Data Privacy Framework certification if it holds one — **I'm not fully certain which, if either, is currently in place, and I'd want that confirmed rather than assumed given how consequential it is (see Finding 1 in the audit report).**
