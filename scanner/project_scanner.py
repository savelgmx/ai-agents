import os

EXCLUDE = {"build",".git",".idea","gradle"}

def scan_project(project_path):

    structure = []

    for root, dirs, files in os.walk(project_path):

        dirs[:] = [d for d in dirs if d not in EXCLUDE]

        level = root.replace(project_path, "").count(os.sep)
        indent = " " * 2 * level

        structure.append(f"{indent}{os.path.basename(root)}/")

        for file in files:
            if file.endswith((".kt",".xml",".gradle",".kts")):
                structure.append(f"{indent}  {file}")

    return "\n".join(structure)
