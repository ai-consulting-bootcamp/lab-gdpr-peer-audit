# Phase 2 · Personal data and role map: AI Use Case Identifier

*Based only on the brief. Where the brief is silent, I note the gap. Covers CFU 1 (Recognize) and CFU 3 (Map roles).*

## CFU 1: Recognize

- **Personal data present:**
  - operator-entered lead contacts (name, email, city);
  - managing directors' and shareholders' names, with year of birth and place of residence from register portals;
  - founders' and managers' names and roles (About pages);
  - named job-ad contacts with direct email or phone;
  - people named in news coverage;
  - free text that may describe identifiable employees.
- **Special-category data:** not sought, but **inferable or incidental**:
  - union membership (named works-council members);
  - health (news about an executive's illness, absences);
  - political opinions (executives' public engagement).

  These could also be revealed *indirectly* when a substitution recommendation targets a very small team.
- **Crosses an EU border:** **yes.** Every run sends collected text to OpenAI (US-headquartered) and uses Tavily (non-EU) for search. Pinecone is US-headquartered, but may not receive personal data (see Q4 in file 03).

## Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Lead contact: name, email, city | Operator, via command-line flags | P3 lead capture | No by itself. Yes if passed into the run state (not stated) | No |
| Managing directors / shareholders: name, year of birth, place of residence | Tavily search of register portals and northdata | P1 research (ownership, size) | **Yes** (Tavily → OpenAI) | No. Year of birth and residence are not Art. 9 data, but are clearly unnecessary |
| Founders and management: names, roles | About page (≤ 5,000 characters) | P1 business model and process map | **Yes** (OpenAI) | No |
| Job-ad contact persons: name, email, phone | Careers page, job postings (≤ 2,500 characters each) | P1 process map | **Yes** (OpenAI) | No |
| People named in the news | Tavily news search | P1 company context | **Yes** (Tavily → OpenAI) | **Possible** (health, politics) |
| Free text describing employees or teams | Website, job ads | P1 process map; P2 substitution recommendations | **Yes** (OpenAI) | **Possible** (union membership via works council) |
| Collected text reused in the outputs | Run state | P2 brief; process-map image | **Yes** (OpenAI text and image models) | As above |
| All of the above, stored | Local `state.json`, `lead.json`, `report.md` | All purposes (storage) | No (local disk) | As above |

**Gaps in the brief:**
- **Retention:** none stated.
- **Volume:** how many companies have been run, and whether any were real.
- **Pinecone query content:** not stated.
- **Image prompt content:** not stated.
- **Whether `report.md` names individuals:** not stated.

## Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| **Client:** the consultancy that operates the tool to prepare sales approaches | **Controller.** It decides which companies to research, what to keep and the sales purpose | All purposes (P1–P3) | n/a (controller). It needs DPAs with every processor |
| **Builder:** Friedrich | **Controller** when he runs it himself. **Processor** if he runs it on a consultancy's instructions. **Not a GDPR role** if he only supplies code that the consultancy runs | Development; possibly runs | **Yes, if he runs it for a client** (Art. 28 contract between them). Unclear from the brief (Q1) |
| **OpenAI** | **Processor** (API) | Text, embeddings and image generation on prompts containing personal data | **Yes.** **None in place** according to the brief |
| **Tavily** | **Mixed.** **Processor** for our queries and the results returned to us. **Independent controller** for its own crawled index | Search queries and returned content | **Yes,** for the processing done on our behalf. **None in place** |
| **Pinecone** | **Processor** | Vector queries against the use-case library | **Only if** queries carry personal data (Q4). A DPA is recommended anyway. **None in place** |
| **Northdata, register portals, news sites** | **Independent controllers** of their published data | Data source only | No. Their terms of use still apply (scraping and reuse) |
| **Researched companies, and the people named in their data** | **Data subjects** (the people), not parties | — | n/a. The Art. 14 information duty is owed to them |

## International transfers

| Flow | Mechanism needed | Evidence in brief |
|---|---|---|
| **OpenAI** | For EEA customers, OpenAI Ireland is the contracting entity, and onward transfers to the US run on **SCCs** in OpenAI's DPA, plus a transfer impact assessment. Alternative: EU data residency (eligible API projects, zero data retention). | **None.** "Currently unverified" |
| **Tavily** | DPF certification if available, otherwise SCCs. If Tavily is based in a country with an EU adequacy decision, that decision applies. **Tavily's legal seat is unverified**, so I don't assume a mechanism. | **None** |
| **Pinecone** | EU index region. If the vendor is US-headquartered with an EU region, the DPA should cover support access and US-parent access | **None.** Region unverified |
