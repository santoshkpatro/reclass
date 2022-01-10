from rest_framework import generics, permissions, serializers, status
from rest_framework.exceptions import APIException
from reclass.models import Assignment, Subject, Submission
from ..permissions import IsEnrolled
from ..mixins import SubjectEnrolledMixin


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title']


class AssignmentSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=False)

    class Meta:
        model = Assignment
        fields = [
            'id',
            'title',
            'subject',
            'description',
            'attachment',
            'submission_due'
        ]


class SubmissionSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = [
            'id',
            'is_complete',
            'attachments',
            'submission_note',
            'created_at'
        ]


class AssignmentList(generics.ListAPIView, SubjectEnrolledMixin):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all().order_by('submission_due')
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'subject_id' in self.request.query_params:
            subject = self.get_subject()
            return queryset.filter(subject=subject)
        return queryset.filter(subject__in=self.get_subjects())


class AssignmentDetail(generics.RetrieveAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsEnrolled]


class AssignmentSubmissionDetail(generics.RetrieveAPIView):
    serializer_class = SubmissionSerilaizer
    queryset = Submission.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        assignment_id = self.kwargs['pk']
        try:
            assignment = Assignment.objects.get(id=assignment_id)
            return assignment.submission
        except Assignment.DoesNotExist:
            raise APIException(detail='Assignment Not Found',
                               code=status.HTTP_404_NOT_FOUND)
