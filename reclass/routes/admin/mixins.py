import uuid
import os
import mimetypes
import boto3
import logging
from botocore.exceptions import ClientError
from rest_framework import status
from rest_framework.exceptions import APIException
from django.conf import settings

s3_client = boto3.client('s3',
                         region_name=settings.AWS_REGION,
                         aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
                         aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY
                         )


class FileUploadMixin:
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

    def get_urls(self, expiration=3600):
        if not 'file_type' in self.request.query_params:
            raise APIException(detail='File type not found',
                               code=status.HTTP_404_NOT_FOUND)
        file_type = self.request.query_params['file_type']
        if not self.check_file_extension(file_type):
            raise APIException(detail='File type not supported',
                               code=status.HTTP_400_BAD_REQUEST)

        if os.environ.get('DJANGO_SETTINGS_MODULE') == 'reclass.settings.production':
            try:
                bucket_name = settings.AWS_S3_BUCKET_NAME
                object_name = self.location + '/' + \
                    self.get_filename() + self.get_file_extension(file_type)

                url = s3_client.generate_presigned_url(
                    ClientMethod='put_object',
                    Params={
                        'Bucket': bucket_name,
                        'Key': object_name
                    },
                    ExpiresIn=expiration)
                return {
                    'resource_url': object_name,
                    'upload_url': url
                }

            except ClientError as e:
                logging.error(e)
                return None
        else:
            resource_url = self.location + '/' + \
                self.get_filename() + self.get_file_extension(file_type)
            upload_url = 'https://127.0.0.1:8000/media/' + resource_url

            return {
                'resource_url': resource_url,
                'upload_url': upload_url
            }
