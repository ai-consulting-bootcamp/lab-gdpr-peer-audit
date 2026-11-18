# Data processing brief - AI Search Visibility Agent (Barsha Mishra, Project 3)

*For the GDPR peer audit. Brief only: no lawful bases, DPIA analysis, findings or memo.*


*Written for a Data Protection Officer who has never seen the project.*

**Does the system process personal data at all?**
**Yes, but only a small amount, and mostly as a side effect.** The system is built to analyse **companies**: brands, their Google rankings, and how often AI assistants mention them. Most of the data is therefore company data, which GDPR does not cover. However, personal data enters the system in four places:
1. the **email address** of the person who requests the report
2. **names of people** in news articles and search results (journalists, authors, CEOs and spokespeople, reviewers, influencers)
3. **brand names that are also people**, for example a freelancer or personal brand entered as "brand" or "competitor"
4. **technical data** such as the requester's IP address, which the form host and the email image service may log

So "no personal data" would be the wrong conclusion. GDPR applies, but at low intensity.

**What personal data does it process?**
- Recipient email address, typed into the form
- Names and professional details of people mentioned in news articles (NewsAPI), Google search snippets (Serper) and AI answers (OpenAI)
- Article text that describes people, e.g. "CEO X resigns"
- Names of natural persons if a personal brand is analysed
- Technical data: IP address and timestamps in n8n execution logs and hosting logs (probable, not yet verified)
- The generated report, which can repeat any of the above

The system does **not** infer attributes about people. The scores are about brands.

**Where does the data come from?**
- **Directly from the user:** the form (brand, competitors, country, search questions, email).
- **From third-party sources:** Serper (Google results), NewsAPI (news articles), and OpenAI (AI-generated answers about the brands).
- **Not from company databases:** no customer database is used. The RAG knowledge base (Pinecone) contains only public SEO and AI-search guideline documents.

**What is the data used for?** One purpose each:
1. Delivering the report to the requester by email
2. Measuring brand visibility on Google and in AI answers, and collecting brand news
3. Generating the written report with an LLM
4. Fact-checking the report (LangGraph service)
5. Running and troubleshooting the workflow (execution logs)
6. *Planned, not built:* weekly scheduled runs and a results history in Google Sheets

**Who processes it?**
- My n8n workflow
- OpenAI (AI answer check, report writing, fact-checking)
- Serper and NewsAPI (they receive search queries containing brand names)
- Render (hosts the fact-checker)
- Gmail SMTP (sends the email; currently a **personal Gmail account**)
- QuickChart (receives chart data, i.e. brand scores, and the recipient's IP when the image loads)
- Pinecone (stores guideline documents only, no user data)

**Where is it stored and processed?**
- **Mostly in the US:** OpenAI, Serper, NewsAPI, Render, Google and QuickChart are US-based or US-hosted. Pinecone's region is not configured for the EU.
- **n8n execution data:** stored in **n8n Cloud** (n8n GmbH, a German company; the hosting region is documented by n8n and should be verified as EU) with the **default execution-saving settings**. No retention period is defined.
- **Reports:** stored as Markdown files and in the recipient's inbox.

**Does it make or assist decisions about people?**
**No.** It ranks and scores **brands**, not people, and it recommends SEO actions. A human (the marketing lead) reads the report and decides what to do. The only edge case is a personal brand: the system would then score one person's online visibility. That still has no legal or similarly significant effect on them.



**Architecture and data flow diagrams:** https://github.com/barsha-mishra/ai-search-visibility-agent (README, Architecture section)
