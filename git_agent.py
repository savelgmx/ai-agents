import subprocess
import re
import configparser
import os


# -------------------------
# LOAD CONFIG
# -------------------------
config = configparser.ConfigParser()
config.read("config.ini")

PROJECT_DIR = config.get("project", "path", fallback=".")

# --- VALIDATION ---
if not os.path.exists(PROJECT_DIR):
    raise Exception(f"❌ PROJECT_DIR not found: {PROJECT_DIR}")

if not os.path.exists(os.path.join(PROJECT_DIR, ".git")):
    raise Exception(f"❌ Not a git repo: {PROJECT_DIR}")


# --- HELPERS ---
def sanitize_branch_name(name: str) -> str:
    name = name.lower()
    name = re.sub(r'[^a-z0-9_\-]', '_', name)
    return f"ai/{name[:50]}"


def run_git_command(cmd):
    return subprocess.run(
        cmd,
        cwd=PROJECT_DIR,   # 🔥 теперь строго из config.ini
        capture_output=True,
        text=True
    )


# --- MAIN ---
def create_branch(feature: str):
    branch = sanitize_branch_name(feature)

    # Проверим существование ветки
    result = run_git_command(["git", "branch"])

    if branch in result.stdout:
        print(f"[GIT] Branch exists, switching: {branch}")
        run_git_command(["git", "checkout", branch])
        return

    result = run_git_command(["git", "checkout", "-b", branch])

    print("[GIT]", result.stdout)
    if result.stderr:
        print("[GIT ERROR]", result.stderr)


def commit_all(message="AI update"):
    run_git_command(["git", "add", "."])
    run_git_command(["git", "commit", "-m", message])
