import os

MAX_CHARS = 10000


def build_relevant_context(mapping):

    context = ""

    for m in mapping:
        if m["file"] != "CREATE_NEW":
            try:
                with open(m["file"], "r", encoding="utf-8") as f:
                    code = f.read()
                    context += f"\n--- {m['file']} ---\n{code}\n"
            except:
                pass

    return context[:12000]
