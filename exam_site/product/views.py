from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from exam_site.auth_app.models import Cart
from exam_site.product.models import Product


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'


class AllEquipment(ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'equipment.html'


class AddToCartView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        user = request.user
        item = get_object_or_404(Product, pk=kwargs['pk'])

        try:
            cart = Cart.objects.get(user=user, item=item)
            cart.quantity += 1
        except Cart.DoesNotExist:
            cart = Cart(user=user, item=item)

        cart.save()
        return redirect('shopping cart')


class CartView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        user = request.user
        items = Cart.objects.filter(user=user)
        return render(request, 'shopping_cart.html', {'items': items})
