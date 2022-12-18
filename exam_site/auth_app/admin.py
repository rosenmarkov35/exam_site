from django.contrib import admin

from exam_site.auth_app.models import Cart, CartItems, Profile


class CartItemsInline(admin.TabularInline):
    model = CartItems
    fields = 'product',


@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemsInline,
    ]
    fieldsets = [
        ('Cart user', {'fields': ['user']}),
        ('Date information', {'fields': ['status']}),
    ]
    list_display = ('user', 'status', 'updated_on')
    list_filter = ['updated_on', 'status', 'user']
    ordering = 'status',


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
