from django.db import models
from django.contrib.postgres.fields import ArrayField
from .assignment import Assignment
from .user import User


class Submission(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='submitted'
    )
    assignment = models.OneToOneField(
        Assignment,
        on_delete=models.CASCADE,
    )
    is_complete = models.BooleanField(default=True)
    attachments = ArrayField(models.URLField(), blank=True, null=True)
    submission_note = models.TextField(blank=True, null=True)
    instructor_remark = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'submissions'
        unique_together = ['user', 'assignment']

    def __str__(self) -> str:
        return self.user.email + ' submitted ' + self.assignment.title
