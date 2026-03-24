from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import run_full_pipeline

app = FastAPI()

class Request(BaseModel):
    feature: str

@app.post("/run")
def run(req: Request):
    run_full_pipeline(req.feature)
    return {"status": "ok"}
