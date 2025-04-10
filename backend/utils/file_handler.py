import pandas as pd
import requests
from io import BytesIO

def get_data_from_file_or_url(file=None, url=None):
    if file:
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            return df, 'CSV'
        elif file.filename.endswith('.xlsx'):
            df = pd.read_excel(file)
            return df, 'XLSX'
    elif url:
        r = requests.get(url)
        content_type = r.headers.get('Content-Type')
        if 'text/csv' in content_type or url.endswith('.csv'):
            df = pd.read_csv(BytesIO(r.content))
            return df, 'CSV'
        elif 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' in content_type or url.endswith('.xlsx'):
            df = pd.read_excel(BytesIO(r.content))
            return df, 'XLSX'
    raise ValueError("Unsupported file type or unreadable URL.")
