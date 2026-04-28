
from fastapi import FastAPI
from orchestrator import run_full_pipeline, apply_approved_changes
from diff.diff_generator import generate_diff

app = FastAPI()

pending_changes = None


@app.post("/run")
def run(data: dict):

    global pending_changes

    feature = data.get("feature", "test")

    changes = run_full_pipeline(feature, preview_only=True)

    enriched = []

    for c in changes:

        try:
            with open(c["file"], "r", encoding="utf-8") as f:
                old_code = f.read()
        except:
            old_code = ""

        diff = generate_diff(old_code, c["code"])

        enriched.append({
            **c,
            "diff": diff["content"],
            "diff_type": diff["type"]
        })

    pending_changes = enriched

    return {
        "status": "preview",
        "changes": enriched
    }


@app.post("/approve")
def approve():

    global pending_changes

    if not pending_changes:
        return {"error": "No pending changes"}

    apply_approved_changes(pending_changes)

    pending_changes = None

    return {"status": "applied"}
