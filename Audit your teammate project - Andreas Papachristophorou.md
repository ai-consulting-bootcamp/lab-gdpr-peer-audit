# W7D3_LAB_GDPR_Audit your teammate's project
- Week 7 / Day 3
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-08-19
---

## Data Processing Brief

EU Policy RAG Assistant

**Purpose:** This document describes the data flows associated with the proposed EU Policy RAG Assistant and is intended to support review by the Data Protection Officer (DPO).

1. System overview: The EU Policy RAG Assistant is an internal employee-facing AI system that enables staff to ask questions about EU legislation, policy guidance, and internal compliance documents through a conversational interface. The system retrieves relevant information from a controlled document repository and generates responses based only on approved source material. The system is intended to reduce routine requests to the policy department and provide employees with faster access to existing information. It is not intended to make decisions on behalf of the organization.

2. What personal data does the system process? The system is designed primarily to process organizational policy documents rather than personal data. However, the following personal data may be processed as part of normal operation:

Employee interaction data

- Employee name or user ID (through Slack or organizational authentication)
- Employee email address or account identifier
- Department/team information where available
- Chat messages and questions submitted by employees

Text content

- Questions entered by employees
- Conversation history, if retained
- References to named individuals contained in policy documents
- Contact details included in policy documents

Technical and operational data

- User account information
- Timestamps
- Workflow logs
- Error logs
- API usage logs

Inferred data: The system does not intentionally create profiles, scores, rankings, or inferred attributes about employees. However, logs may indirectly reveal employee interests, policy concerns, or areas of work based on submitted questions. No special-category personal data (GDPR Article 9) is intentionally processed as part of the system's intended purpose.

3. Where does the data come from? The system receives data from the following sources: Employees Employees submit questions directly through the chat interface. Organizational document repositories Approved policy documents are stored in a designated Google Drive folder and are used as the knowledge base. Enterprise systems User identity information may be obtained through Slack, Google Workspace, or organizational authentication systems. System-generated data Operational logs, retrieval metadata, and usage statistics are generated automatically by the workflow. The system is not intended to collect personal data from public internet sources or external third-party databases.

4. What is the data used for? The system processes data for the following purposes:

1. **Answer employee questions** using approved policy and legislative documents.
2. **Retrieve relevant documents** from the knowledge base.
3. **Generate grounded AI responses** based on retrieved content.
4. **Provide escalation to policy staff** where information is insufficient.
5. **Authenticate users and manage access controls.**
6. **Operate, secure, and troubleshoot the system.**
7. **Monitor system performance and improve retrieval quality.**

The system is not intended to evaluate employees, monitor performance, rank individuals, or make decisions affecting employment.

5. Who processes the data? The following parties may process data: Entity Role Client organization Controller / system owner Employees End users Policy departmentHuman reviewers and content owners n8n Workflow orchestration OpenAI Language model provider (if API used) Pinecone Vector database provider Google Drive / Google Workspace Document storageSlackUser interface and messaging platformIT administrators System support and maintenanceIf OpenAI API services are used, employee questions and retrieved document content may be sent to OpenAI for response generation. If local models are deployed in future, this data flow may change.6. Where is the data stored and processed? Data may be stored and processed in several locations depending on the final architecture:

- **Google Drive:** Policy documents
- **Pinecone:** Vectorized document chunks and metadata
- **n8n:** Workflow execution and logs
- **Slack:** User messages
- **OpenAI:** Model processing (if API architecture is used)

Processing may occur in the EU or outside the EU depending on vendor hosting arrangements. International transfers and transfer mechanisms should be reviewed before production deployment.

7. Does the system make or assist decisions affecting people? The system does **not make automated decisions about individuals**. The system assists employees by retrieving information and generating answers to policy questions. Responses are intended as informational support only. Where the system cannot provide sufficient information, users are directed to the policy department for human support. Policy specialists review system quality during implementation and remain responsible for authoritative interpretation of legislation and organizational policy.

8. Summary The EU Policy RAG Assistant is an internal knowledge-retrieval system that processes employee questions and organizational policy documents to provide faster access to information. The principal data protection considerations are:

- Processing of employee chat content
- Potential personal data contained in policy documents
- Use of third-party AI and cloud services
- International data transfers
- Logging and retention
- Access controls

The system is not intended to profile employees or make decisions affecting their rights, employment, or access to services.

## Phase 1: Read and annotate

### First read — quick understanding

**What I think the teammate’s system does:**

