import re


def classify_item(description):

    text = description.lower()


    # FUEL
    fuel_words = [
        r"\bdiesel\b",
        r"\bfuel\b",
        r"\bpetrol\b",
        r"\bgasoline\b"
    ]

    if any(re.search(x, text) for x in fuel_words):
        return "fuel"



    # EQUIPMENT
    equipment_words = [
        r"\bexcavator\b",
        r"\bexcavation\b",
        r"\bearthwork\b",
        r"\bloader\b",
        r"\bgrader\b",
        r"\broller\b",
        r"\bcrane\b",
        r"\bmixer\b",
        r"\bpump\b",
        r"\btruck\b",
        r"\bequipment\b",
        r"\bmachinery\b",
        r"\brental\b"
    ]

    if any(re.search(x, text) for x in equipment_words):
        return "equipment"



    # LABOUR
    labour_words = [
        r"\blabour\b",
        r"\blabor\b",
        r"\bworker\b",
        r"\bcarpenter\b",
        r"\bmason\b",
        r"\bforeman\b",
        r"\boperator\b",
        r"\bhelper\b",
        r"\bfixing\b"
    ]

    if any(re.search(x, text) for x in labour_words):
        return "labour"



    # MATERIAL
    material_words = [
        "concrete",
        "cement",
        "aggregate",
        "sand",
        "gravel",
        "stone",
        "basalt",
        "steel",
        "rebar",
        "reinforcement",
        "brick",
        "block",
        "mortar",
        "pipe",
        "paint",
        "glass",
        "tile",
        "formwork",
        "timber",
        "wood",
        "hard core",
        "fill",
        "soil",
        "rock"
    ]


    if any(x in text for x in material_words):
        return "material"


    return "material"



def classify_boq_items(items):

    for item in items:

        item["category"] = classify_item(
            item.get(
                "description",
                ""
            )
        )

    return items
