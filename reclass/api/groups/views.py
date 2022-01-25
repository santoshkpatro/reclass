from django.db import IntegrityError
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from reclass.models.group import Group
from reclass.models.enrollment import Enrollment
from reclass.api.groups.serializers import GroupListSerializers, GroupDetailSerializer, GroupUpdateSerializer, GroupEnrollmentSerializer
from reclass.api.permissions import IsEnrolledOrOwner, IsOwner
from reclass.api.exceptions import GroupNotFoundException, UserNotFoundException
from reclass.models.user import User


class GroupListView(generics.ListAPIView):
    serializer_class = GroupListSerializers
    queryset = Group.active_objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(
            group_enrollments__user=self.request.user, 
            group_enrollments__is_active=True
        )


class GroupDetailView(generics.RetrieveAPIView):
    serializer_class = GroupDetailSerializer
    queryset = Group.active_objects.all()
    permission_classes = [permissions.IsAuthenticated, IsEnrolledOrOwner]


class GroupUpdateView(generics.UpdateAPIView):
    serializer_class = GroupUpdateSerializer
    queryset = Group.active_objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class GroupEnrollmentsListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_group(self, pk):
        try:
            group = Group.objects.get(pk=pk, owner=self.request.user)
            return group
        except Group.DoesNotExist:
            raise GroupNotFoundException

    def get(self, request, pk):
        group = self.get_group(pk)
        enrollments = Enrollment.objects.filter(group=group)
        serializer = GroupEnrollmentSerializer(enrollments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class GroupEnrollmentsCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_group(self, pk):
        try:
            group = Group.objects.get(pk=pk, owner=self.request.user)
            return group
        except Group.DoesNotExist:
            raise GroupNotFoundException

    def get_user(self, user_email):
        try:
            user = User.objects.get(email=user_email)
            return user
        except User.DoesNotExist:
            raise UserNotFoundException

    def get(self, request, pk):
        group = self.get_group(pk)
        user_email = request.query_params.get('email', None)
        if user_email is None:
            return Response(data={'detail': 'Please provide user email'}, status=status.HTTP_400_BAD_REQUEST)
        user = self.get_user(user_email)
        enrollment = Enrollment(user=user, group=group)
        try:
            enrollment.save()
        except IntegrityError:
            return Response(data={'detail': 'User is already enrolled in this group'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = GroupEnrollmentSerializer(enrollment)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

