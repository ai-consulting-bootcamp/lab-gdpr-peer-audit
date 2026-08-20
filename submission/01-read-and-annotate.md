# Phase 1 — Read and Annotate

*First read: Anand's data processing brief was read once through without notes. Second-pass annotations below.*

## Personal Data Categories Marked (special-category status noted)

- **Telegram/WhatsApp chat identifiers** — correctly cited by the brief itself as an online identifier under Art. 4(1). No special-category status.
- **Order content linked to an identifiable sender** (school name, class, book list) — ordinary personal data, no special-category status.
- **Incidental content in photo-based orders** — the brief itself flags this as a residual, non-zero special-category risk (handwriting could incidentally reveal names, phone numbers, or other content beyond the book list). Marked as the one category where special-category inference is honestly acknowledged as possible, not ruled out.

## Elements Circled as Unclear

- Exact processing region for OpenAI API calls and Google Workspace/Sheets tenancy — explicitly self-flagged as an open item in the brief.
- Whether "no shared backend" between the India and Germany deployments means logically separate (same vendor account, different data) or physically/contractually separate (different vendor accounts entirely) — the brief asserts separation but doesn't specify the mechanism.
- Whether the "mark fulfilled" step is human-reviewed or auto-runs — explicitly self-flagged as an open item.
- Anand's own ongoing role (processor with continued access, or handed off entirely) — not addressed anywhere in the brief.

## Elements Suggesting an EU Border Crossing or Non-EU Vendor

- The entire **Germany deployment section**, underlined as the single most consequential element in the brief — this is what will bring the system within GDPR's territorial scope, independent of how the India deployment is assessed.
- **OpenAI** as processor — US-headquartered, region unconfirmed.
- **Google Sheets/Workspace** — same, US-headquartered parent, region unconfirmed.

## Elements Flagged as a Potentially Incompatible Purpose

- **Purpose (e) — conversational Q&A over historical order data** — the brief flags this itself as not part of the original design, with historical data (collected for purposes a-d) now being queried for a use case that wasn't contemplated at collection time. This is the single strongest finding in the brief, and notably self-identified by the builder rather than requiring external discovery.

These annotations directly informed the Phase 2 data/role map and the five clarifying questions logged in Phase 3.
