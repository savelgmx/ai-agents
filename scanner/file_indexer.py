import os

def index_project(path="app"):

    index = []

    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".kt"):
                full_path = os.path.join(root, f)

                try:
                    with open(full_path, "r", encoding="utf-8") as file:
                        content = file.read()

                        index.append({
                            "file": f,
                            "path": full_path,
                            "summary": content[:500]
                        })
                except:
                    pass

    return index
