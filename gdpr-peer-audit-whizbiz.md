# GDPR peer audit — Whizbiz: Messenger Accountant

**System audited:** Whizbiz — Messenger Accountant (V1) · **Built by:** Vittal Navale
**Auditor:** Ugo Ahukannah · **Date of audit:** 19 August 2026 · **Basis:** Regulation (EU) 2016/679

**Materials received:** the project repository `vitcipher/W6_Project3-Whizbiz-Messenger-Accountant`
— pitch assets, planning checklist, build learnings, and the exported n8n workflow (52 nodes).
**A written data processing brief was not received**, so this audit is built from the repository and
every point where a brief would have answered something is recorded as a gap rather than filled in
silently.

**Ground rules observed.** I have not seen Vittal's self-audit, his lawful-basis selections, his DPIA
conclusion or his memo, and findings have not been discussed with him ahead of the debrief.

---

## Phase 1: Read and annotate

A solopreneur messages a Telegram bot. Photographs of receipts are read by a vision model and written
to a German-format expense sheet with the image filed to Drive; typed instructions create invoices
and calendar entries; the books are read back for profit reports and a scheduled daily digest.

**The four annotations that drive this audit:**

1. **There are two populations of data subjects, and only one of them consented to anything.** The
   owner chose to use Whizbiz. The **customers named on invoices did not** — the income sheet carries
   `Kunde` and `Addresse`, and those people have no relationship with the product, no notice, and no
   route to object.
2. **Receipt images are unstructured and unfiltered.** A whole photograph goes to a US model. A
   receipt from a pharmacy, a clinic, a church collection or a union office reveals a special
   category of data about the owner, and nothing in the workflow inspects or restricts what is sent.
3. **Telegram is not a neutral pipe.** Every message, photo and file passes through it before the
   system sees it, and it is not an EU service under an adequacy decision.
4. **Retention here is prescribed, not free.** German tax law requires accounting records to be kept
   for ten years. That is unusual and useful: it supplies a lawful basis for keeping the books and it
   sets a hard limit on the right to erasure — but it does **not** cover the chat history, the
   Drive image copies, or the calendar entries, and nothing in the design distinguishes them.

---

## Phase 2: Personal data and role map

Completed from the materials received. "Not stated" marks a gap a brief should have closed.

**Personal data summary:**

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Telegram identifiers — user ID, chat ID, username, display name | Telegram, on every message | Routing replies; identifying the account | **Yes** — Telegram (Telegram FZ-LLC, Dubai; no adequacy decision) | No |
| Free-text message content ("invoice Anna, €45, delivery Friday") | Typed by the owner | Intent classification by gpt-4o-mini; invoice and calendar creation | **Yes** — OpenAI (US), Telegram | Not by design; possible incidentally in free text |
| **Receipt photographs** | Sent by the owner | Vision extraction by gpt-4o; archival copy in Google Drive | **Yes** — OpenAI (US), Google (US), Telegram | **Possible and unmitigated** — a pharmacy, clinic, place of worship or union receipt reveals health, religious or trade-union data |
| Extracted expense fields — vendor, date, gross/net/VAT, category, receipt link | Derived from the photograph | German-format expense bookkeeping (`EÜR`), VAT records | **Yes** — Google Sheets | No |
| **Customer name and postal address** (`Kunde`, `Addresse`) | Typed by the owner about a third party | Invoice creation; income sheet; calendar entry | **Yes** — Google, OpenAI, Telegram | No — but these are identifiable third parties with no notice |
| Order and delivery details, dates, amounts, invoice numbers | Derived from the instruction | Invoicing, scheduling, revenue reporting | **Yes** — Google | No |
| Aggregated revenue and profit figures | Derived from the sheets | Reporting to the owner; daily digest | **Yes** — Google, OpenAI | No |

