import uuid
from django.db import models

"""
This is an abstract base model which can
be inherited by other models
"""
class BaseModel(models.Model):
    # We are using uuid instead of auto increment serial key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    """
    Timestamp is compulsory in every table.
    It is also required for auditing purpose.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True