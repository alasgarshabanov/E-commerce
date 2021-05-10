from django.urls import path
from . import views



urlpatterns = [
    path("", views.HomePageView.as_view(), name="home-page"),
    path("product-page", views.ProductPageView.as_view(), name="product-page"),
    path("about-us", views.Aboutus.as_view(), name="aboutus-page"),
    path("pricing", views.Pricing.as_view(), name="pricing-page"),

]