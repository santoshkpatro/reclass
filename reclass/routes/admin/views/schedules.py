from django.contrib.postgres import fields
from rest_framework import generics, status, permissions, serializers
from rest_framework.exceptions import APIException
from reclass.models import Schedule, Subject
from reclass.models.user import User
from ..permissions import IsAdminUser


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'subject_code']


class ScheduleSerializer(serializers.ModelSerializer):
    subject_id = serializers.IntegerField(write_only=True, required=False)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = [
            'id',
            'user',
            'subject',
            'subject_id',
            'title',
            'description',
            'attachment',
            'is_repeat',
            'schedule_date',
            'start_time',
            'end_time',
            'repeat_cycle',
            'weekly_repeat_day',
            'monthly_repeat_day',
            'daily_exclude_days',
            'is_active',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        subject = None
        if 'subject_id' in validated_data:
            subject_id = validated_data.pop('subject_id')
            try:
                subject = Subject.objects.get(id=subject_id)

            except Subject.DoesNotExist:
                raise APIException(detail='Subject not found',
                                   code=status.HTTP_404_NOT_FOUND)

        schedule = Schedule(**validated_data, subject=subject)
        schedule.save()
        return schedule

    def update(self, instance, validated_data):
        if 'subject_id' in validated_data:
            subject_id = validated_data.pop('subject_id')
            try:
                subject = Subject.objects.get(id=subject_id)
                instance.subject = subject
            except Subject.DoesNotExist:
                raise APIException(detail='Subject not found',
                                   code=status.HTTP_404_NOT_FOUND)
        return super().update(instance, validated_data)


class ScheduleListView(generics.ListCreateAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()

        if 'weekly_repeat_day' in self.request.query_params:
            queryset = queryset.filter(
                weekly_repeat_day=int(
                    self.request.query_params['weekly_repeat_day'])
            )

        if 'monthly_repeat_day' in self.request.query_params:
            queryset = queryset.filter(
                monthly_repeat_day=int(
                    self.request.query_params['monthly_repeat_day'])
            )

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
