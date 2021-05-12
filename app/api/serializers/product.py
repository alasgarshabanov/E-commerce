from rest_framework import serializers

from core.models import Product


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'image_url', 'price' ]

    def get_title(self, obj):
        return obj.title

    def get_image_url(self, obj):
        if obj.image:
            return obj.get_image_url()
   
    def get_price(self, obj):
        return obj.price