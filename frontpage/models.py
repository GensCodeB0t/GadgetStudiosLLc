from django.db import models

class Front_Page(models.Model):
    header_background_image = models.ImageField(upload_to='front_page_images/')
    logo_image = models.ImageField(upload_to='front_page_images/')
    logo_alt = models.CharField(max_length=100)
    site_title = models.CharField(max_length=200)
    site_header = models.CharField(max_length=200)
    about_statement = models.TextField(null=True)
    about_image = models.ImageField(upload_to='front_page_images/', null=True)
    programming_language_image = models.ImageField(upload_to='front_page_images/', null=True)
