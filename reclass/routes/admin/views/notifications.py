from rest_framework import serializers, status, generics, permissions
from rest_framework.exceptions import APIException
from reclass.models import Notification, Subject, User
from ..permissions import IsAdminUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'subject_code']


class NotificationSerializer(serializers.ModelSerializer):
    notifier = UserSerializer(read_only=True, many=False)
    subject = SubjectSerializer(read_only=True, many=False)
    subject_id = serializers.IntegerField(write_only=True, required=False)

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
            'is_published',
            'created_at',
            'updated_at',
            'subject_id'
        ]

    def create(self, validated_data):
        if 'subject_id' in validated_data:
            subject_id = validated_data.pop('subject_id')
            try:
                subject = Subject.objects.get(id=subject_id)
                notification = Notification(**validated_data, subject=subject)
                notification.save()
                return notification

            except Subject.DoesNotExist:
                raise APIException(detail='Subject not found',
                                   code=status.HTTP_404_NOT_FOUND)

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'subject_id' in validated_data:
            subject_id = validated_data.pop('subject_id')
            try:
                subject = Subject.objects.get(id=subject_id)
                instance.subject = subject
                instance.save()
            except Subject.DoesNotExist:
                raise APIException(detail='Subject not found',
                                   code=status.HTTP_404_NOT_FOUND)
        return super().update(instance, validated_data)


class NotificationListView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()

        if 'subject_id' in self.request.query_params:
            subject_id = self.request.query_params['subject_id']
            try:
                subject = Subject.objects.get(id=subject_id)
                queryset = queryset.filter(subject=subject)
            except Subject.DoesNotExist:
                raise APIException(detail='Subject not found',
                                   code=status.HTTP_404_NOT_FOUND)

        return queryset

    def perform_create(self, serializer):
        serializer.save(notifier=self.request.user)


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
