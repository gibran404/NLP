import fitz  # PyMuPDF
from docx import Document
from docx.shared import RGBColor

# Define the word-label dictionary
word_label_dict = {
    'Independence': 'A',
    'India': 'A',
    'Pakistan': 'A',
    'Mahatma': 'B',
    'Gandhi': 'B',
    'Quiad': 'B',
    'Delhi': 'C',
    'Lahore': 'C',
    'Karachi': 'C'
}

# Define the color mapping function
def get_color(label):
    color_map = {
        'A': RGBColor(255, 0, 0),    # Red
        'B': RGBColor(0, 255, 0),    # Green
        'C': RGBColor(0, 0, 255)     # Blue
    }
    return color_map.get(label, RGBColor(0, 0, 0))  # Default to black if label not found

def extract_ne(pdf_path, output_path):
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
    doc.save(output_path)
    print("Named entities extracted and saved to", output_path)
