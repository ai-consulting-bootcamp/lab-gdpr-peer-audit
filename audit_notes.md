# Source annotations and GDPR maps

The [README](https://github.com/jaimegmarquerie-ui/proyecto3-agente-editorial/blob/3939562dec432c07f804a5412cf4a8c02dfdccd3/README.md) and [architecture](https://github.com/jaimegmarquerie-ui/proyecto3-agente-editorial/blob/3939562dec432c07f804a5412cf4a8c02dfdccd3/docs/architecture.md) serve as the initial brief. The 18 November builder response adds details. See the [questions log](clarifying_questions.md).

## Phase 1 annotations

| Where | Mark | Observation and follow-up |
|---|---|---|
| README setup and CLI | Personal data | Author name appears in the example. Free text could include other names. Jaime confirmed no customer or staff data in the current profile. |
| Architecture describe and judge | Special category | Literary themes describe books. Jaime reported that retrieved text about an identifiable person reveals political opinions or affiliations in 7 of 20 run files. |
| Architecture API nodes | External flow | Tavily, Open Library, Google Books and Gemini are used. Actual processing locations and safeguards remain unverified. |
| README outputs and evidence | Purpose change | Research and recommendations serve the bookshop. Public GitHub logs serve a separate portfolio or demo purpose that Jaime said he had not assessed. |

## Phase 2 personal data summary

| Data category | Source | Purpose | Crosses the EEA border | Special category |
|---|---|---|---|---|
| Author name | User query and public catalogues | Find works and check editions | Unverified | Ordinary personal data |
| Author name and details about identifiable people | Search excerpts, catalogues and publisher pages | Describe books and assess fit with the shop | Unverified. Some excerpts and descriptions reach Gemini. | Confirmed for political information in retrieved text. Exact transmission unverified. |
| Query, author and copied source text | Run state and tool responses | Troubleshoot and show what happened in a run | Unverified | Present in 7 of 20 JSON files, according to Jaime. |
| The same data in published run files | Saved evidence JSON | Portfolio and demo | GitHub public access confirmed. Hosting and transfer mechanism unverified. | Present in the published evidence set according to Jaime. |
| Possible customer or staff details | Free-text query | Find books | Unverified | Unverified. Jaime reported no such use in the current tests. |

## Phase 2 role map

| Entity | Proposed role | Activity | DPA needed |
|---|---|---|---|
| Jaime / La Insumisa | Jaime likely controls the prototype. Reassess with each real client. | Sets the purpose, account choices and profile. | Required with vendors acting as processors. |
| Tavily | Unconfirmed | Runs searches, including publisher searches. | If a processor. Jaime reported a personal free account and no signed DPA. |
| Open Library | Unconfirmed | Receives author and ISBN searches. | If a processor. Jaime reported public API access. |
| Google Books | Unconfirmed | Receives ISBN lookups. | If a processor. Jaime reported no DPA. |
| Gemini | Unconfirmed for the actual account, region and terms | Receives excerpts, descriptions and selected profile fields. Also rewrites queries. | Check the terms before assigning the role. Jaime reported an AI Studio free-tier key. Billing status remains unverified. |
| GitHub | Unconfirmed for hosting | Hosts demo dossiers and public evidence files. | Depends on the role for the relevant data and service. |

Jaime reported no documented transfer safeguard. For any confirmed transfer outside the EEA, identify the parties, destination and applicable Chapter V mechanism, such as an adequacy decision or standard contractual clauses. Keep that assessment with the relevant account terms.
