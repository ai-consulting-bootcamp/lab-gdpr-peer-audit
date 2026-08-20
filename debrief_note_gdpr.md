# Phase 5: GDPR debrief record

**Participants:** Gordan (auditor), John Adams (provider) · **Date:** _record on the day_

The auditor's side is pre written so the meeting is spent on the divergence rather than on recall. Only John's responses and the joint note are written afterwards.

## Step 1: Auditor presents

Presented without interruption:

- Two distinct data populations: John's own data, and that of anyone who talks to the bot. Almost all the exposure sits in the second.
- Controller is John. Six processors, all US established: OpenAI, Pinecone, Cohere, Calendly, Resend, Cloudflare. n8n is self hosted so it is not a processor, which is one fewer DPA than the stack list suggests.
- Nine findings. None blocking today because the system is demo only; four convert to blocking the moment a third party uses it.
- Article 22 is not engaged. The system makes no decision with legal or similarly significant effects about the end user.
- A DPIA is not required on the EDPB criteria, but the screening is unrecorded.
- Recommendation: proceed with conditions, four items, roughly one working day of work.

## Step 2: Provider responds

Context missing from the documentation: _record_

Answers to the clarifying questions, to be carried back into the questions log: _record_

## Step 3: Compare lawful basis selections

| | Primary processing purpose | Lawful basis chosen |
|---|---|---|
| Auditor | Operating the conversation and replying | Article 6(1)(f) legitimate interests, with a documented balancing test |
| Provider | | |

If they differ, work out which is stronger. The likely divergence is consent: it is the intuitive choice and the weaker one here, because the processing is not optional to the service and withdrawal would leave no basis for a conversation already underway. The second likely divergence is Article 6(1)(b), contract, which does not fit because no contract exists between John and a recruiter who asks his bot a question.

_Record:_

## Step 4: Compare DPIA conclusions

| | DPIA required? | Reasoning |
|---|---|---|
| Auditor | No | One EDPB criterion met, innovative use of technology. No systematic evaluation with legal effects, no large scale processing, no monitoring of a public area, no vulnerable subjects, no dataset matching. Two or more criteria are the usual trigger. |
| Provider | | |

If you disagree, work the nine EDPB criteria one at a time until you either agree or can name the specific criterion you read differently. The lab asks for that, and "we disagreed about criterion 3" is a better outcome than a vague split.

_Record:_

## Step 5: Compare gap lists

| | Items |
|---|---|
| Caught by the self audit, missed by this audit | _record_ |
| Caught by this audit, missed by the provider | _record_ |
| Caught by both | _record_ |

The auditor's top three for comparison: the email tool as an Article 32 exfiltration path rather than merely an impersonation risk, indefinite retention of conversation transcripts with no deletion routine, and six processor relationships with no agreement or transfer basis recorded.

## Step 6: Joint closing note

_Two to three sentences, written together: what does this debrief reveal about GDPR self assessment specifically, and what kinds of gaps are hardest to catch in your own work?_

_Record:_

---

## Reinforce

**Questions John logged about my system that I cannot answer:** _record._ What that suggests about my documentation: _record._

**One finding from John's report I initially disagreed with:** _record._ Do I still disagree after the debrief, and why: _record._

---

## Auditor prep notes

Not part of the record.

1. **The interesting comparison is not the findings, it is the severity.** A provider auditing his own demo grades the same gaps lower, because he knows nobody is using it. An external reviewer grades against what the system is for. Both are defensible. Naming that difference is a better closing note than a list of missed items.
2. **Be ready to be wrong on Finding 4.** It rests on one ambiguous phrase, "on the end user's behalf". If the recipient is hard coded, downgrade it in the room and say so.
3. **The Article 32 framing is the one thing this audit has that a self audit rarely does.** A builder sees the email tool as a feature. A reviewer sees an outbound channel that untrusted input can aim. Lead with it.
4. **Do not oversell the psychometric point.** CliftonStrengths is not Article 9 data. If John classified it as special category, that is the one place where the external view is likely stricter in the wrong direction, and conceding it cleanly will buy credibility for the findings that matter.
