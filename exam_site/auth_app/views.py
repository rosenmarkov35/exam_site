from django import views
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from exam_site.auth_app.forms import CustomUserCreationForm, ProfileCreationForm, UpdateUserForm, UpdateProfileForm, \
    CustomAuthForm
from exam_site.auth_app.models import Cart, CartItems
from exam_site.product.models import Product


# REGISTRATION SECTION  REGISTRATION SECTION  REGISTRATION SECTION  REGISTRATION SECTION
# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


class CreateUserProfileView(views.View):
    @staticmethod
    def post(request, *args, **kwargs):
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileCreationForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)

            cart = Cart(status='active')

            cart_items = CartItems(cart=cart)

            profile.user = user
            profile.save()

            cart.user = user
            cart.save()
            cart_items.save()

            messages.success(request, 'Your profile was successfully created!')
            return redirect('index')

        else:
            messages.error(request, 'Please correct the error below.')

    @staticmethod
    def get(request, *args, **kwargs):
        user_form = CustomUserCreationForm()
        profile_form = ProfileCreationForm()
        return render(request, 'auth/register.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })


# REGISTRATION SECTION END  REGISTRATION SECTION END  REGISTRATION SECTION END  REGISTRATION SECTION END
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# UPDATE SECTION  UPDATE SECTION  UPDATE SECTION  UPDATE SECTION  UPDATE SECTION
# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


class EditProfileView(views.View):
    @staticmethod
    def post(request, *args, **kwargs):
        user_form = UpdateUserForm(request.POST, instance=request.user)

        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Your profile is updated successfully')

            return redirect('profile details')

    @staticmethod
    def get(request, *args, **kwargs):
        user_form = UpdateUserForm(instance=request.user)

        profile_form = UpdateProfileForm(instance=request.user.profile)

        return render(request, 'auth/edit_profile.html', context={
            'user_form': user_form,
            'profile_form': profile_form,
        })


# UPDATE SECTION END  UPDATE SECTION END  UPDATE SECTION END  UPDATE SECTION END  UPDATE SECTION END
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# LOGIN & LOGOUT SECITION  LOGIN & LOGOUT SECITION  LOGIN & LOGOUT SECITION  LOGIN & LOGOUT SECITION
# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    authentication_form = CustomAuthForm


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class LogoutConfirmationView(TemplateView):
    template_name = 'auth/logout.html'


# LOGIN & LOGOUT SECITION END  LOGIN & LOGOUT SECITION END  LOGIN & LOGOUT SECITION END  LOGIN & LOGOUT SECITION END
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# SHOPPING CART SECTION  SHOPPING CART SECTION  SHOPPING CART SECTION  SHOPPING CART SECTION
# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


class ShoppingCartView(TemplateView):
    template_name = 'auth/shopping_cart.html'
    extra_context = {}


def add_to_cart_view(request, pk):  # This pk is the pk of the product we want to add to the cart.
    product_to_add = Product.objects.get(pk=pk)
    request.user.cart.cartitems.product.add(product_to_add)
    return redirect(request.META['HTTP_REFERER'])


def clear_cart(request):
    cart_to_clear = request.user.cart.cartitems
    cart_to_clear.product.clear()
    return redirect(request.META['HTTP_REFERER'])


def view_shopping_cart(request):
    all_products_added_to_cart = request.user.cart.cartitems.product.all()
    total_price = 0
    for product in all_products_added_to_cart:
        total_price += product.product_price
    context = {
        'added_products': all_products_added_to_cart,
        'total_price': total_price,
    }
    return render(request, 'auth/shopping_cart.html', context)


# SHOPPING CART SECTION END  SHOPPING CART SECTION END  SHOPPING CART SECTION END  SHOPPING CART SECTION END
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class ProfileDetailsView(LoginRequiredMixin, TemplateView):
    template_name = 'auth/profile_details.html'