**Transfer mechanisms.** Three sets of transfers leave the EEA — OpenAI, Google, and Telegram. For
OpenAI and Google the mechanism would be the EU–US Data Privacy Framework where the entity is
certified, otherwise SCCs plus a transfer impact assessment. Telegram is the hardest: it is neither
EU-established nor covered by an adequacy decision, and a consumer messaging service will not sign an
Article 28 agreement with a small bookkeeping vendor. **The repository provides no evidence that any
mechanism is in place for any of the three.**

**Role map:**

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| **Client** — the subscribing solopreneur | **Controller** — decides to record their business's and their customers' data | Everything the bot does on their behalf | Yes, **as the controller side** of an Article 28 agreement with Whizbiz |
| **Builder** — Vittal / Whizbiz | **Processor** on the stated subscription model — processes on the controller's behalf, though it determines much of the means | Receipt extraction, bookkeeping, invoicing, storage, reporting | **Yes — and none exists.** Also owes a sub-processor list and flow-down terms |
| **OpenAI** | **Sub-processor** | Vision extraction, intent classification, digest generation | Yes — plus transfer mechanism |
| **Google** (Drive, Sheets, Calendar) | **Sub-processor** | Receipt images, the books, delivery events | Yes — plus transfer mechanism |
| **Telegram** | **Independent controller** for the messaging layer; unavoidable conduit for all content | Transports every message, photo and file | **Not obtainable in practice** — this is a design constraint to disclose, not a document to chase |
| **n8n host** | **Sub-processor** (hosting the orchestration) | Executes the workflow, holds execution data | Yes — and the production host is **not stated** |

---

## Phase 3: Clarifying questions log

Sent to Vittal in writing on 19 August 2026, before finalising. Unanswered at the time of writing.

**Q1 — Is there any Article 28 agreement between Whizbiz and a subscribing owner, in draft or
otherwise?**
*Obligation:* Article 28 — a controller may only use a processor under a written contract.
*Provisionally assuming:* none exists, since the repository contains no terms, contract or DPA.

**Q2 — Where does the production n8n instance run, and is execution data retained there?**
*Obligation:* Articles 5(1)(f), 28 and 32 — security, sub-processor control, integrity.
*Provisionally assuming:* the shared bootcamp instance, with default execution retention.

**Q3 — Is the owner told that receipt photographs are sent to a US model, and are they warned not to
photograph receipts that reveal health, religion or union membership?**
*Obligation:* Articles 9, 13 and 44 — special-category processing, transparency, transfers.
*Provisionally assuming:* no such notice or warning exists.

**Q4 — How is the owner's customer told their name and address are held in Whizbiz?**
*Obligation:* Article 14 — data not obtained from the data subject.
*Provisionally assuming:* no notice reaches the customer at all.

**Q5 — Is anything deleted, and on what schedule — chat history, Drive images, calendar entries?**
*Obligation:* Article 5(1)(e) storage limitation, and Article 17 erasure.
*Provisionally assuming:* nothing is deleted; the ten-year tax retention rule is being applied
implicitly to everything rather than to the accounting records it actually covers.

---

## Phase 4: Audit report

### Section 1: System summary

Whizbiz is a chat-based bookkeeping assistant for German solo business owners, implemented as an n8n
workflow behind a Telegram bot. It reads photographed receipts with a vision model into a
VAT-structured expense sheet, files the image to Google Drive, turns typed instructions into invoices
and calendar entries recording the customer's name and address, and reports revenue against profit on
request and on a daily schedule.

### Section 2: Data and role map

As set out in Phase 2. The two facts that shape everything below: the system holds personal data
about **third parties who never interact with it** — the owner's customers — and it sends
**unfiltered receipt photographs** to a US model, which is the one path on which special-category
data can enter without anybody choosing to send it.

### Section 3: Compliance findings

> **Finding 1 — No Article 28 agreement between the subscriber and Whizbiz**
> **Severity:** Blocking
> **Description:** On the subscription model described in the pitch, each solopreneur is a controller and Whizbiz is a processor handling their customers' personal data. Article 28(3) requires a written contract before that processing begins, covering instructions, confidentiality, security, sub-processors, assistance with data subject rights, deletion and audit. The repository contains no terms, no DPA and no sub-processor list.
> **Recommended action:** put a DPA in place, with an annexed sub-processor list naming OpenAI, Google, the n8n host and — explicitly — Telegram's role, before the first paying subscriber.
> **Escalation needed?** Yes — legal counsel to draft, not a template pasted in.

