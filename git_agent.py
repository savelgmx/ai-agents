import subprocess
import re


def sanitize_branch_name(name: str) -> str:
    """
    Convert any feature string into valid git branch name
    """
    name = name.lower()

    # replace invalid characters
    name = re.sub(r'[^a-z0-9_\-]', '_', name)

    # trim long names
    name = name[:50]

    return f"ai/{name}"


def create_branch(feature: str):
    branch = sanitize_branch_name(feature)

    try:
        subprocess.run(["git", "checkout", "-b", branch], check=False)
        print(f"[GIT] Created branch: {branch}")
    except Exception as e:
        print(f"[GIT] Branch error: {e}")


def commit_all(message="AI update"):
    try:
        subprocess.run(["git", "add", "."], check=False)
        subprocess.run(["git", "commit", "-m", message], check=False)
        print("[GIT] Commit done")
    except Exception as e:
        print(f"[GIT] Commit error: {e}")
