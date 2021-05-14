from django.contrib import admin
from django.utils.html import format_html

from core.models import Brand



@admin.register(Brand) 
class BrandAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img style="width: 100px; height:auto;" src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return 'Brand: {}'.format(self.name)

    list_display = ['name','image_tag',]