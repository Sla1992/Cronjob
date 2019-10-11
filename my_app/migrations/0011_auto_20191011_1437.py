# Generated by Django 2.2.6 on 2019-10-11 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_auto_20191011_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cronjob',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]