import json
import os

MAX_CONTEXT = 12000


def load_memory_file(name):
    path = f"memory_store/{name}.json"
    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_relevant_context():

    context_parts = []

    # -------------------------
    # 1. ARCHITECTURE
    # -------------------------
    architecture = load_memory_file("architecture")
    if architecture:
        context_parts.append("### ARCHITECTURE ###")
        context_parts.append(json.dumps(architecture, indent=2))

    # -------------------------
    # 2. PLAN
    # -------------------------
    plan = load_memory_file("plan")
    if plan:
        context_parts.append("### PLAN ###")
        context_parts.append(json.dumps(plan, indent=2))

    # -------------------------
    # 3. CURRENT CHANGES
    # -------------------------
    code = load_memory_file("code_raw")
    if code:
        context_parts.append("### CURRENT CHANGES ###")
        context_parts.append(json.dumps(code, indent=2)[:4000])

    # -------------------------
    # 4. PROJECT FILES (ВАЖНО)
    # -------------------------
    for c in code or []:
        file_path = c.get("file")

        if file_path and os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                    if len(content) > 3000:
                        content = content[:3000]

                    context_parts.append(f"--- FILE: {file_path} ---")
                    context_parts.append(content)

            except:
                pass

    full_context = "\n\n".join(context_parts)

    return full_context[:MAX_CONTEXT]