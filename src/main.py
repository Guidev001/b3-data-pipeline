import os

from scraping.scraper import get_b3_data
from storage.s3_manager import upload_to_s3
from etl.transform import clean_data, save_parquet
from datetime import datetime
import schedule
import time


def job():
    df = get_b3_data()

    df = clean_data(df)

    date_str = datetime.today().strftime('%Y-%m-%d')
    filename = f"b3_data_{date_str}.parquet"

    save_parquet(df, filename)

    s3_path = f"raw/{date_str}/{filename}"
    upload_to_s3(filename, s3_path)

    os.remove(filename)

schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(120)