from django.db import models

class City(models.Model):
    name = models.CharField(max_length=35)
    slug = models.SlugField(unique=True)


    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"