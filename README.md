<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=280&color=0:020617,30:0EA5E9,60:06B6D4,100:020617&text=SYSTEM%20ONLINE&fontSize=42&fontAlignY=32&animation=fadeIn&fontColor=F8FAFC&desc=DEVENDRA%20DIWAKAR%20%E2%80%94%20AI%20INFRASTRUCTURE%20ENGINEER&descAlignY=52&descSize=18"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=2600&pause=900&color=38BDF8&center=true&vCenter=true&width=800&lines=Booting+AI+Infrastructure+Stack...;Compiling+Production-Grade+Systems...;Status%3A+Operational;Region%3A+ap-south-1;Mission%3A+Deploy+Production+AI+Systems"/>

<br>

<img src="https://img.shields.io/badge/STATUS-OPERATIONAL-10B981?style=for-the-badge&labelColor=020617"/>
<img src="https://img.shields.io/badge/REGION-AP--SOUTH--1-0EA5E9?style=for-the-badge&labelColor=020617"/>
<img src="https://img.shields.io/badge/UPTIME-100%25-38BDF8?style=for-the-badge&labelColor=020617"/>

</div>

<br>

---

<div align="center">

## ▌ 01 — SYSTEM OVERVIEW

</div>

<table width="100%">
<tr>
<td width="50%" valign="top">

**OPERATOR**
```
Devendra Diwakar
```
**CLASSIFICATION**
```
AI/ML Engineer · Backend + Cloud Builder
```
**CURRENT OBJECTIVE**
```
AI/ML + Backend Internship — 2026–27 Cycle
```

</td>
<td width="50%" valign="top">

**DEPLOYMENT REGION**
```
ap-south-1 (AWS)
```
**PRIMARY STACK**
```
Python · FastAPI · AWS · LangChain · React
```
**CURRENT BUILD**
```
AI Document Intelligence Platform — Phase 2
```

</td>
</tr>
</table>

<div align="center">

> **Mission Statement**
> Closing the gap between *"cool AI demo"* and *"thing that runs reliably in production."*
> RAG pipelines that retrieve the right chunk. Lambda triggers that don't silently fail. Systems that ship end-to-end — infra, API, model, UI.

</div>

---

<div align="center">

## ▌ 02 — LIVE SYSTEM STATUS

</div>

<table width="100%" align="center">
<tr>
<td align="center" width="16%"><b>CLOUD</b><br><img src="https://img.shields.io/badge/ONLINE-10B981?style=flat-square&labelColor=020617"/></td>
<td align="center" width="16%"><b>AI PIPELINE</b><br><img src="https://img.shields.io/badge/ACTIVE-0EA5E9?style=flat-square&labelColor=020617"/></td>
<td align="center" width="16%"><b>BACKEND</b><br><img src="https://img.shields.io/badge/HEALTHY-10B981?style=flat-square&labelColor=020617"/></td>
<td align="center" width="16%"><b>DATABASE</b><br><img src="https://img.shields.io/badge/SYNCED-06B6D4?style=flat-square&labelColor=020617"/></td>
<td align="center" width="16%"><b>MONITORING</b><br><img src="https://img.shields.io/badge/RUNNING-38BDF8?style=flat-square&labelColor=020617"/></td>
<td align="center" width="16%"><b>SECURITY</b><br><img src="https://img.shields.io/badge/PASS-10B981?style=flat-square&labelColor=020617"/></td>
</tr>
</table>

---

<div align="center">

## ▌ 03 — COMMAND CENTER

</div>

```bash
root@devendra:~$ ./mission_status.sh

> CURRENT MISSION
  Building production-ready AI systems using
  AWS Lambda, FastAPI, LangChain and React.

> DEPLOYMENT TARGET
  AI/ML Internship — 2026–27

> ACTIVE FOCUS
  Serverless document intelligence · RAG retrieval
  accuracy · Cloud-native system design

[OK] All subsystems nominal.
```

---

<div align="center">

## ▌ 04 — FLAGSHIP DEPLOYMENT

### AI Document Intelligence Platform

<img src="https://img.shields.io/badge/PHASE_1-COMPLETE-10B981?style=for-the-badge&labelColor=020617"/>
<img src="https://img.shields.io/badge/PHASE_2-IN_PROGRESS-F59E0B?style=for-the-badge&labelColor=020617"/>
<img src="https://img.shields.io/badge/CLOUD-AWS-0EA5E9?style=for-the-badge&logo=amazon-aws&labelColor=020617"/>

</div>

A serverless document intelligence pipeline, built in deliberate phases on AWS — designed to take a raw uploaded document all the way to searchable, structured insight.

