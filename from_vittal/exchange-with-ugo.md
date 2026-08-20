# Peer audit exchange — Whizbiz, GDPR lens

**Between:** Ugo Ahukannah (auditor) and Vittal Navale (builder) · **Sent:** 19 August 2026

One file, one round trip. My full report travels with it:
[`gdpr-peer-audit-whizbiz-by-ugo.md`](./gdpr-peer-audit-whizbiz-by-ugo.md).

I audited independently from your repository — I have not seen your self-audit, lawful-basis
selections or DPIA conclusion.

*(Filenames renamed on receipt to file this exchange under my own self-audit repo per lab
submission structure — content unchanged. My completed self-audit is at
[`../gdpr-self-audit-whizbiz.md`](../gdpr-self-audit-whizbiz.md) and
[`../data-processing-brief.md`](../data-processing-brief.md), both completed before I read your
report, per the ground rules.)*

---

## Part 1 — Five clarifying questions

Each names the obligation it bears on, so the reason for asking is visible. Blanks are fine.

**Q1. Is there any Article 28 data processing agreement between Whizbiz and a subscribing owner —
signed, drafted or planned?** *(Art 28 — processing only under a written contract.)*
> None exists. Confirmed by my own self-audit before I read your report — this is Finding 1 in
> both of our reports independently.

**Q2. Where does the production n8n instance run, and is execution data retained on it?**
*(Arts 5(1)(f), 28, 32 — security and sub-processor control.)*
> There is no production instance yet. The build has only run on a development/bootcamp-shared n8n
> instance, execution retention left at whatever n8n's default is — never configured deliberately.

**Q3. Is the owner told receipt photographs go to a US model, and warned about receipts revealing
health, religion or union membership?** *(Arts 9, 13, 44.)*
> No. No privacy notice or in-product warning of any kind exists yet.

**Q4. How would one of the owner's customers ever learn their name and address are held in Whizbiz?**
*(Art 14 — data not obtained from the data subject.)*
> They wouldn't, currently. No notice reaches them and no mechanism exists for them to find out or
> object.

**Q5. Is anything deleted, and on what schedule — chat history, Drive images, calendar entries, n8n
execution logs?** German tax law prescribes ten years for accounting records; this asks about
everything that is not one. *(Arts 5(1)(e), 17.)*
> Nothing is deleted outside the statutory bookkeeping rows, and even those only have a *retention
> floor* (10 years), not an upper bound that's been implemented. Chat history, Drive image copies,
> calendar entries and n8n logs have no schedule at all — your assumption was correct.

---

## Part 2 — Your position, before you read my report

**Please fill this in before scrolling on** — it is what keeps the comparison honest without a live
reveal.

**Lawful basis you chose for the core bookkeeping purpose:**
> Legal obligation, Art. 6(1)(b)/(c) split: legal obligation (Art 6(1)(c)) for the statutory
> EÜR/VAT bookkeeping itself, since German tax law (§147 AO) requires the records; contract
> (Art 6(1)(b)) for the surrounding features (extraction, invoicing, calendar, reporting) as
> necessary to deliver the subscribed service. Customer name/address on invoices I marked
> **TBD — legal review**, since the basis sits with the owner's relationship to their own customer,
> not with Whizbiz directly, and Whizbiz's own role as processor there isn't documented anywhere.

**Your DPIA conclusion — required or not, and on which EDPB criteria:**
> Required. I read three EDPB criteria as plausibly applying: matching/combining datasets
> (receipts, invoices, calendar and reports joined per user), innovative technology (vision
> extraction + LLM routing), and — as a judgment call rather than a certainty — special-category
> data at scale, since it's unmitigated by design rather than by volume. Two is the EDPB's usual
> threshold, so I concluded a DPIA is very likely required even without treating the third
> criterion as settled.

**Your top three findings from your own self-audit:**
> 1. No Article 28 agreement with any subscriber, and no reviewed processor agreement with
>    OpenAI or Google for this use.
> 2. No transfer mechanism documented for the three cross-border flows (OpenAI, Google, Telegram),
>    and Telegram specifically cannot realistically be brought into an Article 28 relationship at all.
> 3. Customers named on invoices have no notice, no relationship with Whizbiz, and no way to
>    exercise any data subject right — the sharpest gap in the whole system, because it makes the
>    *subscriber* non-compliant without them realising it.

---

## Part 3 — After reading my report

**Your response** — context and corrections.
> No corrections — everything in your report matches what I found working from the inside, which is
> itself the interesting result: an outsider with only the repo and no brief reached the same four
> blocking findings I reached with full builder knowledge. One piece of context: the human-in-the-loop
> confirm/cancel gate you'd have no way to fully weigh from the export alone — it was built and
> functionally working, then cut under deadline pressure (documented in `Learning.md`). It doesn't
> change your Article 22 read (I agree Article 22 isn't engaged either way), but it's the reason
> "the owner reviews everything" is currently an implicit property of the direct-commit flow rather
> than an enforced gate — worth knowing if this comes up again post-MVP.

**If our lawful-basis choices differ, which is stronger and why?**
> They don't really differ — you correctly marked the whole question "cannot determine from brief"
> since you had no brief to work from, but the bases you listed as plausible (contract for the
> owner's own data, legal obligation for the statutory books) are exactly what I independently chose.
> Where we agree most precisely is the customer name/address question — you flagged it as Finding 4
> (no notice, no rights route) and I independently marked the same data category TBD for lawful
> basis. Same gap, found two different ways.

**If our DPIA conclusions differ, which EDPB criteria do we read differently?**
> Both concluded a DPIA is required, which is what matters most, though we counted criteria
> slightly differently. You listed four: innovative technology, data of a highly personal nature,
> matching/combining datasets, and special-category data. I listed three and treated
> "highly personal nature" as folded into the special-category point rather than as its own
> criterion. Framing difference, not a disagreement — either count clears the two-criterion
> threshold.

**What did your self-audit catch that I missed, and what did I catch that you had not seen?**
> You caught something I under-weighted: framing the receipt-image *retention* as its own issue
> (Finding 6) distinct from the extraction purpose. I had folded that into "retention is
> undefined" generally in my self-audit, but your report is right that it's really a
> **purpose-limitation** problem first — the image is kept for a second purpose (archival) that was
> never separately declared or given its own retention rule — and I've reflected that framing back
> into my own worksheet's Phase 1 flag. What I could add that you couldn't determine from the
> repository alone: confirmation that no production n8n environment exists yet at all (your Finding 7
> was a well-reasoned inference from an absence of evidence; I can confirm it outright as the
> builder), and that the German 10-year retention is a floor, not a ceiling that's been implemented
> for anything else.

---

## Part 4 — Joint closing note

Two or three sentences, written together: *what kinds of GDPR gaps are hardest to catch in your own
work?*

**Proposed by Vittal, pending Ugo's confirmation or edits (this exchange is running as a document
round-trip rather than a live meeting, per your note above):**
> The gaps hardest to catch in your own work are the ones that require you to picture a person the
> system was never built to think about — for Whizbiz, that's the owner's own customer, who never
> opens the app, never sees a notice, and was invisible to me as the builder precisely because
> nothing in the product ever puts them on screen. An external, brief-only audit catches that
> reliably because it has no stake in the feature working and no accumulated assumption that "the
> user" means the one person actually chatting with the bot; self-review keeps re-deriving the same
> blind spot because the working system reinforces it every time it runs correctly.
