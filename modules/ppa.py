"""
EngineerPDFAI
PPA-2011 Price Adjustment Engine

Formula:
Pn = A + b(Ln/Lo) + c(Mn/Mo) + d(En/Eo) + e(Fn/Fo)

"""

def calculate_ppa(
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

    labour = b * (Ln / Lo)

    materials = c * (Mn / Mo)

    equipment = d * (En / Eo)

    fuel = e * (Fn / Fo)


    Pn = (
        A
        + labour
        + materials
        + equipment
        + fuel
    )


    escalation = (
        (Pn - 1)
        * 100
    )


    return {

        "Fixed A": A,

        "Labour b": b,

        "Materials c": c,

        "Equipment d": d,

        "Fuel e": e,


        "Coefficient Sum":
        A+b+c+d+e,


        "Labour Factor":
        labour,


        "Material Factor":
        materials,


        "Equipment Factor":
        equipment,


        "Fuel Factor":
        fuel,


        "Pn":
        round(Pn,4),


        "Escalation %":
        round(escalation,2)

    }
