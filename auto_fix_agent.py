from llm_client import call_llm
from memory.memory_agent import load_stage, save_stage
from utilty.json_utils import extract_json
from memory.context_builder import build_relevant_context


def auto_fix_build(build_output):

    code_changes = load_stage("code_raw") or []

    # 🔥 context теперь строится из memory_store
    context = build_relevant_context()

    prompt = f"""
You are Senior Android Kotlin Engineer.

Build failed.

Fix ONLY build/compiler/runtime errors.

IMPORTANT:
- Return STRICT JSON
- Do not use markdown
- Do not use triple quotes
- Do not rewrite unrelated files
- Keep fixes minimal and safe

JSON format:
[
  {{
    "file": "",
    "code": ""
  }}
]

Build errors:
{build_output}

Relevant project context:
{context}

Current generated changes:
{code_changes}
"""

    result = call_llm(prompt)

    try:
        fixes = extract_json(result)

    except Exception as e:

        print("❌ AUTO FIX JSON ERROR")
        print(result[:2000])

        fixes = []

    if fixes:
        save_stage("code_raw", fixes)

    print("🔧 Auto-fix applied")

    return fixes