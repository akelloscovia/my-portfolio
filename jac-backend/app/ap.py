from flask import Flask, request, jsonify
import pandas as pd

app= Flask(__name__)
@app.route("/upload",methods=["POST"])
def upload_file():
    
    #handle file upload logic here
    if __name__ =="__main__":
        app.run(debug=True) 