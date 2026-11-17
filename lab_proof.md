# Lab proof — independent GDPR audit of a teammate's Project 3

**Reviewer** Sean Langsdorf · **Teammate** Jędrzej Czarnota · **Project** Mobile Game Competitor Snapshot mk.III

**Status** Independent review, technical proof and a written comparison with the builder's published self-audit are included. No live debrief, reciprocal CompanyScope review or joint sign-off is claimed.

## Audit source and separation of evidence

The [brief on the teammate's GDPR self-audit branch](https://github.com/jedrzejczarnota-source/lab-gdpr-self-audit/blob/eff19e436f8a6a7f7b019a2ab846a8e4c1355d9c/01_project3_system_brief.md) is the only source for the [Phase 1 and 2 annotations and maps](mobile-game-brief-annotations-and-role-map.md). The independent report was completed without the teammate's self-audit findings. The builder's self-audit was consulted afterward, only for the written comparison. For technical verification only, the audit queried a redacted excerpt of the [workflow at the same commit](https://github.com/jedrzejczarnota-source/lab-gdpr-self-audit/blob/eff19e436f8a6a7f7b019a2ab846a8e4c1355d9c/Mobile%20Game%20Competitor%20Snapshot%20mk.III.json). See [PR #24](https://github.com/ai-consulting-bootcamp/lab-gdpr-self-audit/pull/24) for source provenance.

## Reproduce one offline configuration query

From the lab repository root, run with Python 3 and no packages or network access.

```bash
python3 check-mobile-game-workflow.py mobile-game-workflow-audit-input.json
```

- **Code:** [check-mobile-game-workflow.py](check-mobile-game-workflow.py) checks the namespace wiring and report delivery path without executing n8n or running any integrations.
- **Input:** [Redacted workflow projection](mobile-game-workflow-audit-input.json) records the pinned source SHA-256, write/read parameters, relevant graph edges and the form-recipient expression, with the fallback address removed. No credentials, reports or uploaded PDFs are included.
- **Observed evidence:** [Captured JSON result](mobile-game-workflow-audit-evidence.json) shows a fixed custom namespace on a shared index, an option to clear that namespace on insert, an agent-to-mail route, and a fixed mailbox fallback. The checker returned `HOLD_LIVE_CUSTOM_UPLOADS_AND_DELIVERY` and made zero external requests.
- **Limitation:** Static analysis does not establish that this export is deployed, that executions overlapped, that an invalid address reached Gmail, or that anyone's report was disclosed. The findings are configuration risks, not confirmed incidents.
- **Final output:** [Independent audit report](mobile-game-gdpr-peer-audit-report.md) recommends holding live use of the reviewed hosted configuration. It is supported by the [questions and DPIA screen](mobile-game-gdpr-clarifying-questions.md), [remediation plan](mobile-game-isolation-remediation.md) and [written comparison and individual closing reflection](mobile-game-gdpr-debrief-record.md).

## Legal references

- [GDPR Arts. 5–6, 9, 12–22, 25, 28, 32–36 and 44–46](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02016R0679-20160504)
- [EDPB Guidelines 1/2024 on legitimate interests](https://www.edpb.europa.eu/system/files/2026-11/edpb_guidelines_202401_legitimateinterest_v2_en.pdf) and [EDPB-endorsed DPIA and automated-decision guidance](https://www.edpb.europa.eu/endorsed-wp29-guidelines_en)
- [EDPB Chapter V guidance](https://www.edpb.europa.eu/system/files/documents/2023-02/edpb_guidelines_05-2021_interplay_between_the_application_of_art3-chapter_v_of_the_gdpr_v2_en_0.pdf), [EU–US adequacy decision](https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj) and [EU transfer SCCs](https://eur-lex.europa.eu/eli/dec_impl/2021/914/oj)
