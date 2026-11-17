# Phase 4 · GDPR audit report: AI Use Case Identifier

**System audited:** Friedrich's Project 3, *AI Use Case Identifier* · **Auditor:** Nicolò Marseu · **Date:** 17 Nov 2026
**Basis:** Friedrich's data processing brief (file 01), with assumptions as logged in file 03. Covers CFU 4 (Find the gaps).

## 1. System summary

A command-line agent researches a company from public sources (website, job ads, news, commercial registers) and uses OpenAI to write an AI use-case brief for a consultant. It targets the company but collects people along the way: directors and shareholders (with year of birth and residence) from registers, contact persons from job ads, managers from About pages and news. The operator can add a lead's name, email and city. All collected text goes to OpenAI and is stored without expiry in local files.

## 2. Data and role map

**Personal data:** lead contacts; register data on directors and shareholders; names and roles from About pages; job-ad contacts with direct contact details; people named in the news; free text about employees. Special-category data is **not sought but can arrive incidentally** (union roles, health, politics).

**Roles:**
- The consultancy operating the tool is the **controller** (assumed, Q1).
- OpenAI is a **processor**. Pinecone is a processor *if* its queries carry personal data.
- Tavily is a **processor** for our queries and an **independent controller** of its own index.
- Register portals and news sites are independent controllers of the data they publish.
- **No processor contract exists.**

**Transfers:** every run sends personal data outside the EU (OpenAI, Tavily). **No transfer mechanism is documented**, and provider regions are unverified.

## 3. Compliance findings

**Finding 1: Processor contracts (Art. 28) and transfers (Ch. V)**
- **Severity: Blocking**
- **Description:** OpenAI already receives personal data on every run, and Tavily processes queries on the operator's behalf. Art. 28(3) requires a written contract with each processor, and Chapter V requires a documented transfer mechanism. The brief confirms neither exists, and the regions are unverified.
- **Recommended action:** Execute OpenAI's DPA (SCCs included) or move to an EU-residency API project. Sign Tavily's and Pinecone's DPAs, confirm each region, and record a transfer impact assessment. No runs on real companies until this is done.
- **Escalation needed?** Yes, to legal counsel (transfer impact assessment).

**Finding 2: Data minimisation and necessity of the legitimate-interest basis (Art. 5(1)(c), 6(1)(f))**
- **Severity: Blocking**, until name handling is added
- **Description:** The analysis needs roles and processes, not names, years of birth or home towns. Because a less intrusive route exists, the necessity limb of the legitimate interests test fails, so the research purpose has **no valid lawful basis as built**.
- **Recommended action:** Drop personal register fields, replace names with role labels before text reaches the model, keep names out of the index and image prompt, then document the legitimate interests assessment.
- **Escalation needed?** No.

**Finding 3: Information duty to indirectly sourced data subjects (Art. 14)**
- **Severity: Significant**
- **Description:** People's data is collected without their knowledge and there is no notice. The disproportionate-effort exemption (Art. 14(5)(b)) may cover register data if documented alongside a public notice. It doesn't cover leads who are contacted: they must be informed at the first communication at the latest.
- **Recommended action:** Publish a privacy notice covering the research tool. Document the Art. 14(5)(b) assessment. Add an information paragraph to the first outreach message.
- **Escalation needed?** Yes, to legal counsel (exemption assessment).

**Finding 4: Lead capture is a separate, unbounded purpose (Art. 5(1)(b), 6, 21; § 7 UWG)**
- **Severity: Significant**
- **Description:** `lead.json` links a contact to a research profile for direct marketing. The contact's source isn't recorded, so no basis can be shown. There's no way to honour the absolute objection right, and commercial email needs prior consent under § 7 UWG.
- **Recommended action:** Make a `--lead-source` field mandatory, keep a suppression list, drop "city", and do no email outreach until a consent route exists.
- **Escalation needed?** Yes, to legal counsel (UWG).

**Finding 5: Storage limitation and security of local outputs (Art. 5(1)(e), 32)**
- **Severity: Significant**
- **Description:** `state.json` and `lead.json` persist indefinitely, and nothing is indexed by person, so access and erasure requests can't be met within a month. Disk encryption is not stated. The gitignore entry prevents publication; it isn't a retention rule.
- **Recommended action:** Auto-delete `state.json` after 30 days, set a 12-month lead retention, add a find-and-delete-by-name script, and require an encrypted disk.
- **Escalation needed?** No.

**Finding 6: DPIA screening not documented (Art. 35)**
- **Severity: Significant**
- **Description:** Two EDPB criteria apply (combining datasets; innovative technology), which is the "generally required" threshold. Nothing is documented.
- **Recommended action:** Write a short DPIA now, focused on findings 2–5. It is cheap at this size and closes the question.
- **Escalation needed?** No (DPO or counsel review is optional).

**Finding 7: Accuracy and indirect identification in outputs (Art. 5(1)(d))**
- **Severity: Minor**
- **Description:** The LLM can attribute wrong facts to a named executive, and recommendations for very small teams can single out employees.
- **Recommended action:** Keep names out of reports and describe teams under 5 people at department level only.
- **Escalation needed?** No.

**Finding 8: Inaccurate README statement (Art. 5(2))**
- **Severity: Minor** (fix today)
- **Description:** The README says no personal data is collected, which is untrue.
- **Recommended action:** Replace it with an accurate data statement.
- **Escalation needed?** No.

*AI Act note (outside GDPR):* the tool is minimal risk. Art. 50(2) machine-readable marking may still apply to the generated process-map image and text if the tool is put into service. This needs checking; OpenAI image outputs may already carry provenance metadata (unverified).

## 4. GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | **Gap identified** | Legitimate interests fails on necessity as built (F2); lead basis can't be shown (F4) |
| Purpose limitation respected | **Gap identified** | Register data reused for sales; leads joined to research profiles (F4) |
| Data minimisation | **Gap identified** | Names, year of birth, residence, city not needed (F2, F4) |
| Roles mapped and DPAs in place | **Gap identified** | Roles mapped in the brief; no DPA with any processor (F1) |
| International transfer mechanism documented | **Gap identified** | None; regions unverified (F1) |
| DPIA conducted if required | **Gap identified** | Threshold reached; nothing documented (F6) |
| Art. 22 safeguard if automated decisions affect people | **Appears met** | No decisions about identified people; the consultant reviews |
| Privacy notice covers AI processing | **Gap identified** | No notice; README inaccurate (F3, F8) |
| Data subject rights can be met within deadlines | **Gap identified** | Nothing indexed by person; no deletion routine (F5) |

## 5. Overall recommendation: **Do not proceed** (with real companies), until findings 1 and 2 are closed

Two blocking findings mean personal data is being processed today without a processor contract and without a lawful basis that holds. Neither is hard to fix. Signing three DPAs, confirming regions and adding a name-handling step is roughly a week's work. Once both are closed, the position becomes **proceed with conditions**: findings 3–6 resolved before any client engagement or outreach, and 7–8 as housekeeping. Until then, run the tool only on fictional or anonymised company data, and delete existing real-company outputs (Q2).

## 6. What this report is not

This report is not a legal opinion, not a DPIA and not a certification of compliance. It is a first-pass peer assessment based on a written brief and the assumptions logged in file 03. The client should get legal review before relying on it.
