import os
from memory.memory_agent import load_stage
from diff.patcher import apply_patch

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

        with open(path, "r", encoding="utf-8") as file:
            old_code = file.read()

        new_code = apply_patch(old_code, f["code"])

        with open(path, "w", encoding="utf-8") as file:
            file.write(new_code)

        print(f"✅ Safely updated {path}")
