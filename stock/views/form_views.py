from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

from stock.models import Store, Product, Order, CustomUser
from stock.forms import StoreForm, ProductForm, OrderForm,\
                        CustomAuthenticationForm, CustomUserCreationForm, UserPurchaseForm


def signup(request):

    template_name = 'accounts/signup.html'

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            form.save(commit=True)
            login(request, user)
            messages.success(request, 'Sign up successfuly')

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
        form = CustomAuthenticationForm(request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, context=context, template_name=template_name)


def user_form(request):
    template_name = 'form_generic.html'

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfuly')
            return redirect('users')
    
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

            return redirect('products', id=store_id)
    
    else:
        form = ProductForm()
    
    context = {
        'form': form
    }

    return render(request, context=context, template_name=template_name)


def buy_product(request, id):
    template_name = 'user-purchase.html'

    product = get_object_or_404(Product, id=id)

    form = UserPurchaseForm()

    if request.method == 'POST':
        form = UserPurchaseForm(request.POST)
        if form.is_valid():
            user_purchase = form.save(commit=False)
            user_purchase.product = product

            buyer_user = CustomUser.objects.get(id=int(request.POST['user']))
            user_purchase.user = buyer_user
            user_purchase.save()

            Order.objects.create(
                user=request.user,
                date=datetime.now()
            )
            messages.success(request, 'buy registered successfuly')
            return redirect('home')
    
    context = {
        'form': form
    }

    return render(request, context=context, template_name=template_name)


@login_required
def order_form(request, user_id, order_id):
    template_name = 'form_generic.html'

    user = get_object_or_404(CustomUser, id=user_id)
    order = get_object_or_404(Order, id=order_id, user=user)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            if 'delete' in request.POST:
                order.delete()
            elif 'save' in request.POST:
                form.save()
            elif 'go-back' in request.POST:
                return
        messages.success(request, f'Order created successfuly')

        return redirect('orders', user_id=user_id)
    
    else:
        form = OrderForm()
    
    context = {
        'form': form
    }

    return render(request, context=context, template_name=template_name)
