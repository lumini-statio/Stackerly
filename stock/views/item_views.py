from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from stock.models import Store, Product, Order
from stock.forms import StoreForm, ProductForm, OrderForm


@login_required
def user_item(request, id):
    template_name = 'form_generic.html'

    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('stores')
    else:
        form = UserChangeForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, context=context, template_name=template_name)


@login_required
def store_item(request, id):
    template_name = 'form_generic.html'

    store = get_object_or_404(Store, id=id)

    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)

        if form.is_valid():
            form.save()
            return redirect('stores')
    else:
        form = StoreForm(instance=store)

    context = {
        'form': form,
    }

    return render(request, context=context, template_name=template_name)


@login_required
def product_item(request, id):
    template_name = 'form_generic.html'

    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
    }

    return render(request, context=context, template_name=template_name)


@login_required
def order_item(request, id):
    template_name = 'form_generic.html'

    order = get_object_or_404(Order, id=id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('stores')
    else:
        form = StoreForm(instance=order)

    context = {
        'form': form,
    }

    return render(request, context=context, template_name=template_name)