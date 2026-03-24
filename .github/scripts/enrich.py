#!/usr/bin/env python3
"""
Enriches incomplete repository entries and syncs the root README.

How it works:
  1. Finds category READMEs changed vs origin/main
  2. For each new GitHub repo URL that lacks a full entry, fetches repo
     metadata from the GitHub API and uses Claude to write the complete entry
     in the collection's style.
  3. Reads all category READMEs and calls Claude to regenerate the dynamic
     sections of the root README (tree, use-cases table, highlights,
     recent additions).
"""

import os
import re
import json
import subprocess
import sys
from datetime import datetime

import anthropic
import requests

# ---------------------------------------------------------------------------
# Clients
# ---------------------------------------------------------------------------

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
TODAY = datetime.utcnow().strftime("%Y-%m")

# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def git(*args) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout.strip()


def changed_files() -> list[str]:
    """Files changed on this branch vs origin/main."""
    out = git("diff", "--name-only", "origin/main...HEAD")
    return [f for f in out.splitlines() if f]


def category_readmes_changed(files: list[str]) -> list[str]:
    """Return category README paths that changed (not root README, not .github)."""
    result = []
    for f in files:
        parts = f.split("/")
        if (
            len(parts) == 2
            and parts[1] == "README.md"
            and parts[0] not in (".github", ".claude")
        ):
            result.append(f)
    return result

# ---------------------------------------------------------------------------
# GitHub API
# ---------------------------------------------------------------------------

def github_headers() -> dict:
    h = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        h["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return h


def fetch_repo_data(url: str) -> dict | None:
    m = re.search(r"github\.com/([^/]+)/([^/\s\)#]+)", url)
    if not m:
        return None
    owner, repo = m.group(1), m.group(2).rstrip("/")
    try:
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}",
            headers=github_headers(),
            timeout=10,
        )
        if r.status_code != 200:
            print(f"  GitHub API {r.status_code} for {owner}/{repo}")
            return None
        d = r.json()
        stars = d.get("stargazers_count", 0)
        stars_fmt = f"{stars / 1000:.1f}k" if stars >= 1000 else str(stars)
        return {
            "name": d.get("name", repo),
            "url": url,
            "stars": stars_fmt,
            "description": d.get("description") or "",
            "language": d.get("language") or "",
            "license": (d.get("license") or {}).get("spdx_id") or "",
            "topics": d.get("topics") or [],
            "homepage": d.get("homepage") or "",
        }
    except Exception as e:
        print(f"  Failed to fetch {url}: {e}")
        return None

# ---------------------------------------------------------------------------
# Entry helpers
# ---------------------------------------------------------------------------

ENTRY_RE = re.compile(
    r"(###\s+\[.+?\]\((https://github\.com/[^\)]+)\).*?)(?=\n###\s|\Z)",
    re.DOTALL,
)


def is_stub(entry_text: str) -> bool:
    """True when the entry is missing key sections (stub added by the user)."""
    return not ("**Why it's notable" in entry_text and "**Stack:**" in entry_text)


def sample_entries() -> str:
    """Pull two complete formatted entries for Claude's style reference."""
    samples = []
    for cat in ["local-llm", "agent-frameworks", "speech-to-text"]:
        path = f"{cat}/README.md"
        if not os.path.exists(path):
            continue
        blocks = open(path).read().split("\n---\n")
        for block in blocks[1:]:
            block = block.strip()
            if "**Why it's notable" in block and "**Stack:**" in block:
                samples.append(block)
                break
        if len(samples) >= 2:
            break
    return "\n\n---\n\n".join(samples)

# ---------------------------------------------------------------------------
# Claude calls
# ---------------------------------------------------------------------------

ENTRY_SYSTEM = """\
You maintain a curated collection of open-source projects.
Your job is to write a single, complete, properly formatted entry for the project given.
Return ONLY the markdown entry block — start with ### and end with --- on its own line.
Do not include any preamble, explanation, or extra text."""

ENTRY_USER_TMPL = """\
Write a complete entry for the following repository. Follow the exact style of the examples.

Repository:
  Name        : {name}
  URL         : {url}
  Stars       : {stars}
  Description : {description}
  Language    : {language}
  License     : {license}
  Topics      : {topics}
  Category    : {category}

Style examples (copy structure, not content):
{examples}

Rules:
- One-sentence bold hook immediately after the ### heading
- 2–4 paragraphs: what it does, how it works, key capabilities, differentiators
- Stack, License, and any relevant optional fields (Platforms / Deployment / Markets / Note)
- "Why it's notable:" — 2–4 sentences contextualising within the ecosystem, credibility signals
- End with --- on its own line
"""

