from django.db import models
# from django.contrib.postgres.fields import ArrayField
from .user import User
from .subject import Subject


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    message_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'messages'

    def __str__(self) -> str:
        return self.message
