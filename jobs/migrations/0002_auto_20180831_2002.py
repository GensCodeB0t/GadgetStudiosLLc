# Generated by Django 2.1 on 2018-09-01 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobsConfig',
            new_name='Job',
        ),
    ]
