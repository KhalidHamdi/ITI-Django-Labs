# mart/urls.py

from django.urls import path
from .views import *

# api import
from .api import *

urlpatterns = [
    path('', products, name='products'),
    path('product/', product, name='product'),
    path('product/<int:product_id>/', product, name='product'), 
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('tracking/add/<int:product_id>/', add_to_tracking, name='add_to_tracking'),
    path('tracking/view/', view_tracking, name='view_tracking'),
    
    
    # api routes
    path('api/products/', products_api, name='products_api'),
    path('api/product/<int:product_id>/', product_api, name='product_api'),
    
]
