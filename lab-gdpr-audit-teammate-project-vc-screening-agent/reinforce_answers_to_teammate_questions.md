# Answers to Sandra's questions about my editorial agent

**Received:** 17 Nov 2026, 18:02, Sandra's clarifying questions log for her audit of my system.
**Use:** my answers as the builder, for debrief step 2. They also cover the Reinforce task: *which of her questions can I not answer from my current documentation?*

Every answer is checked against the code (commit `3939562`) and the 20 saved runs, unless marked otherwise. For each answer, **Documented?** says whether my *project documentation* already answered it before this lab.

---

**1. What does the agent send to Gemini and the search APIs?**

- **Tavily:**
  - the bookseller's query text;
  - for each book, the title and author (and the publisher, if there is no publisher domain).
- **Open Library:** the author's name and ISBNs. The User-Agent string is only the project name.
- **Google Books:** the ISBN, plus my API key in the URL.
- **Gemini:**
  - title, author and publisher;
  - up to 4,000 characters of the publisher's page;
  - the Google Books description and categories;
  - Tavily snippets;
  - the profile's values, sections and exclusions. The shop name is **not** sent.
  - For query rewriting: the previous query, the author, result titles and URLs, and the judge's reasons.

Example (no private details): the query is about a published author. Tavily receives that text and the author's name, and Gemini receives the book's publisher page.

**Can a query or profile include customer or staff details?** Technically yes, because the query is free text and is not filtered. In practice, no: the only profile is my own bookshop's, it contains no customer or staff data, and the bookshop has not opened yet.

**Special category data:** yes, incidentally. Retrieved text about a real person described in a non-fiction book reveals political militancy and torture. It is stored in 7 of the 20 run files.

*Documented?* **No.** The flows were only confirmed by reading the code during this lab.

**2. Lawful basis, and publishing run evidence on GitHub?**

- Before this lab, **no lawful basis was documented**.
- My self-audit now proposes **legitimate interests (Art. 6(1)(f))** for researching authors' published work, with a three-step balancing test.
- **Publishing the run files on GitHub was never assessed.** It is a separate purpose (portfolio/demo). I now mark it `TBD — legal review` and lean towards removing or redacting the files.

*Documented?* **No.** It is a confirmed documentation gap.

**3. Who controls the API accounts, and which terms apply?**

| Service | Account | What is known |
|---|---|---|
| Tavily | My own personal account, free plan (1,000 searches a month) [README] | US company. No DPA signed. Processing region and role (processor or independent controller) not confirmed |
| Gemini | My own API key from AI Studio, **free tier** [README] | Under Google's terms, content sent to the free tier can be used to improve Google's products, so there is no processor relationship. Whether billing has been switched on since then: **not confirmed** |
| Google Books | My own API key | No DPA |
| Open Library | No account | Public API |

No transfer safeguard is documented for any provider.

*Documented?* **Partly.** The plans are in the README; roles, locations, DPAs and transfers are not.

**4. What stays in the JSON logs and dossiers, and for how long? How would I handle an access or deletion request?**

- **Each JSON file keeps:**
  - query, author and search history;
  - the full Tavily results (URL, title, content);
  - book data, including publisher page text;
  - Gemini's judgments;
  - errors and tools used.
- The Markdown dossiers contain the report.
- **Retention:** none defined. The files have been kept since 10 Nov.
- **Location:** 20 JSON files and 11 dossiers, **public on GitHub**.
- **Access request:** I could search the files locally by name.
- **Deletion:**
  - local files: easy to delete;
  - GitHub: I would have to rewrite the repository history, and existing clones or forks cannot be recalled;
  - providers: no process.
- **There is no written request procedure.**

*Documented?* **No.**

**5. Expected scale, a DPIA, and combining information about the same person?**

- **Today:** one user (me), one profile and 20 runs, all about one author.
- **Planned Sprint 1:** my bookshop plus 2 Madrid bookshops, offered to about 10 [gtm_future_sprints.md].
- **Planned Sprint 2:** more bookshops, plus a request log per bookshop.
- **A DPIA had not been assessed before this lab.**
- **Combining sources:** yes. By design the agent combines Open Library, Google Books, Tavily and publisher pages **about the same author**.

My self-audit counts 2 EDPB criteria: combining datasets, and innovative technology. My position is a DPIA screening now and a full DPIA before the pilot.

*Documented?* **Partly.** The scale is in the sprint plan; the DPIA is not.

---

## Reinforce: what this tells me about my documentation

**Fully answered by my project documentation before this lab:** none of the five. Questions 3 and 5 were only partly answered (plans and scale).

Everything else I could only answer by **reading the code and the run files**. My project documents how the system works, not how it handles personal data.

The missing pieces are the accountability documents listed in my Lab 2 accountability test:
- record of processing;
- legitimate interests assessment;
- DPA and transfer checks;
- retention schedule;
- rights procedure;
- DPIA screening.
