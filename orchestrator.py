from architect.architect_agent import run_architect
from pipeline.planner_agent import run_planner
from coder.coder_agent import run_coder
from reviewer.reviewer_agent import run_reviewer
from writer.writer_agent import run_writer
from git_agent import create_branch, commit_all
from logs.logger import log
from approval_agent import approve_changes

def run_full_pipeline(feature):

    log("SYSTEM", "Starting pipeline")

    create_branch("ai-feature")

    run_architect(feature)
    run_planner()
    run_coder()

    for i in range(2):
        log("SYSTEM", f"Review loop {i+1}")
        run_reviewer()

    run_writer()

    changes = run_coder()

    if not approve_changes(changes):
        print("❌ Cancelled")
        return

    commit_all("AI feature update")
    log("SYSTEM", "Pipeline finished")


