# Generated by Django 2.2.6 on 2019-10-09 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_auto_20191009_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronjob',
            name='day',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='hour',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='minute',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
