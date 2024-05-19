from flask import Flask, render_template, request, send_file
import os
from NER import extract_ne  # Import the updated function from NER.py

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_ne', methods=['POST'])
def extract_ne_route():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], 'colored_text.docx')
        extract_ne(file_path, output_path)
        
        return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    

