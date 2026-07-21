<div align="center">
<img width="100%" src="https://capsule-render.vercel.app/api?type=soft&height=220&color=0:030712,50:0891B2,100:030712&text=DEVENDRA%20DIWAKAR&fontSize=48&fontAlignY=45&fontColor=E5FFFC&animation=twinkling"/>

### `AI/ML Engineer` · `Backend Systems` · `Cloud (AWS)`

![](https://img.shields.io/badge/status-open_to_internships-0891B2?style=flat-square)
![](https://img.shields.io/badge/focus-2026--27_placements-7C3AED?style=flat-square)

</div>

---

### 📡 Signal

I don't build to fill a contributions graph. I pick problems where an AI/ML idea has to survive contact with a real backend and real infrastructure — queues, storage, latency, cost. If it doesn't deploy, it doesn't count.

---

### 🗂️ What I'm running right now

| | |
|---|---|
| **Building** | AI Document Intelligence Platform — serverless AWS pipeline (S3 → Lambda → DynamoDB → Textract next) |
| **Shipped** | RAG Document Q&A — LangChain + ChromaDB + Gemini + FastAPI |
| **Shipped** | AQI Monitoring Pipeline — DuckDB ELT + live OpenAQ ingestion + Dash dashboard |
| **Learning** | System design, Docker, deeper AWS (IAM, Textract, Step Functions) |
| **Year** | BTech CS/IT, entering 3rd year |

---

### 🧩 Case file — AI Document Intelligence Platform

The project I'd point a recruiter to first.

**The problem:** most student "AI projects" bolt an API call onto a form. I wanted the boring-but-real part — presigned uploads, event-driven processing, state tracking — done properly, *then* the AI layer on top.

**Phase 1 — shipped:**
- React drag-and-drop upload, no server round-trip for the file itself
- S3 presigned URLs for direct client → bucket upload
- Lambda + DynamoDB for UUID-based document tracking with status progression
- API Gateway fronting the whole thing, deployed in `ap-south-1`

**Phase 2 — in progress:**
- S3 upload event triggers a Lambda that calls AWS Textract for extraction

```
[Client] → presigned URL → [S3] → trigger → [Lambda] → [DynamoDB status]
                                                ↓
                                          [API Gateway] → client polls status
```

---

### 🔍 Other systems I've built

**RAG Document Q&A System**
Upload a document, ask it questions in plain English. Chunking + embeddings in ChromaDB, retrieval-grounded answers via Gemini, served through FastAPI with a React front end. Built as the portfolio piece that proves I understand retrieval, not just prompting.

**AQI Monitoring Pipeline**
A full ELT pipeline, not a script — historical batch loads from S3, live polling against the OpenAQ API, all queried through DuckDB. Dash dashboard on top shows a live map, pollutant trends, a heatmap, and a data-freshness indicator so you can tell if the pipeline is actually alive. Tuned to survive on Render's free-tier memory limits.

**CloudVault**
Google Drive-style storage platform — React, Node.js, PostgreSQL, Prisma, AWS S3. Where I learned relational schema design and object storage patterns before taking them into the AWS-native projects above.

---

### ⚙️ Stack, by where I use it

**Reach for AI/ML:** Python · LangChain · PyTorch · Pandas · NumPy · Gemini API

**Reach for backend:** Node.js · Express · FastAPI · Django · Java

**Reach for cloud/infra:** AWS (S3, Lambda, DynamoDB, API Gateway) · Docker · Render

**Reach for data:** PostgreSQL · Prisma · DuckDB · ChromaDB

**Reach for frontend (when the project needs one):** React · Tailwind CSS · Vite

---

### 📈 Where the effort's going

```
AI/ML & RAG systems     ████████░░  build in progress
AWS-native backend      ████████░░  build in progress
System design           █████░░░░░  studying
DSA                     ███████░░░  ongoing
```

---

### 🎯 Next 12 months

- [ ] Finish Textract phase of the Document Intelligence Platform
- [ ] Land an AI/ML or backend engineering internship
- [ ] Get comfortable enough with system design to defend architecture choices in interviews
- [ ] Position clearly as an AI/ML-focused backend engineer, not a generalist

---

<div align="center">

[![Email](https://img.shields.io/badge/Email-devdiwakar27%40gmail.com-0891B2?style=flat-square&logo=gmail&logoColor=white)](mailto:devdiwakar27@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0891B2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devendra-divakar-9649a32a4/)

</div>

<div align="center">
<img src="https://github-readme-stats.vercel.app/api?username=Devendra2306&show_icons=true&theme=tokyonight&hide_border=true&hide_title=true" height="150"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Devendra2306&layout=compact&theme=tokyonight&hide_border=true" height="150"/>
</div>

<div align="center">
<img src="https://streak-stats.demolab.com?user=Devendra2306&theme=tokyonight&hide_border=true"/>
</div>
