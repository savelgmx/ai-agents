from llm_client import call_llm
from utilty.prompt_builder import build_prompt
from utilty.json_utils import extract_json
import json


def map_targets_to_files(plan, file_index):

    task = f"""
Match each target to the MOST relevant file.

PLAN:
{json.dumps(plan, indent=2)}

FILES:
{json.dumps(file_index, indent=2)}

Rules:
- Use semantic matching (ViewModel → *ViewModel.kt)
- Prefer existing files over creating new ones
- If no match → return "CREATE_NEW"

Return JSON:
[
  {{
    "target": "",
    "file": "path or CREATE_NEW"
  }}
]
"""

    prompt = build_prompt(
        system="You are a Senior Android Engineer.",
        context="",
        task=task
    )

    result = call_llm(prompt)
    return extract_json(result)
