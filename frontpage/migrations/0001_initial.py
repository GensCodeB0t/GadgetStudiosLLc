# Generated by Django 2.1 on 2018-09-28 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Front_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_background_image', models.ImageField(upload_to='front_page_images/')),
                ('logo_image', models.ImageField(upload_to='front_page_images/')),
                ('logo_alt', models.CharField(max_length=100)),
                ('site_title', models.CharField(max_length=200)),
                ('site_header', models.CharField(max_length=200)),
            ],
        ),
    ]
