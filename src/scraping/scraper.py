from datetime import datetime

import requests
import pandas as pd

from src.config import B3_URL

URL = B3_URL

def get_b3_data():
    print(f"🚀 Acessando a página da B3")
    response = requests.get(URL)
    if response.status_code == 200:
        print("✅ Página acessada com sucesso")
        print("🚀 Extraindo os dados")
        data = response.json()
        return process_data(data)
    else:
        raise Exception("Erro ao acessar a página da B3")


def process_data(data):
    print("🚀 Processando os dados")
    header_date = data.get("header", {}).get("date", "")

    try:
        reference_date = datetime.strptime(header_date, "%d/%m/%y").strftime('%Y-%m-%d')
    except ValueError:
        print("⚠️ Erro ao converter a data, usando a data de hoje como fallback.")
        reference_date = datetime.today().strftime('%Y-%m-%d')

    records = data.get("results", [])
    print(f"✅ {len(records)} registros processados")
    df = pd.DataFrame(records)
    df["reference_date"] = reference_date
    print("✅ Dados processados com sucesso")
    return df