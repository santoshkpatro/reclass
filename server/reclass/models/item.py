import uuid
from django.db import models
from .user import User


class Item(models.Model):
    ITEM_CHOICES = (
        ('file', 'file'),
        ('folder', 'folder')
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=ITEM_CHOICES)
    resource_url = models.CharField(max_length=200, blank=True, null=True)
    is_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'items'

    def __str__(self) -> str:
        return self.name
