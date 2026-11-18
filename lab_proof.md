# lab_proof.md – GDPR audit of my partner's project (Week 7)
**Auditor:** Murat Çömez · **Partner (builder):** Max · **Project audited:** Career Intelligence Agent (AI career guidance for job seekers; Python, LangGraph, Streamlit, OpenAI, Pinecone, Tavily)

## File map
| File | What it contains |
|---|---|
| [`teammate_gdpr_data_brief_career_intelligence_agent.pdf`](teammate_gdpr_data_brief_career_intelligence_agent.pdf) | Input: partner's data processing brief (shared with permission) |
| [`gdpr_peer_audit_career_intelligence_agent.md`](gdpr_peer_audit_career_intelligence_agent.md) | Full analysis: inventory, roles, lawful basis, risks and rights, law tracking, findings, questions log |

## 1. Workflow
Received the brief only → ran the same five phases as my own GDPR self-audit → logged clarifying questions → findings and recommendation.

## 2. One run – input
Partner's claim in class: "our tool uses no personal data." Brief §1: the system processes name, employment history, education, skills and generates matching scores about the candidate.

## 3. Evidence it produced
Inventory rows 1–5 show identifiable personal data and inferred profiling data; row 4 shows possible Art. 9 data in free text; §5 of the brief confirms no retention policy and unverified transfers.

## 4. Final output
GDPR applies in full in production. Controller = app operator; processors = OpenAI (+ Tavily, hosting). Basis: **Art. 6(1)(b)** contract. **DPIA likely required.** Recommendation: **proceed with conditions** (6 findings).

## 5. Failure or limitation
I could not check logs, user accounts or actual API requests, which is what we agreed would confirm the "no personal data" claim. Without code access, rows 6–8 of the inventory and finding 6 are based on assumptions in the questions log.
