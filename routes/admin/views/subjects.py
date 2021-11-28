from django.utils import timezone
from rest_framework import generics, serializers, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from reclass.models import Subject, SubjectInvite, User
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


class SubjectListView(generics.ListCreateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, IsAdminUser])
def subject_invite(request, id):
    try:
        subject = Subject.objects.get(id=id)
        if not 'emails' in request.data:
            return Response(data={'detail': 'Please add emails'}, status=status.HTTP_404_NOT_FOUND)

        emails = request.data['emails']
        validity = request.data.get('validity', None)
        failed_attempts = []
        for email in emails:
            try:
                user = User.objects.get(email=email)
                invite = SubjectInvite(
                    invitee=user,
                    inviter=request.user,
                    subject=subject
                )
                if validity:
                    invite.expiry = timezone.now() + timezone.timedelta(days=validity)

                invite.note = request.data.get('note', None)
                invite.save()

                # Send email invitation

            except User.DoesNotExist:
                failed_attempts.append(email)
        return Response(data={'detail': 'Invitations link has been sent', 'failed_attemps': failed_attempts}, status=status.HTTP_200_OK)
    except Subject.DoesNotExist:
        return Response(data={'detail': 'Subject not found'}, status=status.HTTP_404_NOT_FOUND)
