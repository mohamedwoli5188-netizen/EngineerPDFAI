import pandas as pd


def load_indices():

    file = "data/ethiopia_indices.csv"

    return pd.read_csv(file)



def get_index(date, category):

    df = load_indices()

    result = df[
        (df["Date"] == date)
        &
        (df["Category"].str.lower() == category.lower())
    ]


    if len(result):

        return float(
            result.iloc[0]["Index"]
        )

    return 1.0



def get_indices(base_date, current_date):

    return {

        "Lo": get_index(
            base_date,
            "Labour"
        ),

        "Ln": get_index(
            current_date,
            "Labour"
        ),


        "Mo": get_index(
            base_date,
            "Cement"
        ),

        "Mn": get_index(
            current_date,
            "Cement"
        ),


        "Eo": get_index(
            base_date,
            "Equipment"
        ),

        "En": get_index(
            current_date,
            "Equipment"
        ),


        "Fo": get_index(
            base_date,
            "Fuel"
        ),

        "Fn": get_index(
            current_date,
            "Fuel"
        )

    }
