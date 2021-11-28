from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status, permissions, serializers
from rest_framework.exceptions import APIException
from reclass.models import Subject, SubjectInvite, User
from ..permissions import IsAdminUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'subject_code']


class SubjectInviteSerializer(serializers.ModelSerializer):
    subject_id = serializers.IntegerField(required=True, write_only=True)
    invitee_id = serializers.IntegerField(required=True, write_only=True)
    subject = SubjectSerializer(read_only=True, many=False)
    inviter = UserSerializer(read_only=True, many=False)
    invitee = UserSerializer(read_only=True, many=False)

    class Meta:
        model = SubjectInvite
        fields = [
            'subject_id',
            'invitee_id',
            'invite_code',
            'subject',
            'inviter',
            'invitee',
            'status',
            'expiry',
            'note',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        subject_id = validated_data.pop('subject_id')
        invitee_id = validated_data.pop('invitee_id')
        try:
            invitee = User.objects.get(id=invitee_id)
            subject = Subject.objects.get(id=subject_id)

            invitation = SubjectInvite(
                **validated_data,
                invitee=invitee,
                subject=subject
            )
            invitation.save()

            # Send Inviation

            return invitation

        except ObjectDoesNotExist:
            raise APIException(
                detail='Details not found!',
                code=status.HTTP_404_NOT_FOUND
            )


class SubjectInviteListView(generics.ListCreateAPIView):
    serializer_class = SubjectInviteSerializer
    queryset = SubjectInvite.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(inviter=self.request.user)


class SubjectInviteDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = SubjectInviteSerializer
    queryset = SubjectInvite.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]
