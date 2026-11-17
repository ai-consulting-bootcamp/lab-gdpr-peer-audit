# Phase 1 · Annotated data processing brief: AI Use Case Identifier (Friedrich)

**Received:** 17 Nov 2026, 16:30, by message.

**Audit-trail note.** The lab specifies that only the data processing brief is exchanged. Friedrich sent his **full self-audit document**: brief, inventory, role map, lawful bases, DPIA view and memo. My audit is built on the brief section only (reproduced below). Because I had sight of his conclusions, my review is **not fully independent**. Where I reach a different view, I say so in the debrief prep (file 05).

**Annotation key**

| Mark | Meaning |
|---|---|
| **[PD]** | Personal data category |
| **[SC?]** | Special-category data possible or inferable |
| **(?)** | Unclear; I need to confirm before forming a view |
| **[EU→]** | Data flow crossing an EU border, or a non-EU vendor |
| **[PURPOSE!]** | Purpose that may be incompatible with the original collection purpose |

---

**What the system does.** An autonomous research agent (Python, LangGraph). It takes a company name and homepage URL, reads public sources about the company, derives a business model and process map, rates each process step against AI-opportunity frameworks, matches the best steps against a curated use-case library in a vector index, and writes a consulting brief with three AI use cases and discovery questions. A human consultant reads the brief; nothing is sent to the company automatically.

> (?) Who is the "consultant" and who runs the tool: Friedrich personally, a consultancy, or a client that commissions runs? This decides who the controller is.
> (?) "Substitution recommendations that bear on jobs": can a small team, and therefore identifiable employees, be singled out?

**Where the data comes from.**

1. **The company website:** home, About and careers pages, and individual job postings, fetched over HTTP.
   > [PD] About pages name founders and management. [PD] Job ads name contact persons with direct email or phone.
   > [SC?] Free text can mention works-council members (union membership) or health-related absences.
2. **Tavily web search** with three query types: news, job ads, and company registers (unternehmensregister.de, handelsregister.de, bundesanzeiger.de, **northdata**).
   > [PD] Register portals publish managing directors' and shareholders' names, often with **year of birth and place of residence**. [PD] News names executives and others.
   > [EU→] Tavily is non-EU.
   > [PURPOSE!] Register data is published for transparency in commercial dealings, and here it is reused to prepare a sales approach.
   > (?) Northdata is a commercial aggregator, not an official register. It's a different source with different terms.
3. **A curated internal library of use-case cards**, written in-house.
   > No personal data, as described.
4. **Optional command-line input:** contact name, contact email, city.
   > [PD] Directly identifying.
   > (?) Where do these contacts come from: an inbound request, a business card, or copied from a website?
   > [PURPOSE!] Joining lead details to a research profile turns company research into direct marketing.
   > (?) Why is the city needed?

**What it's used for.** Three purposes: (1) research the company to build a business model and process map; (2) generate the use-case brief; (3) capture a sales lead where the operator supplies contact details.

> [PURPOSE!] Purpose 3 is a separate processing activity from purposes 1–2 and needs its own basis.

**Who processes it.**
- The application, running locally from the command line.
- **OpenAI** for all text models, embeddings and the process-map image. [EU→] US-headquartered.
- **Tavily** for web search. [EU→] Non-EU.
- **Pinecone** for the vector index of the use-case library. [EU→] US-headquartered.

> (?) Does the Pinecone query carry company text, which could include names, or only abstract process-step labels?
> (?) Does the image prompt for the process map include names?

**Where it's stored and processed.**
- Local files in `outputs/<company>/`: `report.md`, `state.json`, `process-map.png` and, where contacts were given, `lead.json`.
- `outputs/` is excluded from version control.
- Provider processing location is "currently unverified".

> [PD] `state.json` holds all collected text, so every personal data category above.
> (?) Retention, and whether the local disk is encrypted, are not stated.
> [EU→] Provider regions are unverified.

**Does it decide anything about people?** Not about identified individuals. It rates process steps, a consultant reviews the brief, and any decision about people would be taken later by the client, outside the system.

> (?) Accepted provisionally. To check: whether the brief names individuals and how it reaches the client.

**The brief's own statement on personal data.** Personal data is processed in four places (operator contacts, register results, website and job-ad text, news). All four flow into the run state, are written to `state.json` and are sent to OpenAI as prompt content. The README says the opposite.

> [PD] Confirmed by the builder. The README statement is inaccurate.
