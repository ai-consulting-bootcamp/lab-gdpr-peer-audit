# GDPR audit report: Vendor Due-Diligence Agent (Pieter, Project 3)

**Auditor:** Elif Yurdakul · **Builder:** Pieter · **Basis:** Pieter's data processing brief (17 Nov 2026) only

---

## 1. System summary
The system helps a compliance officer check a company before it becomes a vendor. It looks the company up in public registers (GLEIF, KvK), matches all its names against a locally stored copy of the public sanctions lists (about 74,000 entries), searches the news for negative coverage, and uses an AI model to assess the risk and write a report with a rating and a recommendation. Although every check is about a company, the system processes personal data about **sole traders** (vendors who are natural persons), **people named in news articles**, sometimes with alleged or proven offences, and **sanctioned persons** in the stored list. Reports are saved as files and every run is traced.

## 2. Data and role map
- **Personal data:** sole-trader identity data; names, roles and alleged offences of people in news articles (**criminal-offence data, Art. 10**); names, birth dates, nationalities and identifiers of sanctioned persons; operator and user inputs. No special-category data (Art. 9) and, per this brief, no PEP or UBO data in the MVP.
- **Roles:** in production, the **compliance firm is the controller**. Pieter is the provider and, if he runs the service for them, a **processor**. Vendors: **OpenAI, Tavily and GitHub (US)**, **LangSmith (EU endpoint)**, Pinecone (no personal data), GLEIF and KvK (receive only queries), OpenSanctions (bulk download; no names sent back).
- **Transfers:** article text with named people goes to OpenAI (US); company names to Tavily (US); sample reports to GitHub (US, public). Each needs a DPA and a transfer mechanism (Data Privacy Framework or SCCs). The brief gives no evidence of either.

## 3. Compliance findings

**Finding 1: Sample reports with named people and alleged crimes are public on GitHub**
**Severity: Blocking**
**Description:** the three sample reports in the public repo contain real news findings, e.g. "a former ASML employee jailed", "a Heineken manager charged". Publishing criminal-offence data about identifiable people to the whole internet has no lawful basis and no Art. 10 condition, and goes far beyond the screening purpose.
**Recommended action:** remove the reports now; replace them with anonymised or fictional examples; remove them from the git history and check forks.
**Escalation:** No for the removal; Yes (privacy lawyer) to assess whether a breach notification is needed.

**Finding 2: Legal basis and Art. 10 condition for adverse-media screening**
**Severity: Significant** (Blocking before production)
**Description:** researching news about people linked to offences is processing criminal-offence data, which needs both an Art. 6 basis **and** a specific condition under Art. 10 and Dutch law (UAVG). Sanctions screening has a strong basis (EU sanctions law applies to everyone); adverse-media screening of **vendors** does not obviously fall under AML law, which covers clients.
**Recommended action:** document a legitimate-interests assessment per purpose; have counsel confirm the Art. 10 / UAVG condition; limit stored news findings to what supports the decision.
**Escalation:** Yes, privacy lawyer.

**Finding 3: No DPIA**
**Severity: Blocking** (before production with real customers)
**Description:** at least four EDPB criteria apply: evaluation and scoring (incl. sole traders), sensitive data (criminal offences), matching datasets (registers + sanctions + news), innovative technology; data subjects are also unaware. A DPIA is required and none is mentioned.
**Recommended action:** carry out a DPIA template customers complete before use.
**Escalation:** Yes, the customer's DPO.

**Finding 4: Processors and transfers undocumented**
**Severity: Significant**
**Description:** no DPA or transfer mechanism is shown for OpenAI, Tavily or GitHub. LangSmith uses an EU endpoint (good), but stores full prompts, article text and reports.
**Recommended action:** accept DPAs, confirm Data Privacy Framework certification or SCCs, set LangSmith retention or mask personal data in traces.
**Escalation:** No.

**Finding 5: Retention and accuracy**
**Severity: Significant**
**Description:** reports, LangSmith traces and n8n execution history are kept indefinitely. The sanctions file is a downloaded snapshot: if not refreshed, it misses new listings and keeps removed ones, causing wrong matches about real people (accuracy principle).
**Recommended action:** retention schedule with automatic deletion; refresh the sanctions file daily or before each run and record its date in the report.
**Escalation:** No.

**Finding 6: Security and accountability of access**
**Severity: Significant**
**Description:** one shared Streamlit password and one API key means no record of who screened whom, and no way to limit access to criminal-offence data (Art. 32, accountability).
**Recommended action:** individual user accounts and an access log per report.
**Escalation:** No.

**Finding 7: Transparency to people screened**
**Severity: Minor**
**Description:** people in news articles and sole traders are not informed (Art. 14). An exemption for disproportionate effort may apply to news subjects, but must be documented; sole-trader vendors can be informed through the onboarding process.
**Recommended action:** privacy notice for vendors; documented Art. 14(5) reasoning for third parties.
**Escalation:** No.

## 4. Specific GDPR obligations checklist
| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each purpose | **Gap identified** | Not documented; adverse media needs an Art. 10 condition |
| Purpose limitation respected | **Gap identified** | Publication on GitHub exceeds the purpose; news reused from journalism needs a compatibility check |
| Data minimisation | **Cannot determine** | Only matches appear in reports (good); full 74,000-row list stored locally; news text in traces |
| Roles mapped and DPAs in place | **Gap identified** | Roles clear in the brief; no DPAs shown |
| International transfer mechanism documented | **Gap identified** | OpenAI, Tavily, GitHub (US) |
| DPIA conducted if required | **Gap identified** | Required; not conducted |
| Art. 22 safeguard if automated decisions affect people | **Appears met** | Compliance officer decides; risk of rubber-stamping for sole traders |
| Privacy notice covers AI processing | **Cannot determine** | Not mentioned |
| Data subject rights within deadlines | **Gap identified** | Reports stored per company, not searchable per person; no deletion routine |

## 5. Overall recommendation
**Do not proceed until two blocking findings are resolved, then proceed with conditions.** The public sample reports must come down now, and a DPIA must be done before real customers use the system. Both are quick to fix. After that, the system can proceed on condition that the Art. 10 basis is confirmed by counsel, DPAs and transfer mechanisms are in place, and retention and access controls are added. The design has real strengths: sanctions matching runs locally so no names are sent to OpenSanctions, only matches reach the report, and tracing uses an EU endpoint.

## 6. What this report is not
This report is not a legal opinion, not a DPIA and not a certification of compliance. It is based only on the builder's data processing brief. The client should obtain legal review before relying on it.