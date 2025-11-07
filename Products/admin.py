from django.contrib import admin
from .models import Product,Cart

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =('name','price','seller','created_at')
    search_fields =('name','seller__username')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('user','product','quantity','subtotal')
    search_fields =('user__username','product__name')
