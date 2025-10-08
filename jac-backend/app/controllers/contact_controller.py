from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 1️⃣ Upload Excel file
@app.route('/upload', methods=['POST'])
def upload_excel():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({"message": "File uploaded successfully", "filepath": filepath})


# 2️⃣ Read Excel data
@app.route('/read/<filename>', methods=['GET'])
def read_excel(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404

    try:
        df = pd.read_excel(filepath)
        data = df.to_dict(orient="records")  # convert rows to JSON
        return jsonify({"data": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 3️⃣ Send messages (example: pretend SMS/email)
@app.route('/send_messages/<filename>', methods=['POST'])
def send_messages(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404

    df = pd.read_excel(filepath)

    sent_messages = []
    for _, row in df.iterrows():
        name = row.get("Name")
        phone = row.get("Phone")
        message = row.get("Message")

        # Simulate sending (replace with Twilio, SMTP, etc.)
        print(f"Sending to {name} ({phone}): {message}")
        sent_messages.append({"name": name, "phone": phone, "status": "sent"})

    return jsonify({"results": sent_messages})


if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Upload Excel
@app.route('/upload', methods=['POST'])
def upload_excel():
    file = request.files.get('file')
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({"message": "File uploaded", "filepath": filepath})

# Read Excel
@app.route('/read/<filename>', methods=['GET'])
def read_excel(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    df = pd.read_excel(filepath)
    return jsonify(df.to_dict(orient='records'))

# Send messages
@app.route('/send_messages/<filename>', methods=['POST'])
def send_messages(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    df = pd.read_excel(filepath)
    for _, row in df.iterrows():
        print(f"Sending message to {row['Name']} ({row['Phone']})")
    return jsonify({"status": "messages sent"})
