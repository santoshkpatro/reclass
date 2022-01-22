from django.db import models
from django.contrib.postgres import fields
from reclass.models.base import BaseModel
from reclass.models.group import Group
from reclass.models.user import User


"""
This model is responsible for managing
notifications
"""
class Notification(BaseModel):
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='user_notifications'
    )
    title = models.CharField(max_length=300)
    description = models.TextField()
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='group_notifications',
        db_index=True
    )
    attachment = models.CharField(max_length=200, blank=True, null=True)
    tags = fields.ArrayField(models.CharField(max_length=20), blank=True, null=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        db_table = 'notifications'

    def __str__(self) -> str:
        return self.title
