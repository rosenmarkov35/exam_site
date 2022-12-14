from django.urls import path

from exam_site.second_hand.views import BuySecondHandProductsListView, SellSecondHandProductsView, \
    SecondHandProductDetailsView

urlpatterns = [
    path('buy/', BuySecondHandProductsListView.as_view(), name='buy second hand'),
    path('sell/', SellSecondHandProductsView.as_view(), name='sell second hand'),
    path('details/<int:pk>/', SecondHandProductDetailsView.as_view(), name='second hand details')
]
