import json
import re


def extract_json(text: str):
    """
    Robust JSON extractor for LLM responses
    """

    if not text or not text.strip():
        raise ValueError("Empty response from LLM")

    # --- 1. direct parse ---
    try:
        return json.loads(text)
    except:
        pass

    # --- 2. find JSON block ---
    match = re.search(r'(\{.*\}|\[.*\])', text, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in response")

    json_text = match.group(0)

    # --- 3. clean common LLM garbage ---
    json_text = json_text.replace("\n", " ")
    json_text = json_text.replace("\t", " ")
    json_text = re.sub(r",\s*}", "}", json_text)  # trailing commas
    json_text = re.sub(r",\s*]", "]", json_text)

    # --- 4. try again ---
    try:
        return json.loads(json_text)
    except Exception as e:
        print("❌ JSON parsing failed")
        print("---- RAW RESPONSE ----")
        print(text[:1000])
        print("---- EXTRACTED JSON ----")
        print(json_text[:1000])
        raise e
