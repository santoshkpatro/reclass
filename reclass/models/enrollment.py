from django.db import models
from reclass.models.base import BaseModel
from reclass.models.user import User
from reclass.models.group import Group


"""
This model is responsible for user enrollment
and role in a particular group
"""
class Enrollment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_enrollments')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_enrollments')
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        db_table = 'enrollments'
        unique_together = ['user', 'group']

    def __str__(self) -> str:
        return str(self.id)