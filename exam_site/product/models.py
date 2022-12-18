from django.db import models


class Product(models.Model):
    product_name = models.CharField(
        null=False,
        blank=False,
        max_length=40
    )

    product_image = models.URLField(
        null=False,
        blank=False,
    )

    product_price = models.FloatField(
        null=False,
        blank=False,
    )

    product_description = models.TextField(
        max_length=1200,
        null=False,
        blank=True,
    )

    product_details = models.TextField(
        max_length=500,
        null=False,
        blank=True,
    )

    made_for = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

