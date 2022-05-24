from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Invoice, Product
    

@receiver(post_save, sender=Invoice)
def create_invoice_number(sender, instance, created, **kwargs):
    if created:
        instance.invoice_number = (instance.created_at).strftime('%Y%m%d%H%M').upper()+str(instance.pk)
        instance.total_amount = instance.quantity*instance.product_code.price
        instance.save()

        product = Product.objects.get(product_code=instance.product_code.product_code)
        product.quantity = product.quantity - instance.quantity
        product.save()
