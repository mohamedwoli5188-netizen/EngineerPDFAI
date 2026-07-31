import json
import os

PROJECT_FILE = "project.json"


def save_project(
    project,
    contract,
    contractor,
    base_date,
    ipc_date
):

    data = {
        "project": project,
        "contract": contract,
        "contractor": contractor,
        "base_date": base_date,
        "ipc_date": ipc_date
    }

    with open(PROJECT_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_project():

    if os.path.exists(PROJECT_FILE):

        with open(PROJECT_FILE, "r") as f:
            return json.load(f)

    return {}
