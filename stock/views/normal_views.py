from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.models import User

from stock.models import Store, Product, Order
from stock.components.tables import StoreTable, ProductTable, OrderTable, UserTable

# Create your views here.
def signup(request):

    template_name = 'accounts/signup.html'

    form = UserCreationForm()

    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )
            user.save()

            login(request, user)
            return redirect('home')
        else:
            HttpResponse("Passwords do not match")

    context = {
        'form': form,
    }
    
    return render(request, context=context, template_name=template_name)


def login_view(request):
    template_name = 'accounts/login.html'

    form = AuthenticationForm()

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, context=context, template_name=template_name)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def users(request):
    template_name = 'users.html'

    users = User.objects.all()
    table = UserTable(users)

    context = {
        'table': table
    }

    return render(request, context=context, template_name=template_name)


@login_required
def home(request):
    template_name = 'home.html'

    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, template_name=template_name)


@login_required
def stores(request):
    template_name = 'stores.html'

    stores = Store.objects.all()
    table = StoreTable(stores)

    context = {
        'table': table
    }

    return render(request, context=context, template_name=template_name)


@login_required
def products(request, store_id):
    template_name = 'products.html'

    store = get_object_or_404(Store, id=store_id)
    products = Product.objects.filter(related_store=store)
    table = ProductTable(products)

    context = {
        'store': store,
        'table': table
    }

    return render(request, context=context, template_name=template_name)



@login_required
def orders(request, user_id, order_id):
    template_name = 'orders.html'

    user = get_object_or_404(User, id=user_id)
    orders = Order.objects.filter(user=user)
    table = OrderTable(orders)

    context = {
        'user': user,
        'table': table
    }

    return render(request, context=context, template_name=template_name)


@login_required
def profile(request, user_id):
    template_name = 'profile.html'

    user = request.user

    if user.id == user_id:
        orders = Order.objects.filter(user=user)
        table = OrderTable(orders)
    else:
        table = None
        return HttpResponse("You are not authorized to view this profile.")
    
    context = {
        'user': user,
        'table': table
    }

    return render(request, context=context, template_name=template_name)
