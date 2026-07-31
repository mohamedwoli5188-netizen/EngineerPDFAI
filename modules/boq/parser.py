import re


def parse_boq(text):

    items = []

    lines = [
        x.strip()
        for x in text.split("\n")
        if x.strip()
    ]


    i = 0
    item_no = "1"


    while i < len(lines):

        line = lines[i]


        # detect unit line
        if line in [
            "m3",
            "m³",
            "m²",
            "m2",
            "kg",
            "No",
            "No.",
            "lot"
        ]:

            try:

                quantity = float(
                    lines[i+1]
                    .replace(",","")
                )

                rate = float(
                    lines[i+2]
                    .replace(",","")
                )

                amount = float(
                    lines[i+3]
                    .replace(",","")
                )


                # collect description before unit
                desc=[]

                j=i-1

                while j>=0:

                    previous=lines[j]

                    if re.search(
                        r'^[A-Z]\.|^\d+\.|Total|SUMMARY',
                        previous
                    ):
                        break


                    if not re.search(
                        r'^[\d,\.]+$',
                        previous
                    ):
                        desc.insert(0,previous)


                    j-=1


                description=" ".join(desc)


                items.append(
                    {
                    "item_no":str(len(items)+1),
                    "description":description,
                    "unit":line,
                    "quantity":quantity,
                    "rate":rate,
                    "amount":amount
                    }
                )


                i += 4


            except Exception:

                pass


        i += 1


    return items
