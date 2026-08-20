# Phase 3: Clarifying Questions Log

## Question 1 — Anand's own role once the system is live

**What I need to know:** Does Anand retain any ongoing operational access to live order/chat data after delivering the system (e.g., for maintenance, debugging, or support), or does the business operate it entirely independently once handed over?

**Why it matters:** This determines whether Anand is a processor (or joint controller) in his own right, separate from any obligations that fall on the business itself. This affects who needs a DPA with whom, and who bears responsibility if something goes wrong with the data.

**Provisional assumption in the absence of an answer:** Assuming Anand retains at least periodic access for maintenance (consistent with an ongoing "family business support" relationship implied elsewhere in his project materials), making him likely a processor to the business's controller role — but this is unconfirmed.

---

## Question 2 — Confirmed processing region for OpenAI and Google Workspace

**What I need to know:** Has the specific processing region for OpenAI API calls and Google Workspace/Sheets tenancy been confirmed, ahead of the Germany deployment going live?

**Why it matters:** This is the single fact that determines whether an international transfer mechanism (SCCs or otherwise) is required once Germany-based schools' data starts flowing through the system. The brief already flags this as unconfirmed — this question asks whether it's been resolved since the brief was written.

**Provisional assumption in the absence of an answer:** Assuming, conservatively, that **no EU-specific region has been confirmed yet**, since the brief states this explicitly as an open item — treating this as an active gap rather than assuming it will resolve favorably.

---

## Question 3 — Human review on the "mark fulfilled" auto-step

**What I need to know:** Does a human review and confirm the publisher-consolidation "mark fulfilled" step before it's reported as sent, or does it run automatically without review?

**Why it matters:** The brief correctly notes this doesn't rise to an Article 22 issue (it's not a decision *about a person* with legal effect) — but it's still a data-accuracy and operational-integrity question worth resolving, since inaccurate fulfillment records tied to identifiable schools could create downstream disputes.

**Provisional assumption in the absence of an answer:** Assuming, based on the brief's own uncertainty, that this **may currently run without human review** — flagged as a minor operational finding rather than a compliance gap.

---

## Question 4 — Scope and retention of incidental photo data

**What I need to know:** When a photo order contains incidental personal content beyond the book list (names, phone numbers, etc.), is that image discarded immediately after parsing, or retained anywhere (e.g., in Telegram/WhatsApp's own message history, or a debugging log)?

**Why it matters:** The brief acknowledges this risk exists but assesses it as "low but non-zero" without stating what happens to the image afterward. If images are retained anywhere, even incidentally via the messaging platform's own history, that changes the retention and data-minimization picture materially.

**Provisional assumption in the absence of an answer:** Assuming images are **not deliberately persisted by the system itself** beyond the parsing step (consistent with how the Should-Cost Benchmarking Agent's own photo-adjacent flows were assumed to behave in an earlier audit) — but noting that message-platform-level retention (Telegram/WhatsApp's own history) is outside the system's control regardless.

---

## Question 5 — Legal basis under consideration for purpose (e), the Q&A feature

**What I need to know:** Has any lawful basis already been considered for purpose (e) — the conversational Q&A layer over historical order data — or is this purpose currently running without a lawful basis determination at all?

**Why it matters:** This is the brief's own flagged purpose-drift concern. If this feature is already live and querying historical data without a resolved lawful basis, that's a more urgent finding than if it's still in planning. The severity of this finding in the audit report depends heavily on whether this is live or hypothetical.

**Provisional assumption in the absence of an answer:** Assuming, based on the brief's phrasing ("is now being queried"), that **this feature is already active**, treating this as a live gap rather than a future consideration.
