# Generated by Django 2.2.6 on 2019-10-10 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191010_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='imaage',
            new_name='image',
        ),
    ]
