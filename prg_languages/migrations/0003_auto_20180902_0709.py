# Generated by Django 2.1 on 2018-09-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prg_languages', '0002_auto_20180902_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prg_language',
            name='image',
            field=models.ImageField(height_field=50, upload_to='prg_language/'),
        ),
    ]
