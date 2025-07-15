from django.urls import path
from django.views.generic.base import RedirectView
from stock.views.item_views import *
from stock.views.normal_views import *
from stock.views.form_views import *
from stock.views.import_export_views import *


urlpatterns = [
    path('', RedirectView.as_view(url='home', permanent=True)),
    path('signup/', signup, name='signup'),
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/', users, name='users'),
    path('users/<int:id>', user_item, name='user_item'),
    path('users/create-new', user_form, name='user_form'),

    path('users/import/', import_data, name='import_users'),
    path('users/export/', export_data, name='export_users'),

    path('home/', home, name='home'),
    path('profile/<int:id>/', profile, name='profile'),
    path('orders', orders, name='orders'),

    path('boxes/', balance_boxes, name='boxes'),

    path('stores/', stores, name='stores'),

    path('stores/import/', import_data, name='import_stores'),
    path('stores/export/', export_data, name='export_stores'),

    path('stores/create/', store_form, name='store_form'),
    path('stores/<int:id>/', store_item, name='store_item'),
    path('stores/<int:id>/products/', products, name='products'),
    path('stores/<int:store_id>/products/create/', product_form, name='product_form'),
    path('stores/<int:store_id>/products/<int:id>/', product_item, name='product_item'),
    path('home/buy-product/<int:id>/', buy_product, name='buy_product'),

    path('users/<int:id>/orders/', orders, name='orders'),
    path('users/<int:user_id>/orders/create/', order_form, name='order_form'),
    path('users/<int:user_id>/orders/<int:order_id>/', order_item, name='order_item'),

    path('charts/', charts, name='charts'),
]