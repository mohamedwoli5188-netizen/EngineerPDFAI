from modules.pdf_extractor import extract_text
from modules.boq.parser import parse_boq
from modules.boq.classifier import classify_boq_items


# Extract BOQ PDF text
boq_text = extract_text(boq_file)


# Parse BOQ items
boq_items = parse_boq(
    boq_text
)


# Classify items
boq_items = classify_boq_items(
    boq_items
)
