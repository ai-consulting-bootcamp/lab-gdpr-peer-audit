# Phase 1 — Read and annotate: Platform Risk Research Agent data processing brief

Annotation key: **[CAT]** = personal data category / special-category flag · **[?]** = unclear, needs clarifying question · **[EU]** = crosses an EU border · **[PURPOSE]** = purpose-limitation flag

---

## What personal data does the system process?

**1. Account data.** If a buyer signs up, the system collects a name and email. **[CAT: standard identifying data. Not special category.]**

**2. Buyer context data.** The user submits company name, use case, and internal context. This can include names of internal teams or roles if typed in. **[CAT: identifying/pseudo-identifying data — potentially about the buyer's own employees, not just the buyer themselves] [?: is this data about the signed-up user only, or can it name colleagues who never signed up or consented?]**

**3. Incidental data pulled from public web search.** The research agent pulls public content about the vendor, which can include named individuals in breach disclosures, news articles, or reviews. **[CAT: this is the highest-risk category — individuals here have no relationship with the platform at all] [PURPOSE: this data was published for one purpose (news, breach disclosure) and is now being reused for vendor risk-scoring — worth checking for compatibility]**

No special category data is intentionally collected, but it "could be inferred from public breach disclosures if a source names affected individuals and their health, criminal, or other sensitive status." **[CAT: Article 9 special-category risk, acknowledged as a real possibility, not a hypothetical]**

## Where does the data come from?

- Account and buyer context data: submitted directly by the user.
- Vendor research data: pulled from public web sources by the research tools.
- Nothing from an existing company database or data broker. **[good — rules out one common lawful-basis complication]**

## What is the data used for?

Each purpose (login/access, scoping, report generation) is kept separate, and the brief states none of the data is reused for a purpose the user didn't agree to. **[PURPOSE: this claim covers the *user's own* data well, but doesn't address the incidentally-collected third-party individuals in category 3 — they never agreed to anything, since they're not the user]**

## Who processes it?

- The Platform Risk Research Agent itself (FastAPI backend, LangGraph pipeline)
- DeepSeek, via Vercel AI Gateway, for reasoning calls
- OpenAI, for embeddings
- Pinecone, for vector storage
- Railway, for backend hosting

**All four vendors are US-based. [EU: every one of these is a non-EU processor]**

## Where is data stored and processed?

Report data and account data on Railway (US region); embeddings in Pinecone (US region); no EU-based storage. **[EU: brief explicitly states "personal data crosses the EU border on every use, if the buyer is in the EU" — this is the single most load-bearing sentence in the document]** **[?: no transfer mechanism (SCCs, adequacy, DPF certification) is mentioned anywhere in the brief]**

## Does the system make or assist in any decision that affects people?

The brief states the system scores a vendor, not a person, and that the alternative-vendor ranking "affects a business decision, not a person's rights or status," with no Article 22 automated decision currently made. **[reasonable on its face for the primary scoring function — worth treating as provisionally accepted rather than independently re-litigated, since I have no basis in the brief to dispute it]**

## Confirmation

The brief explicitly confirms the system does process personal data and does not qualify for a "no personal data" exemption. **[This closes off one possible minimal-tier argument that existed on the AI-Act side of this exercise — GDPR clearly applies here regardless of AI Act tier.]**
