# Response to Vittal's GDPR audit of AI Pre-Scan

**Builder:** Ugo Ahukannah · **Auditor:** Vittal Navale · **Returned:** 20 August 2026
His exchange file: [`../debrief-ai-prescan.md`](../debrief-ai-prescan.md) ·
His report: [`../gdpr-audit-report-ai-prescan.md`](../gdpr-audit-report-ai-prescan.md)

**Sequencing, so it can be checked rather than trusted.** Parts 1 and 2 were written before opening
his report. My positions in Part 2 are not recalled — they are transcribed from my own GDPR
self-audit, committed as `1e3b7a8` on 19 August 2026, a day before his materials arrived. The git
history is the proof; I would not expect anyone to take my word for it.

---

## Part 1 — Answers to his five questions

**Q1. Does the adviser's free-text `notes` field on a client record hold a contact person's name in
practice?**
> **Yes, it would — and your assumption is right.** `Client.notes` is unstructured and
> adviser-controlled, and a free-text box beside a company record is exactly where "spoke to their
> CFO, prefers email" lands. **My own self-audit never inventoried this field at all.** I catalogued
> the research pipeline — fetched pages, embeddings, reports — and missed the adviser's own client
> list sitting beside it. It is now the clearest example I have of a builder auditing the part of the
> system he finds interesting.

**Q2. Hosted backend, or each adviser self-hosting with her own keys?**
> **Undecided, and deliberately so far.** Today it is local-only: the UI binds to 127.0.0.1, there
> are no accounts, and keys come from the operator's own store. You are right that the GTM language
> points toward a hosted backend, and right that this is the fact deciding whether a processor
> relationship exists at all. My self-audit recorded the same fork — controller today, processor if I
> host, out of scope entirely if each adviser self-hosts — without resolving it. It needs deciding
> before the pilot, not during it.

**Q3. Retention or deletion schedule for the local job store beyond exclusion from git?**
> **None exists.** Exclusion from version control is source-control hygiene, not a retention control
> — your framing is exactly right. My self-audit listed the local scan history as "indefinite; files
> persist until manually deleted", which named the gap without fixing it. Still open.

**Q4. Transfer mechanism or processor agreement for OpenAI, Pinecone or Notion before the pilot, and
on what timeline?**
> **Not scheduled — your assumption is correct.** The line in `docs/proposal.md` §9 is an honest flag
> of a known gap, not a tracked remediation item with a date. It has no owner and no deadline
> attached, which is a fair criticism of the candour: admitting a gap in a document is not the same
> as managing it.

**Q5. Once a report is filed to Notion, can a person named in it have it removed?**
> **No, and this is the sharpest question in your log.** `store.purge_scan` covers the research
> store; it does not touch the delivered artefact. My self-audit did record Notion delivery as
> "indefinite once filed" in the data inventory — but I filed it under *retention* and never
> connected it to *erasure*, so the right that would actually be exercised against it went
> unexamined. The purge design covers the copy I built and forgets the copy I sent, which is a
> distinction a builder is poorly placed to notice and an auditor spots immediately.

---

## Part 2 — His position, recorded before reading my report

Transcribed from Ugo's self-audit, commit `1e3b7a8`, 19 August 2026.

**Lawful basis for the primary purpose (researching a client company):**
> **Article 6(1)(f), legitimate interests**, with a written three-part LIA. The interest is that a
> compliance adviser cannot apply the AI Act without knowing which systems a client runs. The LIA
> concludes that the basis holds **for reading and quoting public sources** but **failed on the
> necessity limb as the system was then built**, because whole fetched pages were stored when the
> evidence gate only ever needed the validated passage. Recorded as "LI available in principle, not
> satisfied in practice".

**DPIA conclusion:**
> **Threshold crossed, full DPIA not asserted.** Three EDPB criteria apply — innovative technology,
> matching or combining datasets, and cross-border transfer where undocumented transfers impede
> rights. That crosses the usual two-criteria threshold, but since no individual is assessed I stopped
> short of asserting a mandatory DPIA and required instead that the **Article 35(1) threshold
> assessment be performed and recorded**, flagged `TBD — legal review`.

**Top three findings from his own self-audit:**
> 1. Whole fetched pages were stored, embedded, in a US vector database with **no deletion path of
>    any kind** — while the project's own proposal claimed no personal data was recorded. Policy
>    without a control.
> 2. **No Article 28 agreements and no transfer mechanism** for OpenAI or Pinecone.
> 3. **Accountability: 2 of 13** expected documents exist, and both were built for accuracy rather
>    than compliance — everything present asks whether the output is *true*, everything absent asks
>    whether the processing is *lawful*.

**One change since:** finding 1 is **fixed**. Commit `3eee7f6` (19 August) stores only gate-validated
passages, adds `delete_namespace` and `purge_scan`, and purges before every live scan. The proposal's
ethics section now states what is stored and which function enforces it. His Q5 shows the fix stops
at the boundary of what he controls — the delivered report is still outside it.

