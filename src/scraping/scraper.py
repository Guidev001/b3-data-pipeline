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
    records = data.get("results", [])
    print(f"✅ {len(records)} registros processados")
    df = pd.DataFrame(records)
    print("✅ Dados processados com sucesso")
    return df