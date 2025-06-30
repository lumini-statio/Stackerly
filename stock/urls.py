from django.urls import path
from stock.views.normal_views import *
from stock.views.item_views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('/', home, name='home'),
    path('profile/', profile, name='profile'),

    path('stores/', stores, name='stores'),
    path('stores/<int:id>/products/', products, name='products'),
    path('stores/<int:store_id>/products/<int:product_id>', product_item, name='products'),

    path('users/', users, name='users'),
    path('users/<int:id>/orders/', orders, name='orders'),
    path('users/<int:user_id>/orders/<int:order_id>/', order_item, name='order_detail'),
]