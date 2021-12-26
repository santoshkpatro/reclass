import os
import boto3
import logging
from botocore.exceptions import ClientError
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .permissions import IsAdminUser

s3_client = boto3.client('s3', region_name=settings.AWS_REGION)


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def get(self, request, filename):
        location = request.query_params['location']

        if(os.environ.get('DJANGO_SETTINGS_MODULE') == 'reclass.settings.production'):
            try:
                bucket_name = settings.AWS_S3_BUCKET_NAME
                object_name = location + filename
                expiration = 3600

                url = s3_client.generate_presigned_url(
                    ClientMethod='put_object',
                    Params={
                        'Bucket': bucket_name,
                        'Key': object_name
                    },
                    ExpiresIn=expiration)

            except ClientError as e:
                logging.error(e)
                return None
        else:
            url = location + filename
        return Response(url, status=status.HTTP_200_OK)

    # Valid for localhost
    def put(self, request, filename):
        file_obj = request.FILES['file']
        location = request.query_params['location']
        url = location + filename

        fs = FileSystemStorage()
        file = fs.save(url, file_obj)
        resource_url = 'http://127.0.0.1:8000' + fs.url(file)

        return Response(resource_url, status=status.HTTP_201_CREATED)
