from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name} - {self.location}'
    

class ProductState(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50, blank=True, null=True)
    related_store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    state = models.ForeignKey(ProductState, on_delete=models.CASCADE)
    last_updated_state = models.DateField(auto_now=True)

    def can_change_state(self):
        if self.state.name == 'Sold' and self.last_updated_state > date.today():
            diff = self.last_updated_state - date.today()

            if diff.days > 30:
                return False
        
        return True
    
    def change_state(self, new_state):
        if self.can_change_state():
            self.state = new_state
            self.last_updated_state = date.today()
            self.save()
        else:
            raise ValueError("Cannot change state due to restrictions.")

    def __str__(self):
        return f'{self.name} - {self.state}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.product.name} by {self.user.username} on {self.date.strftime("%Y-%m-%d %H:%M:%S")}'


class Balance(models.Model):
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Balance: {self.current_amount} (Last updated: {self.last_updated.strftime("%Y-%m-%d %H:%M:%S")})'

    class Meta:
        ordering = ['date']