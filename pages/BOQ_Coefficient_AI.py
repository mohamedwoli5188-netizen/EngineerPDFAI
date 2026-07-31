import streamlit as st

from modules.coefficient_engine import generate_coefficients


def show():

    st.title("📊 BOQ Coefficient Generator")

    st.write(
        "Generate PPA-2011 coefficients automatically from BOQ cost distribution"
    )


    materials = st.number_input(
        "Materials Amount",
        value=300000
    )


    labour = st.number_input(
        "Labour Amount",
        value=200000
    )


    equipment = st.number_input(
        "Equipment Amount",
        value=100000
    )


    if st.button("Generate Coefficients"):

        items = [
            {
                "category":"material",
                "amount":materials
            },
            {
                "category":"labour",
                "amount":labour
            },
            {
                "category":"equipment",
                "amount":equipment
            }
        ]


        result = generate_coefficients(items)


        st.success("Coefficient Generated")


        st.json(result)
