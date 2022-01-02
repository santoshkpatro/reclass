from django.db import models
from django.contrib.postgres.fields import ArrayField
from .subject import Subject
from .user import User


class PublishedNotification(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


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
        related_name='notifications',
        blank=True
    )
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    attachment = models.CharField(blank=True, null=True, max_length=200)
    is_published = models.BooleanField(default=False)
    tags = ArrayField(models.CharField(max_length=15), blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published_objects = PublishedNotification()

    class Meta:
        db_table = 'notifications'

    def __str__(self) -> str:
        return self.title
