from rest_framework import serializers, generics, status, permissions
from rest_framework.exceptions import APIException
from reclass.models import Assignment, Subject
from ..permissions import IsAdminUser


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            'id',
            'title',
            'subject_code',
            'description',
            'thumbnail',
            'is_active',
            'created_at',
            'updated_at'
        ]


class AssignmentSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True, many=False)
    subject_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Assignment
        fields = [
            'id',
            'subject_id',
            'subject',
            'title',
            'description',
            'attachment',
            'submission_due',
            'allow_submission_after_due',
            'is_active',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        subject_id = validated_data.pop('subject_id')
        try:
            subject = Subject.objects.get(id=subject_id)
            assignment = Assignment(**validated_data, subject=subject)
            assignment.save()
            return assignment

        except Subject.DoesNotExist:
            raise APIException(detail='Subject not found',
                               code=status.HTTP_404_NOT_FOUND)

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


class AssignmentListView(generics.ListCreateAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
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
        return serializer.save(user=self.request.user)


class AssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
