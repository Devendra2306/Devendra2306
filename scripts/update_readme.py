#!/usr/bin/env python3
"""Rebuild README.md exactly matching ganeshbirajdar286 (without custom image SVGs)."""
import datetime as dt
import json
import os
import urllib.request
from pathlib import Path
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
    
    # 1. Contact & Social Badges
    L += ['<div align="center">', '  <p align="center">']
    if links.get("portfolio"):
        L.append(f'    <a href="{links["portfolio"]}" target="_blank">')
        L.append('      <img src="https://img.shields.io/badge/Portfolio-00FF87?style=for-the-badge&logo=react&logoColor=black" alt="Portfolio"/>')
        L.append('    </a>')
    if links.get("linkedin"):
        L.append(f'    <a href="{links["linkedin"]}" target="_blank">')
        L.append('      <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>')
        L.append('    </a>')
    L.append(f'    <a href="https://github.com/{user}" target="_blank">')
    L.append('      <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>')
    L.append('    </a>')
    if links.get("email"):
        L.append(f'    <a href="mailto:{links["email"]}" target="_blank">')
        L.append('      <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>')
        L.append('    </a>')
    L += ['  </p>', '  ']
    
    # Profile Views and Followers
    L += [
        '  <p align="center">',
        f'    <img src="https://komarev.com/ghpvc/?username={user}&label=PROFILE+VIEWS&color=00FF87&style=for-the-badge" alt="Profile Views"/>',
        f'    <img src="https://img.shields.io/github/followers/{user}?style=for-the-badge&color=60EFFF" alt="Followers"/>',
        '  </p>',
        '</div>',
        '',
    ]

    # 2. About Me
    L += ['### 👨‍💻 About Me', '', '<br/>', '']
    L += [f"> 💡 **Welcome to my personal digital showcase!** {cfg['tagline'].strip()}", '<br/>', '']

    # 3. What I'm Doing Currently
    L += ['### 💻 What I\'m Doing Currently', '']
    for item in cfg.get("currently", []):
        L.append(f"- 🔭 I’m currently working on **{item}**")
    L.append("- 👯 I’m looking to collaborate on **Open Source Projects**")
    L.append("- 💬 Ask me about **AI, ML, and Backend Development**")
    L.append("- ⚡ Fun fact: **Code Creates Reality**")
    L.append('')

    # 4. Featured Projects
    L += ['### 🚀 Featured Projects', '', '<br/>', '']
    for i, p in enumerate(projects, 1):
        L.append(f"#### {i}. 🌟 [{p['title']}]({p['url']})")
        L.append(f"- 📝 **Description**: {p['summary']}")
        if p["stack"]:
            stack_str = " ".join([f"`{s}`" for s in p["stack"]])
            L.append(f"- 🛠️ **Tech Stack**: {stack_str}")
        L.append(f"- 🔗 **Repository**: [github.com/{p['full_name']}](https://github.com/{p['full_name']})")
        L.append('')
        
    L += [
        '<div align="center">',
        f'  ⭐ <i>Explore more projects & repositories on my <b><a href="https://github.com/{user}?tab=repositories" target="_blank">GitHub Profile</a></b>!</i>',
        '</div>',
        '<br/>',
        ''
    ]

    # 5. Tools & Technologies
    L += ['### ⚙️ Tools & Technologies', '', '<div align="center">']
    L.append('  <img src="https://skillicons.dev/icons?i=c,cpp,java,py,js,html,css&perline=7" />')
    L.append('  <br>')
    L.append('  <img src="https://skillicons.dev/icons?i=react,nodejs,express,django,tailwind,vite&perline=7" />')
    L.append('  <br>')
    L.append('  <img src="https://skillicons.dev/icons?i=postgres,mysql,prisma,dynamodb,aws&perline=8" />')
    L.append('  <br>')
    L.append('  <img src="https://skillicons.dev/icons?i=git,github,docker,vercel,render,postman&perline=9" />')
    L += ['</div>', '', '<br/>', '']

    # 6. GitHub Analytics
    L += ['### 📈 GitHub Analytics', '', '<div align="center">']
    L.append(f'  <img src="https://github-readme-activity-graph.vercel.app/graph?username={user}&theme=github-compact&color=00FF87&line=00FF87&point=00FF87&area=true&area_color=00FF87&title_color=00FF87&text_color=ffffff&bg_color=0D1117&radius=16" alt="Activity Graph" width="100%"/>')
    L += ['</div>', '', '<br/>', '']

    L += ['<div data-importer="stats" align="center">']
    L.append(f'  <img src="https://streak-stats.demolab.com?user={user}&locale=en&mode=daily&theme=dracula&hide_border=false&border_radius=5&order=3" height="150" alt="streak graph"  />')
    L.append(f'  <img src="https://github-profile-trophy.vercel.app/?username={user}&theme=dracula&column=-1&row=1&margin-w=8&margin-h=8&no-bg=false&no-frame=false" height="150" alt="trophy graph"  />')
    L += ['</div>', '', '<br/>']

    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")
    print(f"README.md written ({len(projects)} projects)")

if __name__ == "__main__":
    main()