```text
   React (Drag & Drop Upload)
            │
            ▼  presigned URL
        API Gateway
            │
            ▼
           S3  ───────────▶  Lambda Trigger
            │                     │
            ▼                     ▼
        Textract            DynamoDB (UUID + Status)
     (Phase 2 — WIP)              │
            │                     ▼
            ▼              Client Status Poll
     Embedding Layer
            │
            ▼
      Vector Database
            │
            ▼
          LLM Layer
            │
            ▼
       Insight Dashboard
```

<table width="100%">
<tr><th>MODULE</th><th>SPECIFICATION</th></tr>
<tr><td>Architecture</td><td>Event-driven, serverless, per-document state tracking via UUID</td></tr>
<tr><td>Scaling</td><td>Lambda concurrency scales per upload — no persistent compute cost</td></tr>
<tr><td>Security</td><td>Presigned S3 URLs — no direct client-to-bucket credentials exposed</td></tr>
<tr><td>Performance</td><td>Async polling via API Gateway, no long-held client connections</td></tr>
<tr><td>Challenge</td><td>Keeping retrieval precision high once Phase 2 introduces OCR noise</td></tr>
</table>

**ROADMAP**

- [x] `PHASE 1` — Upload + tracking infrastructure (S3 · Lambda · DynamoDB · API Gateway)
- [ ] `PHASE 2` — Textract extraction pipeline
- [ ] `PHASE 3` — Semantic search, insight generation, multi-tenant auth

---

<div align="center">

## ▌ 05 — ACTIVE DEPLOYMENTS

</div>

<table width="100%">
<tr>
<td width="50%" valign="top">

**DEPLOYMENT: CLOUDVAULT**
<br>
<img src="https://img.shields.io/badge/STATUS-PRODUCTION-10B981?style=flat-square&labelColor=020617"/>

```
Stack   React · Node.js · PostgreSQL
        Prisma · AWS S3

Mission Drive-inspired cloud storage
        platform, built to actually
        understand auth and relational
        modeling — not just wire up
        a template.
```

</td>
<td width="50%" valign="top">

**DEPLOYMENT: AQI MONITORING PLATFORM**
<br>
<img src="https://img.shields.io/badge/STATUS-OPERATIONAL-0EA5E9?style=flat-square&labelColor=020617"/>

```
Stack   Python · DuckDB · Dash
        OpenAQ API

Mission Real-time + historical air
        quality analytics. Live map,
        trend charts, pollutant
        heatmap, data-freshness
        checks — deployed on a
        memory-constrained free tier.
```

</td>
</tr>
</table>

---

<div align="center">

## ▌ 06 — TECH ECOSYSTEM

</div>

<table width="100%">
<tr><td width="20%"><b>ARTIFICIAL INTELLIGENCE</b></td><td>
<img src="https://img.shields.io/badge/LangChain-0EA5E9?style=flat-square&logo=langchain&logoColor=white"/>
<img src="https://img.shields.io/badge/RAG-06B6D4?style=flat-square"/>
<img src="https://img.shields.io/badge/Gemini_API-38BDF8?style=flat-square&logo=googlegemini&logoColor=white"/>
<img src="https://img.shields.io/badge/PyTorch-F59E0B?style=flat-square&logo=pytorch&logoColor=white"/>
</td></tr>
<tr><td><b>BACKEND</b></td><td>
<img src="https://img.shields.io/badge/FastAPI-0EA5E9?style=flat-square&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Node.js-10B981?style=flat-square&logo=node.js&logoColor=white"/>
<img src="https://img.shields.io/badge/Express-06B6D4?style=flat-square&logo=express&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-38BDF8?style=flat-square&logo=django&logoColor=white"/>
</td></tr>
<tr><td><b>CLOUD & DEVOPS</b></td><td>
<img src="https://img.shields.io/badge/AWS_Lambda-F59E0B?style=flat-square&logo=awslambda&logoColor=white"/>
<img src="https://img.shields.io/badge/S3-0EA5E9?style=flat-square&logo=amazons3&logoColor=white"/>
<img src="https://img.shields.io/badge/API_Gateway-06B6D4?style=flat-square&logo=amazonapigateway&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-38BDF8?style=flat-square&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Render-10B981?style=flat-square&logo=render&logoColor=white"/>
<img src="https://img.shields.io/badge/Vercel-F8FAFC?style=flat-square&logo=vercel&logoColor=black"/>
</td></tr>
<tr><td><b>FRONTEND</b></td><td>
<img src="https://img.shields.io/badge/React-0EA5E9?style=flat-square&logo=react&logoColor=white"/>
<img src="https://img.shields.io/badge/TailwindCSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white"/>
<img src="https://img.shields.io/badge/Vite-38BDF8?style=flat-square&logo=vite&logoColor=white"/>
</td></tr>
<tr><td><b>DATABASES</b></td><td>
<img src="https://img.shields.io/badge/PostgreSQL-0EA5E9?style=flat-square&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/DynamoDB-F59E0B?style=flat-square&logo=amazondynamodb&logoColor=white"/>
<img src="https://img.shields.io/badge/Prisma-06B6D4?style=flat-square&logo=prisma&logoColor=white"/>
<img src="https://img.shields.io/badge/DuckDB-38BDF8?style=flat-square&logo=duckdb&logoColor=white"/>
</td></tr>
<tr><td><b>LANGUAGES</b></td><td>
<img src="https://img.shields.io/badge/Python-0EA5E9?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F59E0B?style=flat-square&logo=javascript&logoColor=white"/>
<img src="https://img.shields.io/badge/Java-06B6D4?style=flat-square&logo=openjdk&logoColor=white"/>
<img src="https://img.shields.io/badge/C++-38BDF8?style=flat-square&logo=c%2B%2B&logoColor=white"/>
</td></tr>
</table>

