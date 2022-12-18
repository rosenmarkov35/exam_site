from django.contrib.auth.models import User
from django.db import models

from exam_site.product.models import Product


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE
    )

    location = models.CharField(
        max_length=50,
        null=False,
        blank=True
    )


class Cart(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)  # active cart or submitted
    updated_on = models.DateTimeField(auto_now_add=True)


class CartItems(models.Model):
    cart = models.OneToOneField(Cart, null=True, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)


