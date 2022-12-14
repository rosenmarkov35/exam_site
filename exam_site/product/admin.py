from django.contrib import admin

from exam_site.product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_image', 'product_price')


admin.site.register(Product, ProductAdmin)
