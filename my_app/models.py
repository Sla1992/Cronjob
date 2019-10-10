from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Cronjob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    title = models.CharField(max_length=128, null=False, default='')

    url = models.URLField(max_length=255, null=False, default='')

    authentification = models.BooleanField(default=False, null=True)

    username = models.CharField(max_length=30, null=True, default='')

    password = models.CharField(max_length=30, null=True, default='')

    day = models.IntegerField(default=0)

    hour = models.IntegerField(default=0)

    minute = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Friend(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    person = models.CharField(max_length=128, null=False, default='')
    lives = models.CharField(max_length=128, null=False, default='')
    land = models.CharField(max_length=128, null=False, default='')
    added = models.DateTimeField(default=timezone.now)
    birthdate = models.CharField(max_length=128, null=False, default='')

    def __str__(self):
        return self.person





