import fitz
import pandas as pd
import re


def extract_text_from_pdf(pdf_file):

    text = ""

    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in doc:
        text += page.get_text()

    return text



def extract_boq_items(pdf_file):

    text = extract_text_from_pdf(pdf_file)

    lines = text.split("\n")

    items = []

    for line in lines:

        if re.search(r"\d+\.\d+", line):

            items.append({
                "description": line,
                "category": "unknown",
                "amount":0
            })


    return items
