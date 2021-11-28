from rest_framework import generics, serializers, permissions
from reclass.models import Subject, Enrollment


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'subject_code', 'description', 'thumbnail']


class SubjectList(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.active_objects.all().order_by('created_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(enrollments__user=self.request.user)


class SubjectDetail(generics.CreateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.active_objects.all().order_by('created_at')
    permission_classes = [permissions.IsAuthenticated]
