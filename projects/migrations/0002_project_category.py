# Generated by Django 2.1 on 2018-10-03 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('.desktop', 'desktop'), ('.websites', 'websites'), ('.mobile', 'mobile'), ('.IoT', 'IoT')], default='.desktop', max_length=10, null=True),
        ),
    ]
