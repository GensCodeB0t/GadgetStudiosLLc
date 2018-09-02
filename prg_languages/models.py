from django.db import models

class Prg_Language(models.Model):
    image_height = models.PositiveIntegerField(default=10)
    image_width = models.PositiveIntegerField(default=10)

    image = models.ImageField(upload_to='prg_language/', height_field='image_height', width_field='image_width')
    description = models.CharField(max_length=100)
