import os
import re

def extract_symbols(code: str):
    classes = re.findall(r'class\s+(\w+)', code)
    functions = re.findall(r'fun\s+(\w+)', code)

    return {
        "classes": classes,
        "functions": functions
    }


def index_project(path="app"):

    index = []

    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".kt"):
                full_path = os.path.join(root, f)

                try:
                    with open(full_path, "r", encoding="utf-8") as file:
                        content = file.read()

                        symbols = extract_symbols(content)

                        index.append({
                            "file": f,
                            "path": full_path,
                            "classes": symbols["classes"],
                            "functions": symbols["functions"],
                            "snippet": content[:800]
                        })

                except:
                    pass

    return index
