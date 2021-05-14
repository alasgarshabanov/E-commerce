from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=35)
    image=models.ImageField()
    slug = models.SlugField(unique=True)


    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name 