from django.db import models
from .subject import Subject
from .user import User


class Assignment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assignment_created'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='assignments'
    )
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    attachment = models.URLField(blank=True, null=True)
    submission_due = models.DateTimeField(blank=True, null=True)
    allow_submission_after_due = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'assignments'

    def __str__(self) -> str:
        return self.title
