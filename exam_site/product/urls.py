from django.urls import path

from exam_site.product.views import ProductDetailsView, AllEquipment

# from exam_site.product.views import product_details

urlpatterns = [
    path('<int:pk>/', ProductDetailsView.as_view(), name='product details'),
    path('equipment/', AllEquipment.as_view(), name='all equipment'),
]
