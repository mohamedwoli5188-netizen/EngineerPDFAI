from modules.price_adjustment_engine import calculate_adjustment


def run_project(data):

    result = calculate_adjustment(
        data["ipc_amount"],
        data["A"],
        data["b"],
        data["c"],
        data["d"],
        data["e"],
        data["Lo"],
        data["Ln"],
        data["Mo"],
        data["Mn"],
        data["Eo"],
        data["En"],
        data["Fo"],
        data["Fn"]
    )

    result["Project"] = data["project"]
    result["Contract"] = data["contract_no"]

    return result
