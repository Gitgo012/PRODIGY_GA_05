from flask import Flask, render_template, request, send_from_directory
from style_transfer.model import perform_style_transfer
import os
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
# Set UPLOAD_FOLDER relative to this file's directory
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure uploads directory exists at app startup
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transfer', methods=['POST'])
def transfer():
    content = request.files['content']
    style = request.files['style']
    content_path = os.path.join(UPLOAD_FOLDER, 'content.jpg')
    style_path = os.path.join(UPLOAD_FOLDER, 'style.jpg')
    output_path = os.path.join(UPLOAD_FOLDER, 'output.jpg')

    content.save(content_path)
    style.save(style_path)

    result = perform_style_transfer(content_path, style_path)
    result.save(output_path)

    return render_template('index.html', output_url=f'/uploads/output.jpg', content_url=f'/uploads/content.jpg', style_url=f'uploads/style.jpg')

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
