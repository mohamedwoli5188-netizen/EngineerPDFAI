import streamlit as st
from modules.ppa import calculate_ppa


def show():

    st.title("📈 PPA-2011 Price Adjustment Calculator")

    st.write(
        "Calculate construction price escalation using PPA formula."
    )

    st.divider()


    st.subheader("🏗 Project Information")

    project = st.text_input(
        "Project Name",
        "Kabri Dahar University Research Center"
    )

    contract = st.text_input(
        "Contract No",
        "KDU/PRO/R/NCB/001/2014"
    )

    contractor = st.text_input(
        "Contractor",
        "M/S _______"
    )


    col1, col2 = st.columns(2)

    with col1:
        base_date = st.text_input(
            "Base Date",
            "April 2022"
        )

    with col2:
        ipc_date = st.text_input(
            "IPC Date",
            "November 2025"
        )


    st.divider()


    st.subheader("⚖ PPA Coefficients")


    col1, col2, col3 = st.columns(3)


    with col1:
        A = st.number_input(
            "Fixed A",
            value=0.35
        )

        b = st.number_input(
            "Labour b",
            value=0.20
        )


    with col2:
        c = st.number_input(
            "Materials c",
            value=0.30
        )

        d = st.number_input(
            "Equipment d",
            value=0.10
        )


    with col3:
        e = st.number_input(
            "Fuel e",
            value=0.05
        )


    total = A+b+c+d+e


    if abs(total-1) > 0.001:
        st.warning(
            f"Coefficient Sum = {total:.3f}"
        )
    else:
        st.success(
            "Coefficient Sum = 1.000 ✔"
        )


    st.divider()


    st.subheader("📊 Price Indices")


    col1, col2 = st.columns(2)


    with col1:

        st.markdown("### Base Indices")

        Lo = st.number_input(
            "Labour Lo",
            value=180.0
        )

        Mo = st.number_input(
            "Material Mo",
            value=1.0
        )

        Eo = st.number_input(
            "Equipment Eo",
            value=1.0
        )

        Fo = st.number_input(
            "Fuel Fo",
            value=35.43
        )


    with col2:

        st.markdown("### Current Indices")

        Ln = st.number_input(
            "Labour Ln",
            value=600.0
        )

        Mn = st.number_input(
            "Material Mn",
            value=1.9914
        )

        En = st.number_input(
            "Equipment En",
            value=1.7023
        )

        Fn = st.number_input(
            "Fuel Fn",
            value=120.94
        )


    st.divider()


    if st.button(
        "Calculate PPA",
        type="primary"
    ):

        result = calculate_ppa(
            A,b,c,d,e,
            Lo,Ln,
            Mo,Mn,
            Eo,En,
            Fo,Fn
        )


        st.subheader(
            "📄 Result"
        )


        st.metric(
            "Pn Factor",
            round(result["Pn"],4)
        )


        st.metric(
            "Escalation %",
            f'{result["Escalation %"]:.2f}%'
        )


        st.json(result)


        st.success(
            "PPA Calculation Completed Successfully"
        )
