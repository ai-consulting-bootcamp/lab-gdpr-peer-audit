# Data and role map, clarifying questions: Application Prep Agent

Auditor: Friedrich Tschoepke · Builder: Nicolò Marseu · 23 November 2026

## CFU 1 – Recognize

- **Categories:** identity and contact data, work and education history, skills, self-reported achievements, email address, and inferred data (fit score, requirement ratings, generated cover letter and CV text).
- **Special categories:** not requested, likely present in practice (photos, disability, health-related gaps, union roles) and can be carried into the score or the cover letter.
- **EU border:** yes, through OpenAI and Google. Ironhack hosting location unknown.

## Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Identity and contact data from CV | Job seeker or coach (form upload) | Generate application pack | Yes (OpenAI) | No |
| Work and education history, skills | Same | Score fit; write pack | Yes (OpenAI) | Possible (gaps, disability, union roles) |
| Photo, date of birth, nationality (if in CV) | Same | None intended; processed anyway | Yes (OpenAI, as extracted text) | Possible (ethnic origin, religion) |
| Free-text achievements | Same | Write pack | Yes (OpenAI) | Possible |
| Email address | Form | Deliver report | Yes (Google) | No |
| Fit score and ratings | Generated | Gate decision; report | Yes (Google, in email) | Inferred profile |
| Full run data (all of the above) | n8n | Operation, debugging (not stated in brief) | Unknown (Ironhack) | As above |
| Planned: saved profiles, scores in dashboard | Partners | Re-use without re-entry; reporting | Unknown | As above |

**Brief silent on:** retention, hosting location, legal basis, what a coach-submitted candidate is told.

## Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Client (career service, outplacement firm) – planned | Controller for its candidates | Decides to process candidates' CVs with the tool | – |
| Builder (Nicolò Marseu) | Controller for the public demo; processor for each client once sold. Controller again for own purposes (pilot evaluation, product improvement) | Runs the workflow, configures vendors | Yes, as processor towards each client (Article 28) |
| OpenAI | Processor (sub-processor once clients exist) | Scoring and writing on full CV text | Yes. OpenAI's DPA must be accepted and archived. |
| Ironhack (n8n host) | Processor, or independent controller if it uses data for itself | Runs the workflow; stores run history | Yes. None known. |
| Google (personal Gmail account) | Not usable as a processor on consumer terms | Sends reports; keeps sent mail | Yes, and not available on consumer terms. Replace. |
| Jina Reader, Tavily, NewsAPI, Pinecone | No role for candidate data | Company research, guidelines | No |

**International transfers.**

| Flow | Mechanism needed | Evidence in brief |
|---|---|---|
| OpenAI (Ireland → US parent, sub-processors) | Covered by OpenAI's DPA; verify whether it relies on the EU-US Data Privacy Framework or standard contractual clauses | None |
| Google (US) | Data Privacy Framework or SCCs under a Workspace or email-provider contract | None; consumer account offers none |
| Ironhack n8n | Unknown until location is known | None |

## Clarifying questions log

Information requested from the builder in writing on 23 November 2026. Questions 1–3 are the most important. Questions sent on 16 November for the AI Act audit are still unanswered and partly overlap.

| # | What I need to know | GDPR obligation affected | Provisional assumption |
|---|---|---|---|
| 1 | Has the live form processed CVs of real people, and how many? | Whether Articles 28, 35 and 13 apply to processing that has already happened, or only before launch. Decides Blocking vs Significant. | Yes, a small number from classmates and testers. |
| 2 | Where does data remain after a run, for how long, and who can open it (n8n run history on the Ironhack instance, Gmail sent folder, OpenAI)? | Article 5(1)(e) storage limitation, Article 5(1)(a) transparency of the "Nothing stored" claim, Article 28 for Ironhack. | Kept under n8n defaults, visible to instance administrators; Gmail keeps every report; OpenAI 30 days. |
| 3 | Which lawful basis do you rely on, and what are users told before they submit? Specifically for a CV that a coach submits about someone else. | Articles 6, 9, 13, 14. | No basis documented, no notice; candidates of coaches are not informed. |
| 4 | Is the Gmail account a personal account or Google Workspace with a data processing agreement? | Articles 28 and 44. | Personal account. |
| 5 | Will partners in sprint 3 see individual fit scores, and may they use them to decide whom to support or put forward? | Article 22, Article 35, purpose limitation (Article 5(1)(b)). | Yes, as described in the go-to-market plan. |
