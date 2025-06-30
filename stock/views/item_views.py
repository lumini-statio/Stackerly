from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from stock.models import Store, Product, Order
from stock.forms import ProductForm, OrderForm

@login_required
def product_item(request, store_id, product_id):
    template_name = 'form_generic.html'

    store = get_object_or_404(Store, id=store_id)
    product = get_object_or_404(Product, id=product_id, related_store=store)

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            if 'delete' in request.POST:
                product.delete()
                return redirect('products', store_id=store_id)
            elif 'go-back' in request.POST:
                return redirect('products', store_id=store_id)
    
    else:
        form = ProductForm()
    
    context = {
        'form': form
    }

    return render(request, context=context, template_name=template_name)


@login_required
def order_item(request, user_id, order_id):
    template_name = 'form_generic.html'

    user = get_object_or_404(User, id=user_id)
    order = get_object_or_404(Order, id=order_id, user=user)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            if 'delete' in request.POST:
                order.delete()
                return redirect('orders', user_id=user_id)
            elif 'go-back' in request.POST:
                return redirect('products', user_id=user_id)
    
    else:
        form = OrderForm()
    
    context = {
        'form': form
    }

    return render(request, context=context, template_name=template_name)
