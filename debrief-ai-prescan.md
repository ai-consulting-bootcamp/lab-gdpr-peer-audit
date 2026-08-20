# Phase 5 — Debrief: AI Pre-Scan

**Auditor:** Vittal Navale · **Builder:** Ugo Ahukannah · **Run as:** a document round-trip, not a
live meeting — each step below still follows the sequence `instructions.md` specifies.

Run independently before this point: my audit — [`gdpr-audit-report-ai-prescan.md`](./gdpr-audit-report-ai-prescan.md)
and [`clarifying-questions-log.md`](./clarifying-questions-log.md) — and Ugo's own self-audit of AI
Pre-Scan (commit `1e3b7a8`, 19 August 2026, not seen by me before writing my report). Ugo's full
returned response, unedited: [`from-ugo/response-to-vittals-gdpr-audit.md`](./from-ugo/response-to-vittals-gdpr-audit.md).

---

## 1. Auditor presents

My report concluded **proceed with conditions**, with two Blocking findings: no processor
agreement or transfer mechanism for OpenAI/Pinecone (Finding 1), and the same gap for Notion, which
is not even named as a known issue anywhere in the repository (Finding 2). Full findings 1–6 in
[`gdpr-audit-report-ai-prescan.md`](./gdpr-audit-report-ai-prescan.md#section-3-compliance-findings).

## 2. Builder responds

Ugo's response confirmed every one of my five clarifying-question assumptions as correct (the
`notes` field would hold personal data in practice; the hosting model is genuinely undecided; no
retention schedule exists for the local job store; the OpenAI/Pinecone/Notion transfer gap has no
owner or date; a Notion-filed report has no erasure path). He also supplied context I could not have
had from the repository alone:

- A written three-part LIA **does exist** for the primary processing purpose — but it lives in a lab
  submission, not the project repository, so it was invisible to an audit built from the repo. His
  own framing: *"compliance reasoning stored where an auditor will never look is indistinguishable
  from compliance reasoning never done."*
- The whole-page storage defect his own self-audit found as its top finding was **already fixed**
  (commit `3eee7f6`, 19 August) before I audited — I was auditing a repository where only the
  *residue* of that fix remained, which is what became my Finding 4 (the delivered-report erasure
  gap).
- His own audit had already identified Notion as a processor needing a DPA, again only in the lab
  document rather than in the project's own admission — the same failure mode as the LIA.

## 3. Compare lawful basis selections

**Same basis, different evidentiary position.** Both of us independently landed on **Article
6(1)(f), legitimate interests**, for the primary research purpose. My report marked it "cannot
determine from brief — no LIA appears anywhere," which was accurate given what the repository showed.
Ugo's self-audit contains the full three-part LIA, and its own conclusion is sharper than a plain
"basis applies": the interest is legitimate and the processing is necessary *for reading and quoting
public sources*, but the LIA's necessity limb **failed** against the system as it stood before 19
August, because whole pages were being stored when the evidence gate only ever needed the validated
passage. **Agreed:** neither of us was wrong — the LIA needs to move from the lab submission into
`docs/` so it is where an audit would actually find it.

## 4. Compare DPIA conclusions

Both concluded a DPIA is not yet mandatory but the position needs to be recorded, not left implicit —
that much agreed immediately. Where we differed: Ugo counted **three** EDPB criteria applying today
(innovative technology, matching/combining datasets, cross-border transfer without a documented
mechanism) and required an Article 35(1) threshold assessment to be written down now. I counted
**two**, excluding matching/combining datasets at the prototype's current scale, and tied the DPIA
itself to **GTM sprint 2's scheduled re-scans** rather than sprint 1.

**Resolution reached:** Ugo conceded my systematic-monitoring framing is better calibrated than his
flat "threshold crossed today" — repeated, scheduled research about the same companies over time,
potentially naming the same individuals repeatedly, is what actually triggers that criterion, not a
single scan. I conceded his read on matching/combining datasets: search, news, registry and vendor
sources are already joined per company today, not just at sprint 2. **Agreed position:** record the
Article 35(1) threshold assessment now, three criteria noted as applying, with the DPIA itself gated
on sprint 2's scheduled sweeps rather than sprint 1's pilot.

## 5. Compare gap lists

**What Ugo's self-audit caught that my external audit missed:** Article 14 (data not obtained from
the data subject, so the information duty applies and the disproportionate-effort exemption needs
active reasoning, not assumption); Article 9 by inference (a page about a health matter or a
diversity programme is ingested identically to any other page, with nothing that would catch it);
and the accountability count — 2 of 13 expected regulator-facing documents exist, and both were built
to prove the output is *true*, not that the processing is *lawful*. None of these were visible from
outside the repository.

**What my external audit caught that Ugo's self-audit missed:** the `notes` field on a client record
(Finding 5) — his self-audit inventoried the research pipeline in detail and never looked at the
adviser's own client list sitting beside it; and erasure of the delivered report (Finding 4) — his
self-audit recorded Notion retention as "indefinite once filed" but filed it under storage
limitation, never connecting it to the erasure right that would actually be exercised against it.

## 6. Joint closing note

**Agreed final version:**
> The hardest gaps to catch in your own work are not the ones you never considered — they are the
> ones you already reasoned through *somewhere an auditor will never look* (a lab submission, a
> private note), so they read as absent even though the thinking exists; and the ones just past the
> edge of the part of the system you find interesting, where a builder's attention naturally stops at
> the boundary of what he built rather than the boundary of what he's responsible for. An external
> audit that works from the repository alone catches both reliably, precisely because it has no
> access to reasoning that lives outside it and no attachment to which corner of the system feels
> finished — it can only see what the project itself is willing to show, which is exactly the
> discipline that makes it useful.
