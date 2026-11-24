# Green Warehouse Network — GDPR Data Processing Brief

> **Purpose of this document:** describe the system, its data, and its data flows in a format that a privacy professional or project reviewer can use for their own GDPR assessment.
>
> **This is not a GDPR audit, legal opinion, compliance decision, or risk assessment.** It records the current project design and identifies questions for the reviewer to consider.

## 1. Document and system overview

| Item | Description |
|---|---|
| **System** | Green Warehouse Network |
| **System purpose** | Help logistics planners compare resilient warehouse networks in Germany. The system selects a primary and backup warehouse for each customer and reports cost, CO₂, capacity, distance, and failure scenarios. |
| **Project scope** | Course-project MVP using static planning data. It is not connected to live customer, warehouse, order, HR, or delivery systems. |
| **Intended users** | Logistics and supply-chain planners. |
| **Main outputs** | Warehouse recommendations, customer-to-warehouse assignments, cost and CO₂ metrics, capacity warnings, failure simulations, scenario comparisons, maps, and an optional HTML report. |
| **Human involvement** | A planner reviews the inputs, assumptions, warnings, solver status, and assignments before using a result. The system does not automatically approve a recommendation or change operations. |
| **Source files** | [`README.md`](README.md), [`docs/Spec.md`](docs/Spec.md), [`Audit_eu-ai-act_system_brief.md`](Audit_eu-ai-act_system_brief.md) |

## 2. Processing summary

| Question for the GDPR reviewer | Current project description | Useful source |
|---|---|---|
| **What data does the system process?** | Customer IDs, names/labels, latitude, longitude, annual demand, warehouse data, distance data, emissions factors, user chat messages, scenario settings, solver results, assignments, warnings, and report content. The current sample does not intentionally contain email addresses, phone numbers, behavioural histories, or personal profiles. | [`data/customers.csv`](data/customers.csv), [`data/candidate_sites.csv`](data/candidate_sites.csv), [`agent/graph.py`](agent/graph.py) |
| **Where does the data come from?** | Customer and warehouse CSV files maintained for the project; cached distance and emissions data; and scenario instructions entered by the dashboard user. A user can also add customer records to a scenario. | [`src/data.py`](src/data.py), [`src/tools.py`](src/tools.py), [`data/`](data/) |
| **Why is it processed?** | To validate planning inputs, calculate primary and backup assignments, compare cost and CO₂ objectives, simulate warehouse failure, display planning results, and optionally generate a report. | [`src/tools.py`](src/tools.py), [`src/model.py`](src/model.py), [`app.py`](app.py) |
| **Who or what processes it?** | The local Streamlit application, LangGraph orchestration, validation code, and PuLP/CBC optimizer process the planning data. OpenAI processes selected prompts for intent parsing, explanations, and optional report writing. OpenRouteService and Climatiq support one-time data refreshes; normal runs use cached outputs. | [`README.md`](README.md), [`agent/graph.py`](agent/graph.py), [`src/geo.py`](src/geo.py), [`src/climatiq.py`](src/climatiq.py) |
| **Where is it stored or processed?** | CSV inputs, caches, solver results, and generated reports are stored in the local project/runtime environment. Chat state is held in the current Streamlit/LangGraph session. External service hosting locations, retention terms, and transfer arrangements are not specified in this project. | [`README.md`](README.md), [`data/cache/`](data/cache/), [`reports/`](reports/) |
| **Does it make a decision about a person?** | The system recommends warehouse locations and customer-to-warehouse assignments for logistics planning. It does not approve, reject, rank, employ, price, or profile individuals, and it does not execute operational changes. Whether the planning output could nevertheless affect identifiable people or businesses is for the GDPR reviewer to assess. | [`docs/Spec.md`](docs/Spec.md), [`Audit_eu-ai-act_system_brief.md`](Audit_eu-ai-act_system_brief.md) |

## 3. Data inventory

