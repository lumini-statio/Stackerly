from django.urls import path
from django.views.generic.base import RedirectView
from stock.views.item_views import *
from stock.views.normal_views import *
from stock.views.form_views import *


urlpatterns = [
    path('', RedirectView.as_view(url='home', permanent=True)),
    path('signup/', signup, name='signup'),
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/', users, name='users'),

    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),

    path('stores/', stores, name='stores'),
    path('stores/create/', store_form, name='store_form'),
    path('stores/<int:id>/', store_item, name='store_item'),

    path('stores/<int:id>/products/', products, name='products'),
    path('stores/<int:store_id>/products/create/', product_form, name='product_form'),
    path('products/<int:id>/', product_item, name='product_item'),

    path('users/<int:id>/orders/', orders, name='orders'),
    path('users/<int:user_id>/orders/create/', order_form, name='order_form'),
    path('users/<int:user_id>/orders/<int:order_id>/', order_item, name='order_item'),
]