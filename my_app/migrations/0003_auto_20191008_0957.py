# Generated by Django 2.2.6 on 2019-10-08 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20191008_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='cronjob',
            name='authentification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]
