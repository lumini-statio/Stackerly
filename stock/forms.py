from django.forms import ModelForm
from stock.models import Store, Product, Order


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ('__all__')


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')