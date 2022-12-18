from django.urls import path

from exam_site.review.views import CreateReviewView, MyReviewsView, remove_review_view

urlpatterns = [
    path('add_review/<int:pk>/', CreateReviewView.as_view(), name='create review'),

    path('my_reviews/', MyReviewsView.as_view(), name='my reviews'),

    path('remove_review/<int:pk>/', remove_review_view, name='remove review'),
]
