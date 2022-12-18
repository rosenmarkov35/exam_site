from django import views
from django.shortcuts import render, redirect
from exam_site.product.models import Product
from exam_site.review.forms import ReviewCreationForm
from exam_site.review.models import Review


class CreateReviewView(views.View):

    def post(self, request, *args, **kwargs):
        review_form = ReviewCreationForm(request.POST)
        about_product = Product.objects.get(pk=self.kwargs['pk'])
        if review_form.is_valid():
            review = review_form.save(commit=False)

            review.user = request.user
            review.product = about_product

            review.save()

            return redirect('product details', pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        about_product = Product.objects.get(pk=self.kwargs['pk'])
        review_form = ReviewCreationForm()
        return render(request, 'reviews/add_review.html', {
            'review_form': review_form,
            'product_pk': about_product.pk
        })


class MyReviewsView(views.View):
    @staticmethod
    def get(request, *args, **kwargs):
        all_my_reviews = Review.objects.filter(user=request.user).all()

        return render(request, 'reviews/my_reviews.html', {
            'all_my_reviews': all_my_reviews,
        })


def remove_review_view(request, pk):
    Review.objects.filter(pk=pk).delete()
    return redirect(request.META['HTTP_REFERER'])

