from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Seller


@receiver(post_save, sender=CustomUser)
def create_seller_profile(sender, instance, created, **kwargs):
    if created and instance.is_seller:
        Seller.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_seller_profile(sender, instance, **kwargs):
    if instance.is_seller:
        instance.save()