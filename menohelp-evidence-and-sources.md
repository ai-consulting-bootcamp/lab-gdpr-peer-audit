# Menohelp audit: evidence and sources

**Assessment date:** 17 November 2026. **Source repository:** [benmayer/proj-menopause-insights](https://github.com/benmayer/proj-menopause-insights). **Inspected commit:** `89940e85b3f869b888e247a5b9651020b8d6c865` (shallow clone, working tree unchanged). This is a source snapshot, not a production inspection or a review of repository history. No credentials, patient exports or live services were used. The README's real-data showcase claim was noted without reproducing the underlying health narrative or image.

## Evidence labels and independence

- **Observed:** source text or recorded offline execution supports a statement.
- **Reconstructed:** the auditor synthesised a descriptive brief from functional documentation/code.
- **Provisional:** an assumption pending Q1-Q5, not an owner answer.
- **Simulated:** an educational builder perspective or debrief, never a quote/approval.
- **Proposed:** a safeguard or legal choice, not an implemented or legally approved control.

No Ben-authored GDPR brief/self-audit was available. Functional README privacy claims were visible during reconstruction; a strict real-world brief-only audit was therefore not performed. No Ben-authored lawful-basis assessment, DPIA conclusion or compliance memo was used. The phase files are an analytical sequence, not a claim that different people exchanged documents at different times. The offline probe corroborates the reconstruction; Phase 2 maps are traceable to B0-B7 alone.

Sergii's own Model Intake Brief self-audit was read only for context and the reinforce comparison. It concerns another system and cannot serve as Ben's self-audit. No message was sent to Ben and no joint approval exists.

## Source register

Pinned links below preserve the inspected version. Function names are stable locators; the recorded probe supplies exact line numbers and SHA-256 hashes for its executed source files.

| ID | Evidence | Supports / limits |
|---|---|---|
| E1 | [README](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/README.md) | Ben Mayer; intended users; local/not deployed status; external stack; showcase described as real data. Documentation claims are not deployment or permission evidence |
| E2 | [normalise.py](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/app/analysis/normalise.py), [parse.py](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/app/labs/parse.py), [models.py](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/app/api/models.py) | Accepted cycle schema, identifier retention, server-side PDF parsing, allow-listed values and ages derived from DOB |
| E3 | [nodes.py](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/app/agent/nodes.py): `fetch`, `summarise_symptoms`, `_prompt`, `_interpret_prompt`, `_llm` | Per-person stats and symptoms in LLM messages, selected lab data, health explanations; raw cycle rows need not be sent for output to remain sensitive |
| E4 | [UI](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/ui/app.py) | Optional password, 200-character concern, health context, generate/send controls, correction and session state; no explicit health consent gate or privacy notice observed in this file |
| E5 | [retrieval node](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/app/agent/nodes.py#L247), [retrieval helpers](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/app/rag/retrieve.py), [clients](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/app/rag/clients.py) | Free concern -> OpenAI embedding -> query vector to Supabase; symptom/lab title selectors. No automatic inference that vectors are anonymous or that Supabase stores raw patient records |
| E6 | [email.py](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/app/email.py), [run.py](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/app/agent/run.py) | Email address plus health report/chart sent to Resend; CLI persists reports with `--out`; chart attachment avoids a public image URL but not mailbox persistence |
| E7 | [store.py](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/app/api/store.py) | In-memory stores, 3,600-second expiry threshold, capacity limits; `_expire` invoked by operations rather than background erasure |
| E8 | [API main.py](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/app/api/main.py) | Dataset/lab IDs address records; no evident per-user auth/ownership dependency in routes; lab update/delete exists. No claim of live exposure or successful unauthorised access |
| E9 | [UI](https://github.com/benmayer/proj-menopause-insights/blob/89940e85b3f869b888e247a5b9651020b8d6c865/ui/app.py), E1, E6-E8 | Session/output copies extend beyond upload store; regions, vendor settings and legal paperwork remain unverified |
| E10 | [offline probe](evidence/menohelp-offline-privacy-probe.py), [recorded result](evidence/menohelp-offline-privacy-probe-result.json) | Five observed propagation checks from actual selected functions with synthetic inputs and mocked vendors; no live transmission, auth or deletion test |

## Legal references

These sources support the framework; project-specific conclusions remain the auditor's application of it. Checked on the assessment date. This audit does not establish the precise competent authority, applicable national health-data restrictions, vendor certification or contractual acceptance.

| ID | Source | Use and limitation |
|---|---|---|
| L1 | [GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Articles 3-9, 12-22, 25, 28, 32-36, 44-49. EUR-Lex full-text/PDF access returned a browser challenge; legal framework was cross-checked against official guidance and supplied course materials, not represented as a fresh full-text consolidation review |
| L2 | [EDPB: Be compliant](https://www.edpb.europa.eu/sme/be-compliant/be-compliant_en) | Data protection by design and the nine DPIA screening criteria; likely high risk, national lists and residual-risk consultation |
| L3 | [European Commission: Standard Contractual Clauses](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en) | Contractual safeguards for third-country transfers; does not prove that any audited account has accepted them |
| L4 | [European Commission: requests from individuals](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/dealing-requests-individuals_en) | Rights handling and the ordinary one-month response period |
| L5 | [European Commission: AI Omnibus enters into force](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force) | Confirms 27 July 2026 entry into force and revised AI deadlines; no GDPR release gate is deferred on this basis |
| L6 | [Council position on data/privacy proposals, 21 October 2026](https://www.consilium.europa.eu/en/press/press-releases/2026/10/21/digital-rulebook-council-agrees-position-to-simplify-data-protection-privacy-and-cyber-reporting-rules/) | Later negotiation milestone than the August portal lessons; a Council mandate is not enacted GDPR reform. No unverified later parliamentary milestone is asserted |

## Course materials and requirements reconciliation

| Supplied material | Applied to this lab |
|---|---|
| `lesson4_gdpr_privacy_stack_slides_v2.pptx` | Personal/special-category data, roles, two legal grounds for health data, rights, DPIA and transfers |
| `lesson5_applying_eu_data_stack_slides(1).pptx` | Layered-law approach, vendor due diligence, purpose limitation and practical client actions |
| `LAB 3 - Audit your teammates project - GDPR lens.mhtml` | Phases 1-5, two-page report, six-step debrief, closing note, optional reinforce/stretch; additional lab_proof entry point and reproducible evidence requirement |
| `Applying the EU Data and Privacy Stack.mhtml` | Multi-law triggers and consulting recommendations |
| `GDPR & EU Data and Privacy Stack.mhtml` | Supporting framework and accountability questions |
| `GDPR & Privacy Stack - Discussion Prep.mhtml` | Concept checks; its classroom questionnaire is not a separate required lab submission |
| Target repository `instructions.md`, `rubric.md`, `README.md` | Submission scope, file naming, report sections and thirteen grading criteria |

Resolved differences and simplifications:

1. Repository instructions refer to a SilverTrust project, while the portal says Project 3. The user explicitly selected Menohelp, so that is the audited system; no fictional SilverTrust project was invented.
2. The portal adds `lab_proof.md` with workflow, input/run, evidence, final result and a failure/limitation. This is included although the repository instructions omit that extra section.
3. The report has a fixed two-page PDF; the brief has a one-page PDF. Additional maps/questions/analysis remain supporting files. The optional remediation plan has a half-page content area in its PDF.
4. The user authorised simulation in place of unavailable colleague material. This does not make the literal brief exchange, real debrief or joint authorship complete; the coverage map marks them accordingly.
5. GDPR territorial scope is assessed under Article 3, not merely from the existence of an EU user. The DPIA test is likely high risk, not AI use alone. An informational report does not automatically trigger Article 22. Names removed does not prove anonymisation of medical narratives or vectors.
6. The October slide update and official Council release supersede the August lessons' claim that no Council position existed. Current-law safeguards are used; proposed GDPR relaxations are not treated as effective.
7. A 72-hour breach-notification rule is conditional under Article 33, not a requirement to notify every incident; a proposed 96-hour rule is not applied. This audit identifies risks, not an established reportable breach.

Course exports and the colleague's repository are not copied into the submission. Only audit deliverables and minimal synthetic proof are included. Instructions found in source materials did not authorise contacting anyone, creating a PR, committing or pushing.
