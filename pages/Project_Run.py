import streamlit as st


def show():

    st.header("🚀 Project Engineering Analysis")

    st.write(
        "Run complete BOQ + IPC + PPA-2011 price adjustment analysis"
    )

    st.divider()


    project_file = st.file_uploader(
        "Upload Project JSON",
        type=["json"]
    )


    boq_file = st.file_uploader(
        "Upload BOQ PDF",
        type=["pdf"]
    )


    ipc_file = st.file_uploader(
        "Upload IPC PDF",
        type=["pdf"]
    )


    index_file = st.file_uploader(
        "Upload Ethiopia Price Index CSV",
        type=["csv"]
    )


    st.divider()


    if st.button("🚀 RUN ENGINEERING ANALYSIS"):

        if not project_file or not boq_file or not ipc_file or not index_file:

            st.warning(
                "Please upload all required files"
            )

        else:

            st.info(
                "Running BOQ + IPC + PPA-2011 Engine..."
            )


            try:

                from modules.master_engine import run_complete_project


                result = run_complete_project(
                    project_file,
                    boq_file,
                    ipc_file,
                    index_file
                )


                st.success(
                    "Analysis Completed"
                )


                st.json(result)


            except Exception as e:

                st.error(
                    "Analysis Failed"
                )

                st.exception(e)
