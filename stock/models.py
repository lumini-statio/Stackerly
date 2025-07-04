from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import date

from stock.managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username} - {self.email}'


class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
    

class BalanceBox(models.Model):
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='balances')

    def calculate_amount(self) -> float:
        amount_spent = sum([purchase.spent for purchase in Purchase.objects.all()])
        return float(amount_spent)

    def __str__(self):
        return f'Balance: {self.current_amount} (Last updated: {self.last_updated.strftime("%Y-%m-%d %H:%M:%S")})'


class Store(models.Model):
    name = models.CharField(max_length=100)
    balance = models.ForeignKey(BalanceBox, on_delete=models.PROTECT, related_name='stores')
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='stores')

    def __str__(self):
        return f'{self.name} - {self.location}'
    

class ProductState(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def builder():
        state = ProductState.objects.get_or_create(name='Available')
        return state

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50, blank=True, null=True)
    related_store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    state = models.ForeignKey(ProductState, on_delete=models.PROTECT)
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.product.name} by {self.user.username} on {self.date.strftime("%Y-%m-%d %H:%M:%S")}'
    

class Purchase(models.Model):
    purchased_item = models.CharField(max_length=50)
    spent = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()

    class Meta:
        ordering = ['-date']