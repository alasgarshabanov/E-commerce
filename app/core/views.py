from django.db import models
from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView

from core.models import Product, City, Material, Category

class HomePageView(TemplateView):
    template_name = "index.html"

class Aboutus(TemplateView):
    template_name = "pages/about-us.html"

class Pricing(TemplateView):
    template_name = "partials/home/category.html"

class ProductPageView(DetailView):
    model = Product
    template_name = "partials/home/productpage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class CategoryView(ListView):
    model = Category
    context_object_name="categories"
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

class Profile(TemplateView):
    template_name = "partials/home/profile.html"