from modules.coefficient_engine import generate_coefficients
from modules.price_adjustment_engine import calculate_adjustment


def calculate_from_boq(
        boq_items,
        ipc_amount,
        Lo,
        Ln,
        Mo,
        Mn,
        Eo,
        En,
        Fo,
        Fn
):


    coefficients = generate_coefficients(
        boq_items
    )


    result = calculate_adjustment(

        ipc_amount,

        coefficients["A"],
        coefficients["b"],
        coefficients["c"],
        coefficients["d"],
        coefficients["e"],

        Lo,
        Ln,

        Mo,
        Mn,

        Eo,
        En,

        Fo,
        Fn

    )


    result["Coefficients"] = coefficients


    return result
