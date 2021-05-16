from rest_framework import serializers

from core.models import Product


class ProductAutoCompleteSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = ('title', 'url')

    def get_url(self, obj):
        return obj.get_absolute_url()
