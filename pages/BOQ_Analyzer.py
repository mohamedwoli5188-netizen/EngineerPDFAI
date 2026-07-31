import streamlit as st

from modules.boq_parser import parse_boq
from modules.boq_analysis import analyze_boq


def show():

    st.title(
        "📑 BOQ Analyzer"
    )

    st.write(
        """
        Upload BOQ PDF and extract
        construction quantities and cost structure.
        """
    )


    boq_file = st.file_uploader(
        "Upload BOQ PDF",
        type=["pdf"]
    )


    if boq_file:


        with open(
            "uploaded_boq.pdf",
            "wb"
        ) as f:

            f.write(
                boq_file.getbuffer()
            )


        st.success(
            "BOQ Uploaded Successfully"
        )


        if st.button(
            "Analyze BOQ"
        ):


            text = parse_boq(
                "uploaded_boq.pdf"
            )


            result = analyze_boq(
                text
            )


            st.subheader(
                "BOQ Analysis Result"
            )


            st.json(
                result
            )
