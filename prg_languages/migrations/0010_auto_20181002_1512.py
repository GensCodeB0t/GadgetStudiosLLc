# Generated by Django 2.1 on 2018-10-02 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prg_languages', '0009_auto_20181002_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prg_language',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='prg_language',
            name='image_width',
        ),
    ]
