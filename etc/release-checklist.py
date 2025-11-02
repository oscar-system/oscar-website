#!/usr/bin/env python3
import os
import sys
from datetime import datetime, timezone, timedelta
from github import Github, Auth

# --- Config you may tweak via env ---
TARGET_REPO = os.getenv("TARGET_REPO", "oscar-system/Oscar.jl")
RECENCY_DAYS = int(os.getenv("RECENCY_DAYS", "7"))   # consider a release "new" if within the last N days
ISSUE_PREFIX  = os.getenv("ISSUE_PREFIX", "OSCAR")   # title will be like "OSCAR vX.Y.Z release checklist"
ISSUE_LABELS  = [s.strip() for s in os.getenv("ISSUE_LABELS", "release-process").split(",") if s.strip()]
PING_LINE     = os.getenv("PING_LINE", "CC: @your-team-handle")  # customize mentions

# This token must allow reading TARGET_REPO releases and creating issues in *this* repo
API_KEY = (os.getenv("API_KEY") or os.getenv("GITHUB_TOKEN") or "").strip()
if not API_KEY:
    print("API key not found (set API_KEY or GITHUB_TOKEN).", file=sys.stderr)
    sys.exit(1)

gh = Github(auth=Auth.Token(API_KEY))

def gh_output(**kvs):
    """
    Write GitHub step outputs; avoids any file writes to the repo.
    """
    path = os.getenv("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as f:
        for k, v in kvs.items():
            # Support multiline values safely
            v = "" if v is None else str(v)
            f.write(f"{k}<<__EOF__\n{v}\n__EOF__\n")

def format_issue(version: str, published_iso: str) -> tuple[str, str]:
    title = f"{ISSUE_PREFIX} v{version} release checklist"
    body = "\n".join([
        f"# {ISSUE_PREFIX} {version} release detected — website & comms checklist",
        "",
        f"A new {ISSUE_PREFIX} release **{version}** was published on **{published_iso}** (UTC).",
        "",
        "Please complete the following steps:",
        "",
        "- [ ] Update docs landing page badges/version strings",
        "- [ ] Publish blog/news post for the release",
        "- [ ] Verify API docs links and release notes",
        "- [ ] Announce on Twitter/Mastodon/Discourse/Slack",
        "- [ ] Check downstream integrations (conda, Homebrew, etc.)",
        "",
        PING_LINE,
        "",
        "_Opened automatically by a scheduled workflow._",
    ])
    return title, body

def main():
    # 1) Get latest release from TARGET_REPO (purely from GitHub)
    repo = gh.get_repo(TARGET_REPO)
    rel = repo.get_latest_release()
    version = ((rel.title or rel.tag_name or "").lstrip("v")).strip()
    published_at = (rel.published_at or rel.created_at)  # use published_at if available
    if not version or not published_at:
        gh_output(new="false", reason="missing-data")
        print("Latest release missing version or published time.", file=sys.stderr)
        sys.exit(0)

    published_at = published_at.replace(tzinfo=timezone.utc)
    published_iso = published_at.isoformat(timespec="seconds")

    # 2) Decide "newness" by recency only (no website state needed)
    now = datetime.now(timezone.utc)
    window = timedelta(days=RECENCY_DAYS)
    is_recent = (now - published_at) <= window

    # 3) Avoid duplicates: search for an open issue with this exact title in the *current* repo
    #    (the repo running the workflow)
    this_owner, this_repo = os.environ.get("GITHUB_REPOSITORY", "").split("/", 1)
    issues = gh.get_repo(f"{this_owner}/{this_repo}")
    title, body = format_issue(version, published_iso)

    # Search open issues with the same title
    existing = issues.get_issues(state="open")
    exists = any(i.title == title for i in existing)

    # 4) Emit outputs for the workflow
    gh_output(
        new=str(is_recent and not exists).lower(),
        version=version,
        published_utc=published_iso,
        issue_title=title,
        issue_body=body,
        target_repo=TARGET_REPO,
        duplicate=str(exists).lower(),
        recent=str(is_recent).lower(),
        reason=("duplicate" if exists else ("stale" if not is_recent else "ok")),
    )

    # Also print some logs
    print(f"Latest {TARGET_REPO} release: v{version} (published {published_iso})")
    if not is_recent:
        print(f"Release is older than {RECENCY_DAYS} days; not opening an issue.")
    if exists:
        print("An open checklist issue for this version already exists; skipping.")

if __name__ == "__main__":
    main()
