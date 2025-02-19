import boto3

from src.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME
from datetime import date

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

today = date.today()


def upload_to_s3(file_path, s3_path):
    print(f"🚀 Iniciando upload do arquivo {file_path} para S3")
    s3.upload_file(file_path, AWS_BUCKET_NAME, s3_path)
    print(f"✅ Arquivo {file_path} enviado para S3: {s3_path}")
