from django.db import models
from django.contrib.postgres import fields
from reclass.models.base import BaseModel
from reclass.models.user import User
from reclass.models.assignment import Assignment


class Submission(BaseModel):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='user_submissions'
    )
    assignment = models.ForeignKey(
        Assignment, 
        on_delete=models.CASCADE, 
        related_name='assignment_submissions',
        db_index=True
    )
    attachments = fields.ArrayField(
        models.CharField(max_length=200),
        blank=True,
        null=True
    )
    note = models.TextField(blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    is_complete = models.BooleanField(default=True, db_index=True)
    submitted_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'submissions'
        unique_together = ['user', 'assignment']

    def __str__(self) -> str:
        return str(self.id)