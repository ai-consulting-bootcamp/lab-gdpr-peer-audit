# Reinforce — reflections on the GDPR peer audit

## 1. The clarifying questions logged about my own system

Five received. My prediction — that I would fail on retention, records of processing, and transfer
mechanisms — was right about the *shape* and wrong about the *worst* one.

| His question | Can my project documentation answer it? |
|---|---|
| Q1 — does the `notes` field hold a contact person's name? | **No.** And worse than unanswerable: I had never inventoried the field at all |
| Q2 — hosted backend or adviser self-hosting? | **Partially.** My self-audit records the fork; the project says nothing, and the decision is unmade |
| Q3 — retention schedule for the local job store? | **No.** Predicted. Exclusion from git is source-control hygiene, not a control |
| Q4 — transfer mechanism, and on what timeline? | **Half.** The gap is stated candidly in `docs/proposal.md` §9; the *timeline* is not, because there isn't one |
| Q5 — can a person named in a filed report have it removed? | **No.** My purge covers the research store and forgets the delivered artefact |

**What this says about my documentation, beyond the predicted genre gap.** Three of my answers were
"yes, but it lives in a lab submission rather than in the repository" — the LIA, the Notion processor
assessment, the retention entry for filed reports. **Compliance reasoning kept where an auditor will
not look is indistinguishable from compliance reasoning never done**, and an auditor is right to mark
it absent. That is a filing problem masquerading as a documentation gap, and it is more embarrassing
than simply not having done the work, because the work was done.

## 2. A finding I initially disagreed with

**His Finding 6 — that a DPIA is *not* required today, only before GTM sprint 2's scheduled re-scans.**

**Why I disagreed.** My self-audit counted three EDPB criteria — innovative technology, matching or
combining datasets, and cross-border transfer with no documented mechanism — crossing the
two-criteria threshold, and I required the Article 35(1) assessment be recorded now. He counts two,
rejecting systematic monitoring and large-scale processing at prototype scale, and gates the DPIA on
sprint 2. My instinct was that he had under-counted: "matching or combining datasets" plainly applies
when search, news, registry and vendor sources are joined per company, and a threshold that depends
on today's scale is a threshold that moves under you.

**Where I ended up, and it is mostly his way.** His reasoning contains a criterion mine never
touched: **scheduled re-scans are systematic monitoring**. Repeated automated research about the same
companies over time, naming the same individuals repeatedly, is a materially different processing
activity from a one-off scan — and it is precisely the point at which that criterion bites. My flat
"threshold crossed today" is less useful advice than his "here is the specific product milestone that
requires a DPIA", because mine tells a client to do paperwork and his tells them *when and why*.

**Where I still hold ground.** The dataset-combination criterion does apply today, so I read three
rather than two — and the Article 35(1) decision should be written down **now** regardless of which
count is right, which his own recommendation ("worth a documented decision") already concedes. The
agreed position we landed on is better than either original: record the threshold assessment now,
gate the DPIA itself on the scheduled-sweep milestone. Neither of us proposed that alone.

## 3. What this audit revealed about GDPR self-assessment, written before the debrief

Auditing Whizbiz surfaced something my own self-audit could not have taught me: **the gaps hardest to
see in your own work are the ones your design intent explains away.**

In my own system I discounted a whole-page evidence store because I knew it was never read back — my
knowledge of intent told me it was inert, when for data protection "collected and never used" is the
least defensible category of all. In Vittal's system the equivalent is the `Kunde` and `Addresse`
columns: obviously necessary for an invoice, and *because* they are obviously necessary, the fact
that they identify a person who never agreed to anything disappears from view. Necessity hides the
data subject. Neither of us would have caught our own instance; each of us caught the other's in
minutes.

The second thing is about regimes rather than people. The same system produced *proceed with
conditions* under the AI Act and *do not proceed* under GDPR. A builder self-assessing under one
framework — usually the one their project was pitched against — will get a defensible answer to the
wrong question, and nothing in the self-audit process would ever tell them so.
