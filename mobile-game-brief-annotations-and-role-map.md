# Mobile Game Competitor Snapshot — brief annotations and role map

**Independent reviewer** Sean Langsdorf · **Builder** Jędrzej Czarnota\
**Basis** [Builder's system brief from the GDPR self-audit submission](https://github.com/jedrzejczarnota-source/lab-gdpr-self-audit/blob/eff19e436f8a6a7f7b019a2ab846a8e4c1355d9c/01_project3_system_brief.md). These tables use the brief alone. The separate [workflow check](lab_proof.md) supplements, but does not backfill, the brief. The teammate's self-audit conclusions were not consulted for this independent assessment.

## 1. Annotation log

| Brief section | What it establishes | Flag / what is not established |
| --- | --- | --- |
| What Inputs It Takes · user form | Required email and competitor name. Optional studio strategy/KPI PDF, otherwise a fictional playbook. | **Personal data:** named work emails and identifiers or free text in real PDFs. **Art. 9:** none declared, possible in uncontrolled PDF contents. **Unknown:** validation, upload restrictions, authorization, retention and who can submit. |
| What Inputs It Takes · external sources | Parallel company research, news and US-store iOS metrics. Names and job titles can appear in news or web results. | **New purpose:** publication for news or company information does not establish lawful AI reuse. US storefront selection is not evidence of a transfer. **Unknown:** API recipient entity, locations, excerpt filtering and publication dates. |
| What It Outputs / Who Is Affected | Report compares industry facts and studio strategy. It includes game-level ratings and a LiveOps label plus suggested tests. | **Personal data:** attributed claims or strategy-derived references can enter the email. **Unknown:** exposed excerpts, recipients, onward sharing. Product scoring does not establish person scoring. |
| Human Review in Practice | Email delivery is autonomous. Staff review reports afterward and decide whether to act on business suggestions. | **Risk:** no review before disclosure. Automated delivery is not by itself an Art. 22 decision about a person. **Unknown:** address verification, report recall and redress. |
| Who Built It and Who Uses It in Production | Builder-hosted validation and separate client-managed import. OpenAI for chat/embeddings, Pinecone for retrieval, Tavily/GNews/Apple for research, Gmail for delivery. | **Potential Chapter V flows:** from hosted n8n to external recipients, or onward via support/subprocessors. **Unknown:** service entities, deployment regions, storage, transfer mechanisms, contracts and actual tenant isolation. |

## 2. Personal data summary

| Category | Source | Purpose | Crosses EEA border? | Special category? |
| --- | --- | --- | --- | --- |
| Report recipient email, potentially a named employee address | Requester submits it | Deliver the requested report | Gmail path is external. Recipient entity, region and onward access unknown. | No on described input. |
| Competitor name, potentially eponymous or identifying a sole trader | Requester submits it | Target company/storefront research | Sent to research APIs. Actual locations unknown. US storefront intended, not a confirmed transfer. | Not as described. |
| Names, professional roles and statements about founders, staff or journalists | Third-party web and news | Company and market context for synthesis | External retrieval and OpenAI pipeline. Actual transfer path unknown. | None stated. Snippets could incidentally reveal protected traits. |
| Uploaded strategy/KPI PDF and extracted chunks, embeddings and retrieval results if attributable | Requester uploads internal document | Tailor the report to the requesting studio | External embeddings and vector storage are described. Regions, subprocessors and onward access unknown. | Not intended. PDF contents are unspecified and could include sensitive or identifiable personnel material. Vectors are not presumed anonymous. |
| Name-linked claims or strategy details reproduced in the report | Model output using public and internal inputs | Deliver suggested product or marketing tests | Gmail sends the report. Regions, recipients and onward copying unknown. | Possible if sensitive input survives. No inferred protected traits described as an intended use. |
| Game ratings, counts and update telemetry | Apple storefront search | Product-level performance comparison | US catalog requested. Network processing locations unknown. | Normally not personal when aggregated and not linked to individuals. No player-level identities described. |

**Purpose check.** Email delivery does not imply permission for marketing or user tracking. Internal playbooks are prepared for planning, not necessarily for external embedding, retention, model reuse or cross-client retrieval. For the same controller's further use, assess compatibility under Art. 6(4) where applicable. A recipient independently collecting public data needs its own lawful basis and an Art. 14 assessment. The brief does not establish vendor training, persistent profiling or any permission for those uses.

## 3. Role map from the brief

Roles follow real decisions about purpose and essential means, not product labels or who pays.

| Entity | Provisional role | Activity | Art. 28 DPA needed? |
| --- | --- | --- | --- |
| Client mobile studio | Controller for own staff's internal competitive research and use of results in the client-managed mode. Also likely controller for commissioning own studies in hosted mode. | Chooses queries, approved strategy material and how staff act on the report. | Yes with any processor acting for it. None evidenced. |
| Builder / hosted operator | Processor to the extent it executes client instructions. Separate controller for own sales, billing or GTM analytics if it sets those purposes. In client-managed mode supplying an export alone does not create processor status. | Hosts or supplies the n8n workflow, depending on mode. | Needed for instructed hosted or support access. No evidence of jointly defined purposes or a joint-control arrangement. |
| n8n hosting provider, if separate | Likely processor or subprocessor for managed hosting. Self-hosted software alone is not a recipient. | Hosting, execution data, binary uploads and possibly operational access. | Yes if managed processing or personal-data access, with appropriate authorization. Hosting arrangement unknown. |
| OpenAI | Likely processor/subprocessor for instructed chat or embedding content under applicable terms. Review any independent uses separately. | Embeddings, report synthesis and potentially retrieved strategy context. | Yes for instructed processing. Actual agreement and account controls unknown. |
| Pinecone | Likely processor/subprocessor for tenant vector operations. | Stores and retrieves strategy representations and document data. | Yes for instructed processing. Region, deletion and DPA not evidenced. |
| Tavily | Role for submitted queries depends on contract and use. Distinguish instructed processing from own indexing or service purposes. | Public company search and snippets. | Yes for processor activity only. Terms unknown. |
| GNews | Same split to verify separately. | Receives competitor query and provides news results. | Yes for processor activity only. Terms unknown. |
| Apple iTunes Search | Likely independent controller for operating its storefront/search service. Query and service-log roles unconfirmed. | Returns public US-store app data. | Not for independent controller activity. Reassess if any instructed processing applies. |
| Google / Gmail | Potential processor/subprocessor for instructed delivery if covered by appropriate business-account terms. Own-purpose processing and consumer mailbox status must be assessed. | Handles recipient email and report contents. | Yes for processor service. Account type and contract not specified. |

**Chapter V.** Neither a provider brand nor a US storefront shows which entity receives personal data or from where it is accessed. Verify the exporter, importer, subprocessors, region and remote access per operating mode. If a Chapter V transfer exists, confirm applicable adequacy, including relevant, current EU–US Data Privacy Framework coverage where applicable, or sign suitable SCCs with a transfer assessment and effective supplementary safeguards. Use the correct controller/processor module for each leg. No mechanism is evidenced by the brief.
