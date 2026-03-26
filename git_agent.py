import subprocess

def create_branch(feature):
    name = f"ai/{feature.replace(' ', '_')}"
    subprocess.run(["git", "checkout", "-b", name])



def commit_all(message="AI update"):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
