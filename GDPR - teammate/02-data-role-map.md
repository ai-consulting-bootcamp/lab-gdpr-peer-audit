# Data and role map — RegGuard-Mini
Auditor: Nelly Pourmehr. Builder: Kimia Asgari.

## Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Designer identity (name) | Entered directly by designer at session start | Session attribution, version tracking | Not stated. Storage location not documented. Gap. | No |
| Designer's typed questions (free text) | Typed directly by designer, sent to a commercial LLM API | Powers plain-language Q&A feature | Likely yes. LLM provider not named, location unknown. Gap. | Not intended, but free text could incidentally contain it. Cannot rule out. |
| Handoff recipient data (colleague name + address) | Entered by designer, about a third party who did not submit it themselves | Enables report delivery to the named colleague | Not stated. Gap. | No |

## Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Client (design company deploying RegGuard-Mini) | Controller | Decides why designer identity, questions, and handoff data are collected | Yes, with Builder |
| Builder (Kimia's team) | Processor | Runs the system, routes typed questions to the LLM | Yes, with Client |
| Commercial LLM provider | Sub-processor | Receives typed questions for the reasoning/language layer | Yes. Provider not named yet. Cannot confirm a DPA exists. |

## International transfer notes

Transfer mechanism needed: Cannot confirm. Depends on where the LLM provider and any hosting are located. If either is outside the EU, SCCs or another Art. 44-49 mechanism are needed.
Evidence it is in place: None provided in the brief. Open gap.
