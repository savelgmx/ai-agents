from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import run_full_pipeline

from fastapi import FastAPI
from orchestrator import run_full_pipeline, apply_approved_changes

app = FastAPI()

pending_changes = None


@app.post("/run")
def run(data: dict):

    global pending_changes

    feature = data.get("feature", "test")

    pending_changes = run_full_pipeline(feature, preview_only=True)

    return {
        "status": "preview",
        "changes": pending_changes
    }


@app.post("/approve")
def approve():

    global pending_changes

    if not pending_changes:
        return {"error": "No pending changes"}

    apply_approved_changes(pending_changes)

    pending_changes = None

    return {"status": "applied"}
