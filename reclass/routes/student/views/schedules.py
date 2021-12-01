from django.db.models import Q
from rest_framework import generics, permissions, serializers, status
from reclass.models import Schedule, Subject
from ..mixins import SubjectEnrolledMixin


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'user',
            'subject',
            'title',
            'description',
            'attachment',
            'schedule_date',
            'start_time',
            'end_time',
        ]


class ScheduleListView(generics.ListAPIView, SubjectEnrolledMixin):
    serializer_class = ScheduleSerializer
    queryset = Schedule.active_objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            Q(subject__in=self.get_subjects()) |
            Q(subject=None)
        )
        return queryset
