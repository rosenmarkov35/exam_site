from django.shortcuts import render
from django.views.generic import ListView

from exam_site.product.models import Product


# def index(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#     }
#
#     return render(request, 'index.html', context)


class Index(ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'index.html'


