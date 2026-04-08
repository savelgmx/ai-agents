import os

LOG_FILE = "logs/agent.log"

os.makedirs("logs", exist_ok=True)

runtime_logs = []


def log(agent, message):

    entry = f"[{agent}] {message}"

    # файл
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

    # память (для UI)
    runtime_logs.append(entry)

    print(entry)


def get_logs():
    return runtime_logs


def clear_logs():
    global runtime_logs
    runtime_logs = []
