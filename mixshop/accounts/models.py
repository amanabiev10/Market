from django.db import models
from django.contrib.auth.models import AbstractUser


class Address(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='user_address')
    address_type = models.CharField(max_length=255, choices=[('shipping', 'Shipping'), ('billing', 'Billing')])
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.street}, {self.postal_code} {self.city}'


class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Seller(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=255)
    seller_description = models.TextField()

    def __str__(self):
        return self.seller_name
