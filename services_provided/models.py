from django.db import models

class Service_Provided(models.Model):
    image = models.ImageField(upload_to='services_provided/')
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
