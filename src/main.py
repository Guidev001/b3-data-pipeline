import os
import time
import logging
from datetime import datetime
import schedule

from scraping.scraper import get_b3_data
from storage.s3_manager import upload_to_s3
from etl.transform import clean_data, save_parquet

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def job():
    try:
        logging.info("Iniciando o processo de extração de dados da B3...")

        df = get_b3_data()
        df = clean_data(df)

        date_str = datetime.today().strftime('%Y-%m-%d')
        filename = f"b3_data_{date_str}.parquet"

        save_parquet(df, filename)

        s3_path = f"raw/{date_str}/{filename}"
        upload_to_s3(filename, s3_path)

        os.remove(filename)

        logging.info(f"Arquivo {filename} salvo e enviado para S3 com sucesso!")

    except Exception as e:
        logging.error(f"Erro ao executar o job: {e}", exc_info=True)


schedule.every().day.at("10:00").do(job)

logging.info("Agendamento iniciado. Aguardando execução diária às 10h...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Verifica a cada minuto
