# Stretch: remediation plan for Finding 1 (processor contracts, Art 28)

**Gap:** OpenAI, Tavily, Jina Reader, Hugging Face and Pinecone receive request data, and possibly page text with names and emails. No accepted DPA is verified, and two of them are used without an account.

| Question | Plan |
|---|---|
| **Artifact that closes it** | (1) A **vendor contract register**: one row per vendor with contracting entity, role (processor or independent controller), DPA version and acceptance date, sub-processor list link, region, retention setting, transfer mechanism. (2) The **accepted DPAs** filed as PDFs. (3) A half-page **role note** for Jina and Hugging Face: either they are independent controllers for keyless public access (with reasoning), or they get a contracted plan or are replaced. (4) A **config gate**: live mode refuses to run unless `INTAKE_LIVE_APPROVED=true` is set after the register is complete. |
| **Owner** | **Sergii** as controller today. In a client deployment, the **client's DPO** approves the register and authorises sub-processors (Art 28(2)); external counsel reviews the Jina/HF role note. |
| **Timeline** | Day 1: accept the OpenAI, Tavily and Pinecone DPAs (self-serve) and fill in the register. Days 2-5: settle Jina and Hugging Face (ask the vendors, decide, or swap Jina for a local extractor). Week 2: client DPO sign-off. **The gate goes in on day 1**, so live mode stays off until then. |
| **Evidence for a regulator** | Dated DPA acceptances tied to the account IDs actually in use · the register with a review date · the role note · a test showing live mode is blocked without the approval flag · the sub-processor list sent to the client and its written authorisation. |

**Why this one first:** it is the only blocking finding, and it is mostly paperwork. Pairing it with Sergii's redaction gate (his G1) means that even before the contracts are done, the data reaching vendors would be close to non-personal.
