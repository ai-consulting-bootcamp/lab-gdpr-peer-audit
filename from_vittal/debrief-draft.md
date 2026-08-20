# Peer audit exchange — AI Pre-Scan, GDPR lens

**Between:** Vittal Navale (auditor) and Ugo Ahukannah (builder) · **Sent:** 19 August 2026

Following the same document-round-trip format you used for Whizbiz. My full report travels with it:
[`gdpr-audit-report-ai-prescan.md`](./gdpr-audit-report-ai-prescan.md).

I audited independently from your public repository — I have not seen your self-audit, lawful-basis
selections, or DPIA conclusion (I did read the one factual line in `LESSONS.md` noting that a prior
self-audit surfaced the missing transfer-mechanism gap, which is repository documentation rather than
your reasoning, and treated it the same as any other repo evidence).

---

## Part 1 — Five clarifying questions

Full versions with obligations and my provisional assumptions: [`clarifying-questions-log.md`](./clarifying-questions-log.md).

**Q1.** Does the adviser's `notes` field on a client record end up holding a contact person's name in
practice?
> _Your answer:_

**Q2.** Once past the local prototype, will you host a backend that processes on each adviser's
behalf, or will each adviser self-host with her own keys? *(This is the fact that decides whether you
are a processor at all.)*
> _Your answer:_

**Q3.** Is there a retention/deletion schedule for the local job store (`store_jobs.py`) beyond its
exclusion from git?
> _Your answer:_

**Q4.** Is a transfer mechanism or processor agreement for OpenAI/Pinecone planned before the GTM
sprint 1 pilot, and on what timeline?
> _Your answer:_

**Q5.** Once a report is filed to Notion, is there any way for a person named in it to have it
removed?
> _Your answer:_

---

## Part 2 — Your position, before you read my report

**Please fill this in before scrolling on**, same as you asked of me.

**Lawful basis you chose for the primary processing purpose (researching a client company):**
> _Your answer:_

**Your DPIA conclusion — required or not, and on which EDPB criteria:**
> _Your answer:_

**Your top three findings from your own self-audit:**
> 1.
> 2.
> 3.

---

## Part 3 — After reading my report

**Your response** — context and corrections.
> _Your response:_

**If our lawful-basis choices differ, which is stronger and why?**
> _Your answer:_

**If our DPIA conclusions differ, which EDPB criteria do we read differently?**
> _Your answer:_

**What did your self-audit catch that I missed, and what did I catch that you had not seen?**
> _Your answer:_

---

## Part 4 — Joint closing note

Two or three sentences, written together: *what kinds of GDPR gaps are hardest to catch in your own
work?*

**Agreed final version:**
> _pending_
