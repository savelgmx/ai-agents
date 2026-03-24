import os
from memory.memory_agent import load_stage

OUTPUT_DIR = "generated"


def run_writer():

    files = load_stage("code_final")

    if not files:
        print("❌ No files")
        return

    for f in files:
        path = os.path.join(OUTPUT_DIR, f["file"])

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w", encoding="utf-8") as file:
            file.write(f["code"])

    print("✅ Files written")
