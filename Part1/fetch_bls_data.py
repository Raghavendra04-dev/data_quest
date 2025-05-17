import boto3
import requests
import os
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    DATA_SOURCE = os.environ.get('source_url')
    bucket_name = os.environ.get('bucket')
    s3_key = os.environ.get('s3_key')+"/"
    print(DATA_SOURCE)
    client = boto3.client('s3')
    paginator = client.get_paginator('list_objects')
    operation_parameters = {'Bucket': bucket_name,
                            'Prefix': os.environ.get('s3_key')}
    page_iterator = paginator.paginate(**operation_parameters)
    bucket_objects = []
    for page in page_iterator:
        for key in page['Contents']:
            fileName = key.get("Key").split("/")[1]
            if fileName:
                bucket_objects.append(fileName)
            
    

    deleted_list = bucket_objects.copy()

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
            }
    r = requests.get(DATA_SOURCE, headers=headers)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')



    for link in soup.find_all("a"):
        # Download the current file
        file_name = link.get_text()
        if file_name == "[To Parent Directory]":
            continue
        file_dl = requests.get(DATA_SOURCE + file_name, headers=headers)
        
        # If the file doesn't exist in S3, upload it
        if file_name not in bucket_objects:
        
            client.put_object(Bucket=bucket_name, Key=s3_key+file_name, Body=file_dl.content)
            print("if")
            #bucket.put_object(Key=file_name, Body=file_dl.content)
        # If the file exists in S3
        elif file_name in bucket_objects:
            # Get the S3 file
            print("elif")
            s3_response = client.get_object(Bucket=bucket_name, Key=s3_key+file_name)
            s3_file_content = s3_response['Body'].read()
            # If the S3 file is different from the website file, update the S3 file
            if file_dl.content != s3_file_content:
                print("content diff")
                client.put_object(Bucket=bucket_name, Key=s3_key+file_name, Body=file_dl.content)
            # Remove the file from the deleted list
            deleted_list.remove(file_name)

    # Remove files from S3 that are no longer on the website
    for file in deleted_list:
        if file != "population.json":
            client.delete_object(Bucket=bucket_name, Key=s3_key+file_name)