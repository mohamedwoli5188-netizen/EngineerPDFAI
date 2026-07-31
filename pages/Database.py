import streamlit as st
from modules.database.db import list_projects, load_project


def show():

    st.title("🗄️ Project Database")

    projects = list_projects()


    if not projects:

        st.warning("No projects stored")

        return


    selected = st.selectbox(
        "Select Project",
        projects
    )


    if selected:

        data = load_project(selected)

        st.json(data)
