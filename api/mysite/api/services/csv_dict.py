import pandas as pd
from rest_framework.response import Response
from rest_framework import status

def csv_to_dict(file):
    if not file.name.lower().endswith('.csv'):
        raise ValueError("Invalid file format. Please upload a CSV file.")
    
    df = pd.read_csv(file, sep=',', encoding='utf-8')
    data = df.to_dict(orient='records')
    return data