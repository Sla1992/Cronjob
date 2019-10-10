# Generated by Django 2.2.6 on 2019-10-10 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0004_auto_20191010_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friend',
            name='person',
            field=models.CharField(default='', max_length=128),
        ),
    ]
