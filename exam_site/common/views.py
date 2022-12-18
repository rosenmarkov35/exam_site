from django.shortcuts import render
from django.views.generic import ListView

from exam_site.product.models import Product


class Index(ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'common/index.html'


