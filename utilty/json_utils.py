import json
import re


def extract_json(text: str):
    """
    Robust JSON extractor for LLM responses
    """

    if not text or not text.strip():
        raise ValueError("Empty response from LLM")

    # --- 1. remove markdown ```json blocks ---
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    # --- 2. replace triple quotes (Kotlin style) ---
    text = text.replace('"""', '"')

    # --- 3. direct parse ---
    try:
        return json.loads(text)
    except:
        pass

    # --- 4. extract JSON block ---
    match = re.search(r'(\[.*\]|\{.*\})', text, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in response")

    json_text = match.group(0)

    # --- 5. cleanup ---
    json_text = json_text.replace("\n", " ")
    json_text = json_text.replace("\t", " ")

    # trailing commas
    json_text = re.sub(r",\s*}", "}", json_text)
    json_text = re.sub(r",\s*]", "]", json_text)

    # --- 6. escape inner quotes inside "code": ---
    def fix_code_blocks(match):
        content = match.group(1)
        content = content.replace('"', '\\"')
        return f'"code": "{content}"'

    json_text = re.sub(r'"code":\s*"(.*?)"', fix_code_blocks, json_text, flags=re.DOTALL)

    # --- 7. final parse ---
    try:
        return json.loads(json_text)
    except Exception as e:
        print("❌ JSON parsing failed")
        print("---- RAW RESPONSE ----")
        print(text[:1000])
        print("---- EXTRACTED JSON ----")
        print(json_text[:1000])
        raise e
