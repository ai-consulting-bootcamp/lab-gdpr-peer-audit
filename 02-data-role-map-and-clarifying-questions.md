# Phases 2-3: Personal data and role map, clarifying questions - Model Intake Brief

Built **from the brief alone** (plus the project README's architecture). Gaps in the brief are marked **[gap]**. ⚖️ = needs counsel.

**Scope.** The brief covers today's local educational prototype. Sergii's AI Act brief assumed a future professional deployment by an EU client, so I map **both**: *today* (Sergii as sole operator) and an *assumed client deployment* (see Q2).

## Phase 2: Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Author names, repository handles in model IDs and URLs | Public model cards, Hugging Face Hub, provider docs (indirect, Art 14) | P1 retrieve docs; P2 assess and quote | **Yes**: Hugging Face (model ID), Jina (URL), OpenAI (snippets) | No |
| Named business contacts, email addresses | Public docs (indirect) | P2 (they reach the LLM payload, as his probe shows); P3 if quoted in the report | **Yes**: OpenAI | No |
| Same data inside quotes and source URLs of the report | Generated report | P3 retain and share for review and educational demo | Depends where the report is stored **[gap]** | No |
| Operator IP address, account and request metadata | Sergii today; client reviewers later | P4 operate and troubleshoot; implied by P1/P2 | **Yes**: every vendor, plus every source website during link checks | No |
| Reviewer identity (who ran what) | Client deployment only **[gap: not described]** | P3 accountability for the review decision | Unknown | No |
| Incidental sensitive text in fetched pages | Arbitrary web content | Not a purpose; a by-product of P1/P2 | Yes (OpenAI) | **Possible, not expected** |
| Regulatory corpus, checklist queries | Public law texts, fixed queries | Regulatory retrieval | Yes (OpenAI embeddings, Pinecone) | **Not personal data** |

**Purpose-compatibility check (Art 6(4)):**
- **P1-P2, compatible.** People publish model cards and contacts *so that* others can evaluate and contact the provider. Governance review fits that context.
- **P3 "educational demonstration", flag 🚩.** Publishing reports that preserve individuals' names or emails takes the data into a new audience. Today's two samples contain none. That is luck, not a control.
- **Possible future reuse, flag 🚩.** Using harvested contact emails to send the "provider questions" to individuals is a new purpose. It is fine for a corporate address, but a personal one needs a check.

## Phase 2: Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| **Client** (assumed EU company, future) | **Controller** | Decides to review models and why; receives and keeps reports; its staff operate the tool | n/a. Needs an Art 28 DPA **with Sergii** if he hosts the tool. |
| **Builder** (Sergii) | **Today: controller** (sets purpose and means). **Client deployment: processor** if he hosts it as a service; **no GDPR role** if the client runs it as licensed software on its own machines ⚖️ | Builds and runs the pipeline | **Yes**, with the client, if he hosts it. **[gap]** |
| **OpenAI** | **Processor** (today, to Sergii) / **sub-processor** (client deployment) | Assessment and embeddings | **Yes.** Acceptance unverified (brief). |
| **Tavily** | Processor / sub-processor | Search queries (model names, provider domains) | **Yes**, if queries carry personal handles. Unverified. |
| **Jina Reader** | Processor / sub-processor | Fetches and extracts page text, sees URLs that may contain handles | **Yes.** Used **without an account or key**, so there is **probably no contract at all** **[gap]**. |
| **Hugging Face Hub API** | Processor, or **independent controller** of its own API logs ⚖️ | Repository metadata lookups by model ID | Depends on the role; unauthenticated public API, so likely no contract **[gap]** |
| **Pinecone** | Processor (operator account data only) | Vector store for the regulatory corpus | Yes, for account and metadata; low risk |
| **Source websites** | **Independent controllers** | Receive operator IP addresses during link checks | No |
| **People named in docs** | **Data subjects** | n/a | n/a |

### International transfers

| Flow | Mechanism needed | Evidence in brief |
|---|---|---|
| → OpenAI (US) | EU-US Data Privacy Framework (only if the OpenAI entity is on the active DPF list ⚖️), else SCCs + transfer impact assessment. Or avoid it with EU data residency | **None**. "EEA-only processing cannot be claimed" |
| → Tavily, Pinecone (US) | DPF or SCCs + TIA | None |
| → Hugging Face (US/FR) | DPF or SCCs if processing is in the US | None |
| → Jina Reader | Depends on location **[gap]** | None |
| → Source websites (anywhere) | Arguably not a transfer by the controller: the operator *visits* public sites and sends only its own IP. Low risk ⚖️ | n/a |

## CFU 2 - Probe: the three most important questions

The top 3 from the log below, ranked by how much the answer changes my opinion:

1. **Q1:** Are vendor DPAs in place? (Decides blocking vs significant.)
2. **Q2:** Who hosts it in a client deployment? (Decides the whole role map.)
3. **Q3:** What happens to reports after they are generated? (Decides retention, purpose limitation and rights.)

## Phase 3: Clarifying questions log

| # | What I need to know | Why it matters (GDPR obligation) | Provisional assumption |
|---|---|---|---|
| **Q1** | Have the DPAs of OpenAI, Tavily, Pinecone and Hugging Face been accepted, and with which contracting entity and region? Is Jina Reader used under any contract? | **Art 28(3)**: a processor needs a written contract *before* it handles personal data. **Chapter V**: transfers need a documented mechanism. | **Not accepted**, US processing for all, **no contract** with Jina (keyless use). → Blocking for live mode. |
| **Q2** | In a client deployment, who runs it: Sergii as a hosted service, or the client on its own machines under a licence? | **Art 4(7)-(8), 26, 28**: decides whether Sergii is processor, joint controller or out of scope, and who signs the vendor DPAs. | **Hosted by Sergii** for one EU client. Client = controller, Sergii = processor, vendors = sub-processors. |
| **Q3** | Where are reports stored, for how long, and who receives them (colleagues, suppliers, public samples)? Do quotes keep personal names or emails verbatim? | **Art 5(1)(c), (e)**: minimisation and retention. **Art 6(4)**: compatibility of sharing. **Art 17**: erasure must be possible. | Kept indefinitely on laptops or a shared drive, shared internally, names verbatim, no deletion. |
| **Q4** | Will the client deployment record which reviewer ran which report and what they decided? | **Art 6(1)(f)/§26 BDSG** for employee data; Art 13 notice to staff; works-council consultation (BetrVG §87(1) no. 6) if it can monitor performance ⚖️. | Yes, a run log with reviewer name will be added, because his AI Act audit recommended human sign-off. |
| **Q5** | Could fetched page text steer the pipeline into sending data elsewhere (prompt injection triggering extra fetches)? | **Art 32**: security of processing. **Art 5(1)(f)**: integrity and confidentiality. | No. The LLM proposes status and quote only; link checks fetch URLs already in the sources. Residual risk is low. |
