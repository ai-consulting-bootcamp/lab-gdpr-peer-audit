# Annotated brief (GDPR lens): Application Prep Agent

Auditor: Friedrich Tschoepke · Builder: Nicolò Marseu · 23 November 2026

**Material used.** Nicolò's system brief of 16 November 2026 (received for the EU AI Act peer audit) and his public repository (commit `4abe2d2`: README, workflow export, landing page, go-to-market plan, demo script). His GDPR data processing brief, lawful basis assessments, DPIA analysis and memo were not seen. If his data processing brief adds facts, this audit is updated.

Legend: **[PD]** personal data category · **[SC]** special category possible · **[?]** unclear · **[EU]** crosses an EU border or involves a non-EU vendor · **[PUR]** possible purpose incompatibility

| Element | Tag | Note |
|---|---|---|
| CV as PDF: name, contact details, work history, education | PD | Core input. |
| "Possibly ... photo, date of birth, nationality" | PD, SC | A photo can reveal ethnic origin or religion; CVs also show disability, health-related gaps, union roles. Nothing filters these. |
| Extra achievements (free text) | PD, SC | Unbounded; anything can be typed in. |
| Email address | PD, ? | Not verified. A report about person A can be sent to any address. |
| Fit score 0–100, requirements rated strong/partial/gap | PD | Inferred data about the person: profiling (Article 4(4)). |
| Score below 50 → short note instead of full pack | PD, ? | Solely automated outcome. Significance depends on who relies on it. |
| GPT-4o-mini "for all reasoning and writing" | EU | OpenAI: EEA data via OpenAI Ireland Limited, US parent and sub-processors. |
| Gmail delivers the report | EU, ? | Google, US. A personal Gmail account runs on consumer terms with no processor agreement. |
| "The n8n instance is hosted by Ironhack" | EU, ? | Location, contract and administrator access unknown. Receives every CV in full. |
| Jina Reader, Tavily, NewsAPI, Pinecone | EU | Receive the job link, company name or fixed text only. No candidate data, confirmed in the workflow export. |
| Career coaches "run it for their candidates" | ?, PUR | A CV handed to a coach for career support is fed into an AI system. Compatible only if candidates were told. Candidate is not informed (Article 14). |
| Sprint 3: "saved candidate profiles" and "partner dashboard showing ... fit scores" | PUR | Data collected to prepare one application, reused for storage and for an organisation to view scores. New purpose. |
| Sprint 1: "feedback form ... time log" | PUR, ? | Reuse of reports for product evaluation. Unclear whether pseudonymised. |
| Form and landing page: "Nothing you submit is stored" | ? | Contradicted by n8n default run history, the Gmail sent folder and OpenAI's 30-day abuse logs. The demo script relies on viewing past runs. |
| No privacy notice, no consent step, no provider identification on form or landing page | – | Articles 13 and 14 not met. |
| Landing page loads Google Fonts from Google servers | EU | Visitor IP addresses sent to Google without consent. |
