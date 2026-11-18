# Stretch — Remediation plan for Finding 1 (DPIA required but not conducted)

**Why this finding:** it is Blocking, and it pulls in Finding 2 (lawful basis for minors) and Finding 3 (vendors and transfers). A DPIA forces both to be answered and documented.

| Question | Plan |
|---|---|
| **What artifact closes the gap?** | A **DPIA** for the production system covering: description of processing and data flows (per vendor); necessity and proportionality, including the **lawful basis for minors** (contract + parent/guardian) and why each profile field is needed; risks (wrong deadlines or costs, exposure of children's data via Telegram, US transfers, reuse for marketing); mitigations (age gate, EU delivery channel, minimal logging, DPAs, retention schedule, privacy notice). |
| **Who owns it?** | **Unioptt as controller (Elif)** owns and signs it. An **external privacy counsel or DPO** reviews the minors and transfer sections. In the B2B version each school does its own DPIA, using Unioptt's as input. |
| **Realistic timeline** | Week 1: answers to Q1–Q5, data-flow map per vendor. Week 2: draft DPIA using the synthetic MVP to test mitigations. Week 3: counsel review, vendor DPAs signed, notice drafted. **About 3–4 weeks, before the first real profile.** |
| **Evidence for a regulator** | Signed and dated DPIA with version number; counsel's review notes; signed DPAs and transfer records (DPF check or SCCs + TIA); the published privacy notice; age-gate screenshots; a scheduled DPIA review date (e.g. before the B2B launch). |
