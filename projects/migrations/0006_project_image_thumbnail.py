# Generated by Django 2.1 on 2018-10-11 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_thumbnail',
            field=models.ImageField(null=True, upload_to='projects/'),
        ),
    ]
