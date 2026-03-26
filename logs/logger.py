import os

LOG_FILE = "logs/agent.log"

os.makedirs("logs", exist_ok=True)


def log(agent, message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{agent}] {message}\n")

    print(f"[{agent}] {message}")
