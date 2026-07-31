import streamlit as st
from modules.database.db import list_projects


def show():

    st.header("🏗️ EngineerPDFAI Dashboard")

    st.subheader(
        "AI Construction Price Adjustment Platform"
    )


    projects = list_projects()


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "Projects",
        len(projects)
    )


    col2.metric(
        "Modules",
        "10"
    )


    col3.metric(
        "Standards",
        "PPA-2011"
    )


    col4.metric(
        "Country",
        "Ethiopia"
    )


    st.divider()


    st.subheader(
        "Engineering Workflow"
    )


    st.write(
    """
    📁 Project Upload
       
       ↓

    📄 BOQ PDF Analysis

       ↓

    📊 IPC Measurement Analysis

       ↓

    🤖 AI Coefficient Generator

       ↓

    📈 PPA-2011 Price Adjustment

       ↓

    📑 PDF & Excel Claim Reports
    """
    )


    st.divider()


    st.subheader(
        "Recent Projects"
    )


    if projects:

        for project in projects:
            st.success(project)

    else:

        st.info(
            "No projects uploaded yet. Go to Upload Project."
        )
