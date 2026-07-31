import fitz
import pytesseract
from PIL import Image
import io


def extract_text(pdf_file):

    text = ""

    pdf = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    for page in pdf:

        page_text = page.get_text()

        if page_text.strip():

            text += page_text + "\n"

        else:

            pix = page.get_pixmap(dpi=300)

            img = Image.open(
                io.BytesIO(
                    pix.tobytes("png")
                )
            )

            text += pytesseract.image_to_string(img)

    return text
