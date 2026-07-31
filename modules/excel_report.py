from openpyxl import Workbook
from datetime import date


def create_excel_report(data, filename):

    wb = Workbook()

    ws = wb.active
    ws.title = "Price Adjustment"


    ws.append(
        [
            "EngineerPDFAI",
            "PPA-2011 Price Adjustment Report"
        ]
    )

    ws.append([])

    for key, value in data.items():

        ws.append(
            [
                key,
                value
            ]
        )


    ws.append([])

    ws.append(
        [
            "Generated",
            str(date.today())
        ]
    )


    wb.save(filename)


    return filename
