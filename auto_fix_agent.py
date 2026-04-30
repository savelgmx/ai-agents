from llm_client import call_llm
from memory.memory_agent import load_stage, save_stage
from utilty.json_utils import extract_json


def auto_fix_build(build_output):

    code = load_stage("code_raw")

    prompt = f"""
Build failed.

Fix the code.

Return JSON:
[
  {{
    "file": "",
    "code": ""
  }}
]

Build errors:
{build_output}

Code:
{code}
"""

    result = call_llm(prompt)

    try:
        fixes = extract_json(result)
    except:
        fixes = []

    save_stage("code_raw", fixes)

    print("🔧 Auto-fix applied")

    return fixes
