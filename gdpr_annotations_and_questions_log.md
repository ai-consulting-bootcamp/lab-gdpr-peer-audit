# Phase 1 annotations and Phase 3 clarifying questions log

Companion to `gdpr_audit_report_virtual_coffee_chat_bot.md`. Both were completed before John's self audit was opened.

---

## Phase 1: Annotated read

Source read once without notes, then annotated. Notation follows the lab: **[PD]** personal data category, **[?]** unclear or needs confirmation, **[X]** crosses an EU border or involves a non EU vendor, **[P]** purpose that may be incompatible with the original collection purpose.

### Purpose and users

- **[PD]** "A recruiter or hiring manager can ask about his work history, skills, and projects." The counterparty is a natural person acting in a professional capacity. Professional context does not remove GDPR protection; a work email address is still personal data.
- **[?]** Is the bot reachable by anyone other than John? Answered by the provider: demo only. Recorded as a statement of intent, not a technical control.

### Knowledge base

- **[PD]** `kb/facts/` holds CV content and CliftonStrengths results. The data subject is the provider himself.
- **[PD][?]** CliftonStrengths is psychometric assessment output. Not an Article 9 category on its own, since it reveals no health, belief, union membership or sexual orientation. Marked because it is sensitive in effect and because a reviewer will reach for Article 9 reflexively.
- **[?]** Does `kb/narrative/` name former managers, colleagues or clients? Those are data subjects who consented to nothing, cannot exercise rights they do not know they have, and may be the subject of generated statements.
- **[X]** The entire knowledge base is embedded through OpenAI and stored in Pinecone. Both US.

### Conversation and logging

- **[PD]** "Every turn logged with the question, answer, and thumbs up/down feedback." Free text. Whatever the end user types is retained, including anything they volunteer about themselves, their employer, or a role.
- **[?][PD]** A recruiter could disclose Article 9 data unprompted, for example a health related accommodation question. The system has no filter and no reason to expect one.
- **[P]** Thumbs feedback exists for quality review. That is a distinct purpose from operating the conversation, and it is the reuse most likely to fail a compatibility test if it is never assessed.
- **[?]** No retention period, deletion routine, lawful basis or notice appears anywhere in the source.

### Tools and actions

- **[PD][X]** Calendly availability and booking. Captures name, email, meeting time and timezone. US established, and a controller in its own right for its platform data.
- **[PD][X][?]** Resend "sends email on the end user's behalf." The recipient scope is unstated. If agent selected, this is an outbound channel that untrusted conversation input can aim, which makes it an Article 32 exposure rather than merely an impersonation risk.
- **[?]** Five tools stated, four listed. An unenumerated capability cannot be assessed.
- **[?]** No prompt injection defence or input validation mentioned anywhere.

### Infrastructure

- **[X]** Cloudflare tunnel. Transport, IP addresses, US established.
- Self hosted n8n. Worth marking as an absence: because the platform is self hosted rather than SaaS, n8n itself processes nothing and is not a processor. That is one fewer DPA than a reviewer would assume from the stack list.
- Credentials held in the n8n credential store rather than in the repository, and Basic Auth on the widget. Both are Article 32 positives and should be said so in the debrief.

### Provider's own limitations section

- **[?]** The stated admission that a node reporting success on silently wrong output goes undetected. Under GDPR this reads as an accuracy question under Article 5(1)(d) and a detection question under Article 33: a wrong booking or a misdirected email would not surface on its own.

---

## Phase 3: Clarifying questions log

Five questions. Each provisional assumption is the position the audit report adopts pending an answer.

**Q1. Is the system reachable by anyone other than you, and has anyone else used it?**
*What I need to know:* whether third party personal data has already been processed, including in demos to classmates, instructors or contacts.
*Why it matters:* determines whether Articles 6, 13, 28 and 44 are live obligations or prospective ones, and therefore whether four findings are Significant or Blocking.
*Provisional assumption:* answered by the provider as demo only. The audit adopts that, and notes that any demo to another person has already triggered the obligations for that person.

**Q2. Can the agent choose the email recipient, or is it fixed at the node?**
*What I need to know:* whether conversation input can direct outbound mail.
*Why it matters:* Article 32 security of processing, and Article 33 breach notification if retrieved context or transcript content can be mailed to an attacker chosen address.
*Provisional assumption:* agent controlled, since the documentation says "on the end user's behalf". Finding 4 written on that basis.

**Q3. What exactly does `chat_log` store, for how long, and can it be queried by data subject?**
*What I need to know:* field list, retention period if any, and whether an access or erasure request could be fulfilled within one month.
*Why it matters:* Articles 5(1)(e), 15 and 17.
*Provisional assumption:* full transcript with any identifiers volunteered, retained indefinitely, queryable by session but not by person.

**Q4. Does `kb/narrative/` name identifiable third parties?**
*What I need to know:* whether former colleagues, managers or clients appear by name in the corpus.
*Why it matters:* those individuals are data subjects with no relationship to the controller, no notice, and no correction route, and the system may generate statements about them.
*Provisional assumption:* employer organisations only, no named individuals. If wrong, this becomes a new Significant finding.

**Q5. Which processor agreements and transfer mechanisms have you actually accepted?**
*What I need to know:* whether the standard DPA was accepted for OpenAI, Pinecone, Cohere, Calendly, Resend and Cloudflare, and whether each relies on Data Privacy Framework certification or standard contractual clauses.
*Why it matters:* Articles 28 and 44 to 49. Accepting a DPA at signup is common and often forgotten, so the gap may be documentary rather than substantive.
*Provisional assumption:* none recorded, none consciously accepted. Findings 2 and 3 written on that basis and would downgrade to Minor if the vendor defaults apply.

| Question | Sent | Answer | Effect if answered otherwise |
|---|---|---|---|
| Q1 | | Demo only, per the provider | Public exposure moves four findings to Blocking |
| Q2 | | | Fixed recipient downgrades Finding 4 to Minor |
| Q3 | | | A stated retention period closes Finding 6 |
| Q4 | | | Named third parties open a new Significant finding |
| Q5 | | | Accepted DPAs downgrade Findings 2 and 3 to Minor |
