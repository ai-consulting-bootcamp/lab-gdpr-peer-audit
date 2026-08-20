# Phase 2: Personal Data and Role Map

## Personal Data Summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Chat identifiers (Telegram/WhatsApp online identifiers) | Schools, submitted directly via message | (a) parsing, (b) matching, (c) consolidation, (d) status replies, (e) Q&A | Depends on deployment — India deployment: no (India schools, presumably India-region processing, unconfirmed). Germany deployment: yes, once live, since this brings the processing within GDPR's territorial scope | No |
| Order content tied to an identifiable sender (school name, class, book list) | Schools, submitted directly | Same five purposes as above | Same as above | No |
| Incidental photo content (handwriting beyond the book list — possible names/phone numbers) | Schools, submitted directly via photo | Transiently processed during image parsing; not intentionally extracted or stored | Same as above | Not intentional, but the brief itself flags a low-but-nonzero residual risk — worth marking as "possible, not confirmed absent" rather than a clean no |

## Role Map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Client (the bookshop business — father, and separately, the prospective Germany operator) | Controller | Determines why and how order data is processed; operates the bot day-to-day | N/A (controller, not a processor relationship) |
| Builder (Anand) | Likely a processor, or joint controller with the business — genuinely unclear from the brief alone | Designed and built the system; unclear from the brief whether Anand has ongoing operational access to live data or purely delivered the system | **Cannot determine from brief** — flagged as Clarifying Question 1 below |
| OpenAI (GPT-4o / GPT-4o-mini) | Processor | Text and image parsing of order content, including any incidental personal data in photos | **Yes — needed**, and specifically needs to cover image-content processing, not just text, given the incidental-data risk the brief itself names |
| Google Sheets / Workspace | Processor | Catalogue and order storage — meaning chat identifiers and order content tied to a sender are stored here | **Yes — needed** |
| n8n | Processor | Workflow orchestration — passes data between Telegram/WhatsApp, OpenAI, and Sheets | **Yes — needed**, especially if using n8n's hosted/cloud offering rather than self-hosted |
| Telegram / WhatsApp | Processor (message transport) | Transport layer for all incoming/outgoing messages | **Yes — needed**, though these platforms' own terms may already provide a form of processor terms; needs confirming rather than assuming standard consumer terms are sufficient for business use |

## International Transfer Note

The brief's own logic is sound: **India-only processing of India-based schools is not currently an EU personal data transfer issue**, since no EU data subjects or EU territorial hook is engaged yet. The **Germany deployment is the trigger** — the moment it goes live, GDPR's territorial scope applies independently of India, and at that point:

- OpenAI's processing region needs confirming — if EU-region OpenAI infrastructure isn't specifically used, this becomes a live international transfer requiring Standard Contractual Clauses (SCCs) or another valid mechanism.
- Google Workspace/Sheets tenancy region needs the same confirmation.

**This matches exactly what the brief itself already flagged as an open item** — worth noting in your audit report as another self-identified gap, not one you're surfacing independently.
