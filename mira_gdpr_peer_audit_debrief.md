# MIRA GDPR Peer Audit — Debrief and Comparison

**Auditor:** Gretel Ceballos  
**Builders:** Maria Cavalli and Elza Paegle  
**Project audited:** MIRA  
**Date:** 20 August 2026

---

# Phase 5 — Debrief and Comparison

## Debrief basis

The builder self-audit conclusions were reviewed only after the independent audit was completed.

A team-level debrief had already been conducted between Paola Hintze and Maria Cavalli. Maria provided direct builder-side responses to the external findings and approved the joint closing note. Those responses are used here as debrief evidence without implying that Gretel personally conducted that earlier conversation.

---

## 1. Auditor presents

My independent assessment is:

**Do not proceed with production personal-data processing until the blocking prerequisites are resolved.**

The principal concerns are:

- purpose-specific lawful bases;
- minimisation of birth details;
- incidental Article 9 data;
- DPIA completion;
- processor/DPA governance;
- international-transfer readiness;
- retention, deletion, transparency and rights operations.

---

## 2. Builder responds

Maria confirmed that:

- Article 6(1)(b) contract is the strongest candidate for the core personalised creative-direction service;
- contractual necessity for optional reference images and exact birth details still needs to be demonstrated;
- MIRA does not intentionally collect Article 9 data, but sensitive information may be disclosed or inferred and appropriate controls are therefore required;
- a DPIA should be completed before production;
- whether Article 35 makes the DPIA strictly mandatory remains legally TBD pending further evidence and legal review;
- processor governance and DPAs must be resolved before production where compliant agreements are not already evidenced;
- vendor regions and transfer mechanisms still need to be verified and documented;
- transparency, retention, deletion and rights controls may partly exist technically but are not yet sufficiently documented or tested as compliance evidence.

---

## 3. Compare lawful-basis selections

### Agreement

Both the external audit and builder-side position agree that:

- Article 6(1)(b) may support the core service where processing is objectively necessary to provide the requested creative direction;
- exact birth details require a separate necessity assessment;
- optional features cannot automatically be treated as contractually necessary merely because the user chooses them;
- incidental or inferred Article 9 data require separate controls and legal analysis.

### Difference

The external audit applies a more conservative position to exact birth details and optional functionality because the builders confirmed they are not necessary for the basic creative-direction functionality.

The stronger production approach is therefore to document objective necessity for each optional data category or use a separate valid basis where appropriate.

---

## 4. Compare DPIA conclusions

### External audit

The combined risk indicators justify treating completion of a full DPIA as a blocking prerequisite before production personal-data processing.

### Builder self-audit

A DPIA should be completed before production, but the strict Article 35 legal requirement remains TBD pending final production facts and legal review.

### Agreed position

There is no operational disagreement.

Both positions require the DPIA to be completed before production.

The remaining difference is legal characterisation: whether Article 35 already makes it mandatory based on the facts currently available, or whether that conclusion should remain formally TBD until the final production configuration is known.

---

## 5. Compare gap lists

| Area | Comparison |
|---|---|
| Core lawful basis | Agreement that contract is strongest for objectively necessary core processing |
| Optional images | External audit applies a stricter necessity test |
| Birth details | Agreement that necessity/minimisation remains unresolved |
| Article 9 | Agreement that incidental disclosure/inference is possible and requires controls |
| DPIA | Agreement on completing before production; difference only on strict legal characterisation |
| Processor governance | Agreement that contracts/roles must be evidenced |
| International transfers | Agreement that regions and mechanisms remain unresolved |
| Retention/deletion | Agreement that production controls are not yet sufficiently evidenced |
| Privacy notice/rights | Agreement that final implementation/testing remains incomplete |
| Implementation context | Builder self-audit provides deeper technical context |
| Evidence discipline | External audit more clearly distinguishes implemented controls from undocumented assumptions |

---

## 6. Joint Closing Note

> We agreed that contract is the strongest candidate for the core service and that a DPIA should be completed before launch, while questions remain around the contractual necessity of optional images and birth details and the precise Article 35 legal characterisation. The comparison showed that self-audits benefit from implementation context, while external audits make undocumented assumptions — particularly around vendors, transfers, retention, deletion and lawful necessity — more visible. The hardest GDPR gaps to identify in one's own system are often controls that feel operationally understood but are not yet documented, testable or independently verifiable.

---

# Stretch — Remediation Plan

## Priority finding: DPIA and production privacy readiness

### Artifact required

A controller-approved MIRA DPIA containing:

- precise processing purposes;
- lawful basis by purpose;
- data-category and data-flow inventory;
- necessity and proportionality analysis;
- Article 9 and Article 22 screening;
- vendor/subprocessor register;
- international-transfer analysis;
- retention and deletion design;
- security controls;
- rights-handling workflow;
- risk scoring and mitigation measures;
- residual-risk decision;
- approval and change log.

### Ownership

- **Controller:** accountable for approval
- **Privacy lead / DPO:** DPIA coordination and GDPR assessment
- **Product:** purpose and feature necessity
- **Engineering:** architecture, retention, deletion and rights evidence
- **Security:** technical and organisational controls
- **Procurement/legal:** DPAs, vendors, transfer documentation
- **Qualified counsel:** final legal review where required

### Evidence of closure

The gap should be treated as closed only when there is:

- an approved DPIA;
- documented lawful bases;
- an agreed controller identity;
- signed processor terms;
- documented transfer mechanisms;
- approved retention rules;
- tested deletion and access workflows;
- evidence of privacy-notice publication;
- documented residual-risk sign-off.