# MIRA GDPR Peer Audit Report

**Auditor:** Gretel Ceballos  
**Builders:** Maria Cavalli and Elza Paegle  
**Project audited:** MIRA V4, with V3 shared-platform context where relevant  
**Date:** 20 August 2026

---

# Phase 4 — GDPR Audit Report

## Section 1 — System Summary

MIRA is a private authenticated application that provides AI-assisted creative direction and generates a personalised Creative DNA profile and visual moodboard. It processes account data, free-text creative inputs, birth details, optional images, generated inferences and visual outputs, with data persisted through database and object-storage services. External AI/model and infrastructure providers participate in the processing chain. Users retain creative control and MIRA does not currently make consequential decisions about individuals. Several production-governance elements, including the final controller, vendor contracts, processing regions, retention rules and rights workflows, remain TBD.

---

## Section 2 — Data and Role Map

The processing includes identifiers, session data, free text, birth details, user images, AI-generated profiles/inferences, generated assets and operational metadata.

The final production controller has not yet been legally established. External authentication, AI/model, database, storage and optional integration providers are expected to act as processors or subprocessors where they process data on the controller's instructions.

International-transfer compliance cannot currently be confirmed because final vendor entities, processing regions and transfer mechanisms remain undocumented.

---

## Section 3 — Compliance Findings

### Finding 1 — Lawful basis, purpose limitation and birth-data minimisation

**Severity:** **Blocking**

**Description:**  
Articles 5 and 6 require a defined processing purpose and valid lawful basis for each activity. Article 6(1)(b) may support processing that is objectively necessary to provide the user-requested creative-direction service, but it does not automatically justify all data currently collected.

The builders confirmed that exact birth date, birth time and city are not necessary for the basic creative-direction functionality. Their use for Human Design/numerology-informed Creative DNA may represent an optional or extended purpose and therefore requires a separate necessity and lawful-basis assessment.

Optional image processing, analytics, future model improvement, support reuse and other secondary uses must likewise be assessed separately rather than assumed to fall within the core contract.

**Recommended action:**  
Create a purpose-by-purpose processing register identifying:

- data category;
- specific purpose;
- Article 6 lawful basis;
- necessity test;
- retention period;
- recipient/vendor;
- whether the processing is optional or necessary for the core service.

Minimise or remove exact birth time/city unless their necessity is demonstrated. Where processing is genuinely optional, assess whether consent or another lawful basis is more appropriate than Article 6(1)(b).

**Escalation needed?**  
Yes — controller, privacy counsel/DPO and product owner.

---

### Finding 2 — Incidental Article 9 data and sensitive inference controls

**Severity:** **Blocking**

**Description:**  
MIRA does not intentionally require Article 9 data for the basic service. However, users may disclose sensitive information in free-text responses or images, and AI-generated Creative DNA or visual outputs may infer sensitive personal characteristics.

An Article 6 lawful basis alone is insufficient where MIRA intentionally processes special-category data. The current documentation does not establish a complete operational policy for detecting, avoiding, deleting or lawfully processing such information.

**Recommended action:**  

- define categories of sensitive information that must not be collected;
- introduce user guidance and input minimisation;
- implement redaction or detection controls where proportionate;
- prevent unnecessary sensitive attributes from entering prompts or persistent profiles;
- define escalation and deletion procedures;
- where intentional Article 9 processing is genuinely necessary, document both the Article 6 basis and the applicable Article 9(2) condition before processing.

**Escalation needed?**  
Yes — controller, privacy counsel/DPO, product and engineering.

---

### Finding 3 — DPIA before production

**Severity:** **Blocking**

**Description:**  
Article 35 requires a DPIA where processing is likely to result in a high risk to individuals.

MIRA combines several risk indicators:

- profiling/evaluation through Creative DNA;
- innovative generative AI;
- free-text inputs;
- user images;
- potential sensitive inferences;
- persistent personal profiles;
- multiple external service providers;
- currently unresolved vendor regions and transfers.

The exact legal conclusion on whether Article 35 already makes a DPIA mandatory may depend on final production scale, geography, design and supervisory-authority guidance. However, the combined risk indicators make completing a DPIA before production the appropriate operational condition.

**Recommended action:**  
Complete and approve a DPIA before production personal-data processing, covering:

- purposes and lawful bases;
- necessity and proportionality;
- Article 9 risks;
- profiling and inference risks;
- Article 22 screening;
- vendor and transfer flows;
- retention and deletion;
- security;
- data-subject rights;
- mitigation controls;
- residual-risk decision.

