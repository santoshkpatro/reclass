from django.db import models
from django.contrib.postgres import fields
from reclass.models.base import BaseModel
from reclass.models.group import Group
from reclass.models.user import User


"""
This model is responsible for
managing list of events
"""
class Event(BaseModel):
    STATUS_CHOICES = (
        ('scheduled', 'scheduled'),
        ('inprogress', 'inprogress'),
        ('complete', 'complete'),
        ('cancelled', 'cancelled')
    )

    EVENT_TYPE_CHOICES = (
        ('lecture', 'lecture'),
        ('seminar', 'seminar'),
        ('conferences', 'conferences'),
        ('workshop', 'workshop')
    )

    organizer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='organizer_events')
    thumbnail = models.CharField(max_length=200, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='group_events', db_index=True)
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True, default='scheduled')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    event_type = models.CharField(max_length=12, default='lecture', choices=EVENT_TYPE_CHOICES)
    scheduled_on = models.DateTimeField(blank=True, null=True, db_index=True)
    attachment = models.CharField(max_length=200, blank=True, null=True)
    tags = fields.ArrayField(models.CharField(max_length=20), blank=True, null=True)

    class Meta:
        db_table = 'events'

    def __str__(self) -> str:
        return self.title