import os
import json

PROJECT_DIR = "data/projects"


def list_projects():

    if not os.path.exists(PROJECT_DIR):
        return []

    return [
        f for f in os.listdir(PROJECT_DIR)
        if f.endswith(".json")
    ]


def load_project(filename):

    path = os.path.join(PROJECT_DIR, filename)

    if not os.path.exists(path):
        return None

    with open(path, "r") as f:
        return json.load(f)


def save_project(filename, data):

    if not os.path.exists(PROJECT_DIR):
        os.makedirs(PROJECT_DIR)

    path = os.path.join(PROJECT_DIR, filename)

    with open(path, "w") as f:
        json.dump(
            data,
            f,
            indent=4
        )

    return filename
