from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Invoice, Product


@receiver(post_save, sender=Invoice)
def manage_quantity_save(sender, instance, **kwargs):
    product = Product.objects.get(product_code=instance.product_code.product_code)
    product.quantity = product.quantity - instance.quantity
    product.save()
