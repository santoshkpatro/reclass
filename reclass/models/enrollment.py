from django.db import models
from .user import User
from .subject import Subject


class Enrollment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='enrolled'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )

    enrolled_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'enrollments'
        unique_together = ['user', 'subject']

    def __str__(self) -> str:
        return self.user.email + ' is enrolled in subject ' + self.subject.title
