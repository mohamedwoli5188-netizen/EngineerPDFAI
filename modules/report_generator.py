import pandas as pd
import csv
from datetime import date


def create_report(data):

    report = {

        "Generated Date": str(date.today()),

        "Project": data.get(
            "project",
            ""
        ),

        "Contract": data.get(
            "contract",
            ""
        ),

        "IPC Amount": data.get(
            "ipc_amount",
            0
        ),

        "Pn": data.get(
            "Pn",
            0
        ),

        "Escalation %": data.get(
            "Escalation %",
            0
        ),

        "Adjustment Amount": data.get(
            "Adjustment Amount",
            0
        )

    }

    return report



def create_excel_report(data):

    filename = (
        "EngineerPDFAI_Price_Adjustment_Report.xlsx"
    )

    df = pd.DataFrame(
        [data]
    )

    df.to_excel(
        filename,
        index=False
    )

    return filename



def create_csv_report(data):

    filename = (
        "EngineerPDFAI_Price_Adjustment_Report.csv"
    )

    with open(
        filename,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Parameter",
                "Value"
            ]
        )

        for key, value in data.items():

            writer.writerow(
                [
                    key,
                    value
                ]
            )

    return filename
