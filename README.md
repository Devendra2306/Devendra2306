<div align="center">
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=260&color=0:0F172A,30:10B981,70:F59E0B,100:0F172A&text=DEVENDRA%20DIWAKAR&fontSize=55&fontAlignY=38&animation=fadeIn&fontColor=ffffff&desc=AI%2FML%20Engineer%20%7C%20Backend%20%2B%20Cloud%20Builder&descAlignY=58"/>
</div>

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&pause=1200&color=10B981&center=true&vCenter=true&width=900&lines=AI%2FML+Engineer+in+the+making;Backend+%2B+Cloud+Systems+Builder;AWS+%7C+Lambda+%7C+DynamoDB+%7C+S3;LangChain+%7C+RAG+%7C+Gemini+API;Turning+data+into+deployed+systems.;Build.+Deploy.+Learn.+Repeat."/>

<br>

<a href="mailto:devdiwakar27@gmail.com"><img src="https://img.shields.io/badge/Email-10B981?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/devendra-divakar-9649a32a4/"><img src="https://img.shields.io/badge/LinkedIn-F59E0B?style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<br><br>

<img src="https://komarev.com/ghpvc/?username=Devendra2306&label=PROFILE+VIEWS&color=10B981&style=for-the-badge"/>
<img src="https://img.shields.io/github/followers/Devendra2306?style=for-the-badge&color=F59E0B"/>

</div>

---

### About

BTech CS/IT, third year. I spend most of my time in the gap between "cool AI demo" and
"thing that runs reliably in production" — RAG pipelines that actually retrieve the right
chunk, Lambda triggers that don't silently fail, dashboards that stay fresh without
babysitting.

Right now I'm building toward AI/ML + backend internships for the 2026–27 cycle, and
positioning myself as **the engineer who ships the AI system end-to-end** — infra, API,
model, UI.

```text
Python                  ██████████ 100%
FastAPI / Node          █████████░  90%
AWS (Lambda/S3/DDB)     ████████░░  80%
LLM / RAG               █████████░  85%
React                   █████████░  85%
System Design           ██████░░░░  60%
Docker                  █████░░░░░  50%
```

---

## 🧠 Flagship: AI Document Intelligence Platform

A serverless document pipeline on AWS, built in deliberate phases — Phase 1 is live,
Phase 2 is next.

<img src="https://img.shields.io/badge/Status-Phase%201%20Complete-10B981?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Cloud-AWS-F59E0B?style=for-the-badge&logo=amazon-aws"/>
<img src="https://img.shields.io/badge/Frontend-React-10B981?style=for-the-badge&logo=react"/>

```text
React (drag-and-drop upload)
      │
      ▼ presigned URL
     S3  ──▶ Lambda trigger ──▶ DynamoDB (UUID + status)
      ▲                              │
      └────── API Gateway ◀──────────┘
              (client polls for status)
```

| Layer | Choice |
|---|---|
| Frontend | React, drag & drop upload |
| Storage | S3, presigned URLs |
| Compute | AWS Lambda |
| State | DynamoDB (per-document UUID + status) |
| API | API Gateway |
| Region | ap-south-1 |

**Roadmap**
- [x] Phase 1 — upload + tracking infrastructure
- [ ] Phase 2 — Textract extraction
- [ ] Phase 3 — semantic search + insights, multi-tenant auth

---

## 🚀 Other things I've shipped

**🌫️ AQI Monitoring Pipeline** — live air quality tracking, from historical batch loads
to real-time polling.
`Python → DuckDB → Dash → OpenAQ API`
Live map, trend charts, pollutant heatmap, data-freshness checks — deployed on Render's
free tier, which forced some real lessons in memory-constrained design.

**☁️ CloudVault** — a Drive-style file storage platform, built to actually understand
auth and relational modeling rather than just wire up a template.
`React → Node.js → PostgreSQL → Prisma → AWS S3`

---

