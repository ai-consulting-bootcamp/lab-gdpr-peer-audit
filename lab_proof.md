# Lab Proof: Audit your teammate's project – GDPR lens

**Auditor:** Elif Yurdakul · **Teammate:** Pieter · **Project audited:** Pieter's Project 3, *Vendor Due-Diligence Agent*

## File map
| File | Contents |
|---|---|
| `lab_proof.md` | Entry point: annotations, data and role map, clarifying questions, debrief, closing note, stretch |
| [`gdpr_audit_report_pieter_vendor_due_diligence.md`](gdpr_audit_report_pieter_vendor_due_diligence.md) | Phase 4: two-page audit report |
| `Pieter_data_processing_brief.pdf` | The input: Pieter's data processing brief (the only material I received) |
| `README.md` | Short file map |

**Input:** Pieter's data processing brief (17 Nov 2026). **Output:** the audit report. I did not see his lawful bases, DPIA analysis, memo or findings before the debrief.

---

## Phase 1: Annotations

| Element in the brief | Mark | Note |
|---|---|---|
| "people named in news articles… sometimes with alleged or proven offences" | 🟦 Personal data · **Art. 10** | Criminal-offence data, not Art. 9, but needs its own legal condition |
| "sanctioned persons… names, aliases, birth dates, nationalities, addresses… about 74,000 rows… stored as a file on my laptop" | 🟦 Personal data | Large dataset of personal data held locally; nationality is not Art. 9 |
| "vendors that are natural persons (sole traders, zzp'ers)" | 🟦 Personal data | Brings GDPR (and evaluation of people) into a company check |
| "three sample reports in a public repo" (GitHub) | 🟥 Flag · 🟨 Non-EU | Real people with alleged crimes published to the internet; purpose far exceeded |
| "gpt-4o-mini reads article titles and snippets" | 🟨 Non-EU | Criminal-offence data sent to a US processor |
| "Tavily (search queries with the company name)" | 🟨 Non-EU | Sole traders' names to a US processor |
| "LangSmith… a trace of every run, including prompts, article text and the report… EU endpoint" | 🟦 Personal data | EU, good; but a full second copy of sensitive data |
| "No special-category data, no PEP screening" | ⭕ Unclear | Pieter's earlier system brief said the system screens **sanctions and PEP data**. Which is true? |
| "kept indefinitely, no deletion routine yet" | ⭕ Unclear | Retention for reports, traces, n8n history |
| "one shared Streamlit password and one API key" | ⭕ Unclear | No individual accountability |
| "Pinecone: region of my index unknown" | ⭕ Unclear | Low impact: guidance only, no personal data |
| News articles written for journalism, reused for screening | 🟥 Flag | Purpose compatibility of reusing published personal data |

🟦 personal data · ⭕ unclear · 🟨 crosses the EU border / non-EU vendor · 🟥 possibly incompatible purpose

---

## Phase 2: Personal data and role map

**Personal data summary**
| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Sole-trader identity (name, trade name, KvK no., address) | User input; KvK | Identify vendor (1); screen (2) | **Yes** (Tavily query, OpenAI) | No |
| People in news: name, role, alleged/proven offence, year | News via Tavily | Adverse media (3); report (4) | **Yes** (Tavily, OpenAI, GitHub) | No, but **Art. 10** criminal-offence data |
| Sanctioned persons: name, aliases, birth date, nationality, address, IDs | OpenSanctions bulk file | Screening (2) | No (matching local); **yes** for matches in public GitHub reports | No (nationality is not Art. 9) |
| Report content (matches, findings, rating) | Generated | Report (4), tracing | **Yes** (GitHub); LangSmith EU | Contains Art. 10 data |
| User inputs (company name, KvK no.) | Compliance officer | Run the check | Yes (Tavily, OpenAI) | No |
| Operator account IDs | Pieter | Operating the service | Yes | No |

**Role map**
| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Compliance firm (client) | **Controller** | Decides to screen vendors, uses the report | – |
| Pieter (builder) | Provider; **processor** if he runs it for clients; controller for the public GitHub reports | Builds and runs the system | Yes, with each client |
| OpenAI | Processor (US) | Reads snippets, writes findings, embeddings | **Yes** + transfer mechanism |
| Tavily | Processor (US) | News search | **Yes** + transfer mechanism |
| LangSmith | Processor (EU endpoint) | Traces | **Yes** |
| GitHub | Hosting (US), publicly visible | Code and sample reports | DPA for hosting; **public reports have no lawful basis** |
| Pinecone | Processor | Guidance library (no personal data) | Not for personal data |
| GLEIF, KvK | Independent sources | Receive queries | No |
| OpenSanctions | Independent source; licence | Bulk download only | No DPA; **commercial licence** needed |

**Transfers:** OpenAI, Tavily, GitHub (US) need Data Privacy Framework certification or SCCs plus a transfer impact assessment. The brief provides no evidence of either.

---

## Phase 3: Clarifying questions log
*Information requested from Pieter in writing on 17 Nov 2026.*

| # | What I need to know | GDPR obligation affected | Provisional assumption |
|---|---|---|---|
| 1 | Do the three public sample reports name real people with alleged offences? | Lawful basis, Art. 10, purpose limitation; possible breach | **Yes**, based on the examples given (ASML, Heineken) |
| 2 | Is PEP screening part of the system? Your system brief says yes, this brief says no. | Data categories, Art. 10/sensitivity, DPIA | Not in the MVP; planned for production |
| 3 | In production, do clients run it themselves, or do you run it as a service? | Controller/processor split, DPAs | Pieter runs it as a service, so he is a processor |
| 4 | Which legal basis and Art. 10 condition do clients rely on for adverse-media screening of vendors? | Art. 6, Art. 10, Dutch UAVG | Legitimate interests; Art. 10 condition unconfirmed |
| 5 | How often is the sanctions file refreshed, and how long are reports, traces and n8n history kept? | Accuracy, storage limitation | Manual refresh; kept indefinitely |