> **Finding 2 — No transfer mechanism for three separate exports of personal data**
> **Severity:** Blocking
> **Description:** Personal data reaches OpenAI (US), Google (US) and Telegram (Dubai) on the main path of every transaction. Chapter V requires a documented mechanism for each: DPF certification where available, otherwise SCCs with a transfer impact assessment. Telegram is the structural problem — it is the transport for everything, it is outside adequacy, and it will not enter an Article 28 relationship with a small vendor.
> **Recommended action:** document DPF or SCCs for OpenAI and Google. For Telegram, either treat it as an independent controller and disclose it plainly to subscribers, or offer an EU-hosted channel as an alternative. Do not describe this as solved when it is disclosed.
> **Escalation needed?** Yes.

> **Finding 3 — DPIA required and not conducted**
> **Severity:** Blocking
> **Description:** Applying the EDPB's nine criteria: **innovative technological solution** (vision-model extraction plus LLM routing), **data of a highly personal nature** (a complete financial record of a business and its named customers), **matching or combining datasets** (receipts, invoices, calendar and reporting joined per user), and **special-category data** entering by way of unfiltered receipt images. Four criteria, where two ordinarily trigger the requirement. No DPIA exists.
> **Recommended action:** conduct the DPIA before onboarding external subscribers; its most useful output will be deciding what must *not* be sent to the vision model.
> **Escalation needed?** Yes — DPO or privacy counsel.

> **Finding 4 — Third-party customers have no notice and no route to their rights**
> **Severity:** Blocking
> **Description:** `Kunde` and `Addresse` identify people who never interact with Whizbiz. Because their data is not obtained from them, **Article 14** requires that they be informed — ordinarily within a month. The controller here is the owner, not Whizbiz, but the product creates the obligation and currently gives the owner no means of meeting it. Nothing in the workflow supports access, rectification or objection for those individuals.
> **Recommended action:** supply subscribers with model wording for their own invoices and privacy notice, and build a per-customer lookup so an access or rectification request can actually be answered. This is the finding where the product can most easily make its users non-compliant without their realising it.
> **Escalation needed?** Yes.

> **Finding 5 — Unfiltered receipt images can carry special-category data (Article 9)**
> **Severity:** Significant
> **Description:** The vision node receives the whole photograph. A pharmacy or clinic receipt reveals health data; a place-of-worship donation reveals religious belief; a union receipt reveals membership. Article 9(1) prohibits processing these absent a condition, and none of the Article 9(2) conditions fits a bookkeeping bot — explicit consent could be argued for the owner's *own* data but has never been sought, and cannot cover data about anyone else.
> **Recommended action:** warn the user at onboarding, and consider a pre-send category check that refuses or blurs obviously sensitive vendors. At minimum, record the residual risk in the DPIA rather than leaving it undiscovered.
> **Escalation needed?** Yes — this is the finding most likely to need a lawyer's view on whether consent is workable at all.

> **Finding 6 — Retention is undefined everywhere except where the law defines it**
> **Severity:** Significant
> **Description:** German tax law requires accounting records to be retained for ten years, which supplies both a lawful basis and a legitimate limit on erasure for the books. It does **not** cover the Telegram chat history, the Drive image copies, the calendar entries or the n8n execution logs — and nothing distinguishes them. The likely real-world outcome is that everything is kept for ever by default, with the tax rule cited as the justification.
> **Recommended action:** write a retention schedule that separates statutory records from operational copies, and implement deletion for the second group.
> **Escalation needed?** No — though the ten-year rule should be confirmed against the client's own tax position.

