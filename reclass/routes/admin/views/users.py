import os
import uuid
import mimetypes
import time
from django.db.models import Q
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework import generics, permissions, serializers, views, status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.decorators import api_view
from reclass.models import User, Enrollment, Subject
from ..permissions import IsAdminUser
from ..helpers import file_extension, handle_file_upload


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'subject_code']


class EnrollmentSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'subject', 'enrolled_on', 'is_active']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    enrolled = EnrollmentSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'phone',
            'gender',
            'avatar',
            'password_reset_required',
            'is_active',
            'is_admin',
            'is_instructor',
            'updated_at',
            'created_at',
            'last_login',
            'password',
            'enrolled',
        ]

    # While saving new user
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    # While updating user details
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            instance.save()
        return super().update(instance, validated_data)


class UserAvatarUpload(views.APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def put(self, request, pk, format=None):
        try:
            user = User.objects.get(id=pk)

            file_obj = request.FILES['file']
            fs = FileSystemStorage()
            ext = os.path.splitext(file_obj.name.lower())[1]
            file_name = 'avatars/' + uuid.uuid4().hex + ext
            file = fs.save(file_name, file_obj)
            user.avatar = 'http://127.0.0.1:8000' + fs.url(file)
            user.save()
            serializer = UserSerializer(instance=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=204)


# class UserAvatar(views.APIView):
#     parser_classes = [MultiPartParser]
#     permission_classes = [permissions.IsAuthenticated, IsAdminUser]

#     def get(self, request, pk):
#         pass

#     # Valid for local upload only
#     def put(self, request, pk):
#         pass


class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()

        # Checking for instructor filter
        if 'instructor' in self.request.query_params:
            value = self.request.query_params['instructor']
            if value.lower() in ['True', 'true', '1', 't', 'y', 'yes']:
                queryset = queryset.filter(is_instructor=True)

        # Search filter
        if 'search' in self.request.query_params:
            search = self.request.query_params['search']
            queryset = queryset.filter(
                Q(email__icontains=search) |
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search)
            )

        q = queryset.filter(is_admin=False)
        return q


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]


@api_view(['GET'])
def get_upload_url_avatar(request, pk):
    file_type = request.query_params['file_type']
    ext = mimetypes.guess_extension(file_type)
    resource_url = f'avatars/{uuid.uuid4()}{ext}'
    upload_url = 'http://127.0.0.1:8000/media' + '/' + resource_url
    return Response(data={'resource_url': resource_url, 'upload_url': upload_url}, status=status.HTTP_200_OK)
