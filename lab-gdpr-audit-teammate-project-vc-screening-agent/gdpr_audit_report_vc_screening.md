# GDPR Audit Report — VC startup-screening agent

**Auditor:** Jaime Garate Marquerie · **Builder:** Sandra Obregón · **Date:** 18 Nov 2026 · **Sources:** Sandra's GDPR data processing brief and written answers; her AI Act System Brief; her public repository `Sobregonm/project3-vc-screening` (commit `84afd71`), checked on 18 Nov. Data flows are **verified in code**; contracts and account settings are declared only.

## 1. System summary
For a fictional fund, Puente Ventures, the agent helps an analyst decide whether to invite a startup to a first meeting; the analyst decides. Tavily receives the startup name and domain and returns excerpts. Jina Reader reads the company website. GDELT searches news by name. OpenAI (GPT-4o mini) receives the name, source links and Tavily excerpts to find evidence of headquarters and funding stage. Reports are saved locally, and the two test reports (Kalipso, Lawra) are **public on GitHub**.

## 2. Data and role map
- **Personal data:**
  - names and job titles of founders and staff in excerpts, titles and news;
  - founder information, marked "Not verified" in the reports.
- **Art. 9:** not expected. **Art. 10** is possible if news covers criminal allegations.
- **Roles:**
  - the fund is **controller**;
  - OpenAI is a **processor** (DPA needed); sign-in is with Gmail; no organisation account, plan or DPA confirmed;
  - Tavily and Jina are **TBD**, probably processors;
  - GDELT is an independent source;
  - GitHub hosts content the controller chose to publish.
- **Transfers:** US vendors. Locations and safeguards are **unverified**.

## 3. Compliance findings

**F1 — Public reports on GitHub (Art. 5(1)(b))** · **Severity:** Minor
- **Description:** the two test reports are public. A scan found no person names (founder section: "Not verified"), but publication is a separate purpose and future reports could name people.
- **Recommended action:** keep real screening reports out of public repositories; publish only redacted samples.
- **Escalation needed?** No.

**F2 — Processor contracts (Art. 28)** · **Severity:** Significant
- **Description:** code confirms OpenAI receives the startup name and Tavily excerpts (≤ 3,000 characters each), which may contain names. OpenAI and Tavily publish DPA documentation, but **coverage of the accounts used is pending verification** (Sandra, 18 Nov). Jina: no terms checked.
- **Recommended action:** confirm each DPA applies to the account (organisation account for OpenAI); check Jina's terms.
- **Escalation needed?** Yes, to legal. It becomes **Blocking** if names are confirmed to flow without a DPA.

**F3 — Lawful basis (Art. 6(1)(f))** · **Severity:** Significant
- **Description:** legitimate interests is considered and an initial assessment is drafted, but it is marked `TBD — legal review`.
- **Recommended action:** complete the three-step LIA, including the need for names and job titles.
- **Escalation needed?** Yes, to legal review.

**F4 — Transparency and rights (Arts. 14, 15, 17, 21)** · **Severity:** Significant
- **Description:** no Art. 14 notice or exemption, and no process for access, erasure or objection.
- **Recommended action:** add a notice in the fund's privacy policy or document Art. 14(5)(b); create a request channel.
- **Escalation needed?** No.

**F5 — Transfers (Arts. 44–46)** · **Severity:** Significant
- **Description:** provider regions and safeguards are unverified.
- **Recommended action:** choose EU residency, or document DPF certification or SCCs.
- **Escalation needed?** Yes, to legal.

**F6 — Retention, minimisation, DPIA (Arts. 5(1)(c)(e), 35)** · **Severity:** Minor
- **Description:** no deletion rule. Excerpts are not filtered for names. About two EDPB criteria apply (combining datasets, innovative technology).
- **Recommended action:** set retention; strip names before the LLM call; record a DPIA screening.
- **Escalation needed?** No.

## 4. Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each purpose | **Gap identified** | `TBD — legal review` (F3) |
| Purpose limitation respected | **Gap identified** | Reports published on GitHub (F1, minor) |
| Data minimisation | **Cannot determine from brief** | Excerpts not filtered; names unconfirmed |
| Roles mapped and DPAs in place | **Gap identified** | DPAs exist; account coverage pending verification (F2) |
| International transfer mechanism documented | **Gap identified** | Unverified (F5) |
| DPIA conducted if required | **Cannot determine from brief** | No DPIA view stated (F6) |
| Art. 22 safeguard if automated decisions | **Appears met** | No automatic rejection; the analyst sees everything |
| Privacy notice covers AI processing | **Gap identified** | No Art. 14 notice (F4) |
| Rights can be operationalised in time | **Gap identified** | No request process (F4) |

"Gap identified" means the builder's own brief reports the missing element. It is a documentation gap, not a proven infringement.

## 5. Overall recommendation — **Proceed with conditions**
No Blocking finding on the declared facts. **Before any pilot with real data:**
1. keep real reports out of public repositories;
2. verify that the OpenAI and Tavily DPAs cover the accounts used, check Jina's terms and the transfer safeguards;
3. complete the LIA and the Art. 14 approach;
4. set retention and record a DPIA screening.

If names are confirmed to reach a vendor whose DPA does not cover the account, F2 becomes Blocking: **Do not proceed** until it is fixed.

## 6. What this report is not
This report is not a legal opinion, not a DPIA and not a certification of compliance. It rests on the builder's declarations and a read of her public code, without contracts, account settings or API logs. The client should obtain legal review before relying on it.
