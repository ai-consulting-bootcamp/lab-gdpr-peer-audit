# GDPR Audit Report — Unioptt University Programme Fact-Checker

**System owner:** Elif Yurdakul (Unioptt) · **Auditor:** Pieter Albrecht · **Date:** 17 November 2026
**Basis:** Elif's system brief only; assumptions and open questions in [data_role_map_and_questions_log.md](data_role_map_and_questions_log.md).

## 1. System summary

The system checks the facts about one university programme for a Turkish student and their family. It extracts tuition, deadlines and requirements from official web pages with an OpenAI model, labels each fact by rule (Verified, Needs Review, Inferred, Unknown), and converts costs to Turkish lira. In production it takes a real student's profile (grades, language scores, budget, citizenship), often a minor's, and compares it with the requirements to produce a met / gap / check list. The report is delivered via n8n and Telegram, and runs are logged in Airtable. The MVP uses synthetic profiles, so **this audit assesses the production design before real data is processed**.

## 2. Data and role map

**Personal data:** children's academic records, family budget, citizenship, Telegram identity, and the system's own evaluation of the student (profiling). No Art. 9 data by design. Health data could enter through scholarship checks.

**Roles:** Unioptt is **controller** (B2C). In the school version, each school is controller and Unioptt its **processor**. Airtable, OpenAI (if it sees profiles) and cloud-hosted n8n are processors needing DPAs. Telegram is a consumer messenger with no standard DPA. Tavily, Jina, Pinecone and Frankfurter appear to receive no personal data (to confirm).

**Transfers:** Airtable (US), OpenAI (US) and Telegram (non-EU) receive or may receive personal data. **No transfer mechanism is documented.**

## 3. Compliance findings

**Finding 1 — DPIA required but not conducted (Art. 35)** · Severity: **Blocking** (before real data)
*Description:* At least three EDPB criteria apply: evaluation of individuals (met/gap), vulnerable data subjects (minors), innovative technology (LLM pipeline). Combining student profiles with external data arguably makes a fourth. No DPIA is mentioned.
*Recommended action:* Complete a DPIA before the first real profile. Use the synthetic MVP to test mitigations.
*Escalation:* **Yes**, to a privacy lawyer or external DPO.

**Finding 2 — No lawful basis defined for processing minors' data (Arts. 6, 8)** · Severity: **Blocking** (before real data)
*Description:* The primary purpose (the report the student asked for) fits **contract (Art. 6(1)(b))**. But minors' capacity to contract, and the parental consent needed where consent is the basis (Art. 8, age 13–16 depending on the member state), are not addressed. Turkish rules apply too if users are in Turkey.
*Recommended action:* Choose contract as the basis for the report, with a parent or guardian as account holder (or confirming) for users under the applicable age; add an age gate.
*Escalation:* **Yes**, to legal counsel (national age thresholds, KVKK).

**Finding 3 — Non-EU vendors without DPAs or transfer mechanisms (Arts. 28, 44–46)** · Severity: **Significant** (Blocking once real data flows)
*Description:* Airtable logs and Telegram deliveries will carry children's profiles and evaluations outside the EU. No DPAs, transfer mechanisms or transfer impact assessments are described. Telegram offers neither a DPA nor an EU option.
*Recommended action:* Sign DPAs (Airtable, OpenAI if relevant, n8n cloud) and verify DPF or SCCs. Replace Telegram with an EU-hosted channel for minors, or send only a link to an access-controlled report. Log only what is needed (no full profile).
*Escalation:* No

**Finding 4 — No privacy notice covering AI processing (Arts. 12–14)** · Severity: **Significant**
*Description:* Users must be told, in plain and child-appropriate language, what is collected, that AI reads the sources, that their profile is compared automatically, which vendors are involved and where the data goes.
*Recommended action:* A short layered notice in Turkish and English, shown before the profile is entered.
*Escalation:* No

**Finding 5 — Purpose limitation undefined for logs, platform and school data (Art. 5(1)(b))** · Severity: **Significant**
*Description:* The brief doesn't state why runs are logged or what Unioptt the platform does with profiles. Using them for marketing, university referrals or model improvement, or reusing school-provided data, would be incompatible with the original purpose.
*Recommended action:* Write down the purposes; technically separate school data per school; get separate consent for any marketing use.
*Escalation:* No

**Finding 6 — Retention and rights workflow undefined (Arts. 5(1)(e), 15–17)** · Severity: **Minor**
*Description:* Nothing on how long profiles, reports and logs are kept, or how a family can get a copy or have data deleted across Airtable and Telegram.
*Recommended action:* Retention schedule (e.g. delete the profile 12 months after the intake date); one deletion routine covering all stores.
*Escalation:* No

## 4. Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | **Gap identified** | None stated; minors make the choice critical (F2) |
| Purpose limitation respected (no incompatible reuse) | **Cannot determine from brief** | Logging and platform purposes unstated (F5) |
| Data minimisation (only necessary data collected) | **Appears met** (profile) / **Cannot determine** (logs) | Profile fields match the purpose; log content unknown |
| Controller/processor roles mapped and DPAs in place | **Gap identified** | Vendors listed, roles and DPAs not (F3) |
| International transfer mechanism documented | **Gap identified** | US and non-EU vendors, no mechanism (F3) |
| DPIA conducted if required | **Gap identified** | Required, not done (F1) |
| Art. 22 safeguard if automated decisions affect people | **Appears met** | No decision is made; universities and families decide. Profiling still needs explaining in the notice |
| Privacy notice covers AI processing | **Gap identified** | No notice mentioned (F4) |
| Data subject rights can be operationalised within deadlines | **Cannot determine from brief** | Data spread over Airtable, Telegram, n8n (F6) |

## 5. Overall recommendation

**Do not proceed with real student data.** The synthetic MVP can continue, but two Blocking findings (no DPIA; no lawful basis for minors' data) must be resolved before any real profile is processed. The design is privacy-friendly in places: rules rather than AI decide, there is no score or decision, and the profile fields are proportionate. The gaps are paperwork and vendor choices rather than a redesign, so once the DPIA, lawful basis, DPAs and notice are in place, and Telegram is reconsidered for minors, the system can go live.

## 6. What this report is not

This report is not a legal opinion, not a DPIA and not a certification of compliance. It is based on a one-page brief and stated assumptions. Unioptt should obtain legal review before relying on this assessment.
