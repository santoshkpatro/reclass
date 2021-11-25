from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=150)
    subject_code = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subjects'

    def __str__(self) -> str:
        return self.title
