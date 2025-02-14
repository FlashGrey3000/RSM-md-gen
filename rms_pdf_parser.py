import fitz  # PyMuPDF
import re

def extract_questions_from_pdf(pdf_data):
    """Extracts questions from a given pdf file data"""

    doc = fitz.open(stream=pdf_data, filetype="pdf")

    text = "\n".join(page.get_text() for page in doc)

    # Clean up formatting issues (extra spaces, newlines)
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)

    # Split using question numbers (e.g., "1.", "2.", "3." at the start of a sentence)
    questions = re.split(r'(?=\d+\.)', text)

    questions = [q.strip() for q in questions if q.strip()]
    
    return questions

if __name__ == "main":  # just for testing purposes can be removed
    pdf_questions = extract_questions_from_pdf("example_maxarr.pdf")

    for i, q in enumerate(pdf_questions, start=1):
        print(f"Question {i}: {q}\n")
