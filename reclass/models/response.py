from django.db import models
from reclass.models.base import BaseModel
from reclass.models.user import User
from reclass.models.form import Form


class Response(BaseModel):
    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        related_name='form_responses'
    ),
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_responses'
    )
    form_data = models.JSONField(blank=True, null=True)
    upload_data = models.JSONField(blank=True, null=True)
    is_spam = models.BooleanField(default=False)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'responses'

    def __str__(self) -> str:
        return str(self.id)