from rest_framework import generics, status, serializers, permissions
from rest_framework.exceptions import APIException
from reclass.models import Assignment, Submission, Subject
from ..permissions import IsEnrolled, IsOwner


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = [
            'id',
            'title'
        ]


class SubmissionSerilaizer(serializers.ModelSerializer):
    assignment_id = serializers.IntegerField(write_only=True)
    assignment = AssignmentSerializer(read_only=True)

    class Meta:
        model = Submission
        fields = [
            'id',
            'assignment_id',
            'assignment',
            'is_complete',
            'attachments',
            'submission_note',
            'created_at'
        ]


class SubmissionList(generics.ListCreateAPIView):
    serializer_class = SubmissionSerilaizer
    queryset = Submission.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        assignment = self.request.data['assignment_id']
        try:

            assignment = Assignment.objects.get(id=assignment)
            if not assignment.subject in Subject.active_objects.filter(
                    enrollments__user=self.request.user):
                raise APIException(
                    detail='Unauthorized access',
                    code=status.HTTP_401_UNAUTHORIZED
                )

        except Assignment.DoesNotExist:

            raise APIException(
                detail='Assignment not found',
                code=status.HTTP_404_NOT_FOUND
            )

        return serializer.save(user=self.request.user, assignment=assignment)


class SubmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubmissionSerilaizer
    queryset = Submission.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated, IsOwner]
