# GDPR peer audit — AI Pre-Scan

**System audited:** AI Pre-Scan — evidence-backed AI-system inventory tool for compliance advisers
**Built by:** Nnanyelugo (Ugo) Ahukannah · **Auditor:** Vittal Navale · **Date of audit:** 19 August 2026
**Basis:** Regulation (EU) 2016/679

**Materials received:** the public repository `nyelugo/PROJECT-AI-Pre-Scan` — README, `docs/architecture.md`,
`docs/proposal.md`, `LESSONS.md`, `stack_decision.md`, and the relevant source (`clients.py`,
`store_jobs.py`, `notify.py`, `config.py`, `schemas.py`). **A written data processing brief was not
received**, so this audit is built entirely from the repository; every point a brief would have
settled is recorded as a gap in [`clarifying-questions-log.md`](./clarifying-questions-log.md) rather
than filled in silently.

**Ground rules observed.** I have not seen Ugo's own self-audit of this system, his lawful-basis
selections, or his DPIA conclusion. `LESSONS.md` records that a prior GDPR self-audit "surfaced" the
missing-transfer-mechanism gap as a fact — that single sentence is repository documentation, not his
conclusions, and is treated here the same as any other repo evidence.

---

## Phase 1: Read and annotate

An external compliance adviser (the persona "Maria") enters a client company's name. The system
researches that company's public footprint — website, careers pages, product pages, vendor
changelogs, news coverage, company registries — and returns an evidence-backed inventory of AI
systems the company appears to run, plus a discussion list of questions public evidence cannot
settle. It explicitly makes no legal classification; a separate deterministic tool (the Future of
Life Institute's EU AI Act Compliance Checker) does that.

**The four annotations that drive this audit:**

1. **The stated research subject is the organisation, not any individual — and the project says so
   explicitly and correctly manages the gap between that claim and reality.** `docs/proposal.md`
   §9: *"Public sources still name people, so a quote may name someone; the claim here is
   minimisation and a bounded lifetime, not that personal data is impossible."* This is the right
   framing, and unusual to see stated this plainly — but it means the system **does** process
   personal data, incidentally, whenever quoted evidence names an individual (an executive quoted in
   a press release, a founder credited on a product page).
2. **A material role-mapping question turns on an implementation detail not yet built.** The current
   prototype has no accounts, no hosted backend, and reads keys from a shared bootcamp store — Maria
   runs it on her own machine. GTM sprint 1 describes "making it something Maria can open from her
   own office" as a future deployment step. Whether that becomes a hosted service (making the builder
   a processor) or stays adviser-self-hosted (leaving the builder outside the processing relationship
   entirely) is undecided, and changes which Article 28 obligations even apply.
3. **The retention design is genuinely stronger than a typical MVP, and still has an open edge.**
   Fetched pages are read in memory and never persisted; only evidence-gate-validated passages are
   stored, one vector each, purged before the *next* scan of that company. That is real, deliberate
   minimisation. But the **finished report**, once filed to Notion via the n8n delivery workflow, is
   outside that purge cycle entirely — nothing describes its retention or deletion path, and it is the
   one artefact most likely to contain a person's name verbatim.
4. **The transfer-mechanism gap is admitted in the repository itself**, not something this audit
   discovered: §9 states outright that "processor agreements and a transfer mechanism are not yet in
   place and are required before any real client use" for OpenAI and Pinecone. Notion (via n8n) carries
   the same gap but is not mentioned in that admission at all.

---

## Phase 2: Personal data and role map

