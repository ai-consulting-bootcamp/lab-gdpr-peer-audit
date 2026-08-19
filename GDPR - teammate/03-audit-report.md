# GDPR Audit Report — RegGuard-Mini
Auditor: Nelly Pourmehr
Builder: Kimia Asgari
Date: August 19, 2026

## Section 1: System summary
RegGuard-Mini helps designers check vehicle geometry against a regulatory rule set and get plain-language explanations of the results. Designers ask free-text questions, which are sent to a commercial LLM for the reasoning layer. Designers can also assemble a report and send it to a named colleague. The system suggests changes but never applies them; the designer decides and saves each version. The system processes three types of personal data: designer identity, designer's typed questions, and a handoff colleague's name and address.

## Section 2: Data and role map
Three personal data categories exist: designer identity, typed questions, and handoff recipient data. None are special category by design, but typed free text could incidentally include it. The client is the controller. Kimia's team is the processor. The commercial LLM provider is an unnamed sub-processor. Storage location and international transfer status are undocumented for all three data categories.

## Section 3: Compliance findings

### Finding 1 — DPA with LLM sub-processor
Severity: Blocking
Description: Typed questions containing personal data already go to a commercial LLM provider. The provider is not named, and no DPA is confirmed. Art. 28 requires a DPA before a processor handles personal data.
Recommended action: Confirm the LLM vendor and execute a DPA before continuing to route typed questions through it.
Escalation needed? Yes — to legal/DPO.

### Finding 2 — International transfer mechanism undocumented
Severity: Significant
Description: Typed questions, designer identity, and handoff data may leave the EU depending on where the LLM and storage are located. No transfer mechanism is documented.
Recommended action: Confirm hosting locations. Put SCCs or another Art. 44-49 mechanism in place if any location is outside the EU.
Escalation needed? Yes — to legal/DPO.

### Finding 3 — Free-text input risk of special category data
Severity: Significant
Description: Designers type open questions with no described filtering. There is a small but real chance a question could include health, disability, or other special category information.
Recommended action: Add designer guidance against entering personal or sensitive details in free text. Consider basic input screening.
Escalation needed? No.

### Finding 4 — Confidence-scored assessment and employee monitoring
Severity: Significant
Description: The system generates confidence-scored assessments of a designer's work. Depending on deployment jurisdiction and use, this could trigger local employee-monitoring rules, such as German works council co-determination.
Recommended action: Confirm deployment jurisdiction and whether scores are ever used in performance evaluation. Consult employment law if Germany is in scope.
Escalation needed? Yes — to legal/HR.

### Finding 5 — Retention period undefined
Severity: Minor
Description: No retention period is documented for typed questions or handoff recipient data.
Recommended action: Define and document a retention schedule.
Escalation needed? No.

## Section 4: GDPR obligations checklist

| Obligation | Assessment | Note |
|---|---|---|
| Lawful basis identified for each processing purpose | Cannot determine from brief | Brief describes purposes, not the legal basis chosen for each |
| Purpose limitation respected (no incompatible reuse) | Appears met | Each data use maps to a feature the designer actively used |
| Data minimisation (only necessary data collected) | Gap identified | Free text has no filtering against incidental over-collection |
| Controller/processor roles mapped and DPAs in place | Gap identified | LLM sub-processor DPA not confirmed |
| International transfer mechanism documented | Gap identified | Hosting and provider location not stated |
| DPIA conducted if required | Cannot determine from brief | Not mentioned. Confidence-scored assessments raise the question. |
| Article 22 safeguard in place if automated decisions affect people | Appears met | Designer stays in control, no automated decision on people described |
| Privacy notice covers AI processing | Cannot determine from brief | Not mentioned |
| Data subject rights can be operationalised within deadlines | Cannot determine from brief | Not mentioned |

## Section 5: Overall recommendation
Position: Do not proceed with routing typed questions through the LLM until Finding 1 and Finding 2 are resolved. Other data flows may continue while Significant and Minor findings are addressed.
Rationale: Typed questions already reach an unnamed processor with no confirmed DPA and no documented transfer mechanism. This is a Blocking gap under Art. 28. The rest of the system carries lower risk and can proceed while these two items are fixed.

## Section 6: What this report is not
This report is not a legal opinion, not a DPIA, and not a certification of compliance. The client should obtain legal review before relying on this assessment.
