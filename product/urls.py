# This urls.py is to contain urls related with store.
from django.urls import path

from . import views

urlpatterns = [
    path('create_review/<int:product_id>/', views.create_review, name='create_review'),
    path('search/', views.search, name='search'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('change-quantity/<str:product_id>/', views.change_quantity, name='change_quantity'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('cart/success/', views.success, name='success'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('update-order-status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
]