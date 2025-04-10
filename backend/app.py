from flask import Flask, request, jsonify
from utils.file_handler import get_data_from_file_or_url
from utils.analyzer import analyze_data
from utils.db_handler import save_to_sql_server

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('file')
    url = request.form.get('url')

    if file:
        df, source = get_data_from_file_or_url(file=file)
    elif url:
        df, source = get_data_from_file_or_url(url=url)
    else:
        return jsonify({'error': 'No file or URL provided'}), 400

    analysis = analyze_data(df)
    save_to_sql_server(df, source)

    return jsonify({'source': source, 'analysis': analysis})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
