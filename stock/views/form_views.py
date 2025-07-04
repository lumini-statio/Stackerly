from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse

from stock.models import Store, Product, Order
from stock.forms import StoreForm, ProductForm, OrderForm, CustomAuthenticationForm, CustomUserCreationForm


def signup(request):

    template_name = 'accounts/signup.html'

    form = CustomUserCreationForm()

    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )
            user.save()
            login(request, user)
            messages.success(request, 'Sign up successed')

            return redirect('home')
        else:
            HttpResponse("Passwords do not match")

    context = {
        'form': form,
    }
    
    return render(request, context=context, template_name=template_name)


def login_view(request):
    template_name = 'accounts/login.html'

    form = CustomAuthenticationForm()

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


@login_required
def store_form(request):
    template_name = 'form_generic.html'

    if request.method == 'POST':
        form = StoreForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Store created successed')

            return redirect('stores')
    else:
        form = StoreForm()
    
    context = {
        'form': form
    }

    return render(request, context=context, template_name=template_name)


@login_required
def product_form(request, store_id):
    template_name = 'form_generic.html'

    store = get_object_or_404(Store, id=store_id)

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save(commit=False)
            product.related_store = store
            product.save()
            messages.success(request, f'product {product.id} created successed')

            return redirect('product', id=store_id)
    
    else:
        form = ProductForm()
    
    context = {
        'form': form
    }

    return render(request, context=context, template_name=template_name)


@login_required
def order_form(request, user_id, order_id):
    template_name = 'form_generic.html'

    user = get_object_or_404(User, id=user_id)
    order = get_object_or_404(Order, id=order_id, user=user)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            if 'delete' in request.POST:
                order.delete()
            elif 'save' in request.POST:
                form.save()
            elif 'go-back' in request.POST:
                pass
        messages.success(request, f'Order created successed')

        return redirect('orders', user_id=user_id)
    
    else:
        form = OrderForm()
    
    context = {
        'form': form
    }

    return render(request, context=context, template_name=template_name)
