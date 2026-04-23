import subprocess
import re
import configparser
import os


# -------------------------
# LOAD CONFIG
# -------------------------
config = configparser.ConfigParser()
config.read("config.ini")

PROJECT_DIR = config.get("project", "path", fallback="app")


# -------------------------
# HELPERS
# -------------------------
def sanitize_branch_name(name: str) -> str:
    name = name.lower()
    name = re.sub(r'[^a-z0-9_\-]', '_', name)
    return f"ai/{name[:50]}"


def run_git_command(cmd):
    result = subprocess.run(
        cmd,
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )

    if result.stdout:
        print("[GIT]", result.stdout.strip())

    if result.stderr:
        print("[GIT ERROR]", result.stderr.strip())

    return result


# -------------------------
# MAIN ACTIONS
# -------------------------
def create_branch(feature: str):
    branch = sanitize_branch_name(feature)

    # Проверка: есть ли уже ветка
    existing = run_git_command(["git", "branch", "--list", branch])

    if existing.stdout.strip():
        print(f"[GIT] Branch exists, switching: {branch}")
        run_git_command(["git", "checkout", branch])
        return branch

    run_git_command(["git", "checkout", "-b", branch])

    print(f"[GIT] Created branch: {branch}")
    return branch


def commit_all(message="AI update"):
    run_git_command(["git", "add", "."])

    # commit может упасть если нет изменений
    result = run_git_command(["git", "commit", "-m", message])

    if "nothing to commit" in result.stderr.lower():
        print("[GIT] Nothing to commit")


def push_branch(branch):
    run_git_command(["git", "push", "-u", "origin", branch])
