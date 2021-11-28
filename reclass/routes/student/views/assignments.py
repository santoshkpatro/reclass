from rest_framework import generics, permissions, serializers
from reclass.models import Assignment, Subject
from ..permissions import IsEnrolled
from ..mixins import SubjectEnrolledMixin


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'attachment', 'submission_due']


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
