#!/usr/bin/env python3
"""Rebuild README.md from profile.yml + live GitHub data for a FLASHY, modern layout!"""
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

    name_encoded = urllib.parse.quote(cfg['name'])
    headline_encoded = urllib.parse.quote(cfg['headline'])

    L = []
    
    # 1. Flashy Header Banner
    L += [
        '<div align="center">',
        f'  <img src="https://capsule-render.vercel.app/api?type=waving&height=250&color=0:020617,50:0EA5E9,100:020617&text={name_encoded}&fontSize=50&fontAlignY=35&animation=fadeIn&fontColor=F8FAFC&desc={headline_encoded}&descAlignY=55&descSize=20"/>',
        '',
        '  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3000&pause=1000&color=38BDF8&center=true&vCenter=true&width=800&lines=Building+Production-Grade+AI+Systems;FastAPI+%E2%80%A2+LangChain+%E2%80%A2+AWS+%E2%80%A2+React;Bridging+the+gap+between+AI+Demos+%26+Production"/>',
        '  <br><br>',
        f'  <img src="https://komarev.com/ghpvc/?username={user}&style=for-the-badge&label=Profile+Views&color=0ea5e9"/>',
        '</div>',
        '<br>',
        ''
    ]

    # 2. About Me Section
    L += ['### 👨‍💻 About Me', '']
    L += [f"> {cfg['tagline'].strip()}", ""]
    
    for item in cfg.get("currently", []):
        L.append(f"- 🔭 I'm currently working on **{item}**")
    L.append(f"- 💼 Open to **{cfg['open_to']}**")
    if links.get("email"):
        L.append(f"- 📫 How to reach me: **{links['email']}**")
    if links.get("linkedin"):
        L.append(f"- 🔗 Let's connect on [LinkedIn]({links['linkedin']})")
    L.append("")

    # 3. Flashy Skills Section
    L += ['### 🛠️ Tech Stack & Skills', '']
    
    stack = cfg.get("stack", {})
    
    # Pre-defined shields.io logo mapping for a modern look
    # Format: "Name": ("BadgeLabel", "Color", "LogoName")
    badge_map = {
        "python": ("Python", "3776AB", "python"),
        "javascript": ("JavaScript", "F7DF1E", "javascript"),
        "java": ("Java", "ED8B00", "openjdk"),
        "c++": ("C++", "00599C", "c%2B%2B"),
        "langchain": ("LangChain", "1C3C3C", "langchain"),
        "rag": ("RAG", "06B6D4", ""),
        "chromadb": ("ChromaDB", "4C5564", "python"),
        "gemini api": ("Gemini_API", "8E75B2", "googlegemini"),
        "pytorch": ("PyTorch", "EE4C2C", "pytorch"),
        "fastapi": ("FastAPI", "009688", "fastapi"),
        "node.js": ("Node.js", "339933", "node.js"),
        "express": ("Express", "000000", "express"),
        "django": ("Django", "092E20", "django"),
        "postgresql": ("PostgreSQL", "4169E1", "postgresql"),
        "prisma": ("Prisma", "2D3748", "prisma"),
        "dynamodb": ("DynamoDB", "4053D6", "amazondynamodb"),
        "aws (lambda, s3, api gateway)": ("AWS", "232F3E", "amazonwebservices"),
        "docker": ("Docker", "2496ED", "docker"),
        "render": ("Render", "46E3B7", "render"),
        "vercel": ("Vercel", "000000", "vercel"),
        "react": ("React", "61DAFB", "react"),
        "vite": ("Vite", "646CFF", "vite"),
        "tailwindcss": ("TailwindCSS", "06B6D4", "tailwindcss")
    }

    for category, items in stack.items():
        L.append(f'<details open>')
        L.append(f'<summary><b>{category}</b></summary>')
        L.append('<br>')
        badges = []
        for item in items:
            key = item.lower()
            if key in badge_map:
                label, color, logo = badge_map[key]
                logo_str = f"&logo={logo}&logoColor=white" if logo else ""
                # Adjust text color if background is bright
                if color.upper() in ["F7DF1E", "61DAFB", "46E3B7"]:
                    logo_str = logo_str.replace("logoColor=white", "logoColor=black")
                    badges.append(f'<img src="https://img.shields.io/badge/{label}-{color}?style=for-the-badge{logo_str}"/>')
                else:
                    badges.append(f'<img src="https://img.shields.io/badge/{label}-{color}?style=for-the-badge{logo_str}"/>')
            else:
                encoded_item = urllib.parse.quote(item.replace("-", "--"))
                badges.append(f'<img src="https://img.shields.io/badge/{encoded_item}-0EA5E9?style=for-the-badge"/>')
        L.append(" ".join(badges))
        L.append('</details>')
        L.append('')

    L.append("")

    # 4. Featured Projects (Flashy Cards)
    L += ['### 🚀 Featured Projects', '', '<div align="center">']
    for p in projects:
        L.append(f'  <a href="{p["url"]}">')
        L.append(f'    <img src="https://github-readme-stats.vercel.app/api/pin/?username={user}&repo={p["name"]}&theme=tokyonight&bg_color=020617&title_color=38BDF8&icon_color=0EA5E9&text_color=F8FAFC&border_color=0EA5E9" />')
        L.append('  </a>')
    L += ['</div>', '', '']

    # 5. GitHub Analytics
    L += ['### 📊 GitHub Analytics', '', '<div align="center">']
    L.append(f'  <img src="https://github-readme-stats.vercel.app/api?username={user}&show_icons=true&theme=tokyonight&bg_color=020617&title_color=38BDF8&icon_color=0EA5E9&text_color=F8FAFC&border_color=0EA5E9&hide_border=false" height="195"/>')
    L.append(f'  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={user}&layout=compact&theme=tokyonight&bg_color=020617&title_color=38BDF8&text_color=F8FAFC&border_color=0EA5E9&hide_border=false" height="195"/>')
    L.append('  <br><br>')
    L.append(f'  <img src="https://streak-stats.demolab.com?user={user}&theme=tokyonight&background=020617&stroke=0EA5E9&ring=38BDF8&fire=F59E0B&currStreakLabel=F8FAFC&border=0EA5E9" height="195"/>')
    L += ['</div>', '', '']

    # Footer
    L += [
        '<div align="center">',
        '  <img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:020617,50:0EA5E9,100:020617&section=footer"/>',
        '</div>'
    ]

    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")
    print(f"README.md written ({len(projects)} projects)")

if __name__ == "__main__":
    main()
