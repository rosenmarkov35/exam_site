from django.urls import path

from exam_site.auth_app.views import CustomLoginView, MyLogoutView, ProfileDetailsView, \
    CreateUserProfileView
from exam_site.product.views import CartView, AddToCartView

urlpatterns = [
    path('register/', CreateUserProfileView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('details/', ProfileDetailsView.as_view(), name='profile details'),
    path('add_to_cart/<int:pk>/', AddToCartView.as_view(), name='add to cart'),
    path('view_cart/', CartView.as_view(), name='shopping cart'),
]
