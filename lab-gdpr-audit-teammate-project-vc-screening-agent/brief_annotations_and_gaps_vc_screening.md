# Phase 1 — Read and annotate · VC startup-screening agent (teammate's Project 3)

## What I actually received

| Expected by the lab | Received | Consequence |
|---|---|---|
| Teammate's **GDPR data processing brief**, one page, from her self-audit | **Received after the first pass**, in her document *GDPR Questions and Answers for the VC Screening Agent* (section 1) | The first pass below was done on the AI Act brief. The report was then **updated** with her GDPR brief and answers |
| Architecture or data-flow diagrams (optional) | Not received | — |
| — | Her **AI Act System Brief** (324 words), written for the previous lab | Used as the only source. It describes the system, but it was **not written to answer GDPR questions** |

**Independence:** I have not seen her self-audit, lawful-basis choices, DPIA view, memo or code. Everything below rests on **declared** facts [D] from that brief, plus my own assumptions [A]. **Nothing has been verified against her code or runs.**

**Tags:** **[D]** declared in her brief · **[A]** my inference or assumption · **[NC]** not covered by the brief · **[V]** checked by me in the brief's text or in an official source.

## Annotations

Marks used:
- **[PD]** personal-data category (plus special-category note);
- **[?]** unclear, must confirm;
- **[X-BORDER]** a non-EU vendor or possible transfer;
- **[PURPOSE]** possible incompatibility with the original collection purpose.

| # | Brief statement (paraphrased) | Mark | Note |
|---|---|---|---|
| 1 | Analyst enters a startup's name and official website [D] | — | Company data. The analyst's own use data is minimal |
| 2 | System collects public information and prepares an internal report to help decide on a first meeting [D] | [PURPOSE] | The purpose is clear and narrow. Original sources were published for other purposes (press, company marketing). Reuse for investor screening is plausibly compatible, but not assessed |
| 3 | **Tavily** finds public sources [D] | [X-BORDER] [PD] | US company (AlphaAI Technologies Inc.) [V: Tavily privacy policy]. Search results can contain founders' and employees' names |
| 4 | **Jina Reader** reads the company's website [D] | [PD] [?] [X-BORDER?] | Websites often have **team pages**: names, photos, bios, LinkedIn. Is the full text kept? Where does Jina process it? [NC] |
| 5 | **GDELT** looks for recent news [D] | [PD] [?] | News can name people. **Art. 10** risk: litigation, fraud or criminal allegations about founders. In the saved Lawra test, the news search failed [D] |
| 6 | Fund criteria come from a local file [D] | [?] | Are the criteria about the company only, or also about founders (experience, track record)? This decides whether people are evaluated |
| 7 | **OpenAI** receives the company name and short Tavily extracts, looking for HQ location and funding stage [D] | [PD] [X-BORDER] | US provider. EU data residency exists for eligible API projects [V: OpenAI]. Which region and account? [NC] |
| 8 | "Public sources may contain personal data, such as founders' names"; whether the saved test sent personal data to the model **remains unverified** [D] | [PD] [?] | The builder flags this uncertainty herself. It is good practice, but it is still an open gap |
| 9 | Quotes returned by the model are checked against the extracts [D] | — | An accuracy control (Art. 5(1)(d)). It is not a privacy control |
| 10 | Report saves findings, source links and questions; marks criteria "Meets / Does not meet / Not verified" [D] | [PD?] [?] | Where are reports stored, for how long, and who sees them? [NC] |
| 11 | Users are analysts and associates; startups may be affected [D] | [?] | Startups are legal persons; GDPR protects **natural persons**: founders and staff |
| 12 | Analyst checks sources and makes the final meeting decision; the system sends no invitations and makes no investment decisions [D] | — | Points away from Art. 22, if true in practice |
| 13 | Tested with two real startups (Kalipso, Lawra); a pilot is a future step [D] | [PD] | The tests may already have processed real founders' data |

## Brief silences (gaps)

The brief does not cover:
- lawful basis;
- controller/processor roles;
- DPAs;
- hosting regions and transfer mechanism;
- retention;
- access controls;
- information to founders (Art. 14);
- rights handling;
- DPIA view [V: my keyword check found none of these terms; see `lab_proof.md`].

This is expected: it is an AI Act brief. These silences are **documentation gaps, not proven non-compliance**.

## Described system vs verified processing

| Aspect | Described [D] | Verified by me |
|---|---|---|
| Tools in use | Tavily, Jina, GDELT, OpenAI, local criteria | **No.** Code not seen |
| Data sent to OpenAI | Name + short Tavily extracts | **No.** The builder herself says it is unverified |
| Human decision | Analyst decides | **No.** Workflow described, not observed |
| Tests | Kalipso, Lawra | **No.** Reports not seen |

## Facts Sandra already declared in the AI Act peer-audit exchange (17 Nov 2026)

These come from her written answers to my AI Act clarifying questions, not from a GDPR brief. They are tagged [D] and used here:
- The model is **GPT-4o mini** (OpenAI).
- **Website text read by Jina is labelled as the company's own description and is not sent to the model.**
- Criterion statuses are assigned by **Python rules**, not by the model.
- Startups are **never rejected automatically**.
- **No API plan, access rule or retention rule** has been decided yet.
- The system screens **companies only**: no loans, no individuals.

Effect on this audit:
- Annotation 4: the Jina → OpenAI flow is closed, but Jina itself still processes team pages.
- Annotation 7: the model is known; the plan and region are still open.
- Annotation 10: retention is confirmed as **not decided** (a gap, not just "not stated").

## Update after receiving her GDPR data processing brief (18 Nov 2026)

| Brief statement (paraphrased) | Mark | Note |
|---|---|---|
| Tavily receives the startup name **and domain**; returns titles, links, excerpts | [PD] [X-BORDER] | Names may appear in excerpts |
| Jina Reader receives the website URL; its text describes the company and is **not sent to OpenAI** | [PD?] | Team pages may still be read and stored locally |
| GDELT receives the startup name; returns titles, links, dates | [PD?] | Article 10 risk if news covers allegations |
| OpenAI receives the name, source links and Tavily excerpts; signed in with **Gmail**; plan, region and DPA unverified | [PD] [X-BORDER] | A Gmail sign-in does not show an organisation account with a DPA |
| Reports saved locally; **Kalipso and Lawra reports public on GitHub** | [PURPOSE] | A publication purpose that is not part of screening |
| Locations, retention and transfer safeguards unverified | [?] | Stated by the builder herself |

**Described vs verified:** still declared only. No code, API log or contract was seen.
