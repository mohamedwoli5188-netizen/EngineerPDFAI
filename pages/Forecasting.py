import streamlit as st


def show():

    st.title("📈 Payment Forecasting")

    st.write(
        """
        Forecast future IPC payments based on:

        • Previous IPC values
        • Price escalation trend
        • Project progress
        • PPA adjustment factors
        """
    )


    st.divider()


    st.subheader("Forecast Inputs")


    current_ipc = st.number_input(
        "Current IPC Amount (ETB)",
        value=0.0
    )


    progress = st.number_input(
        "Expected Progress (%)",
        value=10.0
    )


    escalation = st.number_input(
        "Expected Escalation (%)",
        value=20.0
    )


    if st.button("Generate Forecast"):

        forecast = current_ipc * (
            1 + escalation / 100
        )

        st.success(
            "Forecast Generated"
        )


        st.metric(
            "Forecast Payment (ETB)",
            f"{forecast:,.2f}"
        )
