import pandas as pd

def csv_to_dict(file):
    df = pd.read_csv(file, sep=',', encoding='utf-8')
    data = df.to_dict(orient='records')
    return data