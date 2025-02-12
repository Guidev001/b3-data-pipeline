import requests
import pandas as pd
from io import StringIO

from src.config import B3_URL

URL = B3_URL

def get_b3_data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return process_data(data)
    else:
        raise Exception("Erro ao acessar a página da B3")


def process_data(data):
    records = data.get("results", [])
    df = pd.DataFrame(records)
    return df

if __name__ == "__main__":
    df = get_b3_data()
    print(df.head())