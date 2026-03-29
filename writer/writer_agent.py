import os
from memory.memory_agent import load_stage

BACKUP_DIR = "backup"


def backup_file(path):
    os.makedirs(BACKUP_DIR, exist_ok=True)

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        backup_path = os.path.join(BACKUP_DIR, os.path.basename(path))

        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(content)


def run_writer():

    files = load_stage("code_raw")

    for f in files:
        path = f["file"]

        os.makedirs(os.path.dirname(path), exist_ok=True)

        backup_file(path)

        with open(path, "w", encoding="utf-8") as file:
            file.write(f["code"])

        print(f"✅ Updated {path}")
