import configparser
import os


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

ROOT_DIR = os.path.dirname(BASE_DIR)

CONFIG_PATH = os.path.join(
    ROOT_DIR,
    "config.ini"
)

config = configparser.ConfigParser()

config.read(CONFIG_PATH)


def get_project_path():

    return config.get(
        "project",
        "path",
        fallback="."
    )