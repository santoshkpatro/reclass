from django.db.models import Q
from rest_framework import generics, permissions, serializers
from reclass.models import Notification, Subject, User
from ..mixins import SubjectEnrolledMixin


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar']


class NotificationSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True, many=False)
    notifier = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Notification
        fields = [
            'id',
            'notifier',
            'subject',
            'title',
            'description',
            'attachment',
            'tags',
            'created_at'
        ]


class NotificationList(generics.ListAPIView, SubjectEnrolledMixin):
    serializer_class = NotificationSerializer
    queryset = Notification.published_objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'subject_id' in self.request.query_params:
            subject = self.get_subject()
            return queryset.filter(subject=subject)

        queryset = queryset.filter(
            Q(subject__in=self.get_subjects()) |
            Q(subject=None)
        )

        return queryset
