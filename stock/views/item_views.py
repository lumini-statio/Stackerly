from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages

from stock.models import Store, Product, Order, CustomUser
from stock.forms import StoreForm, ProductForm, OrderForm


@login_required
def user_item(request, id):
    template_name = 'mod_generic.html'

    user = get_object_or_404(CustomUser, id=id)
    email = user.email

    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)

        if form.is_valid():
            if 'save' in request.POST:
                form.save()
                messages.success(request, f"User '{user.email}' edited successfully")
            elif 'delete' in request.POST:
                user.delete()
                messages.success(request, f"User {email} deleted successfully")

            return redirect('stores')
    else:
        form = UserChangeForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, context=context, template_name=template_name)


@login_required
def store_item(request, id):
    template_name = 'mod_generic.html'

    store = get_object_or_404(Store, id=id)
    st_name = store.name

    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)

        if form.is_valid():
            if 'save' in request.POST:
                form.save()
                messages.success(request, f"Store '{store.name}' edited successfully")
            elif 'delete' in request.POST:
                store.delete()
                messages.success(request, f"Store {st_name} deleted successfully")
                
            return redirect('stores')
    else:
        form = StoreForm(instance=store)

    context = {
        'form': form,
    }

    return render(request, context=context, template_name=template_name)


@login_required
def product_item(request, store_id, id):
    template_name = 'mod_generic.html'

    product = get_object_or_404(Product, id=id)
    pr_name = product.name

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            if 'save' in request.POST:
                form.save()
                messages.success(request, f"Product '{product.name}' edited successfully")
            elif 'delete' in request.POST:
                product.delete()
                messages.success(request, f"Product {pr_name} deleted successfully")

            return redirect('products', id=store_id)
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
    }

    return render(request, context=context, template_name=template_name)


@login_required
def order_item(request, id):
    template_name = 'mod_generic.html'

    order = get_object_or_404(Order, id=id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            if 'save' in request.POST:
                form.save()
                messages.success(request, f"Order {id} edited successfully")
            elif 'delete' in request.POST:
                order.delete()
                messages.success(request, f"Product {id} deleted successfully")

            return redirect('stores')
    else:
        form = StoreForm(instance=order)

    context = {
        'form': form,
    }

    return render(request, context=context, template_name=template_name)