ROOT_SYSTEM = """\
You maintain the root README of a curated OSS collection.
You will be given the current root README and a JSON summary of every project currently
in the collection. Regenerate ONLY the four dynamic sections:
  1. The "X categories · Y projects" line in the header paragraph
  2. The Collection Overview tree (under ## Collection Overview)
  3. The Use Cases table (under ## Use Cases)
  4. The Highlights section (under ## Highlights)
  5. The Recent Additions table (under ## Recent Additions)

Return the COMPLETE updated README.md — preserve all other sections unchanged.
Return ONLY the file content, no preamble or code fences."""

ROOT_USER_TMPL = """\
Current README.md:
{readme}

Projects in the collection (derived from category READMEs):
{projects_json}

Today's date: {today}

Regenerate the README with all dynamic sections updated to reflect the current projects.
New projects should appear at the top of Recent Additions with date {today}.
"""


def enrich_entry(repo: dict, category: str) -> str:
    examples = sample_entries()
    prompt = ENTRY_USER_TMPL.format(
        name=repo["name"],
        url=repo["url"],
        stars=repo["stars"],
        description=repo["description"],
        language=repo["language"],
        license=repo["license"],
        topics=", ".join(repo["topics"]),
        category=category,
        examples=examples,
    )
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        system=ENTRY_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text.strip()


def update_root_readme(projects: list[dict]) -> str:
    with open("README.md") as f:
        readme = f.read()
    prompt = ROOT_USER_TMPL.format(
        readme=readme,
        projects_json=json.dumps(projects, indent=2),
        today=TODAY,
    )
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8000,
        system=ROOT_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text.strip()

# ---------------------------------------------------------------------------
# Extract structured project list from all category READMEs
# ---------------------------------------------------------------------------

def extract_projects() -> list[dict]:
    projects = []
    for item in sorted(os.listdir(".")):
        if not os.path.isdir(item) or item.startswith("."):
            continue
        path = f"{item}/README.md"
        if not os.path.exists(path):
            continue
        content = open(path).read()
        for m in ENTRY_RE.finditer(content):
            entry_text = m.group(1)
            url = m.group(2)
            # Extract project name from ### [Name](url)
            name_m = re.search(r"###\s+\[(.+?)\]", entry_text)
            name = name_m.group(1) if name_m else ""
            # Extract stars
            star_m = re.search(r"⭐\s*([\d\.]+k?)", entry_text)
            stars = star_m.group(1) if star_m else ""
            # Extract one-liner (first bold line after heading)
            oneliner_m = re.search(r"\*\*(.+?)\*\*", entry_text)
            oneliner = oneliner_m.group(1) if oneliner_m else ""
            projects.append(
                {
                    "name": name,
                    "url": url,
                    "stars": stars,
                    "category": item,
                    "one_liner": oneliner,
                }
            )
    return projects

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    files = changed_files()
    print(f"Changed files: {files or '(none)'}")

    changed_cats = category_readmes_changed(files)
    enriched = False

    for readme_path in changed_cats:
        category = readme_path.split("/")[0]
        content = open(readme_path).read()
        new_content = content

        for m in ENTRY_RE.finditer(content):
            entry_text = m.group(1)
            url = m.group(2)
            if not is_stub(entry_text):
                continue
            print(f"  Enriching stub: {url}")
            repo = fetch_repo_data(url)
            if not repo:
                print(f"  Skipping — could not fetch GitHub data for {url}")
                continue
            full_entry = enrich_entry(repo, category)
            new_content = new_content.replace(entry_text, full_entry + "\n\n")
            enriched = True

        if new_content != content:
            with open(readme_path, "w") as f:
                f.write(new_content)
            print(f"  Saved: {readme_path}")

    # Sync root README whenever anything changed in the collection
    if changed_cats or enriched:
        print("Updating root README...")
        projects = extract_projects()
        print(f"  Found {len(projects)} projects across {len(set(p['category'] for p in projects))} categories")
        new_root = update_root_readme(projects)
        with open("README.md", "w") as f:
            f.write(new_root + "\n")
        print("  Root README updated.")
    else:
        print("No category READMEs changed — skipping root README update.")


if __name__ == "__main__":
    main()
