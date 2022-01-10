
from django.db.models import Q
from rest_framework import generics, permissions, serializers, views, status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from reclass.models import User, Enrollment, Subject
from ..permissions import IsAdminUser
from ..mixins import FileUploadMixin


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


class UserAvatarUpload(views.APIView, FileUploadMixin):
    parser_classes = [FileUploadParser]
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
    location = 'avatars'
    supported_file_types = ['.png', '.jpg', '.jpeg']

    def get(self, request, pk):
        data = self.get_urls(expiration=3600)
        return Response(data=data, status=status.HTTP_200_OK)


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
