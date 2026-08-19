# Peer Audit Report — Stups (GDPR lens)

**Auditor:** JohnA

**System audited:** Stups (a personal daily evening-suggestion agent for Hamburg, built on n8n)

**Builder / client:** GordonS

**Materials provided:** README.md, Report_1.md (sample outputs), Stups0.6.md (n8n workflow export), gtm_future_sprints.md, stack_decision_1.md — all in the Day 2 lab's `Peers Project files/` folder (same underlying project, GDPR lens applied independently for this lab)

**Date of review:** 2026-08-19

This report follows the phase structure in `instructions.md`. Work was done independently; clarifying questions were logged in writing (Phase 3) before findings were finalized.

## Submission hygiene

Filenames are clear and descriptive (`stups_gdpr_audit_report.md`, not `peer_review.md`). This repository is scoped to this lab only, with no unrelated projects, dumps, or personal files. `README.md` includes a file map naming the teammate (GordonS) and the project audited (Stups). No secrets, API keys, or tokens are committed.

## Ground rules

Only GordonS's data processing brief materials were exchanged before this audit began (the `Peers Project files/` folder from the Day 2 lab — README, sample outputs, workflow export, GTM sprints, and stack decision doc). No discussion of GordonS's own GDPR conclusions took place before the debrief in Phase 5. Where the brief was unclear, questions were logged in writing with a stated provisional assumption before any answer was received — see Phase 3.

---

## Phase 1: Read and annotate

**Personal data identified (current build):**
- Telegram chat ID (identifies the user)
- Hand-written taste profile (food, activity, budget preferences) — personal but not special-category
- No special-category data present (no health, ethnicity, religion, etc.)

**Cross-border flows identified:**
- DeepSeek (China) — receives taste profile + weather/event context to generate suggestions
- OpenAI (US) — backup LLM, same data
- Telegram (US) — message delivery
- OpenWeatherMap, Ticketmaster — receive only city name / generic query, not personal data; not processors

**Unclear / flagged for clarifying questions:** DPA status with vendors, lawful basis, DPIA status, transparency/rights process, future storage location — see Phase 3.

**Purpose limitation:** No incompatible reuse identified. Current single-user use only.

---

## Phase 2: Personal data and role map

**Personal data summary:**

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Telegram chat ID | User setup | Message delivery | Yes (Telegram, US) | No |
| Taste profile (food, activity, budget prefs) | User-authored text | Personalize suggestions | Yes (sent to DeepSeek/China, OpenAI/US) | No |

**Role map:**

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Client (builder) | Controller | Decides purpose/means, receives output | N/A — is the controller |
| DeepSeek | Processor | Generates suggestion text from taste profile | Yes — not evidenced in brief |
| OpenAI | Processor | Backup LLM, same processing | Yes — not evidenced in brief |
| Telegram | Processor | Delivers message | Yes — not evidenced in brief |

OpenWeatherMap and Ticketmaster receive only a city name / generic date query — no personal data — so they are not processors under GDPR.

**International transfer note:** Transfers to DeepSeek (China) and OpenAI/Telegram (US) currently have no documented transfer mechanism (e.g. SCCs). Not yet a live risk, since today's only data subject is the builder himself (personal/household use). Becomes a live risk the moment a second user's data is processed.

**At-scale callout (roadmap, not current state):** Once real users onboard (per `gtm_future_sprints.md` Sprint 0–1), the following must be decided and documented before launch:
- DPAs with DeepSeek, OpenAI, and Telegram
- A transfer mechanism for the China and US flows
- EU-region hosting as the default if/when a database or n8n data table is added for persistent memory, to avoid a second uncontrolled transfer

---

## Phase 3: Clarifying questions log

**Q1 — Is a DPA in place with DeepSeek, OpenAI, or Telegram?**
- Why it matters: Art. 28 requires a written DPA with any processor.
- Answer (confirmed by builder): No DPAs currently in place.

**Q2 — Under what lawful basis is the taste profile and chat ID processed?**
- Why it matters: Art. 6 requires a lawful basis for any processing.
- Answer: Today, single-user personal use likely falls outside GDPR's material scope (Art. 2(2)(c), purely personal/household activity). Builder confirmed future sprints will add real users creating profiles and answering personalization questions — at that point consent is the likely lawful basis, not yet designed.

**Q3 — Will there be a DPIA before onboarding real users?**
- Why it matters: automated profiling of multiple users' preferences, plus a planned behavioral learning loop, can trigger the Art. 35 DPIA requirement.
- Answer (confirmed by builder): Nothing in place as of today; only a demo prototype has been built.

**Q4 — Will onboarded users be told their suggestions are AI-generated, and can they access/delete their taste profile data?**
- Why it matters: Art. 13/14 transparency and Art. 15/17 data subject rights (access, erasure).
- Answer (confirmed by builder): Transparency is planned — users will be informed content is AI-generated, linked to relevant policies once in place. Erasure rights are understood as a legal obligation the builder intends to honor. As of today, nothing is implemented (single user, the builder himself).

