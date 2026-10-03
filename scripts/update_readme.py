#!/usr/bin/env python3
"""Rebuild README.md with a highly UNIQUE, Cyberpunk/System Terminal aesthetic."""
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
    
    # 1. Boot Sequence Header
    L += [
        '<div align="center">',
        '<code>',
        '██████╗ ███████╗██╗   ██╗███████╗███╗   ██╗██████╗ ██████╗  █████╗ ',
        '██╔══██╗██╔════╝██║   ██║██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔══██╗',
        '██║  ██║█████╗  ██║   ██║█████╗  ██╔██╗ ██║██║  ██║██████╔╝███████║',
        '██║  ██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██╔══██╗██╔══██║',
        '██████╔╝███████╗ ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║  ██║██║  ██║',
        '╚═════╝ ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝',
        '</code>',
        '</div>',
        '<br>',
        '<div align="center">',
        f'  <b><a href="https://github.com/{user}">GITHUB_DATA_LINK</a></b> // <b><a href="mailto:{links.get("email", "")}">SECURE_COMM_CHANNEL</a></b> // <b><a href="{links.get("linkedin", "")}">NETWORK_NODE</a></b>',
        '</div>',
        '<br><hr>',
    ]

    # 2. Terminal Output: About
    L += [
        '### <code>[SYS_ADMIN] ./initialize_profile.sh</code>',
        '',
        '```json',
        '{',
        f'  "operator": "{cfg["name"]}",',
        f'  "classification": "{cfg["headline"]}",',
        f'  "objective": "{cfg["tagline"].strip()}",',
        f'  "availability": "{cfg["open_to"]}"',
        '}',
        '```',
        ''
    ]

    # 3. Stack YAML Dump
    L += [
        '### <code>[SYS_ADMIN] cat /etc/infrastructure_stack.yaml</code>',
        '',
        '```yaml'
    ]
    for category, items in cfg.get("stack", {}).items():
        items_str = ", ".join([f'"{item}"' for item in items])
        L.append(f'{category.lower().replace(" ", "_")}: [{items_str}]')
    L += ['```', '']

    # 4. Active Subsystems (Projects)
    L += [
        '### <code>[SYS_ADMIN] docker ps --format "table {{.Status}}\t{{.Names}}\t{{.Ports}}"</code>',
        '',
        '| STATUS | MODULE_NAME | SPECIFICATION_OVERVIEW |',
        '|:---:|:---|:---|'
    ]
    for p in projects:
        stack_str = ", ".join(p["stack"]) if p["stack"] else "Unknown"
        L.append(f'| 🟢 `UP` | **[{p["title"].upper()}]({p["url"]})** | {p["summary"]} <br> <sub>`STACK: {stack_str}`</sub> |')
    L += ['', '']

    # 5. Background Tasks
    L += [
        '### <code>[SYS_ADMIN] htop --filter "current_tasks"</code>',
        '',
        '```bash',
        '  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND'
    ]
    for i, item in enumerate(cfg.get("currently", []), 1):
        pid = 1000 + i * 23
        L.append(f'{pid} {user.lower()[:8]}  20   0   9.8g   4.2g   2.1g R  99.9   1.2   0:00.00 {item}')
    L += ['```', '']

    # 6. Matrix Hacker Analytics
    L += [
        '### <code>[SYS_ADMIN] ./render_telemetry.py</code>',
        '',
        '<div align="center">',
        f'  <img src="https://github-readme-stats.vercel.app/api?username={user}&show_icons=true&theme=matrix&bg_color=000000&title_color=00FF00&icon_color=00FF00&text_color=00FF00&border_color=00FF00&hide_border=true" height="170"/>',
        f'  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={user}&layout=compact&theme=matrix&bg_color=000000&title_color=00FF00&text_color=00FF00&border_color=00FF00&hide_border=true" height="170"/>',
        '</div>',
        '<br>'
    ]

    # Footer
    L += [
        '<div align="center">',
        '<code>[EOF] CONNECTION_TERMINATED</code>',
        '</div>'
    ]

    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")
    print(f"README.md written ({len(projects)} projects)")

if __name__ == "__main__":
    main()
