# Generated by Django 2.2.6 on 2019-10-11 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_auto_20191011_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronjob',
            name='cronjob',
            field=models.CharField(default='* * * * *', max_length=5),
        ),
    ]