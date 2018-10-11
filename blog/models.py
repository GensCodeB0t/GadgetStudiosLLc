from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='blogimages/')
    image_thumbnail = models.ImageField(upload_to='blogimages/', null=True)
    author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_formated(self):
        return self.pub_date.strftime('%b %e %Y')

    def __int__(self, title, pub_date, body, image, author):
        self.title = title
        self.pub_date = pub_date
        self.body = body
        self.image = image
        self.author = author
