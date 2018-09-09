from django.db import models

class Service_Provided(models.Model):
    image = models.ImageField(upload_to='services_provided/')
    description = models.CharField(max_length=200)
