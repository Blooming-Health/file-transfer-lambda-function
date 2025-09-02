import os
import boto3
from google.cloud import storage
import json

def lambda_handler(event, context):
    # Get S3 event details
    s3_info = event['Records'][0]['s3']
    bucket_name = s3_info['bucket']['name']
    object_key = s3_info['object']['key']

    # Download file from S3
    s3 = boto3.client('s3')
    tmp_file = f'/tmp/{object_key.split("/")[-1]}'
    s3.download_file(bucket_name, object_key, tmp_file)

    # Authenticate to GCP
    gcp_key_path = os.path.join(os.path.dirname(__file__), 'jenny1-1-aglley-c693e3454b7b.json')
    storage_client = storage.Client.from_service_account_json(gcp_key_path)
    gcp_bucket_name = os.environ['GCP_BUCKET_NAME']
    bucket = storage_client.bucket(gcp_bucket_name)
    blob = bucket.blob(object_key)

    # Upload to GCP bucket
    blob.upload_from_filename(tmp_file)

    return {
        'statusCode': 200,
        'body': json.dumps('File moved from S3 to GCP Storage successfully!')
    }