**Personal data summary:**

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Individuals incidentally named in quoted public evidence (executives, spokespeople, credited staff) | Public web pages, news, vendor changelogs fetched during research | Evidence for an AI-system finding about the *company* | **Yes** — OpenAI (US, extraction/embeddings), Pinecone (US, per-scan store) | No, none identified in the materials reviewed — not designed for and not observed |
| Client company name, domain, adviser notes (`Client.notes`) | Typed by the adviser (Maria) into the client book | Tracking which companies to scan, when, and why | Local only, unless synced elsewhere (not specified) | No — but `notes` is free text and could incidentally hold a contact person's name (see clarifying Q1) |
| Finished report content (inventory + discussion list, including any quoted individual's name) | Assembled from validated evidence | Delivered to the adviser; filed to Notion for her records | **Yes** — Notion (via n8n), hosting region not stated | No |
| Search/news queries (company name only) | Sent to Serper, NewsAPI | Locate public footprint | Yes — to those providers, but the query itself carries no personal data | No |

**Transfer mechanisms.** Two transfers are named and acknowledged in the repository as unresolved —
OpenAI and Pinecone, both US, both stated to need a processor agreement and transfer mechanism
"before any real client use." A third, **Notion (reached via the n8n delivery workflow)**, carries
personal data too (any name inside the delivered report) and is not mentioned in that admission at
all — its hosting region and any DPA are simply not addressed anywhere in the materials reviewed.

**Role map:**

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| **Maria (the adviser)** | **Controller** — decides which companies to research, for her own advisory business purpose | Everything the tool does when she runs a scan | She is the controller, so no DPA is owed *to* her by herself — but she needs one from every processor below |
| **Nnanyelugo / AI Pre-Scan (builder)** | **Currently: software provider, not a processor** — the tool runs on Maria's own machine with no hosted backend under the builder's control. **This will likely change** if GTM sprint 1's "open from her own office" becomes a hosted service | Designs which sub-processors are used and how data flows to them, without currently operating infrastructure on Maria's behalf | **Not yet — but only because there is no service relationship yet.** Revisit immediately if hosting centralises (clarifying Q2) |
| **OpenAI** | Sub-processor (of Maria, once she is confirmed as controller) | Evidence extraction (`gpt-4o`), embeddings | **Yes — and repository confirms none exists.** Explicit gap, admitted in `docs/proposal.md` §9 |
| **Pinecone** | Sub-processor | Per-scan evidence store, vendor corpus (design-only, unpopulated) | **Yes — same admitted gap** |
| **Notion** (via n8n) | Sub-processor | Files the finished report, including any personal data it contains | **Yes — not addressed anywhere in the materials reviewed.** Not even flagged as a known gap, unlike OpenAI/Pinecone |
| **Serper / NewsAPI** | Vendor / processor of the *search query* (company name only) | Locates public footprint, surfaces news | Lower priority — the query itself carries no personal data, though returned results may |
| **GLEIF / Wikidata** | Keyless public registries | Legal entity resolution, official domain lookup | No — company-level public data only |

---

## Phase 3: Clarifying questions log

Full log with obligations and provisional assumptions: [`clarifying-questions-log.md`](./clarifying-questions-log.md).
Five questions, unanswered at time of writing: the practical use of the `notes` field, the future
hosting model (the single fact that decides whether a processor relationship exists at all), the
local job store's retention schedule, the timeline for the admitted OpenAI/Pinecone transfer gap, and
whether a filed Notion report has any erasure path once a person's name has shipped inside it.

---

## Phase 4: Audit report

### Section 1: System summary

AI Pre-Scan is a LangGraph-based research agent for compliance advisers. Given a client company's
name, it researches that company's public footprint, extracts candidate AI systems with quoted
evidence, and returns an inventory plus a list of questions requiring the client's own answer — never
a legal classification. It runs today as a local, no-accounts prototype on the adviser's own machine;
a secondary n8n workflow delivers the finished report into Notion. The stated research subject is the
company, not any individual, but the design documentation is honest that public evidence sometimes
names people, and treats minimisation and bounded storage lifetime as the mitigation rather than
claiming personal data is absent.

### Section 2: Data and role map

As set out in Phase 2. The two facts that shape everything below: the system's **research and
storage design is genuinely privacy-conscious by construction** — no page persistence, gated
minimisation, purge-before-rescan — which is materially better practice than the MVP baseline; and
the **role map is currently indeterminate** on the single most consequential fact (does the builder
ever host processing on an adviser's behalf), which this audit cannot resolve from the repository
alone.

### Section 3: Compliance findings

> **Finding 1 — No processor agreement or transfer mechanism for OpenAI or Pinecone, admitted in the
> repository itself**
> **Severity:** Blocking
> **Description:** `docs/proposal.md` §9 states plainly that these are "not yet in place and are
> required before any real client use." Both receive personal data whenever a quoted individual's
> name survives the evidence gate (OpenAI for extraction/embeddings, Pinecone for the per-scan
> store), and both are US-based. This is the same admission a self-audit would make — the difference
> is that nothing in the repository shows it has been scheduled or resolved.
> **Recommended action:** confirm OpenAI's and Pinecone's DPF certification status, or put SCCs plus
> a transfer impact assessment in place, before GTM sprint 1's adviser pilot begins.
> **Escalation needed?** Yes — legal counsel.

> **Finding 2 — Notion carries the same transfer/processor gap as OpenAI and Pinecone, but is not
> even named as a known issue**
> **Severity:** Blocking
> **Description:** The finished report — the one artefact most likely to contain a person's name
> verbatim — is filed to Notion via the n8n delivery workflow. Notion's hosting region and any
> processor agreement are absent from every document reviewed, including the section that candidly
> flags the OpenAI/Pinecone gap. An unflagged gap is harder to close than a flagged one.
> **Recommended action:** extend the same transfer-mechanism and DPA review already planned for
> OpenAI/Pinecone to Notion before any report is filed for a real client.
> **Escalation needed?** Yes.

> **Finding 3 — The role of the builder is undetermined, and it decides whether Findings 1–2 are the
> builder's obligation or solely the adviser's**
> **Severity:** Significant
> **Description:** Today, with no hosted backend and no accounts, the builder is closer to a software
> provider than a processor — Maria runs the tool herself. GTM sprint 1 describes a hosting step that
> would likely convert this into a genuine controller/processor relationship requiring an Article 28
> contract. This isn't a documentation gap so much as a design decision not yet made, but it should be
> made *before* Findings 1 and 2 are closed, since the answer changes who is responsible for closing
> them.
> **Recommended action:** decide the hosting model as part of GTM sprint 1 planning, and revisit the
> role map immediately once it is decided.
> **Escalation needed?** No — this is a product decision with legal consequences, not itself a legal
> question yet.

> **Finding 4 — No retention or deletion path for the finished report once filed to Notion**
> **Severity:** Significant
> **Description:** The Pinecone-side purge-before-next-scan design is a real strength, but it covers
> only the research store. The delivered report is a separate copy, outside that lifecycle, and
> nothing describes how long it lives in Notion or how a data subject named in it could have it
> removed.
> **Recommended action:** define a retention period for filed reports (e.g., tied to the adviser's own
> engagement lifecycle with that client) and confirm Notion supports page-level deletion on request.
> **Escalation needed?** No.

> **Finding 5 — The `notes` field on a client record is unstructured and adviser-controlled, with no
> minimisation guidance**
> **Severity:** Minor
> **Description:** `Client.notes` accepts free text. Nothing prevents — or discourages — an adviser
> from recording a contact person's name or details there, which would be personal data with no
> defined purpose, retention, or basis of its own.
> **Recommended action:** add a short inline note in the client-book UI discouraging personal
> identifiers in free text, or document the field as out-of-scope for personal data in adviser
> onboarding material.
> **Escalation needed?** No.

> **Finding 6 — DPIA not clearly required at current scale, but the position should be revisited
> before scaling**
> **Severity:** Minor
> **Description:** Applying the EDPB's nine criteria, two plausibly apply today — innovative
> technology (the LangGraph research loop with an in-loop evidence gate) and cross-border transfer
> without a documented mechanism (Findings 1–2). Systematic monitoring and large-scale processing do
> not clearly apply yet, given the prototype's scale (a 12-company evaluation, no production client
> list). That balance shifts once GTM sprint 2's scheduled sweeps across a real adviser's client list
> are live — repeated, systematic research about the same companies, potentially naming the same
> individuals repeatedly over time, reads differently under the "systematic monitoring" criterion.
> **Recommended action:** treat a DPIA as not yet required, but as a pre-condition for GTM sprint 2
> (scheduled re-scans), not sprint 1.
> **Escalation needed?** No — worth a documented decision, not immediate counsel time.

### Section 4: Specific GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | **Cannot determine from brief** | No brief and no documentation states one. Legitimate interests (Art 6(1)(f)) is the most plausible fit for Maria's research activity, but no LIA appears anywhere, and it has not been assessed for the incidental personal data specifically |
| Purpose limitation respected (no incompatible reuse) | **Appears met** | Every observed purpose — evidence extraction, inventory assembly, report delivery — matches the stated research purpose. No secondary use of any personal data was found |
| Data minimisation (only necessary data collected) | **Appears met, with one caveat** | The research/storage design (in-memory pages, gated passages only, purge-before-rescan) is a genuine minimisation strength. The caveat is the unstructured `notes` field (Finding 5) |
| Controller/processor roles mapped and DPAs in place | **Gap identified** | Roles are partly clear (Maria as controller) and partly undetermined (the builder's role — Finding 3); no DPA exists for any sub-processor (Findings 1–2) |
| International transfer mechanism documented | **Gap identified** | Admitted for OpenAI/Pinecone (Finding 1); unaddressed for Notion (Finding 2) |
| DPIA conducted if required | **Appears not yet required** | See Finding 6 — revisit before GTM sprint 2 |
| Article 22 safeguard in place if automated decisions affect people | **Appears met — not engaged** | The system explicitly makes no legal or risk determination about anyone, company or individual; findings are advisory inputs to a human adviser's own judgement |
| Privacy notice covers AI processing | **Gap identified** | Nothing in the repository addresses a privacy notice for Maria, her firm, or the (rare) individual who might be named in a report |
| Data subject rights can be operationalised within deadlines | **Cannot determine from brief** | The Pinecone-side deletion path (`store.delete_namespace`, `store.purge_scan`) is real, but only for the research store; the filed-report path (Finding 4) has no equivalent, and no one has been identified as the point of contact for such a request |

### Section 5: Overall recommendation

**Proceed with conditions.** No finding here rises to "cannot be operated at all" in the way a
completely absent processor relationship would — the prototype's actual personal-data footprint is
small, incidental, and genuinely better-minimised than most MVPs at this stage. But two Blocking
findings (Findings 1–2) must close before **any real client's company is scanned with `--live`
research and the report is filed anywhere**, because at that point personal data — however
incidental — is genuinely leaving the EEA with no documented mechanism, in one case (Notion) without
even being on the list of known gaps.

The system's own documentation deserves credit here: the OpenAI/Pinecone gap is stated candidly in
the proposal rather than glossed over, and the storage design (in-memory pages, purge-before-rescan)
reflects real engineering discipline around minimisation. The open items are what remains between a
well-designed prototype and a system a real adviser can point at a real client's name.

### Section 6: What this report is not

This report is not a legal opinion, not a DPIA, and not a certification. It is a first-pass external
review conducted without a written data processing brief and without answers to the Phase 3
questions. Nnanyelugo should engage legal counsel before relying on it for any compliance decision,
and every conclusion should be revisited once the answers to the clarifying-questions log are known —
particularly Q2, which decides whether Finding 3's role-mapping question resolves toward "processor"
or stays out of scope for the builder entirely.

---

## Phase 5: Debrief conversation

Run as a document round-trip — see [`debrief-ai-prescan.md`](./debrief-ai-prescan.md) for the full
six-step debrief, including Ugo's self-audit positions and the agreed joint closing note.