> **Finding 7 — Production environment not established**
> **Severity:** Significant
> **Description:** The workflow is an export; where it runs in production is not recorded. If real subscriber data is processed on a shared teaching instance, the controller has no control over access, retention or security, and Articles 28 and 32 cannot be satisfied on any paperwork.
> **Recommended action:** stand up a dedicated instance under Whizbiz's control before any external data, and record it.
> **Escalation needed?** No.

> **Finding 8 — No privacy notice covering the AI processing**
> **Severity:** Minor
> **Description:** No notice exists for the owner either — covering what is sent to which model, what is stored where, and for how long. It is Minor only because it is downstream of Findings 1–4: the notice cannot be written until those answers exist.
> **Recommended action:** produce it as the last step of remediation, not the first.
> **Escalation needed?** No.

### Section 4: Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | **Cannot determine from brief** | No brief and no documentation states one. Contract (Art 6(1)(b)) would fit the owner's own data, legal obligation (Art 6(1)(c)) fits the statutory books, and the customers' data sits under the owner's own contract with them — but none of this is recorded anywhere |
| Purpose limitation respected (no incompatible reuse) | **Appears met** | Every purpose observed — extraction, bookkeeping, invoicing, reporting — is the purpose the data was given for. The daily digest's web search sends no personal data |
| Data minimisation (only necessary data collected) | **Gap identified** | Whole receipt images rather than the extracted fields; the full photograph is retained in Drive after extraction. Customer address is plausibly necessary for a valid German invoice — that one is a question, not a finding |
| Controller/processor roles mapped and DPAs in place | **Gap identified** | Roles are inferable but nowhere stated, and no DPA exists at any link in the chain (Finding 1) |
| International transfer mechanism documented | **Gap identified** | Three exports, no mechanism evidenced (Finding 2) |
| DPIA conducted if required | **Gap identified** | Required on four EDPB criteria; not conducted (Finding 3) |
| Article 22 safeguard in place if automated decisions affect people | **Appears met — not engaged** | The system produces no decision with legal or similarly significant effects on a person. Categorising an expense is a decision about a transaction. Human review is inherent: every output lands in a chat the owner reads |
| Privacy notice covers AI processing | **Gap identified** | None for the owner, none reaching their customers (Findings 4, 8) |
| Data subject rights can be operationalised within deadlines | **Gap identified** | Access is feasible in principle — the books are readable spreadsheets — but there is no per-person lookup, no deletion path for operational copies, and no mechanism at all for the owner's customers |

### Section 5: Overall recommendation

**Do not proceed — scoped precisely.** Four blocking findings stand between this system and lawful
processing of *other people's* data: no processor agreement, no transfer mechanism, no DPIA, and no
notice to the third-party customers whose names and addresses it holds. On the lab's own definition —
a missing DPA for a processor already handling personal data, or a required DPIA not conducted —
either one alone is blocking, and all four are present.

That verdict applies to **onboarding real subscribers**. It does not condemn the prototype: run by
its builder against his own business data, Whizbiz is a legitimate personal project, and the
engineering is sound. The distance between the two states is paperwork and one hosting decision, not
a redesign — and none of the four blockers is expensive if they are done *before* the first paying
user rather than after.

It is worth naming the divergence with my companion AI Act audit of the same system, which concluded
*proceed with conditions*. That is not an inconsistency: under the AI Act the system is correctly
outside the high-risk regime and its duties are small, while under GDPR it processes third-party
personal data across three borders with no contracts. Same system, two regimes, two different
verdicts — which is exactly why a compliance review that stops at one regime is worth very little.

### Section 6: What this report is not

This report is not a legal opinion, not a DPIA, and not a certification. It is a first-pass external
review conducted without a written data processing brief and without answers to the Phase 3
questions. The controller should engage legal counsel before relying on it for any compliance
decision, and every conclusion should be revisited if the answers to Phase 3 differ from the
assumptions recorded there.

---

## Phase 5: Debrief conversation

_Pending. Six-step sequence: auditor presents, builder responds, compare lawful basis for the primary
purpose, compare DPIA conclusions, compare gap lists, joint closing note._
