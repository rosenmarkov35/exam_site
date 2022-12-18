from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from exam_site.second_hand.forms import SellSecondHandProductsForm
from exam_site.second_hand.models import SecondHandProduct


class SecondHandProductDetailsView(DetailView):
    model = SecondHandProduct
    context_object_name = 'second_hand_product'
    template_name = 'second_hand/secondhand_product_details.html'


class BuySecondHandProductsListView(ListView):
    context_object_name = 'second_hand_products'
    model = SecondHandProduct
    template_name = 'second_hand/all_secondhand_products.html'


class SellSecondHandProductsView(LoginRequiredMixin, views.View):
    @staticmethod
    def post(request, *args, **kwargs):
        sell_secondhand_products_form = SellSecondHandProductsForm(request.POST)
        user = request.user
        if sell_secondhand_products_form.is_valid():
            second_hand_product = sell_secondhand_products_form.save(commit=False)

            second_hand_product.uploaded_by = user

            second_hand_product.save()

            return redirect('my sales')

    @staticmethod
    def get(request, *args, **kwargs):
        sell_secondhand_products_form = SellSecondHandProductsForm()
        return render(request, 'second_hand/sell_secondhand_products.html', {
            'form': sell_secondhand_products_form,
        })


def my_sales(request):
    all_my_sales = SecondHandProduct.objects.filter(uploaded_by=request.user).all()
    return render(request, 'second_hand/my_sales.html', context={
        'all_sales': all_my_sales,
    })


def remove_from_sales(request, pk):  # The pk here is the pk of the second hand product we want to remove from sales
    SecondHandProduct.objects.filter(pk=pk).delete()
    return redirect(request.META['HTTP_REFERER'])
