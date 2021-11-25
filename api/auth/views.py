from django.contrib.auth import authenticate, login
from rest_framework import viewsets, serializers, status, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.tokens import AccessToken
from reclass.models import User


class ProfileSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'phone',
            'gender',
            'avatar',
            'is_admin',
            'is_instructor',
            'access_token'
        ]
        extra_kwargs = {
            'email': {
                'read_only': True
            },
            'is_admin': {
                'read_only': True
            },
            'is_instructor': {
                'read_only': True
            }
        }

    def get_access_token(self, obj):
        return str(AccessToken.for_user(obj))


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


@api_view(['POST'])
def login_view(request):
    login_serializer = LoginSerializer(data=request.data)

    # Check for valid input
    if login_serializer.is_valid():

        # Check for authentication
        user = authenticate(
            email=login_serializer.data['email'],
            password=login_serializer.data['password']
        )

        # Raise error if invalid credentials
        if not user:
            return Response(data={'detail': 'Either email or password is invalid'}, status=status.HTTP_400_BAD_REQUEST)

        # Return user profile along with access token
        serializer = ProfileSerializer(instance=user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(data={'detail': 'Something went wrong!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
