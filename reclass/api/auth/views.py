import uuid
from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from reclass.api.auth.serializers import LoginSerializer, PasswordResetSerializer
from reclass.models.user import User


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(**serializer.data)
            if not user:
                return Response(data={'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

            if user.password_reset_required:
                return Response(data={'detail': 'Please reset your password to continue'}, status=status.HTTP_307_TEMPORARY_REDIRECT)
            
            user.last_login_ip = request.META['REMOTE_ADDR']
            user.save()

            return Response(data={
                'access_token': str(AccessToken.for_user(user)),
                'refresh_token': str(RefreshToken.for_user(user))
            })
        else:
            return Response(data={'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    def get(self, request):
        email = request.query_params.get('email', None)
        if not email:
            return Response(data={'detail': 'Email not found'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email, is_active=True)
            user.password_reset_token = uuid.uuid4().hex
            user.password_reset_expiry = timezone.now() + timezone.timedelta(minutes=60)
            # Send password reset email
            user.save()
            return Response(data={'detail': 'Password reset email has been sent'}, status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response(data={'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        reset_token = request.query_params.get('reset_token', None)
        if not reset_token:
            return Response(data={'detail': 'Reset token not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PasswordResetSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'detail': 'Invalid password input'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(password_reset_token=reset_token, is_active=True)
            user.set_password(serializer.data.get('password'))
            user.password_reset_token = None
            user.password_reset_expiry = None
            user.save()
            return Response(data={'detail': 'Password reset success'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
