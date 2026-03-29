from architect.architect_agent import run_architect
from pipeline.planner_agent import run_planner
from coder.coder_agent import run_coder
from reviewer.reviewer_agent import run_reviewer
from writer.writer_agent import run_writer
from git_agent import create_branch, commit_all
from logs.logger import log
from approval_agent import approve_changes

def run_full_pipeline(feature):

    create_branch(feature)

    run_architect(feature)
    run_planner()

    changes = run_coder()

    if not approve_changes(changes):
        print("❌ Cancelled")
        return

    run_reviewer()
    run_writer()

    commit_all("AI update")


