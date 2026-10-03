#!/usr/bin/env python3
"""Rebuild README.md from profile.yml + live GitHub data for a modern layout!"""
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

def get_skillicons():
    # Icons for skillicons.dev mapped from typical Devendra stack
    return [
        "https://skillicons.dev/icons?i=python,js,java,cpp,react,tailwind,vite&perline=7",
        "https://skillicons.dev/icons?i=fastapi,nodejs,express,django,postgres,prisma,dynamodb&perline=7",
        "https://skillicons.dev/icons?i=aws,docker,vercel,git,github,postman&perline=6"
    ]

def main():
    cfg = yaml.safe_load((ROOT / "profile.yml").read_text(encoding="utf-8"))
    user, links = cfg["github"], cfg["links"]

    repos = gh(f"/users/{user}/repos?per_page=100&sort=pushed&type=owner") or []
    repos_by_name = {r["name"].lower(): r for r in repos}
    projects = build_projects(cfg, repos_by_name)

    name_encoded = urllib.parse.quote(cfg['name'])
    headline_encoded = urllib.parse.quote(cfg['headline'])

    L = []
    
    # Header
    L += [
        '<div align="center">',
        f'  <img src="https://capsule-render.vercel.app/api?type=waving&height=250&color=0:020617,50:0EA5E9,100:020617&text={name_encoded}&fontSize=50&fontAlignY=35&animation=fadeIn&fontColor=F8FAFC&desc={headline_encoded}&descAlignY=55&descSize=20"/>',
        '</div>',
        ''
    ]

    # Contact Badges
    L += ['<div align="center">', '  <p align="center">']
    if links.get("portfolio"):
        L.append(f'    <a href="{links["portfolio"]}" target="_blank">')
        L.append('      <img src="https://img.shields.io/badge/Portfolio-0EA5E9?style=for-the-badge&logo=react&logoColor=black" alt="Portfolio"/>')
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
    L += ['  </p>', '']
    L += [
        '  <p align="center">',
        f'    <img src="https://komarev.com/ghpvc/?username={user}&label=PROFILE+VIEWS&color=0EA5E9&style=for-the-badge" alt="Profile Views"/>',
        f'    <img src="https://img.shields.io/github/followers/{user}?style=for-the-badge&color=38BDF8" alt="Followers"/>',
        '  </p>',
        '</div>',
        ''
    ]

    # About Me
    L += ['### 👨‍💻 About Me', '', '<br/>', '']
    L += [f"> 💡 **Welcome to my personal digital showcase!** {cfg['tagline'].strip()}", "", '<br/>', ""]

    L += ['### 💻 What I\'m Doing Currently', '']
    for item in cfg.get("currently", []):
        L.append(f"- 🔭 I’m currently working on **{item}**")
    L.append(f"- 💼 I’m looking for **{cfg['open_to']}**")
    L.append(f"- 💬 Ask me about **AI, ML, and Backend Development**")
    L.append(f"- ⚡ Fun fact: **Code Creates Reality**")
    L.append('')

    # Featured Projects
    L += ['### 🚀 Featured Projects', '', '<br/>']
    for i, p in enumerate(projects, 1):
        L.append(f"#### {i}. 🌟 [{p['title']}]({p['url']})")
        L.append(f"- 📝 **Description**: {p['summary']}")
        if p["stack"]:
            stack_str = " ".join([f"`{s}`" for s in p["stack"]])
            L.append(f"- 🛠️ **Tech Stack**: {stack_str}")
        L.append(f"- 🔗 **Repository**: [{p['full_name']}](https://github.com/{p['full_name']})")
        L.append('')
        
    L += [
        '<div align="center">',
        f'  ⭐ <i>Explore more projects & repositories on my <b><a href="https://github.com/{user}?tab=repositories" target="_blank">GitHub Profile</a></b>!</i>',
        '</div>',
        '<br/>',
        ''
    ]

    # Tools & Technologies (skillicons)
    L += ['### ⚙️ Tools & Technologies', '', '<div align="center">']
    for row in get_skillicons():
        L.append(f'  <img src="{row}" />')
        L.append('  <br>')
    L += ['</div>', '<br/>', '']

    # GitHub Analytics
    L += ['### 📈 GitHub Analytics', '', '<div align="center">']
    L.append(f'  <img src="https://github-readme-activity-graph.vercel.app/graph?username={user}&theme=tokyonight&color=38BDF8&line=0EA5E9&point=F8FAFC&area=true&area_color=020617&title_color=38BDF8&text_color=ffffff&bg_color=020617&radius=16" alt="Activity Graph" width="100%"/>')
    L += ['</div>', '<br/>']

    L += ['<div data-importer="stats" align="center">']
    L.append(f'  <img src="https://streak-stats.demolab.com?user={user}&locale=en&mode=daily&theme=tokyonight&hide_border=false&border_radius=5&order=3" height="150" alt="streak graph"  />')
    L.append(f'  <img src="https://github-profile-trophy.vercel.app/?username={user}&theme=tokyonight&column=-1&row=1&margin-w=8&margin-h=8&no-bg=false&no-frame=false" height="150" alt="trophy graph"  />')
    L += ['</div>', '<br/>', '']

    # Footer
    L += [
        '---',
        '',
        '<div align="center">',
        '  <img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:020617,50:0EA5E9,100:020617&section=footer" width="100%"/>',
        '</div>'
    ]

    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")
    print(f"README.md written ({len(projects)} projects)")

if __name__ == "__main__":
    main()
