from core.models import Product

def similar_products(request):
    products= Product.objects.all()[:7]
    return {'similar_products': products}