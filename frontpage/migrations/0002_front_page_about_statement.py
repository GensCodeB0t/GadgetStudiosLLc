# Generated by Django 2.1 on 2018-09-29 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='front_page',
            name='about_statement',
            field=models.TextField(null=True),
        ),
    ]