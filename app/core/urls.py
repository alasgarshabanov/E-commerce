from django.urls import path
from . import views



urlpatterns = [
    path("", views.CategoryView.as_view(), name="home-page"),
    path("about-us", views.Aboutus.as_view(), name="aboutus-page"),
    path("pricing/", views.CategoryView.as_view(), name="pricing-page"),
    path("product/<slug>", views.ProductPageView.as_view(), name="product-detail"),

]