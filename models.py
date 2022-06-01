import datetime
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description =models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    image2 = models.ImageField(upload_to='images', null=True, blank=True)
    slug =models.SlugField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
