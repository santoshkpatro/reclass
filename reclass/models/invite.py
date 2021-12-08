import uuid
from django.db import models, transaction
from .user import User
from .subject import Subject
from .enrollment import Enrollment


class SubjectInvite(models.Model):
    INVITE_STATUS = (
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected')
    )

    invite_code = models.CharField(editable=False, unique=True, max_length=35)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True,
        related_name='invites'
    )
    invitee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='invited'
    )
    status = models.CharField(
        max_length=10,
        default='pending',
        choices=INVITE_STATUS
    )
    expiry = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subject_invites'

    def save(self, *args, **kwargs):
        if not self.invite_code:
            self.invite_code = uuid.uuid4().hex
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return 'Invitation for ' + self.invitee.email + ' by ' + self.inviter.email + ' to join ' + self.subject.title

    @transaction.atomic
    def approve(self):
        try:
            enrollment = Enrollment(user=self.invitee, subject=self.subject)
            enrollment.save()
            self.status = 'approved'
            self.save()
            return True
        except:
            return False

    @transaction.atomic
    def reject(self):
        try:
            self.status = 'rejected'
            self.save()
            return True
        except:
            return False
