from llm_client import call_llm
from memory.memory_agent import load_stage, save_stage


def run_tests_generation():

    changes = load_stage("code_raw")

    prompt = f"""
You are a Senior Android Test Engineer.

Generate unit tests for the following Kotlin changes.

Return JSON:
[
  {{
    "file": "path/to/test/File.kt",
    "code": "test code"
  }}
]

Changes:
{changes}
"""

    result = call_llm(prompt)

    try:
        import json
        parsed = json.loads(result)
    except:
        print("❌ Test generation failed")
        parsed = []

    save_stage("tests_generated", parsed)

    return parsed
