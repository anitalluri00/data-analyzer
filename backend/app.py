from flask import Flask, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(__name__)
DATA_DIR = "../data"

def extract_data():
    extracted = {}
    for file in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, file)
        try:
            if file.endswith(".csv"):
                df = pd.read_csv(file_path)
            elif file.endswith(".xlsx"):
                df = pd.read_excel(file_path)
            elif file.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as f:
                    df = f.read()
                extracted[file] = df
                continue
            else:
                continue
            extracted[file] = df.head(5).to_dict(orient="records")
        except Exception as e:
            extracted[file] = f"Error reading file: {e}"
    return extracted

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify(extract_data())

@app.route("/")
def root():
    return "Data Extractor Backend Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
