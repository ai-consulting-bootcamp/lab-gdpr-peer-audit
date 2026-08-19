# Reinforce — reflections on the GDPR peer audit

## 1. The clarifying questions logged about my own system

_Pending — completed once Vittal's questions about AI Pre-Scan arrive._

Written before seeing them, so the answer cannot be retrofitted: the questions I expect to fail are
**"what is your retention period"**, **"where is your record of processing activities"**, and
**"which transfer mechanism covers OpenAI and Pinecone"**. My own GDPR self-audit found that 2 of 13
expected accountability documents exist, so any question aimed at documentation rather than
behaviour will land on nothing. My project documentation answers *how the system works* in unusual
depth and *who is accountable for the data* not at all — which is a genre gap, not an effort gap.

## 2. A finding I initially disagreed with

_Pending the debrief._

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
