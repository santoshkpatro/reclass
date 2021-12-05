from django.db.models import Q
from rest_framework import generics, status, permissions, serializers
from reclass.models import User
from ..permissions import IsAdminUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

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
            'password'
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

        return queryset


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
