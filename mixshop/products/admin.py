from django.contrib import admin
from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...