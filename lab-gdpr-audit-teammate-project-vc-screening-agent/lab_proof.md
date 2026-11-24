# lab_proof — Audit your teammate's project, GDPR lens (VC startup-screening agent)

**Entry point for the reviewer.** Read in this order:
1. [`brief_annotations_and_gaps_vc_screening.md`](brief_annotations_and_gaps_vc_screening.md) — Phase 1
2. [`personal_data_and_role_map_vc_screening.md`](personal_data_and_role_map_vc_screening.md) — Phase 2
3. [`clarifying_questions_log_vc_screening.md`](clarifying_questions_log_vc_screening.md) — Phase 3, five questions: Q1 to send with our brief; Q2–Q5 for the debrief
4. [`gdpr_audit_report_vc_screening.md`](gdpr_audit_report_vc_screening.md) — Phase 4, two pages, six sections
5. [`debrief_and_joint_closing_note.md`](debrief_and_joint_closing_note.md) — Phase 5, **not held; joint note blank**

## 1. Code or workflow export

**NOT APPLICABLE — documentary audit.**
- The teammate's code was not shared, and the lab only requires her brief.
- No workflow of mine exists to export.
- The only code here is a read-only documentary check: [`proof/source_fact_check.py`](proof/source_fact_check.py).

## 2. One query actually run

- **Date:** 17 Nov 2026, ~17:20 CET.
- **Where:** the tutor's (Claude's) sandbox.
- **Input:**
  - the teammate's `System_Brief_VC_Startup_Screening_Agent_Companera.docx` (324 words), converted with `markitdown`. SHA‑256 of the file: `c288d926…1d27d1ef`;
  - term list [`proof/terms_lab3.txt`](proof/terms_lab3.txt).
- **Command:** `python -I source_fact_check.py <brief.md> - terms_lab3.txt`

**Evidence produced** ([`proof/lab3_fact_check.txt`](proof/lab3_fact_check.txt), corrected run):

```text
chars_in_scope 1983 words_in_scope 324
FOUND     Tavily (2)
FOUND     Jina Reader (1)
FOUND     GDELT (1)
FOUND     OpenAI model (1)
FOUND     local criteria file (1)
FOUND     founders names / personal data mentioned (3)
FOUND     personal data sent to model unverified (1)
FOUND     human decision by analyst (1)
FOUND     no automatic invitations / decisions (1)
NOT FOUND retention period (0)
NOT FOUND data location / region / EU (0)
NOT FOUND DPA / contract (0)
NOT FOUND lawful basis (0)
NOT FOUND privacy notice / informing founders (0)
```

## 3. Final output (how the evidence was used)

- **FOUND** items feed the system summary and the role map as **declared** facts [D].
- The five **NOT FOUND** items became:
  - the "brief silences" list;
  - Findings 1–4 and 6;
  - the "Gap identified" / "Cannot determine" entries in the checklist.

  They are treated as **documentation gaps, not proven infringements**.
- "Personal data sent to model unverified" is the builder's own admission. It is the basis for Q2 and for the condition that would make Finding 1 Blocking.
- **Recommendation:** Proceed with conditions. Report length checked by rendering to PDF (see the README).

## 4. Failure or limitation hit

1. **Real failure in the check.** In the first run, "privacy notice / informing founders" came back **FOUND (2)**. That was a false positive: the pattern `inform` matched the word "information" ("collects public information", "conflicting information"). I fixed it with word boundaries and re-ran; the corrected result is above. "data location / region / EU" was hardened the same way.
2. **The input document arrived late.** The first pass used her AI Act System Brief. Her GDPR data processing brief arrived afterwards, inside her Q&A document, and the report was updated. One provisional assumption was wrong: Q4 assumed analysts only, but the test reports are public on GitHub.
3. **Nothing verified against her system.** I have not seen her code, the Kalipso/Lawra reports or any contracts.
4. **Missing official source.** `01_gdpr-fundamentals.md` was not available and has not been read.
5. **Steps not done:** debrief steps 4 (DPIA comparison) and 5 (gap comparison) were not held. On 24 Nov 2026 the instructor said they were not required (reported by Jaime). The comparison therefore shows only my side; Sandra's DPIA conclusion and her self-audit gaps are not recorded. The joint closing note is done.

## 6. Second evidence run — code check of the builder's repository (18 Nov 2026)

- **Input:** public repo `https://github.com/Sobregonm/project3-vc-screening`, commit `84afd71` (12 Nov 2026). Shared by Sandra on 18 Nov as optional technical documentation.
- **Checks:**
  - read the service calls in `tavily_search.py`, `headquarters_extractor.py`, `jina_reader.py`, `gdelt_news.py` and `main.py`;
  - ran a Python regex scan for two-word capitalised names in `reports/*.md`.
- **Output:**
  - OpenAI receives the startup name + Tavily snippets (≤ 3,000 characters each) only;
  - Jina and GDELT text is not sent to the model;
  - no person names in the public reports (heuristic: only phrases such as "Seed Round" and "Latin America" matched).
- **Effect:** F1 lowered to Minor; F2 stays Significant with the DPA status **pending verification** (as Sandra asked).
- **Limitation:** the name scan is a heuristic. A single-word name or a lowercase mention would not be caught.
