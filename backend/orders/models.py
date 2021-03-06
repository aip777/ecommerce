from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model as user_model
User = user_model()

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=100)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=100)
    place = models.CharField(max_length=100, null=True, blank=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   


    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.order} - {self.product} - {self.product}'

@receiver(post_save, sender=OrderItem)
def product_quantity_update(sender, instance, *args, **kwargs):
    product = Product.objects.get(id=instance.product.id)
    product.current_stock = product.current_stock - instance.quantity
    product.save(update_fields=['current_stock'])
