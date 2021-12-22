from django.core.files.storage import FileSystemStorage
from django.conf import settings
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .permissions import IsAdminUser


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def get(self, request, filename):
        location = request.query_params['location']
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
