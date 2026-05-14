import configparser
import os


# ==========================================
# ROOT
# ==========================================

ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CONFIG_PATH = os.path.join(
    ROOT_DIR,
    "config.ini"
)

# ==========================================
# LOAD CONFIG
# ==========================================

config = configparser.ConfigParser()

config.read(CONFIG_PATH)

print("CONFIG PATH:", CONFIG_PATH)

# ==========================================
# GET PROJECT PATH
# ==========================================

def get_project_path():

    path = config.get(
        "project",
        "path",
        fallback="."
    )

    print("PROJECT PATH:", path)

    return path