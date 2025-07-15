from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.models import User

from stock.models import (Store,
                          Product,
                          Order,
                          CustomUser,
                          ProfitLossRecord,
                          BalanceBox,
                          UserPurchase)
from stock.components.tables import (BalanceBoxesTable,
                                     StoreTable,
                                     ProductTable,
                                     OrderTable,
                                     UserTable,
                                     AllProductsTable)

import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot

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
    table = AllProductsTable(products)
    user = request.user

    context = {
        'table': table,
        'user': user,
        'products': products
    }

    return render(request, context=context, template_name=template_name)


@login_required
def balance_boxes(request):
    template_name = 'list/balance_boxes.html'

    boxes = BalanceBox.objects.all().order_by('-id')
    table = BalanceBoxesTable(boxes)

    context = {
        'table': table
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

        user_purchases = UserPurchase.objects.filter(user=user)
        products = [purchase.product for purchase in user_purchases]
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
    records = ProfitLossRecord.objects.all().values('date', 'amount', 'record_type')

    if not records:
        return render(request, 'charts.html', {'plot_div': """
                                                <div class='w-100 d-flex justify-content-center'>
                                                    <p class='text-light'>No hay datos suficientes</p>
                                                </div>
                                               """})

    df = pd.DataFrame.from_records(records)
    df['date'] = pd.to_datetime(df['date'])

    grouped = df.groupby(['date', 'record_type']).sum().reset_index()
    pivot_df = grouped.pivot(index='date', columns='record_type', values='amount').fillna(0)

    income_values = pivot_df['INCOME'] if 'INCOME' in pivot_df.columns else pd.Series([0] * len(pivot_df), index=pivot_df.index)
    expense_values = pivot_df['EXPENSE'] if 'EXPENSE' in pivot_df.columns else pd.Series([0] * len(pivot_df), index=pivot_df.index)

    trace_income = go.Scatter(x=pivot_df.index, y=income_values, mode='lines+markers', name='Incomes', line=dict(color='green'))
    trace_expense = go.Scatter(x=pivot_df.index, y=expense_values, mode='lines+markers', name='Expenses', line=dict(color='red'))

    layout = go.Layout(title='Income and Expenses per Day',
                       xaxis=dict(title='Date'),
                       yaxis=dict(title='Amount'),
                       template='plotly_dark')

    fig = go.Figure(data=[trace_income, trace_expense], layout=layout)

    plot_div = plot(fig, output_type='div', include_plotlyjs=True)

    return render(request, 'charts.html', {'plot_div': plot_div})



def orders(request):
    template_name = 'list/orders.html'

    orders = Order.objects.all()
    table = OrderTable(orders)

    context = {
        'table': table,
    }

    return render(request, context=context, template_name=template_name)
