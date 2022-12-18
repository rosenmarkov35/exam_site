from django.contrib.auth.models import User
from django.db import models

from exam_site.product.models import Product


class Review(models.Model):
    STAR_RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    review_text = models.CharField(
        max_length=500,
        null=True,
        blank=False,
    )

    star_rating = models.IntegerField(
        choices=STAR_RATING_CHOICES,
        default=5,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
