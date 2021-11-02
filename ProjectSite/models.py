

from django.db import models
from django.contrib.auth.models import AbstractUser


class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self


class User(AbstractUser):
    is_Paradym = models.BooleanField('Is Paradym', default=False)
    is_ThirdParty = models.BooleanField('Is ThirdParty', default=False)
    is_Admin = models.BooleanField('Is Admin', default=False)