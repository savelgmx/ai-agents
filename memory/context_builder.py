import json
import os

from memory.memory_agent import load_stage

MAX_CONTEXT = 15000


def build_relevant_context(mapping=None):

    context_parts = []

    # -------------------------
    # 1. ARCHITECTURE
    # -------------------------
    architecture = load_stage("architecture")

    if architecture:
        context_parts.append("### ARCHITECTURE ###")
        context_parts.append(
            json.dumps(architecture, indent=2)
        )

    # -------------------------
    # 2. PLAN
    # -------------------------
    plan = load_stage("plan")

    if plan:
        context_parts.append("### PLAN ###")
        context_parts.append(
            json.dumps(plan, indent=2)
        )

    # -------------------------
    # 3. CURRENT CHANGES
    # -------------------------
    code = load_stage("code_raw")

    if code:
        context_parts.append("### CURRENT CHANGES ###")
        context_parts.append(
            json.dumps(code, indent=2)[:4000]
        )

    # -------------------------
    # 4. RELEVANT FILES
    # -------------------------
    if mapping:

        for m in mapping:

            file_path = m.get("file")

            if (
                not file_path
                or file_path == "CREATE_NEW"
            ):
                continue

            if not os.path.exists(file_path):
                continue

            try:
                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                    if len(content) > 4000:
                        content = content[:4000]

                    context_parts.append(
                        f"--- FILE: {file_path} ---"
                    )

                    context_parts.append(content)

            except Exception as e:
                print(
                    f"⚠ Failed reading {file_path}: {e}"
                )

    full_context = "\n\n".join(context_parts)

    return full_context[:MAX_CONTEXT]