The system is used mainly as an internal company decision support tool to assist employees in evaluating EU policies and answering questions. Its main purpose is to alleviate pressure and reduce the workload on the policy department. The system’s design and intended use do not target personal data, but we cannot exclude the possibility of accidental personal data processing and user data logging.

### Second read — annotations

#### Personal data categories found

- Employee identity data — employee name, user ID, email address, account identifier
- Organisational role data — department/team information
- Employee input data — chat messages, questions submitted by employees, conversation history if retained
- Document-content personal data — references to named individuals and contact details inside policy documents
- Technical and operational data — timestamps, workflow logs, error logs, API usage logs, retrieval metadata, usage statistics
- Inferred / indirect data — logs may indirectly reveal employee interests, policy concerns, or areas of work

#### Special-category data

Special-category data means very sensitive data under GDPR, like health, religion, biometrics, political opinions, etc.

Based on the brief, the best answer is: **none intentionally processed**. However, because employees can type free-text questions, special-category data could accidentally appear in a question or in a policy document. So I would not write “none” alone; I would write “none intentionally processed, but cannot fully exclude accidental or inferable special-category data.”

| Possible special-category data | Why it may be special-category data | Confirmed or inferable? |
| --- | --- | --- |
| None intentionally processed | The brief states that no GDPR Article 9 special-category personal data is intentionally processed. However, employees may enter free-text questions, and policy documents may contain references to individuals, so accidental inclusion cannot be fully excluded. | Cannot determine fully from brief |

#### Unclear points

| Unclear point | Why it matters | Assumption for now |
| --- | --- | --- |
| Exact retention period for chat messages, conversation history, workflow logs, and API logs is not stated. | Retention affects storage limitation and data minimisation. Personal data should not be kept longer than needed. | Assume logs and conversation history may be retained unless a deletion schedule is confirmed. |
| Vendor hosting locations are not confirmed for OpenAI, Pinecone, Slack, Google Drive, and n8n. | This matters for international transfers, because processing may happen outside the EU and may require transfer safeguards. | Assume possible non-EU processing until vendor regions and transfer mechanisms are confirmed. |
| It is unclear whether employee questions are used to improve retrieval quality, monitor usage, or train/improve models. | This matters for purpose limitation and transparency. Data collected to answer questions should not be reused for a new purpose without proper notice and lawful basis. | Assume usage is limited to operating and improving retrieval quality, not employee profiling or model training, unless confirmed otherwise. |
| DPAs with processors and sub-processors are not evidenced in the brief. | If vendors process personal data for the controller, GDPR requires appropriate processor contracts. | Assume DPAs are needed with n8n, OpenAI if API used, Pinecone, Slack, Google Workspace, and any hosting provider. |
| Access controls for policy documents and generated answers are not described in detail. | This matters because employees should only access documents they are authorised to see. Weak access controls could expose internal or personal data. | Assume access is based on existing organisational authentication, but document-level permission checks need confirmation. |

#### EU border / non-EU vendor data flows

| Data flow | EU border crossed? | Non-EU vendor involved? | Evidence from brief |
| --- | --- | --- | --- |
| Vendor hosting for OpenAI, Pinecone, Slack, Google Drive, and n8n. | Cannot determine, but possibly yes. | Yes. These appear to be third-party vendors, including AI, cloud, messaging, vector database, and workflow providers. | The brief mentions that these services may be used, but it does not confirm their hosting locations or transfer mechanisms. |

#### Possible purpose limitation issues

| Original purpose | New / additional purpose | Potential issue? |
| --- | --- | --- |
| Employee questions are used to retrieve relevant information and produce answers to EU policy questions. | The same questions may later be used to train the system or improve its accuracy.
It can also be used to monitor and evaluate the employees performance. | Employees may not have been clearly informed about this additional use. This could raise transparency and purpose limitation concerns, including the right to be informed under Articles 13–14 and, depending on the situation, the right to restriction under Article 18. |

---

## Phase 2: Personal data and role map

### Personal data summary

