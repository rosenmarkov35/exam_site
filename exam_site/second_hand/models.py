from django.db import models


class SecondHandProduct(models.Model):
    second_hand_product_name = models.CharField(
        null=False,
        blank=False,
        max_length=40
    )

    second_hand_product_image = models.URLField(
        null=False,
        blank=False,
    )

    second_hand_product_price = models.FloatField(
        null=False,
        blank=False,
    )

    second_hand_product_description = models.TextField(
        max_length=1200,
        null=False,
        blank=True,
    )

    second_hand_uploaded_on = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
    )
