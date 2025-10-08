from flask import Blueprint, request, jsonify, current_app
import os
import pandas as pd

excel_bp = Blueprint('excel', __name__)

@excel_bp.route('/')
def home():
    return "Flask Excel API is running!"

# Upload Excel file
@excel_bp.route('/upload', methods=['POST'])
def upload_excel():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    upload_folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)
    filepath = os.path.join(upload_folder, file.filename)
    file.save(filepath)

    return jsonify({"message": "File uploaded successfully", "filepath": filepath})


# Read Excel data
@excel_bp.route('/read/<filename>', methods=['GET'])
def read_excel(filename):
    upload_folder = current_app.config['UPLOAD_FOLDER']
    filepath = os.path.join(upload_folder, filename)

    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404

    try:
        df = pd.read_excel(filepath)
        data = df.to_dict(orient="records")
        return jsonify({"data": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500




    
