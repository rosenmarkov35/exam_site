from django.contrib import admin

from exam_site.second_hand.models import SecondHandProduct


@admin.register(SecondHandProduct)
class SecondHandProductAdmin(admin.ModelAdmin):
    list_display = ('second_hand_product_name', 'second_hand_product_price', 'second_hand_uploaded_on')
