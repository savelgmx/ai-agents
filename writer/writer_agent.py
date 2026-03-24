import json
import os

def run_writer():

    with open("pipeline/code_reviewed.json", "r", encoding="utf-8") as f:
        files = json.load(f)

    for file in files:

        path = file["path"]
        code = file["code"]

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(code)

        print(f"Created {path}")

    print("✅ Files written")

if __name__ == "__main__":
    run_writer()
