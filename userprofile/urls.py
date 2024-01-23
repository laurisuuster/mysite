from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    # Vendor panel 
    path('my-store/add-product/', views.add_product, name='add_product'),
    path('my-store/edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('my-store/delete-product/<int:pk>/', views.delete_product, name='delete_product'),
    path('my-store/order-detail/<int:pk>/', views.my_store_order_detail, name='my_store_order_detail'),

    path('my-store/', views.my_store, name='my_store'),
    # Sign Up, Sign In, Logout 
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Vendor account page
    path('myaccount/', views.myaccount, name='myaccount'),

    # Vendor Detail page
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail'),

    
]