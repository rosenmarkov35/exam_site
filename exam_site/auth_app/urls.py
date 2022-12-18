from django.urls import path

from exam_site.auth_app.views import CustomLoginView, MyLogoutView, ProfileDetailsView, \
    CreateUserProfileView, add_to_cart_view, view_shopping_cart, clear_cart, LogoutConfirmationView, EditProfileView

urlpatterns = [
    path('register/', CreateUserProfileView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),

    path('logoutconfirmation/', LogoutConfirmationView.as_view(), name='logout confirmation'),
    path('logout/', MyLogoutView.as_view(), name='logout'),

    path('details/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit_profile/', EditProfileView.as_view(), name='edit profile'),

    path('addtocart/<int:pk>/', add_to_cart_view, name='add to cart'),
    path('clear_cart/', clear_cart, name='clear cart'),

    path('view_shopping_cart/', view_shopping_cart, name='view shopping cart'),
]
