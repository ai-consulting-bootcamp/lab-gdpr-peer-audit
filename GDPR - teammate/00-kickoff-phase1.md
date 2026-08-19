# Kick-off, Ground rules, Phase 1 — RegGuard-Mini
Auditor: Nelly Pourmehr. Builder: Kimia Asgari.

## Kick-off — what was exchanged
Only `data_processing_brief.md` was received from Kimia before the audit started. No findings, no lawful basis assessment, no DPIA analysis, and no compliance memo were seen at that point. `client_memo.md` (Kimia's self-audit memo) arrived later, for the debrief step only, after the audit report was already written.

No architecture or data flow diagrams were provided. Not required, but noted as absent.

## Ground rules — confirmation
- The audit was built independently. No discussion with Kimia before the debrief.
- Points that were unclear in the brief were logged in `01-clarifying-questions.md`, each with a stated provisional assumption.
- Gaps in the brief were noted directly in `02-data-role-map.md`, not filled in with guesses.

## Phase 1 — Read and annotate

### Personal data mentions
1. Designer identity (name) — tied to each session, for attribution and version tracking. Not special category.
2. Designer's typed questions — free text, sent to a commercial LLM for the reasoning layer. Not special category by design, but free text could incidentally include it.
3. Handoff recipient data — a colleague's name and address, entered by the designer, not submitted by the colleague. Not special category.

### Circled — unclear, needs confirmation
- LLM provider is not named.
- Storage location and hosting provider are not documented for any data category.
- No DPA status is stated for the LLM provider.
- No retention period is stated for typed questions or handoff data.

### Underlined — crosses EU border or involves a non-EU vendor
- Typed questions sent to a commercial LLM via API. Vendor and location unconfirmed. Treated as a likely cross-border flow until proven otherwise.
- Storage location for designer identity and handoff data. Unconfirmed, same treatment.

### Flagged — purpose incompatibility
- None identified. Each data use (attribution, Q&A, report delivery) matches a feature the designer actively used. No reuse for an unrelated purpose is described in the brief.
- Adjacent flag, not a purpose-incompatibility issue: the system generates confidence-scored assessments of a designer's work. This could read as employee monitoring depending on deployment jurisdiction. Tracked separately as Finding 4 in the audit report.

These annotations are the evidence base for `01-clarifying-questions.md`, `02-data-role-map.md`, and `03-audit-report.md`.
