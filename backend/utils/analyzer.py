def analyze_data(df):
    total_rows = len(df)
    nulls_percent = df.isnull().mean().mean() * 100
    numeric_percent = (df.select_dtypes(include='number').shape[1] / df.shape[1]) * 100

    return {
        'total_rows': total_rows,
        'null_percentage': round(nulls_percent, 2),
        'numeric_column_percentage': round(numeric_percent, 2),
        'columns': list(df.columns)
    }
