#!/usr/bin/env python3
"""Rebuild README.md with an Ultra-Premium Bento Box / Linear.app aesthetic."""
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
            "metrics": override.get("metrics") or "",
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

    # Encode name and headline for URLs
    name_encoded = urllib.parse.quote(cfg['name'].upper())
    headline_encoded = urllib.parse.quote(cfg['headline'])

    L = []
    
    # 1. Premium Typography Banner
    L += [
        '<div align="center">',
        f'  <h1 align="center">Hi, I\'m {cfg["name"]} 👋</h1>',
        f'  <h3 align="center">{cfg["headline"]}</h3>',
        '</div>',
        '<br><br>'
    ]

    # 2. Sleek Typing Subheader & Social Links
    L += [
        '<div align="center">',
        '  <img src="https://readme-typing-svg.demolab.com?font=Inter&amp;weight=500&amp;size=20&amp;duration=4000&amp;pause=1000&amp;color=E94057&amp;center=true&amp;vCenter=true&amp;width=800&amp;lines=Bridging+the+gap+between+AI+demos+and+production.;Architecting+scalable+backend+infrastructure.;Available+for+2026-27+Internships." />',
        '  <br><br>',
        f'  <a href="{links.get("linkedin", "#")}"><img src="https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge&amp;logo=linkedin&amp;logoColor=white" /></a>',
        f'  <a href="mailto:{links.get("email", "#")}"><img src="https://img.shields.io/badge/Email-000000?style=for-the-badge&amp;logo=gmail&amp;logoColor=white" /></a>',
        f'  <a href="https://github.com/{user}"><img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&amp;logo=github&amp;logoColor=white" /></a>',
        '</div>',
        '<br><br>',
        '---',
        '<br>'
    ]

    # 3. The Bento Box - Projects Grid
    L += [
        '<h2 align="center">✦ Engineered Solutions ✦</h2>',
        '<br>',
        '<table align="center" width="100%" style="border-collapse: collapse;">'
    ]
    
    # Split projects into pairs for the grid
    for i in range(0, len(projects), 2):
        p1 = projects[i]
        p2 = projects[i+1] if i+1 < len(projects) else None
        
        L.append('  <tr>')
        # Project 1
        L.append('    <td width="50%" align="center" valign="top" style="padding: 20px; border: 1px solid #30363D; border-radius: 12px;">')
        L.append(f'      <h3><a href="{p1["url"]}" style="color: #E94057; text-decoration: none;">{p1["title"]}</a></h3>')
        L.append(f'      <p><i>{p1["summary"]}</i></p>')
        if p1.get("metrics"):
            L.append(f'      <p><b>{p1["metrics"]}</b></p>')
        if p1["stack"]:
            stack_str = " • ".join([f"<code>{s}</code>" for s in p1["stack"]])
            L.append(f'      <p>{stack_str}</p>')
        L.append('    </td>')
        
        # Project 2 (or empty cell if odd number)
        if p2:
            L.append('    <td width="50%" align="center" valign="top" style="padding: 20px; border: 1px solid #30363D; border-radius: 12px;">')
            L.append(f'      <h3><a href="{p2["url"]}" style="color: #E94057; text-decoration: none;">{p2["title"]}</a></h3>')
            L.append(f'      <p><i>{p2["summary"]}</i></p>')
            if p2.get("metrics"):
                L.append(f'      <p><b>{p2["metrics"]}</b></p>')
            if p2["stack"]:
                stack_str = " • ".join([f"<code>{s}</code>" for s in p2["stack"]])
                L.append(f'      <p>{stack_str}</p>')
            L.append('    </td>')
        else:
            L.append('    <td width="50%" style="border: none;"></td>')
            
        L.append('  </tr>')
        
        
    L += ['</table>', '<br><br><br>', '---', '<br><br>']

    # 4. Tech Stack & Arsenal
    L += [
        '<br><br>',
        '<h2 align="center">✦ Tech Arsenal ✦</h2>',
        '<br><br>',
        '<p align="center">',
        '  <img src="https://skillicons.dev/icons?i=python,js,java,cpp,react,tailwind,vite&amp;perline=7&amp;theme=dark" /><br><br>',
        '  <img src="https://skillicons.dev/icons?i=fastapi,nodejs,express,django,postgres,prisma,dynamodb&amp;perline=7&amp;theme=dark" /><br><br>',
        '  <img src="https://skillicons.dev/icons?i=aws,docker,vercel,git,github,postman&amp;perline=6&amp;theme=dark" />',
        '</p>',
        '<br><br><br>',
        '---',
        '<br><br>'
    ]

    # 5. Telemetry & Stats (Bento Box 2)
    L += [
        '<h2 align="center">✦ Live Telemetry ✦</h2>',
        '<br><br>',
        '<table align="center" width="100%" style="border-collapse: collapse;">',
        '  <tr>',
        '    <td width="50%" align="center" style="padding: 10px;">',
        f'      <img src="https://github-readme-stats.vercel.app/api?username={user}&amp;show_icons=true&amp;theme=transparent&amp;bg_color=00000000&amp;title_color=E94057&amp;icon_color=F27121&amp;text_color=A0A0A0&amp;hide_border=true" />',
        '    </td>',
        '    <td width="50%" align="center" style="padding: 10px;">',
        f'      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={user}&amp;layout=compact&amp;theme=transparent&amp;bg_color=00000000&amp;title_color=E94057&amp;text_color=A0A0A0&amp;hide_border=true" />',
        '    </td>',
        '  </tr>',
        '</table>',
        '<br><br><br>',
        '---',
        '<br><br>'
    ]

    # 6. 3D Contribution Graph (Requires Action)
    L += [
        '<h2 align="center">✦ 3D Activity Map ✦</h2>',
        '<br><br>',
        '<div align="center">',
        f'  <img src="https://raw.githubusercontent.com/{user}/{user}/main/profile-3d-contrib/profile-night-view.svg" alt="3D Contribution Graph" width="100%"/>',
        '</div>',
        '<br><br><br>',
        '---',
        '<br><br>'
    ]

    # 7. Animated Snake
    L += [
        '<h2 align="center">✦ Contribution Heatmap ✦</h2>',
        '<br><br>',
        '<div align="center">',
        f'  <picture>',
        f'    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/{user}/{user}/output/github-snake-dark.svg">',
        f'    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/{user}/{user}/output/github-snake.svg">',
        f'    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/{user}/{user}/output/github-snake.svg">',
        f'  </picture>',
        '</div>',
        '<br><br>'
    ]

    # Footer
    L += [
        '<div align="center">',
        '  <p><i>Building the layer between AI demos and production.</i></p>',
        '</div>'
    ]

    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")
    print(f"README.md written ({len(projects)} projects)")

if __name__ == "__main__":
    main()