**Q5 — Where will user data (taste profiles, chat IDs, future interaction/mood-tap history) be stored once real users onboard?**
- Why it matters: determines the transfer mechanism needed (Art. 44–49) and whether a new storage vendor becomes a processor requiring its own DPA.
- Answer: No database exists in the current workflow (confirmed against the n8n export — no database node present) or in `stack_decision_1.md`. Builder's stated intent is to use n8n data tables for early friends/family scale-testing; not yet decided or documented. Recommendation: keep data in the EU when possible once a storage choice is made.

---

## Phase 4: Audit report

### Section 1: System summary

Stups is a personal n8n-based evening-suggestion agent that runs on a daily schedule. It reads live Hamburg weather and event data, weighs it against a fixed taste profile using an LLM (DeepSeek or OpenAI), and sends one message with two suggestions to the builder's phone via Telegram. Today it processes one person's data (the builder's own chat ID and hand-written taste profile) with no other users, no database, and no persistent memory between runs. The roadmap plans onboarding real users with their own taste profiles, a feedback/learning loop, and eventual B2B distribution through relocation agencies and employers.

### Section 2: Data and role map

Personal data today is limited to a Telegram chat ID and a static taste profile, both belonging to the builder alone, so the processing likely falls under GDPR's personal/household exemption (Art. 2(2)(c)) as it stands. The builder is the controller; DeepSeek, OpenAI, and Telegram act as processors once real users' data is involved, but no DPAs exist with any of them today. Data crosses the EU border to DeepSeek (China) and OpenAI/Telegram (US) for processing — no transfer mechanism is currently documented, though this is not yet a live risk since no third-party personal data flows through the system today.

At scale (once real users onboard, per the roadmap): DPAs will be needed with DeepSeek, OpenAI, and Telegram before any non-builder personal data is sent to them; a transfer mechanism (e.g., SCCs) will be needed for the China and US transfers; and if a database is added, EU-region hosting should be the default choice to avoid a second uncontrolled transfer.

### Section 3: Compliance findings

> **Finding 1 — Lawful basis (Art. 6)**
> **Severity:** Minor (today) / Significant (at scale)
> **Description:** Today, single-user personal use likely falls outside GDPR entirely (household exemption). Once real users onboard, consent will be the natural lawful basis for taste-profile collection, but no consent flow exists yet.
> **Recommended action:** Design and implement a clear consent step as part of onboarding, before Sprint 0/1 launches.
> **Escalation needed?** No — but must be resolved before onboarding real users.

> **Finding 2 — Purpose limitation (Art. 5(1)(b))**
> **Severity:** Minor
> **Description:** Taste profile is collected for personalized suggestions only, no reuse identified today. Two forward-looking risks: (1) planned B2B distribution (Sprint 3) could send profile data to a new context (employer/relocation dashboards); (2) if precise user location is added later to improve recommendations, that raises the sensitivity of data collected (location patterns can reveal home/work, routine) and needs its own lawful basis and minimization check, not just an extension of the existing taste profile consent.
> **Recommended action:** When designing B2B or location features, reassess purpose limitation and consent scope before building.
> **Escalation needed?** No — flag for future review before Sprint 3 or any location feature.

> **Finding 3 — DPAs missing for processors (Art. 28)**
> **Severity:** Blocking (at scale, before real users)
> **Description:** DeepSeek, OpenAI, and Telegram all process personal data on the builder's behalf once real users exist, but no DPA is in place with any of them today. Confirmed by the builder (Phase 3, Q1).
> **Recommended action:** Execute DPAs with all three vendors before any non-builder personal data flows through the system.
> **Escalation needed?** Yes — to the builder/controller directly, as a go/no-go gate before Sprint 0 launch.

> **Finding 4 — International transfer mechanism (Art. 44–49)**
> **Severity:** Blocking (at scale, before real users)
> **Description:** Personal data would flow to DeepSeek (China, no adequacy decision) and OpenAI/Telegram (US) with no documented transfer mechanism (e.g. SCCs) today.
> **Recommended action:** Put SCCs (or equivalent) in place for all three vendors, with particular attention to the China transfer, before onboarding real users. Consider EU-region alternatives if a China transfer proves hard to justify to users/regulators.
> **Escalation needed?** Yes — to the builder/controller, same go/no-go gate as Finding 3.

> **Finding 5 — DPIA requirement (Art. 35)**
> **Severity:** Blocking (at scale, before real users)
> **Description:** No DPIA has been conducted. Once real users onboard, the system will process personal preference data at scale with a planned behavioral learning loop ("not tonight → why") that profiles user behavior over time. This combination (systematic profiling feeding automated suggestion output) is a DPIA trigger under the EDPB criteria, even though the output itself is low-stakes (a leisure suggestion, not a legal/significant effect).
> **Recommended action:** Conduct a DPIA before Sprint 0/1 launch, focused on the profiling/learning loop rather than the current static profile.
> **Escalation needed?** Yes — to the builder/controller.

> **Finding 6 — Data subject rights operationalisation (Art. 15/17)**
> **Severity:** Significant (at scale)
> **Description:** Builder confirmed erasure rights are understood as a legal obligation and will be honored, but no process exists yet for real users to access or delete their taste profile data (Phase 3, Q4). Today this is moot with one user.
> **Recommended action:** Build a simple access/delete mechanism (even manual, e.g. a support Telegram command) before onboarding real users, and document response-time handling within the one-month GDPR deadline.
> **Escalation needed?** No — but must be resolved before onboarding real users.

> **Finding 7 — Privacy notice / AI transparency (Art. 13/14, Art. 50 AI Act overlap)**
> **Severity:** Minor (today) / Significant (at scale)
> **Description:** Builder confirmed intent to disclose AI-generated content and link to relevant policies once in place (Phase 3, Q4), but no privacy notice exists yet. Consistent with the EU AI Act peer audit finding from the same project (Article 50 transparency gap).
> **Recommended action:** Draft a short privacy notice covering what data is collected, why, which processors receive it, and that suggestions are AI-generated, before Sprint 0 launch.
> **Escalation needed?** No — but should ship alongside the consent flow in Finding 1.

### Section 4: Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | Cannot determine from brief | Household exemption likely covers today's single-user use; consent not yet designed for real users (Finding 1) |
| Purpose limitation respected (no incompatible reuse) | Appears met (today) | Forward risk flagged for B2B and location features (Finding 2) |
| Data minimisation (only necessary data collected) | Appears met | Only chat ID + taste profile collected; no excess data identified |
| Controller/processor roles mapped and DPAs in place | Gap identified | Roles mapped; no DPAs exist with DeepSeek, OpenAI, or Telegram (Finding 3) |
| International transfer mechanism documented | Gap identified | No SCCs or equivalent for China/US transfers (Finding 4) |
| DPIA conducted if required | Gap identified | Not conducted; likely required once profiling/learning loop ships (Finding 5) |
| Article 22 safeguard in place if automated decisions affect people | Appears met | Output is a low-stakes suggestion, not a legal/significant-effect automated decision; Article 22 likely does not apply, but revisit if B2B/employer use changes the stakes |
| Privacy notice covers AI processing | Gap identified | Planned but not yet written (Finding 7) |
| Data subject rights can be operationalised within deadlines | Gap identified | No access/delete process exists yet (Finding 6) |

### Section 5: Overall recommendation

**Proceed with conditions.**

The current single-user prototype is not itself a GDPR problem — it likely sits outside GDPR's scope under the personal/household exemption, and no findings block the demo as it exists today. But the project has a clear, near-term roadmap (Sprint 0/1) to onboard real users, and five of the seven findings above (1, 3, 4, 5, 6) become blocking the moment a second person's data is processed. Conditions for proceeding to Sprint 0:

1. Consent flow designed and implemented for taste-profile collection (Finding 1)
2. DPAs executed with DeepSeek, OpenAI, and Telegram (Finding 3)
3. Transfer mechanism (SCCs or equivalent) in place for China/US flows (Finding 4)
4. DPIA conducted, focused on the planned profiling/learning loop (Finding 5)
5. Basic data subject rights process (access/delete) built (Finding 6)
6. Privacy notice published, covering AI-generated content disclosure (Finding 7)

None of these require re-architecting the product — they are governance and documentation work that can run in parallel with Sprint 0 engineering, provided they land before real user data starts flowing.

### Section 6: What this report is not

This report is not a legal opinion, not a DPIA, and not a certification of compliance. The client should obtain legal review before relying on this assessment.

---

## Phase 5: Debrief conversation

**1. Auditor presents** — Auditor (JohnA) walked through this audit report without interruption.

**2. Builder responds** — Builder (GordonS) provided context: has decided to move off DeepSeek to OpenAI going forward, removing the China transfer from the vendor picture.

**3. Compare lawful basis selections** — Both auditor and builder independently selected **consent** as the lawful basis for the primary processing purpose (taste-profile collection). No disagreement.

**4. Compare DPIA conclusions** — Both audits concluded a DPIA is required once real users onboard, in line with each other.

**5. Compare gap lists** — The external audit (this report) flagged data subject rights (access/deletion) as a forward-looking gap tied to the onboarding roadmap. The builder's self-audit covered the same obligation but framed it narrowly against the current single-user case, where it reads as less urgent since he is the only data subject today. The external view surfaced the gap more clearly because it wasn't anchored to today's low-stakes reality.

**6. Joint closing note:**

> Self-assessment tends to focus on what's built today, not what the roadmap will trigger — DPAs, DPIAs, and where data actually flows once the product scales are easy to underweight when you're inside your own project. Independent review surfaces those forward-looking obligations because it isn't anchored to "it's just me using it right now." The volume of requirements can feel discouraging, like it's designed to stall a launch, but none of the findings here required rebuilding the product — they are governance work that can run in parallel with engineering.
