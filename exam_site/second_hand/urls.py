from django.urls import path

from exam_site.second_hand.views import BuySecondHandProductsListView, SellSecondHandProductsView, \
    SecondHandProductDetailsView, my_sales, remove_from_sales

urlpatterns = [
    path('buy/', BuySecondHandProductsListView.as_view(), name='buy second hand'),
    path('sell/', SellSecondHandProductsView.as_view(), name='sell second hand'),
    path('details/<int:pk>/', SecondHandProductDetailsView.as_view(), name='second hand details'),

    path('my_sales/', my_sales, name='my sales'),
    path('remove_from_sales/<int:pk>/', remove_from_sales, name='remove from sales'),
]
