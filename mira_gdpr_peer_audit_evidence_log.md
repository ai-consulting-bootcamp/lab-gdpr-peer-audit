# MIRA GDPR Peer Audit — Gretel Ceballos

**Auditor:** Gretel Ceballos  
**Builders:** Maria Cavalli and Elza Paegle  
**Project audited:** MIRA V4, with V3 shared-platform context where relevant  
**Date:** 20 August 2026  
**Overall recommendation:** **Do not proceed with production personal-data processing until blocking GDPR prerequisites are resolved**

---

## Audit basis and independence

This audit was formed independently from the builders' GDPR self-audit conclusions.

Before completing the independent assessment, I reviewed only the MIRA system brief, architecture documentation, AI/data inventory, and factual clarifications requested from the builders. I did not rely on their lawful-basis conclusions, DPIA conclusion, compliance memo, or self-audit gap findings when forming the initial assessment.

Where the production setup is not yet final, this report distinguishes between:

- **Confirmed current behaviour**
- **TBD production decisions**
- **Controls not evidenced in the supplied documentation**

The builder-side conclusions were considered only during Phase 5 for comparison and debrief.

---

# Phase 1 — Read and Annotate

## System understanding

MIRA is a private, authenticated creative-direction application designed for founders, creators and consultants developing a personal or organisational brand world.

The current MIRA journey collects account/session information, creative and recognition responses, project context, birth details, and optionally user-provided inspiration or reference images. Language-model services are used to generate adaptive questions and a structured Creative DNA profile, while image-generation services produce visual directions and a five-image editorial moodboard. Journey state, generated outputs and uploaded/generated assets are persisted through database and object-storage infrastructure.

Users retain creative control by selecting, refining and approving outputs. The system does not currently make employment, credit, eligibility, healthcare, service-access or other consequential decisions about individuals.

Production governance is not yet fully established. The final legal controller, vendor set, processing regions, DPAs, transfer mechanisms, retention schedule, deletion rules, privacy notice and tested data-subject-rights workflow remain TBD.

## Personal data identified

### Ordinary personal data

- account and session identifiers;
- authentication and usage metadata;
- creative and recognition responses;
- free-text project and audience descriptions;
- date of birth;
- time of birth;
- city/country associated with birth;
- uploaded inspiration or reference images;
- explanations associated with uploaded images;
- generated Creative DNA profiles and related inferences;
- generated visual outputs;
- timestamps, run data, logs and technical metadata where linked to an identifiable user.

### Potential special-category data

Birth details are not inherently Article 9 special-category data.

A facial image is also not automatically biometric special-category data unless processed for the purpose of uniquely identifying a person.

However, free-text responses, images and model-generated inferences may reveal or infer information concerning:

- health or disability;
- racial or ethnic origin;
- religion;
- political opinions;
- trade-union membership;
- sexual orientation;
- other sensitive personal characteristics.

This creates an incidental Article 9 risk even though MIRA does not intentionally ask users to submit such information for the basic creative-direction service.

## Cross-border and vendor issues flagged

MIRA uses external AI/model and infrastructure services, but the final production vendor set, processor legal entities, processing regions, DPAs and international-transfer mechanisms have not yet been formally established or documented.

Accordingly, international-transfer compliance cannot currently be confirmed.

## Purpose concerns flagged

The basic creative-direction functionality does not require exact birth date, birth time and city.

The builders clarified that those data are collected because Human Design or numerology can inform Creative DNA and visual direction, but their necessity for the production V4 service remains to be determined.

This creates a data-minimisation and purpose-necessity issue.

---

# Phase 2 — Personal Data and Role Map

## Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
|---|---|---|---|---|
| Account/session identifiers | User / authentication system | Authentication, account access, security | TBD depending on production infrastructure | No |
| Creative and recognition responses | User | Creative discovery, adaptive questioning, Creative DNA generation | Potentially; vendor regions TBD | Not inherently, but sensitive information may be volunteered or inferred |
| Project/audience/moodboard context | User | Creative brief and visual-direction generation | Potentially; vendor regions TBD | Usually no, but free text may contain sensitive information |
| Birth date, time and city | User | Human Design/numerology-informed Creative DNA and visual direction | Potentially; vendor regions TBD | No, not inherently |
| Inspiration/reference images | User | Visual synthesis, identity/creative reference | Potentially; vendor regions TBD | Not automatically; may reveal sensitive attributes |
| Generated Creative DNA / model inferences | AI system | Personalised creative-direction output | Potentially | May infer sensitive characteristics |
| Generated images / moodboards | AI system | Creative deliverables | Potentially | Usually no, but may reflect inferred personal characteristics |
| Logs, timestamps, technical metadata | System-generated | Security, troubleshooting, auditability | TBD | No unless linked with sensitive content |

## Role map

| Entity | Role | Processing activity | DPA needed? |
|---|---|---|---|
| Final MIRA operating legal entity | **Controller — TBD legal entity** | Determines purposes and means of production processing | N/A as controller |
| MIRA build/operations team | Acts on behalf of the controller unless structured as a separate legal processor | Product operation, configuration, support | Depends on final organisational structure |
| Authentication provider | Processor/subprocessor if processing only on MIRA's instructions | Authentication and account/session processing | Yes if acting as processor |
| Forge / AI model services | Processor/subprocessor where acting on MIRA's instructions | Language-model and image-generation processing | Yes |
| Database hosting provider | Processor/subprocessor | Persistence of user journey data | Yes |
| Object-storage provider | Processor/subprocessor | Uploaded/generated image and asset storage | Yes |
| Optional integrations such as numerology provider | Processor/subprocessor if enabled and instructed by MIRA | Optional birth-detail processing | Yes if used in production |

### International transfers

The production processing regions and transfer mechanisms are **TBD**.

Before production use involving EEA personal data, MIRA must identify:

- the legal entity for each vendor;
- processing and remote-access locations;
- subprocessors;
- whether an adequacy decision or EU–U.S. Data Privacy Framework applies to the specific recipient;
- where no adequacy mechanism applies, whether SCCs and a Transfer Impact Assessment are required;
- any supplementary technical or organisational safeguards.

A DPA alone does not satisfy Chapter V transfer requirements.

---

# Phase 3 — Clarifying Questions Log

| Question | Why it matters | Builder response | Audit status |
|---|---|---|---|
| Who will be the final legal entity operating MIRA and acting as controller for production users? | Determines accountability, privacy notice ownership, processor contracts and GDPR responsibility. | The final production controller/legal entity is TBD. | **Unresolved — TBD** |
| Are exact birth date, birth time and city necessary for the current V4 service? | Affects data minimisation and whether collection is objectively necessary for the service. | They are collected because Human Design/numerology can inform Creative DNA and visual direction, but they are not necessary for the basic creative-direction functionality. Production necessity remains to be determined. | **Partial answer — minimisation concern remains** |
| Which vendors will process personal data in production, in which regions, and under which DPA / international-transfer mechanism? | Affects Article 28 processor governance and Chapter V compliance. | External AI/model and infrastructure services are used, but the final vendor set, regions, DPAs and transfer mechanisms are not formally established/documented. | **Unresolved — TBD** |
| What retention and deletion rules apply to user inputs, Creative DNA, images, outputs, logs, backups and vendor copies? | Affects storage limitation, erasure rights and deletion propagation. | Journey data and generated assets are persisted, but the final production retention/deletion schedule is not documented. | **Unresolved — TBD** |
| What privacy notice and data-subject-rights workflow will be operational at launch? | Affects Articles 13–14 and the operationalisation of access, rectification, erasure, portability and objection. | Final notice and rights workflow are not yet documented as implemented/tested controls. | **Unresolved — TBD** |