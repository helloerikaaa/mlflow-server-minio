import os

from minio import Minio
from minio.error import InvalidResponseError

accessID = os.environ.get('AWS_ACCESS_KEY_ID')
accessSecret =  os.environ.get('AWS_SECRET_ACCESS_KEY')
minioUrl =  os.environ.get('MLFLOW_S3_ENDPOINT_URL')
bucketName =  os.environ.get('AWS_BUCKET_NAME')

minioUrlHostWithPort = minioUrl.split('//')[1]

s3Client = Minio(
    minioUrlHostWithPort,
    access_key=accessID,
    secret_key=accessSecret,
    secure=False
)

s3Client.make_bucket(bucketName)
