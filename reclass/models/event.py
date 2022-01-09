from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from . subject import Subject
from . user import User

class ActiveSchedule(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Event(models.Model):
    REPEAT_CYCLE = (
        ('daily', 'daily'),
        ('weekly', 'weekly'),
        ('monthly', 'monthly'),
        ('yearly', 'yearly')
    )

    WEEKLY_REPEAT_DAY = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday')
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='event_created'
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        related_name='events',
        blank=True,
        null=True
    )
    title = models.CharField(max_length=355)
    description = models.TextField(blank=True, null=True)
    attachment = models.CharField(max_length=200, blank=True, null=True)
    is_repeat = models.BooleanField(default=False)
    schedule_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    repeat_cycle = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=REPEAT_CYCLE
    )
    weekly_repeat_day = models.IntegerField(
        blank=True,
        null=True,
        choices=WEEKLY_REPEAT_DAY
    )
    monthly_repeat_day = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1, 'month day cannot go below 1'),
            MaxValueValidator(31, 'month day cannot exceed 31')
        ]
    )
    daily_exclude_days = ArrayField(
        models.IntegerField(
            choices=WEEKLY_REPEAT_DAY
        ),
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Managers
    objects = models.Manager()
    active_objects = ActiveSchedule()

    class Meta:
        db_table = 'events'

    def __str__(self) -> str:
        return self.title