If high residual risk remains, assess whether Article 36 supervisory-authority consultation is required.

**Escalation needed?**  
Yes — controller, DPO/privacy counsel, product, security and engineering.

---

### Finding 4 — Processor governance, DPAs and international transfers

**Severity:** **Blocking**

**Description:**  
Article 28 requires appropriate processor contracts before processors handle personal data.

The production vendor set, legal entities, processing regions, DPAs, subprocessors and international-transfer mechanisms remain TBD. This means processor governance and Chapter V compliance cannot yet be demonstrated.

The fact that technical services are already integrated does not prove that production processor obligations are contractually or legally satisfied.

**Recommended action:**  

Create a production vendor register covering:

- legal entity;
- GDPR role;
- processing purpose;
- data categories;
- processing region;
- remote-support access;
- subprocessors;
- Article 28 DPA status;
- security commitments;
- deletion obligations;
- applicable Chapter V mechanism.

Disable any production vendor that cannot meet the required contractual, security and transfer conditions.

**Escalation needed?**  
Yes — controller, privacy/legal, procurement and security.

---

### Finding 5 — Transparency, retention, deletion and data-subject rights

**Severity:** **Significant**

**Description:**  
The builders confirmed that the final production privacy notice, retention schedule, deletion rules and tested data-subject-rights workflow are not yet documented as implemented controls.

MIRA persists journey data and generated assets. Therefore, production compliance must address deletion not only from the user-facing application but also from databases, object storage, logs, backups and vendor systems where applicable.

**Recommended action:**  

Before production launch:

- publish an Articles 13–14-compliant privacy notice;
- identify legal bases and purposes clearly;
- explain AI-generated profiles/inferences and recipients;
- document international transfers;
- define a retention schedule by data category;
- implement deletion propagation;
- test access, rectification, erasure, restriction, portability and objection workflows;
- maintain evidence that requests can be handled within GDPR deadlines.

**Escalation needed?**  
Yes — controller, privacy lead, product and engineering.

---

## Section 4 — Specific GDPR Obligations Checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | **Gap identified** | Core contractual processing may be supportable, but optional images, birth details and secondary purposes still require purpose-specific analysis. |
| Purpose limitation respected | **Cannot determine from brief** | Secondary use, model improvement and optional functionality are not fully defined for production. |
| Data minimisation | **Gap identified** | Exact birth time/city are collected although not necessary for basic creative-direction functionality. |
| Controller/processor roles mapped and DPAs in place | **Gap identified / TBD** | Final controller and vendor contractual framework remain unresolved. |
| International transfer mechanism documented | **Gap identified / TBD** | Final regions and Chapter V safeguards are not documented. |
| DPIA conducted if required | **Gap identified** | No completed production DPIA evidenced. |
| Article 22 safeguard in place if automated decisions affect people | **Appears not currently applicable** | MIRA provides creative outputs; no legal or similarly significant individual decision is described. Human users select/refine outputs. |
| Privacy notice covers AI processing | **Gap identified / TBD** | Final production notice is not documented as implemented. |
| Data-subject rights operational within deadlines | **Gap identified / TBD** | Production workflow is not yet documented/tested. |

---

## Section 5 — Overall Recommendation

### **Do not proceed with production personal-data processing**

MIRA may continue development and testing using synthetic or irreversibly anonymised data, but production processing of EU personal data should not begin until the blocking prerequisites are resolved and evidenced.

Before production, MIRA should at minimum:

1. establish the final controller and purpose-specific lawful-basis framework;
2. resolve birth-data minimisation and Article 9 controls;
3. complete and approve the DPIA;
4. establish Article 28 processor governance and Chapter V transfer safeguards;
5. implement and test privacy notice, retention, deletion and data-subject-rights controls.

The recommendation can be reassessed once those conditions are documented and technically verified.

---

## Section 6 — What This Report Is Not

This report is an educational, first-pass independent GDPR audit based on the supplied system documentation and factual clarifications.

It is not:

- a legal opinion;
- a completed DPIA;
- a certification of GDPR compliance;
- a substitute for advice from qualified EU privacy counsel or the relevant DPO.

---

# Final conclusion

**MIRA — Do not proceed with production personal-data processing until the blocking GDPR prerequisites are resolved and evidenced.**

Development may continue with synthetic or irreversibly anonymised data. Production readiness should be reassessed once the controller, lawful-basis map, minimisation controls, DPIA, processor contracts, transfer safeguards, retention/deletion framework and rights operations are documented and tested.