| Data category | Source | Purpose(s) | Crosses EU border? | Special category? |
| --- | --- | --- | --- | --- |
| Employee identity data, such as name, user ID, email address, and account identifier | Slack, Google Workspace, or organisational authentication systems | Authenticate users, manage access controls, operate the system, and link questions to authorised users | Cannot determine; possible yes depending on vendor hosting locations | No |
| Department or team information | Organisational authentication systems or employee profile data | Manage access controls and understand which users are permitted to access policy information | Cannot determine; possible yes depending on vendor hosting locations | No |
| Employee questions, chat messages, and conversation history if retained | Employees using the chat interface | Answer employee questions, retrieve relevant documents, generate grounded AI responses, and provide escalation to policy staff | Cannot determine; possible yes if sent to OpenAI, Slack, n8n, or other non-EU hosted services | Not intentionally, but special-category data could be accidentally included in free-text questions |
| Technical and operational data, such as timestamps, workflow logs, error logs, API usage logs, retrieval metadata, and usage statistics | Automatically generated by Slack, n8n, OpenAI, Pinecone, Google Workspace, or system infrastructure | Operate, secure, troubleshoot, monitor performance, and improve retrieval quality | Cannot determine; possible yes depending on vendor hosting and logging locations | No, but logs may indirectly reveal employee interests, policy concerns, or areas of work |

### Role map

| Entity | Role | Processing activity | DPA needed? |
| --- | --- | --- | --- |
| Client organisation | Controller / system owner | Decides why and how the EU Policy RAG Assistant is used, what documents are included, who may access it, and how employee data is processed. | No DPA needed with itself, but it must document its controller responsibilities. |
| Employees | Data subjects / end users | Submit questions, use the chat interface, and generate interaction data, identity data, and usage logs. | No. Employees are not processors; they are the people whose data may be processed. |
| Third-party vendors: n8n, OpenAI if API used, Pinecone, Google Drive / Google Workspace, and Slack | Processors or sub-processors; exact roles depend on contracts, hosting setup, and service settings | Provide workflow orchestration, AI response generation, vector search, document storage, identity services, chat interface, message handling, and system logs. | Yes. Appropriate DPAs or cloud processing terms should be in place if these vendors process personal data for the client. |

### International transfer notes

| Transfer identified | Transfer mechanism needed | Evidence mechanism is in place? |
| --- | --- | --- |
| Personal data may be transferred to third-party vendors such as OpenAI, Pinecone, Slack, Google Drive / Google Workspace, and n8n if the production system is cloud-hosted or if these services process data outside the EU. | Cannot determine from the brief. Depending on vendor locations, appropriate safeguards may be needed, such as Standard Contractual Clauses (SCCs), an adequacy decision, or another valid transfer mechanism. | No. The brief says international transfers should be reviewed before production deployment, but it does not provide evidence that a transfer mechanism is already in place. |

---

## Phase 3: Clarifying questions log

Write three to five questions you would ask before finalising your audit.

| Question | What I need to know | Why it matters under GDPR | Provisional assumption |
| --- | --- | --- | --- |
| 1. What lawful basis will the client rely on for processing employee identity data, questions, chat messages, and logs? | Whether the organisation has identified a lawful basis for each purpose, such as answering questions, authentication, troubleshooting, and improving retrieval quality. | Lawful basis is required for all personal data processing under GDPR Article 6. Different purposes may need different lawful bases. | Assume the likely lawful basis is legitimate interests for internal knowledge support, but this must be documented and balanced against employee rights. |
| 2. Will employee questions, conversation history, or logs be retained, and for how long? | The retention period for chat messages, conversation history, workflow logs, API logs, and retrieval metadata. | This matters for storage limitation and data minimisation. Personal data should not be kept longer than necessary. | Assume logs and conversation history may be retained unless a deletion schedule is confirmed. |
| 3. Are employee questions or retrieved document content sent to OpenAI, Pinecone, Slack, Google Drive / Google Workspace, n8n, or any other cloud vendor outside the EU? | The hosting locations, vendor regions, and whether any personal data leaves the EU. | This matters for international transfer compliance. If data leaves the EU, a valid transfer mechanism may be needed. | Assume possible non-EU processing until vendor locations and transfer safeguards are confirmed. |
| 4. Are DPAs or equivalent cloud processing terms in place with all vendors that process personal data? | Whether contracts exist with n8n, OpenAI if API used, Pinecone, Slack, Google Workspace, and any hosting provider. | GDPR requires appropriate processor agreements when vendors process personal data on behalf of the controller. | Assume DPAs are needed and must be verified before production deployment. |
| 5. Will employee questions or logs be used only to operate the system, or also to improve the system, train models, monitor employees, or evaluate performance? | Whether the data will be reused for a new purpose beyond answering policy questions. | This affects purpose limitation, transparency, and employee rights. Employees must be clearly informed if their data is reused for monitoring, improvement, or training. | Assume the system is not intended to monitor or evaluate employees, but improvement use needs clearer documentation. |

---

## Phase 4: Audit report