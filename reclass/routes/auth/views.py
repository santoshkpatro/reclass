import uuid
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets, serializers, status, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.decorators import api_view
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


class PasswordResetSerilaizer(serializers.Serializer):
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise ValidationError(
                detail='Password and confirm password match invalid', code=status.HTTP_400_BAD_REQUEST)
        return super().validate(attrs)


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

        # Saving user details
        user.last_login = timezone.now()
        user.save()

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


@api_view(['POST'])
def password_reset(request):
    email = request.data['email']
    try:
        user = User.objects.get(email=email)
        user.password_reset_token = uuid.uuid4().hex
        user.password_reset_expiry = timezone.now() + timezone.timedelta(minutes=30)
        user.save()

        # Send Email
        url = f'{settings.FRONTEND_BASE_URL}/auth/password_reset/confirm/{user.password_reset_token}'
        send_mail(
            subject='Password Reset Link',
            message=f'Password Reset link has been shared click {url} to reset your password',
            from_email='noreply@reclass.com',
            recipient_list=[user.email],
            fail_silently=True
        )

        return Response(data={'detail': 'Reset link has been sent'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(
            data={'detail': 'No account found with this email id'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['GET'])
def password_reset_verify(request, reset_token):
    try:
        user = User.objects.get(password_reset_token=reset_token)
        if timezone.now() <= user.password_reset_expiry:
            return Response(data={'detail': 'Valid'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Reset link has been expired'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response(data={'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def password_reset_confirm(request, reset_token):
    try:
        user = User.objects.get(password_reset_token=reset_token)
        if timezone.now() <= user.password_reset_expiry:
            serializer = PasswordResetSerilaizer(data=request.data)
            if serializer.is_valid():
                user.set_password(request.data['password'])
                user.password_reset_expiry = None
                user.password_reset_token = None
                user.save()
                return Response(data={'detail': 'Password reset confirm'}, status=status.HTTP_200_OK)
            else:
                return Response(data={'detail': 'Please make sure password and confirm password are valid'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'detail': 'Reset link has been expired'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response(data={'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
