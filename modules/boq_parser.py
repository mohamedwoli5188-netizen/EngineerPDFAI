import pandas as pd
import fitz   # PyMuPDF
import re


def extract_text_from_pdf(pdf_file):

    text = ""

    doc = fitz.open(pdf_file)

    for page in doc:
        text += page.get_text()

    return text



def parse_boq(pdf_file):

    text = extract_text_from_pdf(pdf_file)

    rows = []


    lines = text.split("\n")


    for line in lines:

        line = line.strip()


        if not line:
            continue


        # detect BOQ style rows
        if re.match(r"^\d", line):

            rows.append(
                {
                    "Raw BOQ Line": line
                }
            )


    if len(rows) == 0:

        rows.append(
            {
                "Raw BOQ Line":
                "No structured BOQ rows detected"
            }
        )


    return pd.DataFrame(rows)
