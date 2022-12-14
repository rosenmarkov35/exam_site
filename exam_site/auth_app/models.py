from django.contrib.auth.models import User
from django.db import models

from exam_site.product.models import Product


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )

    location = models.CharField(
        max_length=50,
        null=False,
        blank=True
    )


# This model represents a cart that can hold multiple items
class Cart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')
    created_on = models.DateTimeField(auto_now_add=True)


# This model represents an individual item in a cart
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
#
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()


# This model represents an item that can be added to a cart
# class Item(models.Model):
#   name = models.CharField(max_length=100)
#   description = models.TextField()
#   price = models.DecimalField(max_digits=7, decimal_places=2)
#
# # This model represents a cart that can hold multiple items
# class Cart(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   items = models.ManyToManyField(Item, through='CartItem')
#   created_at = models.DateTimeField(auto_now_add=True)
#
# # This model represents an individual item in a cart
# class CartItem(models.Model):
#   cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#   item = models.ForeignKey(Item, on_delete=models.CASCADE)
#   quantity = models.PositiveIntegerField(default=1)

#
# # This view adds an item to a cart
# def add_to_cart(request):
#   user = request.user
#   if not user.is_authenticated:
#     # Handle unauthenticated users
#     pass
#
#   # Get the item and cart
#   item = get_object_or_404(Item, pk=request.POST['item_id'])
#   cart = user.cart
#
#   # Create a new cart if the user doesn't have one
#   if not cart:
#     cart = Cart.objects.create(user=user)
#
#   # Add the item to the cart
#   try:
#     cart_item = CartItem.objects.get(cart=cart, item=item)
#     cart_
#
#
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()

# TODO | ADD ALL THE PRODUCTS BACK ON THE SITE ALONG WITH SOME USERS AND A COUPLE OF SECOND HAND ITEMS
# TODO | ADD ALL THE PRODUCTS BACK ON THE SITE ALONG WITH SOME USERS AND A COUPLE OF SECOND HAND ITEMS

# TODO | THEN CHECK/IMPLEMENT THE SHOPPING CART FUNCTIONALITY AND THE MEN AND WOMEN SECTION OF THE SITE
# TODO | THEN CHECK/IMPLEMENT THE SHOPPING CART FUNCTIONALITY AND THE MEN AND WOMEN SECTION OF THE SITE

# TODO | •	Authenticated users (private part) have full CRUD for all their created content.

# TODO | •	Admins - at least 2 groups of admins:
# TODO |    o	One must have permission to do full CRUD functionalities (superusers);
# TODO |    o	The other/s have permission to do limited CRUD functionalities (staff).
# TODO |    o	User roles could be manageable from the admin site.
# TODO |    o	Make sure the role management is secured and error-safe.

# TODO | •	Implement Exception Handling and Data Validation to avoid crashes when invalid data is entered
# TODO |    (both client-side and server-side)
# TODO |    o	When validating data, show appropriate messages to the user

# TODO | •	The application must have a customized admin site (accessible only by admins):
# TODO |    o	Add at least 5 custom options (in total) to the admin interface (e.g., filters, list display,
# TODO |        ordering, etc.).

# TODO | o	The application must have at least 5 independent models (models created by extending, inheritance,
# TODO |    and one-to-one relation is considered one model).
# TODO | o	The application must have at least 5 forms.