---

<div align="center">

## ▌ 07 — MISSION LOG

</div>

```text
2024 ─┬─ Frontend Fundamentals
      │
      ├─ Backend Systems (Node · FastAPI)
      │
      ├─ Cloud Infrastructure (AWS)
      │
      ├─ Applied AI (LangChain · RAG)
      │
      ├─ Production Systems (CloudVault · AQI Pipeline)
      │
NOW ──┴─ AI Document Intelligence Platform (Phase 2)
```

---

<div align="center">

## ▌ 08 — SYSTEM METRICS

<img height="165" src="https://github-readme-stats.vercel.app/api?username=Devendra2306&show_icons=true&theme=react&bg_color=020617&title_color=38BDF8&icon_color=0EA5E9&text_color=F8FAFC&border_color=0EA5E9&hide_border=false"/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Devendra2306&layout=compact&theme=react&bg_color=020617&title_color=38BDF8&text_color=F8FAFC&border_color=0EA5E9&hide_border=false"/>

<br>

<img src="https://streak-stats.demolab.com?user=Devendra2306&theme=dark&background=020617&stroke=0EA5E9&ring=38BDF8&fire=F59E0B&currStreakLabel=F8FAFC&border=0EA5E9"/>

<br>

<img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=Devendra2306&bg_color=020617&color=38BDF8&line=0EA5E9&point=F8FAFC&area_color=06B6D4&area=true&hide_border=true"/>

</div>

---

<div align="center">

## ▌ 09 — RADAR: ACTIVE LEARNING

</div>

<table width="100%">
<tr>
<td align="center" width="14%"><b>AWS</b><br><sub>tracking</sub></td>
<td align="center" width="14%"><b>System Design</b><br><sub>tracking</sub></td>
<td align="center" width="14%"><b>Distributed Systems</b><br><sub>tracking</sub></td>
<td align="center" width="14%"><b>Advanced RAG</b><br><sub>tracking</sub></td>
<td align="center" width="14%"><b>LLMOps</b><br><sub>tracking</sub></td>
<td align="center" width="14%"><b>Vector Search</b><br><sub>tracking</sub></td>
<td align="center" width="14%"><b>Multi-Agent AI</b><br><sub>tracking</sub></td>
</tr>
</table>

---

<div align="center">

## ▌ 10 — COMMUNICATION CHANNEL

<table>
<tr>
<td align="center">
<a href="mailto:devdiwakar27@gmail.com">
<img src="https://img.shields.io/badge/EMAIL-devdiwakar27%40gmail.com-0EA5E9?style=for-the-badge&logo=gmail&logoColor=white&labelColor=020617"/>
</a>
</td>
</tr>
<tr>
<td align="center">
<a href="https://www.linkedin.com/in/devendra-divakar-9649a32a4/">
<img src="https://img.shields.io/badge/LINKEDIN-Connect-06B6D4?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=020617"/>
</a>
</td>
</tr>
<tr>
<td align="center">
<a href="https://github.com/Devendra2306">
<img src="https://img.shields.io/badge/GITHUB-Devendra2306-38BDF8?style=for-the-badge&logo=github&logoColor=white&labelColor=020617"/>
</a>
</td>
</tr>
</table>

</div>

---

<div align="center">

```text
> Build.
> Deploy.
> Scale.
> Repeat.

SYSTEM STATUS: ONLINE
```

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:020617,50:0EA5E9,100:020617&section=footer"/>

</div>
