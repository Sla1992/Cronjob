from django.db import models
from django.contrib.auth.models import User


class Cronjob(models.Model):

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default='')

    enabled = models.BooleanField(default=True)

    title = models.CharField(max_length=128, null=False, default='')

    url = models.URLField(max_length=255, null=False, default='')

    authentification = models.BooleanField(default=False)

    username = models.CharField(max_length=30, null=False, default='')

    password = models.CharField(max_length=30, null=False, default='')


