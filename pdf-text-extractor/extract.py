import fitz
import os

PDF_PATH = "pdfs/Resume.pdf"
OUTPUT_PATH = "output/extracted.txt"

def clean_text(text):
    lines = []

    for line in text.splitlines():
        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines)

def extract_pdf(pdf_path, output_path):
    if not os.path.exists(pdf_path):
        print("PDF file not found")
        return

    doc = fitz.open(pdf_path)

    print("PDF opened successfully.")
    print("Number of pages:", len(doc))

    print("\nMetadata:")
    print(doc.metadata)

    with open(output_path, "w", encoding="utf-8") as file:

        for page_number, page in enumerate(doc, start = 1):
            raw_text = page.get_text()
            text = clean_text(raw_text)

            file.write(
                f"\n--Page {page_number}--\n"
            )

            file.write(text)

            file.write("\n")

            print(
                f"Page {page_number}: "
                f"{len(text)} characters extracted"
            )

    doc.close()

    print("Extraction completed.")
    print(f"Output saved to: {output_path}")

extract_pdf(PDF_PATH, OUTPUT_PATH)