import pandas as pd

def csv_to_json(file):
    df = pd.read_csv(file, sep=',', encoding='utf-8')
    data = df.to_json(orient='records', indent=1, force_ascii=False)
    print(data)
    return data