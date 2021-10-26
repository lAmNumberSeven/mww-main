from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self
