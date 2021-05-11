from django.contrib import admin
from django.utils.html import format_html

from core.models import Product

@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img style="width: 200px; height:auto;" src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['title','image_tag',]