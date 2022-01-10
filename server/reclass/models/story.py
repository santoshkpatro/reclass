from django.db import models
from .subject import Subject


class Story(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    image = models.URLField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    background_color = models.CharField(max_length=10, blank=True, null=True)
    valid_upto = models.PositiveBigIntegerField(default=24)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.id)
