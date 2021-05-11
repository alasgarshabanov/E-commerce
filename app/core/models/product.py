from django.db import models

from .city import City
from .category import Category

class Product(models.Model):

    title = models.CharField(max_length=50, verbose_name="Product name")
    description = models.TextField(max_length=3000, null=False, blank=True)
    image =models.ImageField()
    delivery = models.BooleanField(default=False, verbose_name="Delivery")
    price = models.PositiveIntegerField(default=0, verbose_name="Product price")
    view_count=models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"