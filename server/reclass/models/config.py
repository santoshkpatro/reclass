from django.db import models


class Config(models.Model):
    org_name = models.CharField(max_length=50)
