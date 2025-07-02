from django.forms import Form, ModelForm, EmailField, CharField, PasswordInput, ValidationError
from stock.models import Store, Product, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CustomAuthenticationForm(Form):
    username = CharField(label='Username', required=True)
    email = EmailField(label="Email", required=True)
    password = CharField(label='Password', widget=PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = authenticate(email=email, password=password)
        if user is None:
            raise ValidationError("Credenciales inválidas")
        self.user = user
        return self.cleaned_data

    def get_user(self):
        return self.user


class CustomUserCreationForm(UserCreationForm):
    email = EmailField(required=True)
    first_name = CharField(required=True)
    last_name = CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ('__all__')


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('related_store',)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')