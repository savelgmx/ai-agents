import os

MAX_CHARS = 12000

def scan_project(path="app", extensions=(".kt", ".xml", ".json")):

    code = []

    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(extensions):
                try:
                    with open(os.path.join(root, f), "r", encoding="utf-8") as file:
                        content = file.read()
                        code.append(f"\n--- FILE: {f} ---\n{content}")
                except:
                    pass

    full_code = "\n".join(code)

    return full_code[:MAX_CHARS]
