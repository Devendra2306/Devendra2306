#!/usr/bin/env python3
"""Rebuild README.md with an incredibly unique Neofetch/Animated Hacker aesthetic."""
import datetime as dt
import json
import os
import urllib.request
from pathlib import Path
import urllib.parse
import yaml

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def gh(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-readme-bot"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    try:
        with urllib.request.urlopen(urllib.request.Request(API + path, headers=headers), timeout=20) as r:
            return json.load(r)
    except Exception as e:
        print(f"[warn] {path}: {e}")
        return None

def build_projects(cfg, repos_by_name):
    cards, seen = [], set()
    def make(repo_full, override, api):
        api = api or {}
        name = repo_full.split("/")[-1]
        return {
            "name": name,
            "full_name": repo_full,
            "title": override.get("title") or name,
            "url": api.get("html_url") or f"https://github.com/{repo_full}",
            "summary": override.get("summary") or api.get("description") or "",
            "stack": override.get("stack") or [],
        }

    for p in cfg.get("projects", []):
        name = p["repo"].split("/")[-1].lower()
        seen.add(name)
        cards.append(make(p["repo"], p, repos_by_name.get(name)))

    return cards[: cfg["settings"].get("max_projects", 4)]

def main():
    cfg = yaml.safe_load((ROOT / "profile.yml").read_text(encoding="utf-8"))
    user, links = cfg["github"], cfg["links"]

    repos = gh(f"/users/{user}/repos?per_page=100&sort=pushed&type=owner") or []
    repos_by_name = {r["name"].lower(): r for r in repos}
    projects = build_projects(cfg, repos_by_name)

    L = []
    
    # 1. Animated Tech Banner
    L += [
        '<div align="center">',
        '  <img src="https://capsule-render.vercel.app/api?type=waving&amp;height=250&amp;color=0:0D1117,50:00FF87,100:0D1117&amp;text=DEVENDRA%20DIWAKAR&amp;fontSize=50&amp;fontAlignY=35&amp;animation=fadeIn&amp;fontColor=00FF87&amp;desc=AI%20%2F%20ML%20%26%20Backend%20Engineer&amp;descAlignY=55&amp;descSize=20"/>',
        '</div>',
        '<br>'
    ]

    # 2. Animated Neofetch (Terminal Identity)
    L += [
        '### 💻 Terminal Identity',
        '',
        '```bash',
        f'{user}@ai-infrastructure:~$ neofetch',
        '',
        '        ..:::::::::..             -------------------',
        '    ..:::aad8888888baa:::..       OS:      AI/ML Infrastructure Engine',
        '  .::::d:?88888888888?::8b::::.   Host:    Devendra Diwakar',
        ' .:::d8888:?88888888??a888888b::. Kernel:  Backend Engineering (Python, Node)',
        ' :::d8888888a8888888aa8888888b::: Uptime:  24/7/365',
        ' ::::?8888888888888888888888?:::: Shell:   FastAPI, LangChain, React',
        '  ::::?88888888888888888888?::::  Contact: devdiwakar27@gmail.com',
        '    ::::?8888888888888888?::::    Status:  Available for 2026-27 Internships',
        '        ..:::::::::::..           ',
        '```',
        ''
    ]

    # 3. Animated Typing Status
    L += [
        '<div align="center">',
        '  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=600&amp;size=18&amp;duration=3000&amp;pause=1000&amp;color=00FF87&amp;center=true&amp;vCenter=true&amp;width=800&amp;lines=>_Initializing+neural+pathways...;>_Deploying+RAG+Document+Q%26A+System...;>_Compiling+cloud+infrastructure...;>_System+Online.+Welcome." />',
        '</div>',
        '<br>'
    ]

    # 4. Animated GitHub Trophies (Unique Visual)
    L += [
        '### 🏆 Achievements',
        '',
        '<div align="center">',
        f'  <a href="https://github.com/{user}"><img src="https://github-profile-trophy.vercel.app/?username={user}&amp;theme=dracula&amp;column=7&amp;row=1&amp;margin-w=15&amp;margin-h=15&amp;no-bg=false&amp;no-frame=false" alt="Trophies" /></a>',
        '</div>',
        '<br>'
    ]

    # 5. Core Systems (Projects with glowing badging)
    L += ['### 🚀 Core Subsystems (Deployed Projects)', '']
    for p in projects:
        stack_str = " ".join([f"`{s}`" for s in p["stack"]]) if p["stack"] else ""
        L.append(f'#### 🔴 🟡 🟢 `{p["title"]}`')
        L.append(f'> **Mission:** {p["summary"]}')
        if stack_str:
            L.append(f'> **Stack:** {stack_str}')
        L.append(f'> **Link:** [github.com/{p["full_name"]}](https://github.com/{p["full_name"]})')
        L.append('')

    # 6. Tools and Analytics Side-by-Side (Using HTML Tables for crazy layout)
    L += [
        '### ⚙️ System Analytics & Tech Stack',
        '',
        '<table align="center" width="100%">',
        '<tr>',
        '  <td width="50%" align="center">',
        '    <b>Active Tech Stack</b><br><br>',
        '    <img src="https://skillicons.dev/icons?i=py,js,java,cpp,react,tailwind,vite&amp;perline=7" /><br>',
        '    <img src="https://skillicons.dev/icons?i=fastapi,nodejs,express,django,postgres,prisma,dynamodb&amp;perline=7" /><br>',
        '    <img src="https://skillicons.dev/icons?i=aws,docker,vercel,git,github,postman&amp;perline=6" />',
        '  </td>',
        '  <td width="50%" align="center">',
        '    <b>Activity Radar</b><br><br>',
        f'    <img src="https://github-readme-stats.vercel.app/api?username={user}&amp;show_icons=true&amp;theme=dracula&amp;bg_color=0D1117&amp;title_color=00FF87&amp;icon_color=00FF87&amp;text_color=ffffff&amp;border_color=00FF87&amp;hide_border=true" height="155"/>',
        '  </td>',
        '</tr>',
        '</table>',
        '<br>'
    ]

    # 7. Animated Snake (Requires GitHub Action running)
    L += [
        '### 🐍 Contribution Activity',
        '',
        '> *Note: The animated snake is generated daily via GitHub Actions.*',
        '',
        '<div align="center">',
        f'  <picture>',
        f'    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/{user}/{user}/output/github-snake-dark.svg">',
        f'    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/{user}/{user}/output/github-snake.svg">',
        f'    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/{user}/{user}/output/github-snake.svg">',
        f'  </picture>',
        '</div>',
        '<br>'
    ]

    # Footer
    L += [
        '<div align="center">',
        '  <img src="https://capsule-render.vercel.app/api?type=waving&amp;height=100&amp;color=0:0D1117,50:00FF87,100:0D1117&amp;section=footer"/>',
        '</div>'
    ]

    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")
    print(f"README.md written ({len(projects)} projects)")

if __name__ == "__main__":
    main()
