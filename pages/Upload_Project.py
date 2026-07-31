import streamlit as st
import os
import json
from datetime import datetime


def show():

    st.header("📁 Project Upload")

    project_name = st.text_input(
        "Project Name"
    )

    boq = st.file_uploader(
        "Upload BOQ PDF",
        type=["pdf"]
    )

    ipc = st.file_uploader(
        "Upload IPC PDF",
        type=["pdf"]
    )

    contract = st.file_uploader(
        "Upload Contract PDF",
        type=["pdf"]
    )


    if st.button("Create Project"):

        if project_name and boq:

            folder = (
                f"data/projects/{project_name}"
            )

            os.makedirs(
                folder,
                exist_ok=True
            )


            files = {
                "boq.pdf": boq,
                "ipc.pdf": ipc,
                "contract.pdf": contract
            }


            for name,file in files.items():

                if file:

                    with open(
                        f"{folder}/{name}",
                        "wb"
                    ) as f:

                        f.write(
                            file.getbuffer()
                        )


            project = {

                "project_name": project_name,

                "created":
                str(datetime.now()),

                "status":
                "Uploaded",

                "documents":
                list(files.keys())

            }


            with open(
                f"{folder}/project.json",
                "w"
            ) as f:

                json.dump(
                    project,
                    f,
                    indent=4
                )


            st.success(
                "Project Created Successfully"
            )


        else:

            st.warning(
                "Enter project name and BOQ PDF"
            )
