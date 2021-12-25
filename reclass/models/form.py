import uuid
from django.db import models
from .user import User
from .subject import Subject


class Form(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    builder = models.JSONField(blank=True, null=True)
    is_open = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    allow_multiple_response = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'forms'

    def __str__(self) -> str:
        return self.title
