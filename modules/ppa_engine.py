def calculate_pn(A,b,c,d,e,Ln,Lo,Mn,Mo,En,Eo,Fn,Fo):

    if round(A+b+c+d+e,4) != 1.0000:
        raise ValueError(
            "PPA coefficients must equal 1.000"
        )

    Pn = (
        A
        + b*(Ln/Lo)
        + c*(Mn/Mo)
        + d*(En/Eo)
        + e*(Fn/Fo)
    )

    return Pn


def escalation_amount(ipc_amount,Pn):

    return ipc_amount*(Pn-1)
