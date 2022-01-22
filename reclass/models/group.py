from django.db import models
from reclass.models.base import BaseModel
from reclass.models.user import User


"""
This manager is responsible for
managing active group
"""
class ActiveGroupManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Group(BaseModel):
    TYPE_CHOICES = (
        ('subject', 'subject'),
        ('club', 'club'),
        ('guest', 'guest')
    )

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_groups')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True, db_index=True)
    group_type = models.CharField(
        max_length=12, 
        blank=True, 
        null=True, 
        default='subject', 
        choices=TYPE_CHOICES
    )

    objects = models.Manager() # Default manager
    active_objects = ActiveGroupManager() # Active group manager

    class Meta:
        db_table = 'groups'

    def __str__(self) -> str:
        return self.name