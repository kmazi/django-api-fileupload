# Generated by Django 2.0.6 on 2018-07-06 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_auto_20180706_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='created',
        ),
    ]