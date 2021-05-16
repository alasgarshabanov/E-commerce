from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import status

from core.models import Product

from api.serializers.product import ProductAutoCompleteSerializer


class ProductAutoCompleteListApiView(ListAPIView):
    serializer_class = ProductAutoCompleteSerializer

    def get_queryset(self):
        search = Product.objects.all()
        data = self.request.query_params
        if data.get('s'):
            key_word = data.get('s')
            search = search.filter(title__icontains=key_word)
        return search.order_by('-created_at')[:5]
