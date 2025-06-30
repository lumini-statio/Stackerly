from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name} - {self.location}'
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50, blank=True, null=True)
    related_store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.name} - {self.type} - {self.model} - ${self.price}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.product.name} by {self.user.username} on {self.date.strftime("%Y-%m-%d %H:%M:%S")}'
