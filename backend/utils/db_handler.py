import pyodbc

def save_to_sql_server(df, table_name):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=sql_server;DATABASE=datasetdb;UID=sa;PWD=StrongPass123!')
    cursor = conn.cursor()
    df.to_sql(table_name, con=conn, if_exists='replace', index=False)
    conn.commit()
