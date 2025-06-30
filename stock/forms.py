from django.forms import ModelForm
from stock.models import Product, Order


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')