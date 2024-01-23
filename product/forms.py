from django import forms

from .models import Product, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'zipcode', 'city', 'shipping_option',)

# https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image','region')
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-250'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-250'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-250'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-250'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-4 border border-gray-250'
            }),
            'region': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-250'
            }),
        }

from .models import ProductReview

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['rating', 'review_text']


class OrderStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'w-full p-4 border border-gray-250'}),
        }