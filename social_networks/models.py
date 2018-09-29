from django.db import models

class Social_Network(models.Model):
    image = models.ImageField(upload_to='social_network_images/')
    name = models.CharField(max_length=75)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name
