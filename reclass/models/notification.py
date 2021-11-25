from django.db import models
from .subject import Subject
from .user import User


class Notification(models.Model):
    notifier = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='notificated'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        null=True,
        related_name='notifications'
    )
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    attachment = models.URLField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notifications'

    def __str__(self) -> str:
        return self.title
