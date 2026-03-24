import os

def scan_project(path="app"):

    code = ""

    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".kt"):
                try:
                    with open(os.path.join(root, f), "r", encoding="utf-8") as file:
                        code += file.read() + "\n\n"
                except:
                    pass

    return code
