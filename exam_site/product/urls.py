from django.urls import path

from exam_site.product.views import AllEquipment, product_details_view, WomenEquipment, MenEquipment

urlpatterns = [
    path('<int:pk>/', product_details_view, name='product details'),
    path('equipment/', AllEquipment.as_view(), name='all equipment'),

    path('equipment/women/', WomenEquipment.as_view(), name='women equipment'),
    path('equipment/men/', MenEquipment.as_view(), name='men equipment'),
]
