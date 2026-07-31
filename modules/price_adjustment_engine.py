def calculate_adjustment(
    ipc_amount,
    A,
    b,
    c,
    d,
    e,
    Lo,
    Ln,
    Mo,
    Mn,
    Eo,
    En,
    Fo,
    Fn
):

    labour = Ln / Lo
    materials = Mn / Mo
    equipment = En / Eo
    fuel = Fn / Fo


    Pn = (
        A
        + b * labour
        + c * materials
        + d * equipment
        + e * fuel
    )


    escalation = Pn - 1


    adjustment_amount = (
        ipc_amount * escalation
    )


    return {

        "Pn": round(Pn,4),

        "Escalation %":
            round(escalation*100,2),

        "IPC Amount":
            ipc_amount,

        "Adjustment Amount":
            round(adjustment_amount,2)
    }
