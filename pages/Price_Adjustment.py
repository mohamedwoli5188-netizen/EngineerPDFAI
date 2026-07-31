import streamlit as st

from modules.price_adjustment_engine import calculate_adjustment


def show():

    st.title("💰 PPA-2011 Price Adjustment")


    st.write(
        "Calculate IPC escalation using PPA-2011 formula"
    )


    ipc = st.number_input(
        "IPC Amount (ETB)",
        value=85818471.05
    )


    st.subheader("Cost Coefficients")


    A = st.number_input("Fixed A", value=0.35)
    b = st.number_input("Labour b", value=0.20)
    c = st.number_input("Materials c", value=0.30)
    d = st.number_input("Equipment d", value=0.10)
    e = st.number_input("Fuel e", value=0.05)


    st.subheader("Indices")


    Lo = st.number_input("Base Labour Lo", value=180)
    Ln = st.number_input("Current Labour Ln", value=600)

    Mo = st.number_input("Base Material Mo", value=1.0)
    Mn = st.number_input("Current Material Mn", value=1.9914)

    Eo = st.number_input("Base Equipment Eo", value=1.0)
    En = st.number_input("Current Equipment En", value=1.7023)

    Fo = st.number_input("Base Fuel Fo", value=35.43)
    Fn = st.number_input("Current Fuel Fn", value=120.94)



    if st.button("Calculate Adjustment"):


        result = calculate_adjustment(
            ipc,
            A,b,c,d,e,
            Lo,Ln,
            Mo,Mn,
            Eo,En,
            Fo,Fn
        )


        st.success("Calculation Completed")


        st.metric(
            "Pn Factor",
            result["Pn"]
        )


        st.metric(
            "Escalation %",
            f'{result["Escalation %"]}%'
        )


        st.metric(
            "Additional Payment",
            f'{result["Adjustment Amount"]:,.2f} ETB'
        )
