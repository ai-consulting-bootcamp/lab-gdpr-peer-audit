# Phase 2: personal data, roles and risk analysis

**Evidence boundary:** The two required maps below use only [brief B0-B7](menohelp-reconstructed-processing-brief.md). That brief was reconstructed from source, which is a disclosed departure from exchanging a builder-written brief. Legal assessments below are auditor conclusions, not facts supplied by Ben.

## Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Cycle dates/lengths, period length, flow | CSV/JSON or Clue export, B2 | P1 analysis; P2 report | Local upload route depends on deployment; summaries go to OpenAI, destination unknown | Yes, health |
| User ID and age | Upload, UI, or age derived from PDF, B2-B3 | P1 associate records; P2 contextualise | Potential: included in external processing; no verified location | Not alone; linked health record is sensitive |
| Names/DOB and other identifiers in original PDF | User's blood-test document, B2 | P1 parse selected values | Server initially receives PDF; external raw-PDF upload not shown | Combined medical document: yes |
| Analytes, values/ranges, draw dates, cycle day, derived ages | Parsed PDF and user corrections, B2 | P1 analysis; P2 interpretation | Selected information sent to OpenAI; geography unknown | Yes, health |
| Symptoms, hormones/surgery context, free-text concern | User form, B2-B3 | P1 analysis; P2 retrieval and report | External LLM and embeddings; vector/selectors to Supabase, geography unknown | Yes, health; possibly sex life or third-party sensitive details |
| Health inferences, individual statistics, report and chart | Computation and LLM output, B3-B4 | P2 explanation; P3 delivery/export | External LLM; optional Resend/mailbox; local export alone proves no crossing | Yes, health even when inference is wrong |
| Recipient email and linked report | User-entered address, B4 | P3 optional email delivery | Resend and recipient mail service, locations unknown | Address alone: no; linked report: yes |
| Potential real-person showcase | README-described real-data report, B4 | P4 public demonstration | Public publication creates worldwide availability; specific Chapter V recipients not established | Potential health data; provenance and identifiability unresolved |
| Account/request/network metadata | Service requests, B6 | P5 operation and security | External services; exact fields and regions unknown | Ordinarily no, but linkability to health queries can increase sensitivity |
| Synthetic fixtures and generic reference text | Demo/reference materials, B2-B4 | Demonstration and retrieval | Reference/embedding services may process text | No personal data if genuinely non-identifying; the label alone does not prove this for every file |

An EU border crossing within the EEA differs from a Chapter V transfer to a third country. Vendor nationality alone does not prove either. No EEA-only processing claim is justified.

## Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Client / eventual Menohelp operator, legal identity unknown | Provisional controller: decides purpose and essential means | P1-P5 and user-facing accountability | Article 28 agreement with each processor; identify actual legal controller first |
| Ben Mayer / builder team | Same controller if operating own service; processor only under a separate client's instructions | Build, run and support application | No DPA with oneself; controller-builder DPA if separate processor with personal-data access |
| OpenAI | Candidate processor for instructed inference/embeddings; any own-purpose metadata activity assessed separately | Statistics/findings generation and query embeddings | Yes for processor activity; applicable accepted terms not supplied |
| Supabase | Candidate processor for hosted corpus and patient-derived queries/metadata | Vector retrieval and symptom/lab selectors | Yes where personal data processed; no claim it stores patient records in its documents table |
| Resend | Candidate processor for instructed delivery | Recipient address, health report and chart | Yes; also verify onward providers and retention |
| Render / Streamlit Cloud | Planned hosting vendors, not confirmed active processors | Future app hosting and possible logs | Before any personal-data hosting; do not present planned contracts as active |
| Recipient mailbox provider | Role depends on user/provider relationship and delivery arrangements | Receipt/storage of email report | Not automatically the app operator's processor; establish chain and inform user of mailbox persistence |
| Clue / source laboratory | Separate upstream service/provider, not automatically this app's processor | Original collection/export | User-mediated import does not by itself create an Article 28 relationship |

If Ben contracts vendors on a separate controller's behalf, those vendors may be subprocessors; document prior authorisation and flow-down obligations. Actual purposes and activities, not job titles alone, determine roles.

## Transfer register

| Route from B3-B6 | Required evidence before real-person data use | Provisional action |
|---|---|---|
| Local operator to OpenAI, including embeddings | Contracting entity, service region, remote support, retention/training settings, subprocessors, DPA and applicable transfer tool | Hold until verified; EU endpoint selection alone is insufficient |
| App to Supabase | Database region, query/log handling, support/backups, subprocessor chain | Assess query vectors/selectors as potentially personal, even with a generic stored corpus |
| App to Resend and onward delivery | Sending entity/region, message/log retention, onward recipients and DPA | Keep email disabled for real health reports until assessed; offer local report retrieval |
| Future hosts | Hosting/log/backup/support geography and contracts | Re-screen before deployment |

