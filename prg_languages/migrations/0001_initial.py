# Generated by Django 2.1 on 2018-09-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prg_Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='prg_language/')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
