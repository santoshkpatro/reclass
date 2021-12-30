import uuid
import os
import mimetypes
import boto3
import logging
from botocore.exceptions import ClientError
from rest_framework.views import APIView
from django.conf import settings

s3_client = boto3.client('s3',
                         region_name=settings.AWS_REGION,
                         aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
                         aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY
                         )


class FileUploadView(APIView):
    location = ''
    supported_file_types = []

    def get_filename(self):
        return uuid.uuid4().hex

    def get_file_extension(self, file_type):
        return mimetypes.guess_extension(file_type)

    def check_file_extension(self, file_type):
        ext = self.get_file_extension(file_type)
        if not self.supported_file_types:
            return True
        if ext in self.supported_file_types:
            return True
        else:
            return False

    def get_urls(self, file_type):
        if os.environ.get('DJANGO_SETTINGS_MODULE') == 'production':
            try:
                bucket_name = settings.AWS_S3_BUCKET_NAME
                object_name = self.location + self.get_filename + self.get_file_extension
                expiration = 3600

                url = s3_client.generate_presigned_url(
                    ClientMethod='put_object',
                    Params={
                        'Bucket': bucket_name,
                        'Key': object_name
                    },
                    ExpiresIn=expiration)

                return url

            except ClientError as e:
                logging.error(e)
                return None
        else:
            upload_url = 'https://127.0.0.1:8000/media' + self.location + self.file
            return upload_url
