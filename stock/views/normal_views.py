from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.models import User

from stock.models import Store, Product, Order, BalanceBox, CustomUser
from stock.components.tables import StoreTable, ProductTable, OrderTable, UserTable

import pandas as pd
import plotly.express as px

# Create your views here.
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def users(request):
    template_name = 'list/users.html'

    users = CustomUser.objects.all()
    table = UserTable(users)

    context = {
        'table': table
    }

    return render(request, context=context, template_name=template_name)


@login_required
def profile(request):
    template_name = 'profile.html'

    user = request.user

    orders = Order.objects.filter(user=user)
    ord_table = OrderTable(orders)
    
    products = [product for order in orders for product in order.product]

    prod_table = ProductTable(products)

    context = {
        'user': user,
        'ord_table': ord_table,
        'prod_table': prod_table
    }

    return render(request, context=context, template_name=template_name)


@login_required
def home(request):
    template_name = 'home.html'
    
    products = Product.objects.all().order_by('-id')
    table = ProductTable(products)
    user = request.user

    context = {
        'table': table,
        'user': user
    }

    return render(request, context=context, template_name=template_name)


@login_required
def stores(request):
    template_name = 'list/stores.html'

    stores = Store.objects.all()
    table = StoreTable(stores)

    context = {
        'table': table
    }

    return render(request, context=context, template_name=template_name)


@login_required
def products(request, id):
    template_name = 'list/products.html'

    store = get_object_or_404(Store, id=id)
    products = Product.objects.filter(related_store=store)
    table = ProductTable(products)

    context = {
        'store': store,
        'table': table
    }

    return render(request, context=context, template_name=template_name)



@login_required
def orders(request, user_id, order_id):
    template_name = 'list/orders.html'

    user = get_object_or_404(User, id=user_id)
    orders = Order.objects.filter(user=user)
    table = OrderTable(orders)

    context = {
        'user': user,
        'table': table
    }

    return render(request, context=context, template_name=template_name)


@login_required
def profile(request, id):
    template_name = 'profile.html'

    user = request.user

    if user.id == id:
        orders = Order.objects.filter(user=user)
        ord_table = OrderTable(orders)
        products = [order.product for order in orders]
        prod_table = ProductTable(products)
    else:
        ord_table = None
        prod_table = None
        return HttpResponse("You are not authorized to view this profile.")
    
    context = {
        'user': user,
        'ord_table': ord_table,
        'prod_table': prod_table,
    }

    return render(request, context=context, template_name=template_name)


@login_required
def charts(request):
    template_name = 'charts.html'
    bl = BalanceBox.objects.all()

    df = pd.DataFrame({
        'date': [c.date for c in bl],
        'average': [c.average for c in bl],
        'year': [c.year for c in bl]
    })

    co2_fig = px.line(
        data_frame=df,
        x='date',
        y='average',
        animation_frame='year',
        title='Balance Box Evolution across time',
        color_discrete_sequence=['black']
    )
    
    charts = [
        co2_fig.to_html()
    ]

    context = {
        'charts': charts
    }

    return render(request, context=context, template_name=template_name)
