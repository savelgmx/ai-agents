from architect.architect_agent import run_architect
from pipeline.planner_agent import run_planner
from coder.coder_agent import run_coder
from reviewer.reviewer_agent import run_reviewer
from writer.writer_agent import run_writer

def run_full_pipeline(feature: str):

    print("🚀 START PIPELINE")

    run_architect(feature)
    run_planner()
    run_coder()
    run_reviewer()
    run_writer()

    print("✅ DONE")


if __name__ == "__main__":
    feature = input("Feature:\n")
    run_full_pipeline(feature)
