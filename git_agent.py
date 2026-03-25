import subprocess

def create_branch(name="ai-feature"):
    subprocess.run(["git", "checkout", "-b", name])


def commit_all(message="AI update"):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
