# Clarifying questions log — AI Pre-Scan

**Auditor:** Vittal Navale · **Builder:** Nnanyelugo (Ugo) Ahukannah · **Date:** 19 August 2026

No written data processing brief was exchanged for this system before this audit began. Per the lab's
ground rules, this audit was built from the public repository
(`github.com/nyelugo/PROJECT-AI-Pre-Scan`) alone — README, `docs/architecture.md`,
`docs/proposal.md` (particularly section 9, "Ethics and data"), `LESSONS.md`, and the relevant
source files (`clients.py`, `store_jobs.py`, `notify.py`, `config.py`). Every point a brief would
have settled is recorded below as a question, with a provisional assumption stated in its absence,
rather than filled in silently.

---

**Q1 — In practice, does the adviser's free-text "notes" field on a client ever get used to record a
contact person's name or details?**
*Obligation this affects:* Data minimisation (Art. 5(1)(c)) and the role/personal-data-category
assessment generally — the `Client` model (`clients.py`) has no dedicated personal-data field, but
`notes: str = ""` is unstructured and adviser-controlled.
*Provisionally assuming:* it will be, in real use — a free-text field next to a company record is
exactly where "spoke to their CFO, prefers email" ends up. Treating this as a live personal-data
field rather than a theoretical one.

**Q2 — Once this moves past the current local/no-accounts prototype (GTM sprint 1: "making it
something Maria can open from her own office"), will Nnanyelugo host a backend that processes on
each adviser's behalf, or will each adviser self-host with their own API keys?**
*Obligation this affects:* Articles 4(7)/4(8) and 28 — this is the single fact that decides whether a
processor relationship (and therefore a DPA) exists at all between the builder and any adviser.
*Provisionally assuming:* a hosted backend is coming, since "deployment step" language and the
shared bootcamp key store (`~/.config/ironhack/.env.local`) both point toward centralised
infrastructure rather than each adviser managing her own OpenAI/Pinecone accounts.

**Q3 — Is there a retention or deletion schedule for the local job/scan store
(`store_jobs.py`), beyond it being excluded from version control?**
*Obligation this affects:* Articles 5(1)(e) storage limitation and 17 erasure — the store explicitly
says it "contains research about named companies," which can include quoted individuals, and nothing
in the code shows an expiry or deletion path for it.
*Provisionally assuming:* none exists yet — the exclusion from git is a source-control hygiene
decision, not a data-retention control.

**Q4 — Is a transfer mechanism (SCCs or DPF) or processor agreement planned for OpenAI, Pinecone, or
Notion before the GTM sprint 1 pilot, and on what timeline?**
*Obligation this affects:* Chapter V (international transfers) and Article 28 — `docs/proposal.md`
section 9 states outright that "processor agreements and a transfer mechanism are not yet in place
and are required before any real client use," which is unusually candid, but doesn't say when this
closes.
*Provisionally assuming:* not yet scheduled — the admission reads as an accurate flag of a known gap
rather than a tracked remediation item with a date.

**Q5 — When a named individual's public quote survives the evidence gate and ships in a finished
report filed to Notion, is there any process for that person to request its removal after the
Pinecone-side purge-before-next-scan cycle has already happened?**
*Obligation this affects:* Article 17 erasure — `store.purge_scan` deletes the Pinecone-side passage
before the *next* scan of that company, but the **finished report itself, once filed in Notion, is
outside that lifecycle entirely** and has no described retention or deletion path.
*Provisionally assuming:* no — the purge design covers the research store, not the delivered
artefact, and nothing in the architecture or delivery workflow addresses the Notion copy.
