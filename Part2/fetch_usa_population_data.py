import json
import boto3
import requests
import os



def lambda_handler(event, context):
    # Configure S3 client
    s3_client = boto3.client('s3')

    # S3 Bucket details
    bucket_name = os.environ.get('bucket_name')
    s3_key = os.environ.get('s3_key')  # Specify the path where you want to store the file
    data_source = os.environ.get('source_url')
    file_name = os.environ.get('file_name')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
         }

    response = requests.get(data_source, headers=headers)
    s3_client.put_object(Bucket=bucket_name, Key=s3_key+file_name, Body=response.content)
