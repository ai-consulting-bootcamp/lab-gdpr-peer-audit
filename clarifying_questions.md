# Clarifying questions and builder responses

Five questions were sent to Jaime. This summary records his answers dated 18 November 2026, based on his check of the code and 20 saved runs.

| Question | GDPR obligation | Initial assumption | Builder response or remaining gap |
|---|---|---|---|
| What reaches Gemini and the search APIs? Can queries or profiles include personal details? | Data minimisation and special category data, Articles 5 and 9 | The sample inputs show an author name. Other details are unknown. | Gemini sees author and book fields, publisher text, descriptions, snippets and selected profile fields. Free text is unfiltered. Jaime reports political information in 7 run files. Exact transmission of that information to Gemini is unverified. |
| What lawful basis covers research, and what covers public evidence on GitHub? | Lawful basis and purpose limitation, Articles 5 and 6 | Research and publication are separate purposes. The basis is unclear. | Jaime proposes legitimate interests for research with a balancing test. Publication is TBD for legal review. |
| Who controls the accounts and which terms cover transfers and processing? | Article 28 and Chapter V | The services are known. Account terms and transfer safeguards are unclear. | Jaime identified the accounts and plans he used. Actual roles, regions and safeguards remain open. |
| What stays in logs and dossiers, how long, and how are rights requests handled? | Articles 5, 12, 15 and 17 | Logs and dossiers are public. Retention and request process are unclear. | Twenty JSON files and eleven dossiers were public when Jaime reviewed them. There is no defined retention period or written procedure. He can search locally. Provider deletion and existing clones remain open. |
| What scale is planned, and is a DPIA needed? | Article 35 | The agent checks book data. Person-level matching and scale are unclear. | One operator and one profile today. Jaime confirmed cross-source linking around the author, counts two DPIA criteria and proposes a full DPIA before the pilot. |
