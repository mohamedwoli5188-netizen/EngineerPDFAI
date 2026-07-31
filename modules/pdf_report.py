from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(data, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content=[]


    content.append(
        Paragraph(
            "EngineerPDFAI<br/>"
            "PPA-2011 Price Adjustment Report",
            styles["Title"]
        )
    )


    content.append(
        Spacer(1,20)
    )


    for key,value in data.items():

        content.append(
            Paragraph(
                f"{key}: {value}",
                styles["Normal"]
            )
        )


    doc.build(content)


    return filename
