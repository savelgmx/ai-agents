from llm_client import call_llm
from utilty.prompt_builder import build_prompt
import json


def map_targets_to_files(plan, file_index):

    prompt = f"""
Match each target to the best file.

PLAN:
{json.dumps(plan, indent=2)}

FILES:
{json.dumps(file_index, indent=2)}

Return JSON:
[
  {{
    "target": "",
    "file": "exact_file_path.kt"
  }}
]
"""

    result = call_llm(prompt)
    return json.loads(result)
