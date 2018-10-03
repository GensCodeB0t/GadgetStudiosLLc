from django.db import models

class Prg_Language(models.Model):
    image_height = models.PositiveIntegerField(default=10, null=True)
    image_width = models.PositiveIntegerField(default=10, null=True)
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='prg_language/', height_field='image_height', width_field='image_width')
    description = models.CharField(max_length=250)
    source_link = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.title
