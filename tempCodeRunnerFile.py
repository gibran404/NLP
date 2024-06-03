
        return 'No selected file'
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], 'NER_output.docx')
        extract_ne(file_path, output_path)
        
        return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    

