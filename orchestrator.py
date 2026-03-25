from architect.architect_agent import run_architect
from pipeline.planner_agent import run_planner
from coder.coder_agent import run_coder
from reviewer.reviewer_agent import run_reviewer
from writer.writer_agent import run_writer
from git_agent import create_branch, commit_all

def run_full_pipeline(feature):

    create_branch("ai-update")

    run_architect(feature)
    run_planner()
    run_coder()

    for _ in range(2):
        run_reviewer()

    run_writer()

    commit_all("AI generated feature")


if __name__ == "__main__":
    feature = input("Feature:\n")
    run_full_pipeline(feature)
