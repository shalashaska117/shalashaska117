"""Generate public merged-PR cards with Python's standard library and GitHub CLI."""

from datetime import datetime, timezone
from html import escape
import json
from pathlib import Path
import subprocess
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
USERNAME = "shalashaska117"
PROJECTS = (
    ("vprover/vampire", "Vampire"),
    ("project-numina/kakeya-3d", "Kakeya-3d"),
    ("ucsd-progsys/liquidhaskell", "LiquidHaskell"),
    ("apalache-mc/apalache", "Apalache"),
)
THEMES = {
    "light": ("ffffff", "d1d9e0", "1f2328", "59636e", "8250df", "eaeef2"),
    "dark": ("0d1117", "30363d", "e6edf3", "9da7b3", "bc8cff", "21262d"),
}


def search_count(query):
    endpoint = "search/issues?" + urlencode({"q": query, "per_page": 1})
    result = subprocess.run(
        ["gh", "api", endpoint], check=True, capture_output=True,
        encoding="utf-8", timeout=60,
    )
    data = json.loads(result.stdout)
    if data.get("incomplete_results") is not False:
        raise ValueError("GitHub returned an incomplete search; keeping existing cards")
    count = data["total_count"]
    if type(count) is not int or count < 0:
        raise ValueError("Invalid count from GitHub")
    return count


def collect():
    base = f"is:pr is:merged is:public author:{USERNAME} -user:{USERNAME}"
    total = search_count(base)
    projects = [
        {"repository": repo, "name": name, "merged": search_count(f"{base} repo:{repo}")}
        for repo, name in PROJECTS
    ]
    if sum(project["merged"] for project in projects) > total:
        raise ValueError("Search counts are inconsistent; retry after the search index updates")
    return {
        "updated": datetime.now(timezone.utc).date().isoformat(),
        "total": total,
        "projects": projects,
    }


def render(data, theme):
    bg, border, fg, muted, accent, track = THEMES[theme]
    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="420" height="285" viewBox="0 0 420 285" role="img">',
        f'<rect x="0.5" y="0.5" width="419" height="284" rx="10" fill="#{bg}" stroke="#{border}"/>',
        '<g font-family="Segoe UI, Ubuntu, sans-serif">',
        f'<text x="24" y="35" font-size="18" font-weight="600" fill="#{accent}">Merged pull requests</text>',
        f'<text x="24" y="83" font-size="38" font-weight="700" fill="#{fg}">{data["total"]}</text>',
        f'<text x="115" y="65" font-size="13" fill="#{muted}">public PRs merged</text>',
        f'<text x="115" y="84" font-size="13" fill="#{muted}">into repositories owned by others</text>',
        f'<path d="M24 104H396" stroke="#{border}"/>',
    ]
    maximum = max((p["merged"] for p in data["projects"]), default=1) or 1
    for i, project in enumerate(data["projects"]):
        y = 130 + 34 * i
        width = 174 * project["merged"] / maximum
        svg.extend([
            f'<text x="24" y="{y}" font-size="14" fill="#{fg}">{escape(project["name"])}</text>',
            f'<rect x="166" y="{y - 10}" width="174" height="9" rx="4" fill="#{track}"/>',
            f'<rect x="166" y="{y - 10}" width="{width:.1f}" height="9" rx="4" fill="#{accent}"/>',
            f'<text x="395" y="{y}" text-anchor="end" font-size="15" font-weight="600" fill="#{fg}">{project["merged"]}</text>',
        ])
    svg.extend([
        f'<text x="24" y="263" font-size="11" fill="#{muted}">Selected projects · Updated {data["updated"]} UTC</text>',
        '</g></svg>\n',
    ])
    return "\n".join(svg)


def main():
    # Fetch and validate every count before touching the last successful snapshot.
    data = collect()
    files = {f"merged-prs-{theme}.svg": render(data, theme) for theme in THEMES}
    files["contributions.json"] = json.dumps(data, indent=2) + "\n"
    output = ROOT / "profile"
    output.mkdir(exist_ok=True)
    for name, content in files.items():
        (output / name).write_text(content, encoding="utf-8", newline="\n")
    print(f'Updated public contribution cards: {data["total"]} merged PRs')


if __name__ == "__main__":
    main()
