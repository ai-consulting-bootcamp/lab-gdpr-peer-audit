# GDPR peer audit report

**Editorial Research Agent · Auditor Sandra Obregón**

## 1 System summary

The agent helps a bookseller find recent Spanish editions of books by an author or on a topic. It searches public sources, asks Gemini to help judge how well books fit the shop, and writes a dossier. The bookseller makes the final decision. The workflow handles author names and can also collect personal details in source excerpts.

## 2 Data and role map

Jaime likely controls the prototype. Vendor roles and transfer grounds are still unverified. Jaime reported that seven public run files included text revealing political information about an identifiable person. See the [data and role maps](audit_notes.md).

## 3 Compliance findings

| Finding | Severity | Description | Recommended action | Escalation needed |
|---|---|---|---|---|
| 1 Special category data and lawful basis | Blocking | Jaime reported political information in seven run files. The review has no documented Article 9 condition or basis for the public demo use. | Pause collection and public sharing of this material. Take down or redact affected evidence and assess any further use with counsel. | Yes, controller and legal counsel. |
| 2 Vendor roles and international transfers | Significant | The vendor roles, data locations and transfer grounds are unverified. | Check actual account terms, map destinations and document any required DPA and transfer mechanism before the pilot. | Yes, controller and legal counsel. |
| 3 Minimisation, retention and rights | Significant | Raw excerpts are stored in public run evidence. Jaime reported no deletion schedule or written rights process. | Save only essential run fields, set a deletion period and test access and deletion across local and provider copies. | Yes, controller. |
| 4 Impact assessment | Significant | The workflow combines sources about an author and uses an LLM. A DPIA has yet to be documented. | Record the screening and complete a DPIA before the pilot. Include the special category exposure and publication risk. | Yes, controller and legal counsel. |

## 4 GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis for each purpose | Gap identified | Research basis proposed. Publication basis unresolved. |
| Purpose limitation | Gap identified | Public demo use was not assessed. |
| Data minimisation | Gap identified | Raw text was kept in evidence. |
| Roles mapped and DPAs in place | Gap identified | Roles are incomplete and applicable agreements remain unverified. |
| International transfer mechanism | Gap identified | No documented safeguard. |
| DPIA if required | Gap identified | The builder identified criteria and plans a DPIA before pilot. |
| Article 22 safeguard if applicable | Appears met | The workflow recommends books and leaves the decision to the bookseller. The reviewed use does not show a significant automated decision about a person. |
| Privacy notice covers AI use | Cannot determine from brief | No notice was available for review. |
| Rights handled within deadlines | Gap identified | No written process, especially for providers and public copies. |

## 5 Overall recommendation

**Do not proceed with the pilot.** First address the political information in public evidence and document the legal grounds for any personal data that will still be used. Before the pilot, confirm the vendor arrangements, put data minimisation and rights handling in place, and complete the DPIA.

## 6 Scope of this report

This is a peer audit for the bootcamp. A legal opinion, a DPIA and certification of compliance are outside its scope. The client should obtain legal review before relying on this assessment.

[GDPR Articles 5, 6, 9, 22, 28 and 35](https://eur-lex.europa.eu/eli/reg/2016/679/ojv) · [AEPD guidance on impact assessments](https://www.aepd.es/derechos-y-deberes/cumple-tus-deberes/medidas-de-cumplimiento/realizacion-de-evaluaciones-de)
