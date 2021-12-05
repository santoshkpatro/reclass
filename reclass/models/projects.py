from django.db import models
from reclass.models import User


class Project(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='projects'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    collaborators = models.ManyToManyField(User, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects'

    def __str__(self) -> str:
        return self.title
