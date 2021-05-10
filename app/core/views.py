from django.shortcuts import render

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"

class Aboutus(TemplateView):
    template_name = "pages/about-us.html"

class Pricing(TemplateView):
    template_name = "partials/home/pricing.html"

class ProductPageView(TemplateView):
    template_name = "partials/home/productpage.html"

class Category(TemplateView):
    template_name = "partials/home/category.html"

class Profile(TemplateView):
    template_name = "partials/home/profile.html"