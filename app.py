from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_ne', methods=['POST'])
def extract_ne():
    # Call your Python function to extract named entities
    subprocess.run(["python", "NER.ipynb", "arg1", "arg2"])
    return "Named entities extracted!"

if __name__ == '__main__':
    app.run(debug=True)
