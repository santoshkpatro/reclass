from rest_framework import generics, status, permissions
from rest_framework.response import Response
from reclass.api.groups.serializers import GroupListSerializers, GroupDetailSerializer, GroupUpdateSerializer
from reclass.models.group import Group
from reclass.api.permissions import IsEnrolledOrOwner, IsOwner


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
    serializer_class = GroupDetailSerializer
    queryset = Group.active_objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]