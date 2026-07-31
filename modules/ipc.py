def calculate_ipc_adjustment(
    ipc_amount,
    pn
):

    adjustment = ipc_amount * (pn - 1)

    adjusted_amount = (
        ipc_amount +
        adjustment
    )

    return {

        "Original IPC":
        ipc_amount,

        "Pn Factor":
        pn,

        "Price Adjustment":
        adjustment,

        "Adjusted IPC":
        adjusted_amount
    }
