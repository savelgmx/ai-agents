import subprocess
import re
import os

PROJECT_DIR = "app"  # ключевой фикс


def sanitize_branch_name(name: str) -> str:
    name = name.lower()
    name = re.sub(r'[^a-z0-9_\-]', '_', name)
    return f"ai/{name[:50]}"


def run_git_command(cmd):
    return subprocess.run(
        cmd,
        cwd=PROJECT_DIR,  # 🔥 ВАЖНО
        capture_output=True,
        text=True
    )


def create_branch(feature: str):
    branch = sanitize_branch_name(feature)

    result = run_git_command(["git", "checkout", "-b", branch])

    print("[GIT]", result.stdout)
    if result.stderr:
        print("[GIT ERROR]", result.stderr)


def commit_all(message="AI update"):
    run_git_command(["git", "add", "."])
    run_git_command(["git", "commit", "-m", message])
