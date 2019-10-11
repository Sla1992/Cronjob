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

    day = models.CharField(max_length=3, default=0)

    hour = models.CharField(max_length=3, default=0)

    minute = models.CharField(max_length=3, default=0)

    cronjob = models.CharField(max_length=5,null=False,default="* * * * *")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Neuigkeiten(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    title = models.CharField(max_length=128, null=False, default='')
    text = models.TextField(max_length=1000, null=False, default='')
    added = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title