## 🛠 Toolbox

<table>
<tr><td><b>Languages</b></td><td>
<img src="https://img.shields.io/badge/Python-10B981?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Java-F59E0B?style=flat-square&logo=openjdk&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-10B981?style=flat-square&logo=javascript&logoColor=white"/>
<img src="https://img.shields.io/badge/C++-F59E0B?style=flat-square&logo=c%2B%2B&logoColor=white"/>
</td></tr>
<tr><td><b>AI/ML</b></td><td>
<img src="https://img.shields.io/badge/LangChain-10B981?style=flat-square&logo=langchain&logoColor=white"/>
<img src="https://img.shields.io/badge/PyTorch-F59E0B?style=flat-square&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-10B981?style=flat-square&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-F59E0B?style=flat-square&logo=numpy&logoColor=white"/>
</td></tr>
<tr><td><b>Frontend</b></td><td>
<img src="https://img.shields.io/badge/React-10B981?style=flat-square&logo=react&logoColor=white"/>
<img src="https://img.shields.io/badge/TailwindCSS-F59E0B?style=flat-square&logo=tailwind-css&logoColor=white"/>
<img src="https://img.shields.io/badge/Vite-10B981?style=flat-square&logo=vite&logoColor=white"/>
</td></tr>
<tr><td><b>Backend</b></td><td>
<img src="https://img.shields.io/badge/Node.js-F59E0B?style=flat-square&logo=node.js&logoColor=white"/>
<img src="https://img.shields.io/badge/Express-10B981?style=flat-square&logo=express&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-F59E0B?style=flat-square&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-10B981?style=flat-square&logo=django&logoColor=white"/>
</td></tr>
<tr><td><b>Cloud & DevOps</b></td><td>
<img src="https://img.shields.io/badge/AWS-F59E0B?style=flat-square&logo=amazon-aws&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-10B981?style=flat-square&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Render-F59E0B?style=flat-square&logo=render&logoColor=white"/>
<img src="https://img.shields.io/badge/Vercel-10B981?style=flat-square&logo=vercel&logoColor=white"/>
</td></tr>
<tr><td><b>Database</b></td><td>
<img src="https://img.shields.io/badge/PostgreSQL-F59E0B?style=flat-square&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/DynamoDB-10B981?style=flat-square&logo=amazon-dynamodb&logoColor=white"/>
<img src="https://img.shields.io/badge/Prisma-F59E0B?style=flat-square&logo=prisma&logoColor=white"/>
<img src="https://img.shields.io/badge/DuckDB-10B981?style=flat-square&logo=duckdb&logoColor=white"/>
</td></tr>
</table>

---

## 🎯 2026–27 Goals

- [x] Ship Phase 1 of the AI Document Intelligence Platform
- [x] Build a deployable RAG project as a portfolio centerpiece
- [ ] Textract integration (Phase 2)
- [ ] Go deeper on AWS + system design fundamentals
- [ ] Land an AI/ML engineering internship

---

## 📊 GitHub Analytics

<p align="center">
<img height="165" src="https://github-readme-stats.vercel.app/api?username=Devendra2306&show_icons=true&theme=holi&hide_border=true"/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Devendra2306&layout=compact&theme=holi&hide_border=true"/>
</p>

<p align="center">
<img src="https://streak-stats.demolab.com?user=Devendra2306&theme=green-orange&hide_border=true"/>
</p>

<p align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=Devendra2306&theme=react-dark&color=10B981&line=F59E0B&point=ffffff"/>
</p>

---

## 🤝 Let's Connect

<p align="center">
<a href="mailto:devdiwakar27@gmail.com"><img src="https://img.shields.io/badge/Email-10B981?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/devendra-divakar-9649a32a4/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-F59E0B?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
</p>

<div align="center">

### "Build. Deploy. Learn. Repeat."

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:0F172A,50:10B981,100:0F172A&section=footer"/>

</div>
