import json


def load_composition():

    file = "data/database/work_composition.json"

    with open(file, "r") as f:
        return json.load(f)



def detect_work_type(description):

    text = description.lower()

    if "excav" in text or "earth" in text or "rock" in text:
        return "excavation"

    if "concrete" in text:
        return "concrete"

    if "formwork" in text or "shuttering" in text:
        return "formwork"

    if "reinforcement" in text or "rebar" in text or "steel" in text:
        return "reinforcement"

    if "masonry" in text or "block" in text or "stone" in text:
        return "masonry"

    return "default"



def generate_coefficients(boq_items):

    composition = load_composition()

    labour = 0
    materials = 0
    equipment = 0
    fuel = 0


    for item in boq_items:

        amount = item.get("amount",0)

        work_type = detect_work_type(
            item.get("description","")
        )

        factor = composition.get(
            work_type,
            composition["default"]
        )


        materials += amount * factor["material"]
        labour += amount * factor["labour"]
        equipment += amount * factor["equipment"]
        fuel += amount * factor["fuel"]


    total = (
        materials
        +
        labour
        +
        equipment
        +
        fuel
    )


    if total == 0:

        return {
            "A":0.35,
            "b":0,
            "c":0,
            "d":0,
            "e":0.65,
            "Coefficient Sum":1.0
        }


    variable_share = 0.65


    result = {

        "A":0.35,

        "b":round(
            labour/total*variable_share,
            4
        ),

        "c":round(
            materials/total*variable_share,
            4
        ),

        "d":round(
            equipment/total*variable_share,
            4
        ),

        "e":round(
            fuel/total*variable_share,
            4
        )
    }


    # Fix rounding difference
    difference = round(
        1.0000 - sum(result.values()),
        4
    )

    result["e"] = round(
        result["e"] + difference,
        4
    )


    result["Coefficient Sum"] = round(
        sum(result.values()),
        4
    )


    return result
