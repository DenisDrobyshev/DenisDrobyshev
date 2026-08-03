#!/usr/bin/env python3
"""Refresh the latest-releases line in README.md and README.ru.md.

Reads the newest published release of every public, non-archived repository in
the DrobyshevDev organisation and rewrites the block delimited by
RELEASES:START / RELEASES:END markers. Repositories without a release are
skipped. Run by .github/workflows/update-releases.yml once a day.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

ORG = "DrobyshevDev"
START = "<!-- RELEASES:START -->"
END = "<!-- RELEASES:END -->"
ROOT = Path(__file__).resolve().parent.parent

RU_MONTHS = (
    "января", "февраля", "марта", "апреля", "мая", "июня",
    "июля", "августа", "сентября", "октября", "ноября", "декабря",
)


def api(path: str):
    request = urllib.request.Request(f"https://api.github.com{path}")
    request.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def latest_releases() -> list[tuple[datetime, str, str, str]]:
    releases = []
    for repo in api(f"/orgs/{ORG}/repos?per_page=100"):
        if repo["archived"] or repo["private"]:
            continue
        try:
            release = api(f"/repos/{ORG}/{repo['name']}/releases/latest")
        except urllib.error.HTTPError as error:
            if error.code == 404:  # no release yet
                continue
            raise
        published = datetime.strptime(release["published_at"], "%Y-%m-%dT%H:%M:%SZ")
        releases.append((published, repo["name"], release["tag_name"], release["html_url"]))
    releases.sort(reverse=True)
    return releases


def render(releases, lang: str) -> str:
    if not releases:
        return ""
    label = "Последние релизы:" if lang == "ru" else "Latest releases:"
    parts = []
    for published, name, tag, url in releases:
        if lang == "ru":
            date = f"{published.day} {RU_MONTHS[published.month - 1]} {published.year}"
        else:
            date = published.strftime("%d %b %Y").lstrip("0")
        parts.append(f"[**{name}**]({url}) {tag} ({date})")
    return f"{label} " + " · ".join(parts)


def rewrite(path: Path, body: str) -> bool:
    text = path.read_text(encoding="utf-8")
    block = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not block.search(text):
        sys.exit(f"{path.name}: markers {START} / {END} not found")
    updated = block.sub(f"{START}\n{body}\n{END}", text)
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    releases = latest_releases()
    if not releases:
        sys.exit("no releases found — refusing to blank the block")
    changed = False
    for name, lang in (("README.md", "en"), ("README.ru.md", "ru")):
        path = ROOT / name
        if path.exists() and rewrite(path, render(releases, lang)):
            changed = True
            print(f"updated {name}")
    print("no change" if not changed else f"{len(releases)} releases written")


if __name__ == "__main__":
    main()