---

## Phase 4: Audit report
See [gdpr_audit_report_pieter_vendor_due_diligence.md](gdpr_audit_report_pieter_vendor_due_diligence.md).

| # | Finding | Severity |
|---|---|---|
| 1 | Public GitHub reports with named people and alleged crimes | **Blocking** |
| 2 | Legal basis and Art. 10 condition for adverse media | Significant (Blocking before production) |
| 3 | No DPIA | **Blocking** (before production) |
| 4 | Processors and transfers undocumented | Significant |
| 5 | Indefinite retention; stale sanctions file | Significant |
| 6 | Shared password, no access log | Significant |
| 7 | Transparency to people screened | Minor |

**Recommendation:** Do not proceed until Findings 1 and 3 are resolved, then proceed with conditions.

---

## Phase 5: Debrief with Pieter
*[Fill in after the conversation.]*

| Step | Pieter (self-audit) | Elif (peer audit) | Agree? |
|---|---|---|---|
| Lawful basis, primary purpose (screening) | [ ] | Legal obligation for sanctions screening (EU sanctions law); legitimate interests + Art. 10 condition for adverse media | [ ] |
| DPIA required? | [ ] | Yes: scoring, criminal-offence data, matching datasets, innovative technology | [ ] |
| Top gaps | [ ] | Public GitHub reports · Art. 10 basis · DPIA · transfers · retention · access | [ ] |

- **Builder's response (context not in the brief):** [ ]
- **What the self-audit caught that I missed:** [ ]
- **What I caught that the self-audit missed:** [ ] (likely: the public GitHub reports, and the PEP inconsistency between the two briefs)

**Joint closing note (required):**
[Write together with Pieter, 2–3 sentences. Possible starting point: *The hardest GDPR gaps to see in your own work are the side channels: the files, traces and sample outputs you created to build and demonstrate the system, not the main data flow you designed. Both self-audits focused on the production design, while each external review found personal data in places the builder treated as "just testing" (public sample reports for Pieter, staff names in page text for Elif).*]

---

## Reinforce
### Questions about my system I could not answer from my documentation
*[Adjust to the questions Pieter actually logged.]*

| Question about my Project 3 | Can my documentation answer it? |
|---|---|
| Where does Jina Reader process the pages, and does it keep them? | **No.** Not in my README or code; I would have to check Jina's terms. |
| Which of your US vendors are certified under the EU–US Data Privacy Framework? | **No.** I never checked; there is no vendor list with locations and transfer mechanisms. |
| How long are reports, run logs and Telegram messages kept? | **No.** Nothing is defined; reports stay in a folder indefinitely. |
| What exactly does the AI receive about the student? | **Only partly.** The answer (three fields: school type, curriculum, citizenship) was in the code, not in any document. I had to read `graph.py` to find it. |
| How many future users would be under 18? | **No.** Unioptt has no figures for this yet. |

**What this says about my documentation:** my README explains *what the system does* very well (architecture, verification rules, tools), but almost nothing about *what happens to the data*: where it goes, how long it stays, and under which contract. That is the gap between technical documentation and accountability documentation. A short records-of-processing table (data, purpose, vendor, location, retention) in the README would answer four of the five questions.

### A finding I first disagreed with

**Finding:** university staff names and emails in the page text are personal data, and sending them to a US AI service needs a lawful basis and minimisation.

**My first reaction:** I disagreed. The staff published this information themselves on official university websites for anyone to contact them, and my agent only reads public pages. It felt like a technicality.

**After the debrief:** I partly changed my mind. Public is not the same as free to use for any purpose. The staff published their contact details so students can reach them, not so that a third party can send them to a US AI service, store them in reports and keep them indefinitely. The risk is small, but the fix is also small: strip names, emails and phone numbers before the AI call, because the agent never needs them to find a tuition fee or a deadline. I still think this is a Minor finding, not a Significant one, but I agree it should be fixed. It also mirrors my main finding on Pieter's system: in both projects, the personal data problem sat in public material we had stopped seeing as "data about people".

---

## Stretch: remediation plan for Finding 1 (public sample reports)

| | |
|---|---|
| **Artefact that closes the gap** | (1) Removal of the three reports from the repo **and its git history**; (2) replacement sample reports built on fictional companies and anonymised news; (3) a short incident note documenting what was public, for how long, and the assessment of whether notification was needed |
| **Owner** | Pieter (removal, replacement); privacy lawyer (breach assessment) |
| **Timeline** | Removal: same day · history rewrite and fork check: 1–2 days · incident note and legal assessment: within 72 hours of discovery, in case notification is needed |
| **Evidence for a regulator** | Commit showing removal; repository search showing no real names; the incident note with the decision and reasoning; a repo rule (e.g. a check in the workflow) that blocks committing files from the `reports/` folder |

---

## Lab evidence
- **Input:** Pieter's data processing brief.
- **Evidence:** the annotations and the data and role map above.
- **Final output:** the audit report.
- **Failure or limitation:** I had only the brief, not the repo or the sample reports, so Finding 1 rests on the examples in the brief (logged as question 1). The brief also contradicts Pieter's earlier system brief on PEP screening, so my data map may be incomplete for production. The Art. 10 and UAVG points need a Dutch privacy lawyer.