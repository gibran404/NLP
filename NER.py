import fitz  # PyMuPDF
import pandas as pd
from docx import Document
from docx.shared import RGBColor

print("Named entity extraction module loaded!")

# Function to map labels to colors
def get_color(label):
    colors = {
        'A': RGBColor(255, 0, 0),    # Red
        'B': RGBColor(0, 255, 0),    # Green
        'C': RGBColor(0, 0, 255),    # Blue
        # Add more labels and corresponding colors as needed
    }
    return colors.get(label, RGBColor(0, 0, 0))  # Default to black if label not found

word_label_dict = { 'word': ['for', 'and', 'Pakistan'], 'label': ['A', 'B', 'C'] }

def extract_ne():
    pdf_path = 'input_text.pdf'

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Create a new Word document
    doc = Document()

    # Iterate over each page in the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()

        # Split text into paragraphs
        paragraphs = text.split('\n')

        # Add paragraphs to the Word document with respective colors
        for paragraph_text in paragraphs:
            paragraph = doc.add_paragraph()

            # Split paragraph into words
            words = paragraph_text.split()

            # Add words to the paragraph with respective colors
            for word in words:
                if word in word_label_dict:
                    run = paragraph.add_run(word + ' ')
                    run.font.color.rgb = get_color(word_label_dict[word])
                else:
                    paragraph.add_run(word + ' ')

    # Save the document
    doc.save('colored_text.docx')
    print("Named entities extracted and saved to colored_text.docx!")
    
    
extract_ne()