---

## Part 3 — After reading Vittal's report

**His response.** Accurate throughout, and two of your findings land somewhere my own audit did not
reach. Three pieces of context you could not have had from the repository:

*On Finding 1 and the LIA.* You marked lawful basis "cannot determine from brief — no LIA appears
anywhere". A written three-part LIA does exist, and it concludes the necessity limb **fails**. But it
exists in a **lab submission**, not in the project repository, so from where you were standing it may
as well not exist. That is a finding about me rather than about you: compliance reasoning stored
where an auditor will never look is indistinguishable from compliance reasoning never done. It
belongs in `docs/`, and I will move it.

*On the whole-page storage problem — the biggest finding in my own audit, and invisible to you.* Until
19 August the system chunked and embedded **whole fetched pages**, with no deletion path anywhere in
`store.py`. You audited a repository where that had already been fixed the same day (commit
`3eee7f6`): validated passages only, plus `delete_namespace` and `purge_scan`, purging before every
live scan. You then correctly identified the *residue* of that fix — Finding 4, that the purge covers
the research store but not the delivered report. You found the edge of a boundary whose existence you
could not see, which is a better result than finding the original defect would have been.

*On Finding 2, Notion.* You are right that it is unflagged, and the distinction you draw — that an
unflagged gap is harder to close than a flagged one — is the sharpest sentence in your report. My
proposal's §9 names OpenAI and Pinecone and stops. My own audit did list Notion as a processor
needing a DPA, but again in the lab document, not in the project's own admission. Same failure mode
as the LIA.

**If our lawful-basis choices differ, which is stronger?**
> They do not differ in substance — we both land on Article 6(1)(f). The difference is evidentiary:
> you could not verify an LIA you could not see. Yours is the stronger *audit position* on the
> material available, and mine is the stronger *conclusion* now that the LIA is on the table. The
> resolution is not that either of us was wrong; it is that the document has to move.

**If our DPIA conclusions differ, which EDPB criteria do we read differently?**
> **This is our real divergence, and I now think you are more right than I am.** I concluded that
> three criteria apply today — innovative technology, matching/combining datasets, and cross-border
> transfer with no documented mechanism — crossing the two-criteria threshold, and required that the
> Article 35(1) threshold assessment be recorded. You count **two** today, rejecting systematic
> monitoring and large-scale processing at prototype scale, and hold that a DPIA becomes a
> precondition for **GTM sprint 2's scheduled re-scans** rather than sprint 1.
>
> Where you are stronger: the **systematic monitoring** criterion applied to *scheduled re-scans* is
> a reading neither my self-audit nor my count contained. Repeated, automated research about the same
> companies over time, naming the same individuals repeatedly, is a materially different processing
> activity from a one-off scan, and it is the point at which the criterion genuinely bites. Tying the
> DPIA to that trigger is better calibrated than my flat "threshold crossed today".
>
> Where I would hold: "matching or combining datasets" does apply now — search, news, registry and
> vendor sources are joined per company — so I read three rather than two. And regardless of the
> count, the Article 35(1) **decision should be written down now**, which your own recommendation
> ("worth a documented decision") already concedes. **Agreed position: record the threshold
> assessment now, with the DPIA itself gated on sprint 2's scheduled sweeps.**

**What did his self-audit catch that mine did not, and what did mine catch that his did not?**
> *His that mine did not reach:* **Article 14** — the data is not obtained from the data subject, so
> the information duty applies and the disproportionate-effort exemption has to be reasoned rather
> than assumed; **Article 9 by inference**, where a page about a diversity programme or a health
> matter is ingested exactly like any other; and the **accountability count** — 2 of 13 expected
> documents exist, and both were built for accuracy rather than lawfulness.
>
> *Mine that his did not:* **the `notes` field** (my Finding 5, Ugo's Q1 answer above) — he
> inventoried the research pipeline and never looked at the adviser's own client list beside it; and
> **erasure of the delivered report** (my Finding 4) — he recorded Notion retention as "indefinite
> once filed" and filed it under storage limitation, never connecting it to the right that would
> actually be exercised against it. Both are the same shape: he audited the part of the system he
> finds interesting, and stopped at its edges.

---

## Part 4 — Joint closing note (Ugo's half, as sent)

> The hardest gaps to catch in your own work are not the ones you do not know about — they are the
> ones you have already thought about *somewhere else*. My LIA existed, my Notion processor
> assessment existed, and my retention entry for filed reports existed; none of them was where an
> auditor would look, so all three read as absent, and absent is what they effectively were. The
> second pattern is scope: a builder audits the system he finds interesting and stops at its
> boundary, which is why I inventoried an embedding pipeline in detail and never opened the client
> record sitting next to it, and why my purge logic covers the copy I built and forgets the copy I
> sent.

Final agreed version, combining both halves: [`../debrief-ai-prescan.md`](../debrief-ai-prescan.md).
