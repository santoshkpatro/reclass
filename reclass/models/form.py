from django.db import models
from django.contrib.postgres import fields
from reclass.models.base import BaseModel
from reclass.models.user import User
from reclass.models.group import Group


class Form(BaseModel):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_forms'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='group_forms',
        db_index=True
    )
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    builder = models.JSONField(blank=True, null=True)
    is_open = models.BooleanField(default=True, db_index=True)
    allow_multiple_response = models.BooleanField(default=False)
    tags = fields.ArrayField(models.CharField(max_length=20), blank=True, null=True)

    class Meta:
        db_table = 'forms'

    def __str__(self) -> str:
        return self.title