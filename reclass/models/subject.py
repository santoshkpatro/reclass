from django.db import models


class ActiveSubject(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Subject(models.Model):
    title = models.CharField(max_length=150)
    subject_code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    active_objects = ActiveSubject()

    class Meta:
        db_table = 'subjects'

    def __str__(self) -> str:
        return self.title