For an established non-EEA transfer, verify a currently applicable adequacy decision and its recipient/scope coverage, or use appropriate safeguards such as the relevant SCC module with the required transfer assessment and supplementary measures. If relying on the EU-US DPF, verify current validity, the precise recipient's active certification and covered data; this audit does not verify any vendor's certification. A DPA and a transfer mechanism answer different questions. Routine transfers should not be built around exceptional Article 49 derogations. **No transfer mechanism is evidenced in the brief.** [L1, L3]

## Purpose-specific lawful-basis assessment

| Purpose | Candidate Article 6 basis | Article 9 condition and decision |
|---|---|---|
| P1 collect/parse/analyse health inputs | 6(1)(a), consent, proposed for this optional consumer prototype | 9(2)(a), explicit consent, subject to validity and applicable restrictions; obtain before upload, not only before LLM dispatch |
| P2 retrieval and personalised generation | 6(1)(a), proposed | 9(2)(a), explicit consent covering disclosed vendor processing; minimise fields and distinguish embeddings from generation |
| P3 optional health-report email | 6(1)(a), proposed separate optional selection | 9(2)(a) explicit health-data consent covering this delivery route; refusal must preserve on-screen service |
| P4 public demonstration | No established basis | Use wholly synthetic examples; real-person publication needs a distinct defensible basis and Article 9 condition. Private service consent is insufficient |
| P5 minimal service/security metadata | 6(1)(f), potential, subject to necessity and balancing | Keep health text out of logs; incidental health content needs an applicable Article 9 condition, not LI alone |

Article 6(1)(b) may be defensible for objectively necessary service processing under a genuine user contract, but it does not supply an Article 9 condition. No clinical care relationship or professional secrecy arrangement supports assuming Article 9(2)(h). Uploading a file or pressing Generate is not evidence of informed, explicit consent. Consent withdrawal must stop further consent-based processing; retain only information for which another valid ground and, where necessary, Article 9 condition applies. These are proposed choices, not approvals. [L1]

## DPIA screening for intended real-user use

| WP29/EDPB criterion | Assessment from brief |
|---|---|
| Evaluation or scoring | Yes: individual symptoms, patterns and explanations are evaluated |
| Solely automated decisions with legal/similarly significant effects | Not established; informational report is not automatically such a decision |
| Systematic monitoring | Unclear: longitudinal user uploads; no demonstrated continuous tracking service |
| Sensitive or highly personal data | Yes: reproductive/medical data |
| Large scale | Unknown; no evidence of large-scale operation |
| Matching/combining datasets | Yes: cycle records, labs and symptoms for the same individual |
| Vulnerable data subjects | Possible depending on actual users and dependence; adult menopause users are not automatically vulnerable |
| Innovative technology | Yes: LLM/RAG interpretation of health data |
| Preventing rights or access to a service/contract | Not established |

**Provisional conclusion:** likely high risk for intended real-user operation; complete a DPIA before introducing real health data, or obtain a documented, defensible contrary screening decision after clarifying scope and checking the competent authority's mandatory list. Several criteria support this conclusion without inventing scale. The two-criteria rule is guidance, not a mechanical statutory threshold. A genuinely synthetic-only exercise does not create the same health-data risk; service-account metadata remains a separate consideration. If residual high risk cannot be mitigated, consult the supervisory authority under Article 36. [L1-L2]

## Article 22, rights and adjacent laws

No treatment, employment, insurance or access decision is established. Record intended use and reassess if outputs determine care or opportunities in practice. A disclaimer, numeric checker or guardrail is not meaningful human review. If Article 22 applies, assess a lawful exception, Article 22(4) restrictions for special-category data, human intervention, representation/contest rights and the applicable explanation duties. [L1]

For Articles 12-22, designate a contact and track requests against **one calendar month**, with lawful extensions and timely notice where justified. Test access, correction and relevant erasure across input stores, session state, reports, exports and processors; do not promise erasure from a recipient's independent mailbox. Support restriction and consent withdrawal; assess portability for user-provided data processed automatically under consent/contract. Do not collect extra identifiers merely to make anonymous data identifiable. Record recipient notifications where required. [L1, L4]

The law-stack lesson adds checks, not automatic classifications: assess AI Act obligations based on intended/actual use and any medical-device status; a health subject alone does not decide the risk tier. ePrivacy needs a runtime check of cookies/telemetry and national rules; a requested report email is not automatically direct marketing. Wearables are described as dropped, so no current connected-product Data Act role is established; cloud procurement/switching still merits review. Proposed reform does not close a GDPR gap. This report does not rely on Omnibus implementation dates or certify compliance with adjacent laws.
