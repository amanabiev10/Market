from django.contrib import admin
from accounts.models import CustomUser, Address, Seller


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    ...


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    ...


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    ...