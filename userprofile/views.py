
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .models import Userprofile

from product.forms import ProductForm
from product.models import Product, OrderItem, Order

# Vendor details

def vendor_detail (request, pk):
    user = User.objects.get(pk=pk)
    # Can't use filter in template
    products = user.products.filter(status = Product.ACTIVE)

    return render(request, 'userprofile/vendor_detail.html',{
        'user' : user,
        'products': products,
    } )

@login_required
def my_store(request):
    products = request.user.products.exclude(status=Product.DELETED)
    order_items = OrderItem.objects.filter(product__user=request.user).order_by("order__id")
    unique_order_items = {}
    for order_item in order_items:
        unique_order_items[order_item.order.id] = order_item
    return render(
        request,
        "userprofile/my_store.html",
        {
            "products": products,
            "order_items": unique_order_items.values(),
        },
    )


@login_required
def my_store_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    return render(request, 'userprofile/my_store_order_detail.html', {
        'order': order
    })

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')

            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            # Django messages framework
            messages.success(request, 'The product was added to the store!')

            return redirect('my_store')
    else:
        form = ProductForm()

    return render(request, 'userprofile/product_form.html', {
        'title': 'Add product',
        'form': form
    })

@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            # Django messages framework
            messages.success(request, 'Your product details have been updated')

            return redirect('my_store')
    else:
        form = ProductForm(instance=product)

    return render(request, 'userprofile/product_form.html', {
        'title': 'Edit product',
        'product': product,
        'form': form
    })

@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()

    messages.success(request, 'The product was deleted!')

    return redirect('my_store')

@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            return redirect('index')
    else:
        form = UserCreationForm()
    
    return render(request, 'userprofile/signup.html', {
        'form': form
    })


