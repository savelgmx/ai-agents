import subprocess
import re

from config.config_loader import get_project_path


# ==========================================
# CONFIG
# ==========================================

PROJECT_PATH = get_project_path()


# ==========================================
# HELPERS
# ==========================================

def sanitize_branch_name(name: str):

    name = name.lower()

    name = re.sub(
        r"[^a-z0-9_\-]",
        "_",
        name
    )

    return f"ai/{name[:50]}"


def run_git_command(cmd):

    return subprocess.run(
        cmd,
        cwd=PROJECT_PATH,
        capture_output=True,
        text=True
    )


# ==========================================
# BRANCHING
# ==========================================

def create_branch(feature: str):

    branch = sanitize_branch_name(feature)

    existing = run_git_command([
        "git",
        "branch",
        "--list",
        branch
    ])

    # -------------------------
    # SWITCH IF EXISTS
    # -------------------------
    if existing.stdout.strip():

        print(
            f"[GIT] Branch exists, switching: {branch}"
        )

        switch_result = run_git_command([
            "git",
            "checkout",
            branch
        ])

        if switch_result.returncode != 0:
            print("[GIT ERROR]")
            print(switch_result.stderr)

        print("[GIT] Branch ready")

        return branch

    # -------------------------
    # CREATE NEW BRANCH
    # -------------------------
    result = run_git_command([
        "git",
        "checkout",
        "-b",
        branch
    ])

    if result.returncode != 0:

        print("[GIT ERROR]")
        print(result.stderr)

        raise Exception(
            f"Failed to create branch: {branch}"
        )

    print(result.stdout)
    print("[GIT] Branch ready")

    return branch


# ==========================================
# COMMIT
# ==========================================

def commit_all(message="AI update"):

    # add all tracked/untracked changes
    run_git_command([
        "git",
        "add",
        "-A"
    ])

    result = run_git_command([
        "git",
        "commit",
        "-m",
        message
    ])

    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)

    return result.returncode == 0