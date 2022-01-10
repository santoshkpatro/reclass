from rest_framework import serializers, generics, status, permissions
from rest_framework.exceptions import APIException
from reclass.models import User, Subject, Submission, Assignment
from ..permissions import IsAdminUser
from django.core.exceptions import ObjectDoesNotExist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar']


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'submission_due']


class SubmissionSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    assignment_id = serializers.IntegerField(write_only=True)

    user = UserSerializer(read_only=True, many=False)
    assignment = AssignmentSerializer(read_only=True, many=False)

    class Meta:
        model = Submission
        fields = [
            'id',
            'user_id',
            'user',
            'assignment_id',
            'assignment',
            'is_complete',
            'attachments',
            'submission_note',
            'instructor_remark',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        assignment_id = validated_data.pop('assignment_id')
        user_id = validated_data.pop('user_id')
        try:
            user = User.objects.get(id=user_id)
            assignment = Assignment.objects.get(id=assignment_id)

            submission = Submission(
                **validated_data,
                user=user,
                assignment=assignment
            )
            submission.save()
            return submission

        except ObjectDoesNotExist:
            raise APIException(
                detail='Details not found!',
                code=status.HTTP_404_NOT_FOUND
            )

    def update(self, instance, validated_data):
        if 'assignment_id' in validated_data:
            assignment_id = validated_data.pop('assignment_id')
            try:
                assignment = Assignment.objects.get(id=assignment_id)
                instance.assignment = assignment
                instance.save()
            except Assignment.DoesNotExist:
                raise APIException(detail='Assignment not found',
                                   code=status.HTTP_404_NOT_FOUND)

        if 'user_id' in validated_data:
            user_id = validated_data.pop('user_id')
            try:
                user = User.objects.get(id=user_id)
                instance.user = user
                instance.save()
            except Subject.DoesNotExist:
                raise APIException(detail='User not found',
                                   code=status.HTTP_404_NOT_FOUND)
        return super().update(instance, validated_data)


class SubmissionListView(generics.ListCreateAPIView):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'assignment_id' in self.request.query_params:
            assignment_id = self.request.query_params['assignment_id']
            try:
                assignment = Assignment.objects.get(id=assignment_id)
                queryset = queryset.filter(assignment=assignment)
            except Assignment.DoesNotExist:
                raise APIException(detail='Assignment not found',
                                   code=status.HTTP_404_NOT_FOUND)

        if 'user_id' in self.request.query_params:
            user_id = self.request.query_params['user_id']
            try:
                user = User.objects.get(id=user_id)
                queryset = queryset.filter(user=user)
            except User.DoesNotExist:
                raise APIException(detail='User not found',
                                   code=status.HTTP_404_NOT_FOUND)

        if 'subject_id' in self.request.query_params:
            subject_id = self.request.query_params['subject_id']
            try:
                subject = Subject.objects.get(id=subject_id)
                queryset = queryset.filter(assignment__subject=subject)
            except Subject.DoesNotExist:
                raise APIException(detail='Subject not found',
                                   code=status.HTTP_404_NOT_FOUND)

        return queryset


class SubmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
