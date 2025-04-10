from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        file = request.files.get('file')
        url = request.form.get('url')
        data = {}

        if file:
            data['file'] = (file.filename, file.stream, file.mimetype)
        else:
            data['url'] = url

        response = requests.post('http://backend:5000/analyze', files={'file': file} if file else None, data={'url': url})
        result = response.json()

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8501)
