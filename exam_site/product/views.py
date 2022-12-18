from django import views
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from exam_site.product.models import Product


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'product/product_details.html'
    context_object_name = 'product'


def product_details_view(request, pk):  # Where pk is the pk of the product that we want the details of.
    the_product = Product.objects.get(pk=pk)
    reviews_of_product = the_product.review_set.all()
    avg_review_stars = []
    for review in reviews_of_product:
        avg_review_stars.append(review.star_rating)
    if avg_review_stars:
        avg_review_stars = sum(avg_review_stars) / len(avg_review_stars)
    else:
        avg_review_stars = 0
    context = {
        'product': the_product,
        'reviews': reviews_of_product,
        'avg_review_stars': avg_review_stars,
    }
    return render(request, 'product/product_details.html', context)


class AllEquipment(ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'equipment/equipment.html'


class MenEquipment(views.View):
    @staticmethod
    def get(request, *args, **kwargs):
        made_for_men = Product.objects.filter(made_for='men').all()

        return render(request, 'equipment/men_equipment.html', context={
            'products': made_for_men,
        })


class WomenEquipment(views.View):
    @staticmethod
    def get(request, *args, **kwargs):
        made_for_women = Product.objects.filter(made_for='women').all()

        return render(request, 'equipment/women_equipment.html', context={
            'products': made_for_women,
        })
