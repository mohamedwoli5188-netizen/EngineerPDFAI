import re


def analyze_boq(text):

    items=[]

    lines=text.split("\n")

    for line in lines:

        if len(line.strip())>10:

            items.append(
                {
                    "description":line.strip()
                }
            )

    return items
