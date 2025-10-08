from flask import Blueprint, request, jsonify, current_app
import os
import pandas as pd

# 1️⃣ Define blueprint first
excel_bp = Blueprint('excel_bp', __name__, url_prefix='/excel')

# 2️⃣ Use blueprint decorator
@excel_bp.route('/send_messages/<filename>', methods=['POST'])
def send_messages(filename):
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(filepath):
        return jsonify({"success": False, "error": "File not found"}), 404

    try:
        df = pd.read_excel(filepath)
        results = []
        for index, row in df.iterrows():
            phone = row.get("phone")
            message = row.get("message")
            results.append({"phone": phone, "status": "sent", "message": message})

        return jsonify({"success": True, "results": results})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
