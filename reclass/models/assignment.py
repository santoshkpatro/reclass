from django.db import models
from django.contrib.postgres import fields
from reclass.models.base import BaseModel
from reclass.models.group import Group
from reclass.models.user import User


class Assignment(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_assignments'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='group_assignments',
        db_index=True
    )
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    attachment = models.CharField(max_length=200, blank=True, null=True)
    submission_due = models.DateTimeField(blank=True, null=True)
    allow_submission_after_due = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True, db_index=True)
    tags = fields.ArrayField(models.CharField(max_length=20), blank=True, null=True)

    class Meta:
        db_table = 'assignments'

    def __str__(self) -> str:
        return self.title