from django.urls import path
from . import views

urlpatterns = [
    path('autocomplete_product/', views.ProductAutoCompleteListApiView.as_view(), name="autocomplete-products")
   
]