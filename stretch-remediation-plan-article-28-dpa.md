# Stretch — remediation plan for Finding 1 (no Article 28 agreement)

Taking the blocking finding that gates all the others. The DPIA cannot conclude, the transfer
mechanisms cannot be flowed down, and the customer-notice problem cannot be solved for subscribers
until the processor relationship is on paper. Fix this one and three others become tractable.

**The artifact that closes it.** An **Article 28(3) data processing agreement** between Whizbiz (as
processor) and each subscribing solopreneur (as controller), executed as part of subscription
sign-up rather than as a separate negotiation — a solo baker will not run a contract review, so it
has to be accept-at-checkout to be real. It needs four annexes, and the annexes are where the work
actually is:

- **Annex A — processing description:** categories of data subject (the owner, and *their customers*),
  categories of data, purposes, and duration. Writing this honestly is what forces the third-party
  customer question into the open.
- **Annex B — sub-processor list:** OpenAI, Google, the production n8n host, each with location and
  transfer mechanism, plus a plain statement of **Telegram's position** — an independent controller
  that cannot be brought under Article 28, disclosed rather than papered over.
- **Annex C — technical and organisational measures** under Article 32: hosting, access control,
  encryption, execution-log retention.
- **Annex D — assistance with data subject rights**, specifying how Whizbiz helps a controller answer
  access, rectification and erasure — including for the customers named on invoices, which is
  currently impossible and is the clause that will drive a product change.

**Who owns it.** External counsel drafts, because a templated DPA that misdescribes the processing is
worse than none. The **builder** owns Annexes A–C, since only he can state what is actually
processed and where. If a Whizbiz company is incorporated, it signs as processor; until then there is
no entity to sign, which makes **incorporation a dependency of the compliance work**, not a separate
commercial track.

**Realistic timeline.** Two to three weeks: three or four days for the builder to draft the annexes
from the workflow, one to two weeks for counsel to draft and review, a few days to wire acceptance
into sign-up. It runs in parallel with the DPIA, which will feed Annex C — but the DPA must be
executed **before the first paying subscriber**, not before general availability.

**Evidence that would satisfy a regulator.** A countersigned DPA per subscriber, retrievable on
demand; the sub-processor annex with each transfer mechanism attached (DPF certification numbers or
signed SCCs plus the transfer impact assessment); a change log proving subscribers were notified of
sub-processor changes as Article 28(2) requires; and a worked example of a rights request handled
end-to-end under Annex D. The last is the one a regulator will actually test, because it is the only
piece that cannot be produced retrospectively.
