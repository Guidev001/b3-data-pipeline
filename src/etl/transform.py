import pandas as pd

def clean_data(df):
    print("🚀 Limpando os dados")

    if "part" in df.columns:
        df["part"] = pd.to_numeric(df["part"].str.replace(",", "."), errors="coerce")

    if "theoricalQty" in df.columns:
        df["theoricalQty"] = pd.to_numeric(df["theoricalQty"].str.replace(",", "."), errors="coerce")

    print("✅ Dados limpos")
    return df

def save_parquet(df, filename):
    print(f"🚀 Salvando os dados no formato Parquet: {filename}")
    df.to_parquet(filename, engine="pyarrow")
    print(f"✅ Dados salvos com sucesso: {filename}")