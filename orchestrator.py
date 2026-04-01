from architect.architect_agent import run_architect
from memory.memory_agent import save_stage
from pipeline.planner_agent import run_planner
from coder.coder_agent import run_coder
from reviewer.reviewer_agent import run_reviewer
from writer.writer_agent import run_writer
from git_agent import create_branch, commit_all

def run_full_pipeline(feature, preview_only=False):

    run_architect(feature)
    run_planner()

    changes = run_coder()

    if preview_only:
        return changes

    run_reviewer()
    run_writer()

    return changes

def apply_approved_changes(changes):

    save_stage("code_raw", changes)

    run_reviewer()
    run_writer()
    commit_all("AI approved changes")
