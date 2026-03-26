import os
from memory.memory_agent import load_stage

OUTPUT_DIR = "generated"


def run_writer():

    files = load_stage("code_final")

    for f in files:
        path = os.path.join(OUTPUT_DIR, f["file"])

        os.makedirs(os.path.dirname(path), exist_ok=True)

        if f.get("action") == "modify" and os.path.exists(path):
            print(f"✏️ Modifying {path}")
        else:
            print(f"🆕 Creating {path}")

        with open(path, "w", encoding="utf-8") as file:
            file.write(f["code"])
