import fitz


def extract_boq_items(pdf):

    items = []

    try:
        doc = fitz.open(
            stream=pdf.read(),
            filetype="pdf"
        )

        for page_number, page in enumerate(doc, start=1):

            text = page.get_text()

            for line in text.split("\n"):

                line = line.strip()

                if len(line) > 5:

                    items.append(
                        {
                            "page": page_number,
                            "description": line
                        }
                    )

        return items


    except Exception as e:

        return {
            "error": str(e)
        }