| Data asset | Fields / examples | Source | How the application uses it | Where it goes in the current design |
|---|---|---|---|---|
| **Customer planning records** | `id`, `name`, latitude, longitude, annual demand | `data/customers.csv`; additional records may come from a user scenario | Network optimization, customer assignment, capacity checks, distance calculations, cost, CO₂, and failure analysis | Local application and solver. Assignment and result data may be included in prompts used to explain results or generate a report. |
| **Warehouse records** | `id`, name, latitude, longitude, capacity, fixed cost, fixed CO₂ | `data/candidate_sites.csv` | Select candidate sites and calculate network metrics | Local application and solver. |
| **Distance data** | Customer-to-warehouse road distances; estimated distances for some added customers | Cached distance file, originally prepared using OpenRouteService; local fallback calculation for uncached pairs | Determine eligible sites, transport cost, transport CO₂, and average distances | Local distance cache and solver. |
| **Emissions data** | Diesel/electric factors, source, region, and fetch time | `data/emission_factors.csv`, originally refreshed through Climatiq | Calculate transport CO₂ and compare emission scenarios | Local CSV and solver. |
| **Scenario settings** | Objective, warehouse closures, forced sites, demand changes, vehicle mode, backup distance, and other planning parameters | User-entered chat or dashboard controls | Change the assumptions used for a scenario run | Local session; scenario JSON is sent to OpenAI when language processing is used. |
| **Chat and clarification text** | User questions, plain-English requests, and answers to clarification prompts | Dashboard user | Convert a request into structured scenario fields and explain results | Current application session; user text is sent to OpenAI for language processing. |
| **Derived results** | Primary/backup assignments, site loads, cost, CO₂, warnings, solver status, scenario IDs, and comparisons | Calculated by the local application | Display results, compare scenarios, simulate failure, and support explanations | Local session, dashboard, and optional report; selected result data is sent to OpenAI for explanations/report writing. |
| **Generated report** | Request history, scenario changes, results, warnings, metrics, assignments, and map | Current session and solver output | Provide a downloadable planning summary | Generated locally after optional LLM report writing; may be saved in `reports/` or downloaded by the user. |

## 4. Data flow

```text
Static CSVs / cached distances / cached emissions
                    |
                    v
        Streamlit dashboard and session state
                    |
          user chat and scenario fields
                    |
                    v
       OpenAI: intent parsing and explanations
                    |
                    v
     Local validation -> PuLP/CBC optimizer
                    |
                    v
     Assignments, metrics, warnings, comparisons
          |                         |
          |                         +--> optional result/report prompt to OpenAI
          v
    Local dashboard / downloadable HTML report

One-time data refresh:
  coordinates --> OpenRouteService --> local distance cache
  factor query --> Climatiq        --> local emissions-factor CSV
```

## 5. Components and external services

| Component / service | Function | Data it may receive | Runtime use |
|---|---|---|---|
| **Streamlit dashboard** | User interface, session state, maps, metrics, scenario controls, and downloads | User inputs, scenario state, results, and report content | Every interactive run |
| **LangGraph / LangChain** | Conversation flow, intent parsing, validation routing, explanations, and report orchestration | User text, scenario JSON, structured results, and session events | Chat and optional LLM report functions |
| **OpenAI model** | Understand user requests, explain structured results, and write optional report text | User prompt, site catalogue, scenario fields, and selected result/session data | External service during chat/report use; exact processing region and retention are not defined here |
| **PuLP/CBC solver** | Deterministic warehouse-network optimization | Customer, warehouse, distance, emissions, and scenario data | Local calculation |
| **OpenRouteService** | Prepare road-distance matrix | Customer/site coordinates during a distance refresh | One-time/preparation step; normal runtime uses cache |
| **Climatiq** | Prepare emissions-factor data | Emissions-factor queries and scenario metadata during a refresh | One-time/preparation step; normal runtime uses local CSV |
| **Local files and reports** | Store source data, caches, and generated outputs | All corresponding local inputs and outputs | Repository/runtime and user download location |
