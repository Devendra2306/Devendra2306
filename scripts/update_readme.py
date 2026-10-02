#!/usr/bin/env python3
"""Rebuild README.md from profile.yml + live GitHub data.

Usage:  python scripts/update_readme.py
Env:    GITHUB_TOKEN (optional, raises API rate limit; Actions provides it)
Works offline too: if the API is unreachable, cards render from profile.yml.
"""
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
    except Exception as e:  # network down, rate limited, 404...
        print(f"[warn] {path}: {e}")
        return None


def badge(text):
    return f"`{text}`"


def build_projects(cfg, repos_by_name):
    """Merge yml overrides + auto-discovered repos tagged `showcase`."""
    cards, seen = [], set()

    def make(repo_full, override, api):
        api = api or {}
        name = repo_full.split("/")[-1]
        return {
            "title": override.get("title") or name.replace("-", " ").title(),
            "url": api.get("html_url") or f"https://github.com/{repo_full}",
            "summary": override.get("summary") or api.get("description") or "",
            "stack": override.get("stack") or ([api["language"]] if api.get("language") else []),
            "highlights": override.get("highlights") or [],
            "metrics": override.get("metrics") or "",
            "live": override.get("live") or api.get("homepage") or "",
            "demo": override.get("demo") or "",
            "stars": api.get("stargazers_count", 0),
        }

    for p in cfg.get("projects", []):
        name = p["repo"].split("/")[-1].lower()
        seen.add(name)
        cards.append(make(p["repo"], p, repos_by_name.get(name)))

    for name, r in repos_by_name.items():  # auto-discover
        if name in seen or r.get("fork") or "showcase" not in r.get("topics", []):
            continue
        cards.append(make(r["full_name"], {}, r))

    return cards[: cfg["settings"].get("max_projects", 4)]


def render_project(c):
    links = [f"[Code]({c['url']})"]
    if c["live"]:
        links.insert(0, f"[Live demo]({c['live']})")
    out = [f"### [{c['title']}]({c['url']})", ""]
    if c["demo"]:
        out += [f"![{c['title']} demo]({c['demo']})", ""]
    out.append(c["summary"])
    out.append("")
    if c["stack"]:
        out.append("**Stack:** " + " ".join(badge(s) for s in c["stack"]))
        out.append("")
    for h in c["highlights"]:
        out.append(f"- {h}")
    if c["metrics"]:
        out.append(f"- **Result:** {c['metrics']}")
    out += ["", " · ".join(links), ""]
    return "\n".join(out)


def recent_activity(user, n):
    if n <= 0:
        return ""
    events = gh(f"/users/{user}/events/public?per_page=50") or []
    lines, seen = [], set()
    for e in events:
        if e.get("type") != "PushEvent":
            continue
        repo = e["repo"]["name"]
        if repo in seen:
            continue
        seen.add(repo)
        day = e["created_at"][:10]
        commits = e.get("payload", {}).get("commits") or []
        msg = commits[-1]["message"].splitlines()[0] if commits else "pushed updates"
        lines.append(f"- `{day}` [{repo}](https://github.com/{repo}) — {msg}")
        if len(lines) >= n:
            break
    return "\n".join(lines)


def main():
    cfg = yaml.safe_load((ROOT / "profile.yml").read_text(encoding="utf-8"))
    user, s, links = cfg["github"], cfg["settings"], cfg["links"]

    repos = gh(f"/users/{user}/repos?per_page=100&sort=pushed&type=owner") or []
    repos_by_name = {r["name"].lower(): r for r in repos}

    projects = build_projects(cfg, repos_by_name)
    activity = recent_activity(user, s.get("recent_activity", 0))

    L = []
    L += [f"# Hi, I'm {cfg['name'].split()[0]}", "", f"**{cfg['headline']}**", "", cfg["tagline"].strip(), ""]
    L += [f"- **Open to:** {cfg['open_to']}"]
    for item in cfg.get("currently", []):
        L += [f"- **Now:** {item}"]
    L += [""]

    contact = [f"[Email](mailto:{links['email']})"]
    for key, label in (("linkedin", "LinkedIn"), ("portfolio", "Portfolio"), ("resume", "Resume")):
        if links.get(key):
            contact.append(f"[{label}]({links[key]})")
    L += [" · ".join(contact), "", "---", "", "## Featured projects", ""]
    L += [render_project(c) for c in projects] or ["_Add the `showcase` topic to a repo to feature it here._", ""]

    L += ["---", "", "## Stack", "", "| | |", "|---|---|"]
    for group, items in cfg["stack"].items():
        L.append(f"| **{group}** | {' · '.join(items)} |")
    L.append("")

    if activity:
        L += ["---", "", "## Recent activity", "", activity, ""]

    if s.get("show_stats_card", True):
        L += [
            "---", "",
            f'<img height="150" alt="GitHub stats" src="https://github-readme-stats.vercel.app/api?username={user}'
            f'&show_icons=true&hide_border=true&theme=transparent" />',
            "",
        ]

    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    L += [f"<sub>Auto-generated from `profile.yml` + GitHub API · last updated {now}</sub>", ""]

    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")
    print(f"README.md written ({len(projects)} projects)")


if __name__ == "__main__":
    main()
