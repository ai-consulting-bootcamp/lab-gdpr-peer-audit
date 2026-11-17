# Release gate — custom playbook isolation and delivery

**Finding closed** Independent audit Finding 1. **Owner** Workflow maintainer and platform security. The client controller and its DPO or privacy lead review and approve the release gate. **Target** 3–5 working days for design and a synthetic staging check, with live release dependent on that evidence and the wider legal gates.

- **Day 1:** Keep real uploads and auto-mail disabled. Inventory the hosted index, existing namespaces, execution storage and outbox. If investigation establishes unauthorized access or disclosure, invoke the incident process and assess Arts. 33–34. A static finding alone is not evidence of a breach.
- **Days 2–3:** Make upload and retrieval use the same server-generated request or approved tenant scope. Enforce authorization on each read and write, avoid clearing shared data, and set an expiry for custom material. Delete the mailbox fallback. Accept only a verified, authorized destination and use a mock outbox until sign-off.
- **Days 4–5:** In staging with fictional inputs, verify independent client scopes, deprovisioning and expiry. Verify that missing, invalid and unauthorized addresses generate no outbound mail. Record the deployed configuration version, timestamps, expected and observed results, control owner and approval, without saving full playbooks in the evidence.

**Evidence of closure** Reviewed configuration diff, authorization and deletion test output, zero-send assertion for rejected recipients and documented release approval. Legal, transfer and DPIA conditions still apply.
