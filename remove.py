import fitz

# Load PDF
doc = fitz.open("example.pdf")
page = doc[1]
width, height = page.rect.width, page.rect.height

# Define area (rectangle) to delete content
rect = fitz.Rect(0, height-50, width, height)  # Define coordinates of the area to delete

# Iterate through pages
for page in doc:
    page.add_redact_annot(rect, fill=(1, 1, 1))  # Add redaction annotation (white fill)
    page.apply_redactions()  # Apply redactions to make changes permanent

# Save the modified PDF
doc.save("output.pdf")
