import json
import os

MEMORY_DIR = "memory_store"
os.makedirs(MEMORY_DIR, exist_ok=True)


def save_stage(stage: str, data):
    with open(f"{MEMORY_DIR}/{stage}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_stage(stage: str):
    path = f"{MEMORY_DIR}/{stage}.json"
    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_full_context():
    context = {}
    for file in os.listdir(MEMORY_DIR):
        with open(f"{MEMORY_DIR}/{file}", "r", encoding="utf-8") as f:
            context[file] = json.load(f)

    return json.dumps(context, indent=2)
