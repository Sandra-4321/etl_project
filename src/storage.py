# src/storage.py
import boto3

class S3Storage:

    def __init__(self, bucket_name):
        self.s3 = boto3.client("s3")
        self.bucket_name = bucket_name

    def upload(self, local_path, key):
        self.s3.upload_file(local_path, self.bucket_name, key)
        print(f"Uploaded {local_path} → s3://{self.bucket_name}/{key}")
