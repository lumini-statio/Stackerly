from django.forms import Form, ModelForm, EmailField, CharField, PasswordInput, ValidationError
from stock.models import Store, Product, Order, CustomUser, UserPurchase
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


class CustomAuthenticationForm(Form):
    username = CharField(label='Username', required=True)
    password = CharField(label='Password', widget=PasswordInput, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError("Credenciales inválidas")
        self.user = user
        return self.cleaned_data

    def get_user(self):
        return self.user


class CustomUserCreationForm(ModelForm):
    password1 = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = CharField(
        label="Password confirmation",
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match.")
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


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


class UserPurchaseForm(ModelForm):
    class Meta:
        model = UserPurchase
        exclude = ('product')