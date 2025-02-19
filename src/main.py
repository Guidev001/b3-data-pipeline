from scraping.scraper import get_b3_data
from storage.s3_manager import upload_to_s3
from etl.transform import clean_data, save_parquet
from datetime import datetime

# Passo 1: Coletar os dados da B3
df = get_b3_data()

# Passo 2: Transformar os dados
df = clean_data(df)

# Nome do arquivo baseado na data atual
date_str = datetime.today().strftime('%Y-%m-%d')
filename = f"b3_data_{date_str}.parquet"

# Passo 3: Salvar como Parquet
save_parquet(df, filename)

# Passo 4: Enviar para o AWS S3
s3_path = f"raw/{date_str}/{filename}"
upload_to_s3(filename, s3_path)
