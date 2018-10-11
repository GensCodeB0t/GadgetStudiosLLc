from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='projects/', null=True)
    image_thumbnail = models.ImageField(upload_to='projects/', null=True)
    description = models.TextField()
    link = models.CharField(max_length=255)
    DESKTOP = 'desktop'
    WEBSITES = 'websites'
    MOBILE = 'mobile'
    IOT = 'IoT'
    COMING_SOON = '.coming soon...'
    CATEGORY_LIST = (
        (DESKTOP, 'desktop'),
        (WEBSITES, 'websites'),
        (MOBILE, 'mobile'),
        (IOT, 'IoT'),
        (COMING_SOON, 'coming soon...'),
    )
    category = models.CharField(choices=CATEGORY_LIST, default=DESKTOP, null=True, max_length=10)
    pub_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    def __int__(self, title, image, description, link, category, image_thumbnail):
        self.title = title
        self.image = image
        self.image_thumbnail = image_thumbnail
        self.description = description
        self.link = link
        self.category = category

    def summary(self):
        return self.description[:100]
