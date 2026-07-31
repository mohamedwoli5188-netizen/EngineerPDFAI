import streamlit as st

from modules.report_generator import (
    create_excel_report,
    create_csv_report
)


def show():

    st.title(
        "📄 EngineerPDFAI Reports"
    )


    st.write(
        """
        Generate professional PPA-2011
        Price Adjustment Reports.
        """
    )


    sample_data = {

        "Project":
        "Kabri Dahar University Research Center",

        "Contract":
        "KDU/PRO/R/NCB/001/2014",

        "Base Date":
        "April 2022",

        "IPC":
        "November 2025",

        "Pn":
        1.955,

        "Escalation":
        "95.50 %"

    }


    st.subheader(
        "Report Preview"
    )


    st.json(sample_data)



    if st.button(
        "Generate Excel Report"
    ):

        file = create_excel_report(
            sample_data
        )

        st.success(
            "Excel Report Generated"
        )


        with open(file,"rb") as f:

            st.download_button(

                label="Download Excel",

                data=f,

                file_name=file

            )



    if st.button(
        "Generate CSV Report"
    ):

        file = create_csv_report(
            sample_data
        )

        st.success(
            "CSV Report Generated"
        )


        with open(file,"rb") as f:

            st.download_button(

                label="Download CSV",

                data=f,

                file_name=file

            )
