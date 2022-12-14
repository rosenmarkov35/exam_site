from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from exam_site.second_hand.models import SecondHandProduct


class SecondHandProductDetailsView(DetailView):
    model = SecondHandProduct
    context_object_name = 'second_hand_product'
    template_name = 'second_hand/secondhand_product_details.html'


class BuySecondHandProductsListView(ListView):
    context_object_name = 'second_hand_products'
    model = SecondHandProduct
    template_name = 'second_hand/all_secondhand_products.html'


class SellSecondHandProductsForm(ModelForm):
    class Meta:
        model = SecondHandProduct
        fields = ('second_hand_product_name', 'second_hand_product_image', 'second_hand_product_price',
                  'second_hand_product_description')

        widgets = {
            'second_hand_product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_hand_product_image': forms.TextInput(attrs={'class': 'form-control'}),
            'second_hand_product_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'second_hand_product_description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SellSecondHandProductsView(LoginRequiredMixin, CreateView):
    template_name = 'second_hand/sell_secondhand_products.html'
    form_class = SellSecondHandProductsForm
    # TODO: MAKE SUCCESS URL | AFTER YOU UPLOAD AN ITEM FOR SALE SHOW THE USER'S LIST OF ALL ITEMS CURRENTLY FOR SALE
    success_url = reverse_lazy('index')
