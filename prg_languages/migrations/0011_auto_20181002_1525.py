# Generated by Django 2.1 on 2018-10-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prg_languages', '0010_auto_20181002_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='prg_language',
            name='image_height',
            field=models.PositiveIntegerField(default=10, null=True),
        ),
        migrations.AddField(
            model_name='prg_language',
            name='image_width',
            field=models.PositiveIntegerField(default=10, null=True),
        ),
    ]
