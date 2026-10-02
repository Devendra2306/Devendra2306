#!/usr/bin/env python3
"""Rebuild README.md from profile.yml + live GitHub data."""
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
            "language": api.get("language") or (override.get("stack")[0] if override.get("stack") else "Code"),
            "stars": api.get("stargazers_count", 0),
            "forks": api.get("forks_count", 0),
        }

    for p in cfg.get("projects", []):
        name = p["repo"].split("/")[-1].lower()
        seen.add(name)
        cards.append(make(p["repo"], p, repos_by_name.get(name)))

    return cards[: cfg["settings"].get("max_projects", 4)]

def main():
    cfg = yaml.safe_load((ROOT / "profile.yml").read_text(encoding="utf-8"))
    user, links = cfg["github"], cfg["links"]

    user_api = gh(f"/users/{user}") or {}
    followers = user_api.get("followers", 0)

    repos = gh(f"/users/{user}/repos?per_page=100&sort=pushed&type=owner") or []
    repos_by_name = {r["name"].lower(): r for r in repos}

    projects = build_projects(cfg, repos_by_name)

    L = []
    L += [f"# Hi, I'm {cfg['name'].split()[0]} 👋", ""]
    L += [cfg["tagline"].strip(), ""]
    
    L += [
        f'<a href="https://github.com/{user}?tab=followers"><img height="24" src="https://img.shields.io/badge/followers-{followers}-24292f?style=flat-square&logo=github" alt="GitHub followers"/></a>',
        f'<img height="24" src="https://komarev.com/ghpvc/?username={user}&style=flat-square&label=views&color=555555" alt="profile views"/>',
        ""
    ]

    L += ["## 📌 Featured projects", "", "<table>"]
    
    # Pair projects for 2-column table
    for i in range(0, len(projects), 2):
        L.append("  <tr>")
        for j in range(2):
            if i + j < len(projects):
                c = projects[i+j]
                # Pick a color based on language if possible, else gray
                lang_color = "3178C6" if c['language'] == 'TypeScript' else "3776AB" if c['language'] == 'Python' else "E34F26" if c['language'] == 'HTML' else "F7DF1E" if c['language'] == 'JavaScript' else "lightgrey"
                
                L.append('    <td width="50%" valign="top">')
                L.append(f'      <b><a href="{c["url"]}">{c["title"]}</a></b>')
                L.append(f'      <a href="{c["url"]}"><img height="18" src="https://img.shields.io/badge/-Public-lightgrey?style=flat-square" alt="Public"/></a><br/>')
                L.append(f'      <sub>{c["summary"]}</sub><br/>')
                if c["language"]:
                    L.append(f'      <img height="18" src="https://img.shields.io/badge/-{c["language"]}-{lang_color}?style=flat-square" alt="{c["language"]}"/>')
                L.append(f'      <a href="{c["url"]}/stargazers"><img height="18" src="https://img.shields.io/github/stars/{c["full_name"]}?style=social" alt="stars"/></a>')
                L.append(f'      <a href="{c["url"]}/forks"><img height="18" src="https://img.shields.io/github/forks/{c["full_name"]}?style=social" alt="forks"/></a>')
                L.append('    </td>')
            else:
                L.append('    <td width="50%" valign="top"></td>')
        L.append("  </tr>")
    
    L += ["</table>", ""]
    
    L += ["## What I'm building", ""]
    L += [
        "I build the layer between AI demos and production-ready systems.",
        "My current focus includes:",
        ""
    ]
    for item in cfg.get("currently", []):
        L.append(f"- {item}")
    
    L += ["", "## Start here", "", "| Resource | What you'll find |", "| --- | --- |"]
    for c in projects:
        L.append(f"| [{c['title']}]({c['url']}) | {c['summary']} |")
        
    L += ["", "## Connect", ""]
    for key, label in (("linkedin", "LinkedIn"), ("portfolio", "Portfolio"), ("resume", "Resume")):
        if links.get(key):
            L.append(f"- [{label}]({links[key]})")
    if links.get("email"):
        L.append(f"- [Email](mailto:{links['email']})")

    L += [""]
    
    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")
    print(f"README.md written ({len(projects)} projects)")

if __name__ == "__main__":
    main()
