from django.core.files.storage import FileSystemStorage
from django.conf import settings
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from .permissions import IsAdminUser


# Valid for local env
class FileUploadView(APIView):
    parser_classes = [FileUploadParser]
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def put(self, request, filename=None):
        file_obj = request.data['file']
        location = request.query_params['location']
        url = location

        fs = FileSystemStorage()
        file = fs.save(url, file_obj)
        resource_url = 'http://127.0.0.1:8000' + fs.url(file)

        return Response(resource_url, status=status.HTTP_201_CREATED)
