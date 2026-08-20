# Stretch: remediation plan for Finding 4

**Finding:** the email tool is an unauthorised disclosure path for personal data. Article 32, with Article 33 consequences if exploited.
**Objective:** conversation input cannot cause personal data to be transmitted to a recipient the data subject did not choose.

## What closes the gap

Three artifacts, not one.

1. **A technical change.** The Resend node's recipient field set to a literal address in the node configuration rather than an expression referencing agent output. Subject and body drawn from a fixed template with the user's message inserted as quoted text and length capped, so agent output cannot compose the whole message.
2. **A documented technical and organisational measure.** Half a page recording what the email tool can and cannot address, why the constraint sits at the node rather than in the prompt, and what would have to change to widen it. This is the artifact that converts a fix into evidence of a fix, and it is what Article 32 accountability actually asks for.
3. **A breach response line.** One paragraph in the same document stating how an unauthorised disclosure through this channel would be detected and what the Article 33 seventy two hour path would be. Currently there is none, and the provider's own documentation states that silently wrong tool output goes undetected.

## Owner

John Adams, as controller. Provider, deployer and controller are the same natural person, so there is no delegation and no escalation path. That absence is itself worth recording in the measure document, because Article 32 expects organisational measures and there is no organisation.

## Timeline

| Step | Effort | When |
|---|---|---|
| Confirm the current node configuration | 15 minutes | Immediately, before any demo to a third party |
| Pin the recipient and template the body | 1 to 2 hours | Same day if the recipient is agent selected |
| Adversarial test, ten attempts | 45 minutes | Same day, after the change |
| Write the measure and breach response note | 1 hour | Within the week |

Under half a day. The severity comes from the exposure, not the complexity.

## Evidence a regulator would accept

1. The node configuration showing a literal recipient rather than an expression referencing agent output.
2. A dated log of at least ten adversarial attempts through the live interface instructing the agent to mail an arbitrary address, with the outcome of each, including the attempts that came closest to succeeding.
3. A `chat_log` extract covering those attempts, demonstrating that an attempt is visible after the fact rather than silent. This is what turns the control from preventive only into preventive plus detective, which is the pairing Article 32 expects.
4. The measure and breach response document, dated and version controlled.

A prompt level instruction that the agent should only mail John is not evidence, because the channel carrying the instruction is the same channel carrying the attack.
