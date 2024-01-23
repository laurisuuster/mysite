import json
import stripe

from django.conf import settings
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect

from core.forms import ReviewForm

from .models import Category, Product, Order, OrderItem, Review

from.cart import Cart
from .forms import OrderForm
from django.db.models import Q
from django.contrib import messages
from itertools import groupby



# Create your views here.

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('index')

def success(request):
    return render(request, 'store/success.html')

def change_quantity(request, product_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1

        cart = Cart(request)
        cart.add(product_id, quantity, True)
    
    return redirect('cart_view')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')

def cart_view(request):
    cart = Cart(request)

    return render(request, 'store/cart_view.html', {
        'cart': cart
    })

@login_required
def checkout(request):
    cart = Cart(request)

    if cart.get_total_cost() == 0:
        return redirect('cart_view')

    if request.method == 'POST':
        data = json.loads(request.body)
        first_name = data['first_name']
        last_name = data['last_name']
        address = data['address']
        zipcode = data['zipcode']
        city = data['city']
        shipping_option = data['shipping_option']  # Shipping option

        if first_name and last_name and address and zipcode and city:
            form = OrderForm(request.POST)

            total_price = 0
            items = []

            for item in cart:
                product = item['product']
                total_price += product.price * int(item['quantity'])

                items.append({
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': product.title,
                        },
                        'unit_amount': product.price
                    },
                    'quantity': item['quantity']
                })
            
            stripe.api_key = settings.STRIPE_SECRET_KEY
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=items,
                mode='payment',
                success_url=f'{settings.WEBSITE_URL}cart/success/',
                cancel_url=f'{settings.WEBSITE_URL}cart/',
            )
            payment_intent = session.payment_intent

            order = Order.objects.create(
                first_name=first_name,
                last_name=last_name,
                address=address,
                zipcode=zipcode,
                city=city,
                created_by = request.user,
                is_paid = True,
                payment_intent = payment_intent,
                paid_amount = total_price,
                shipping_option=shipping_option,  # Shipping option
                
            )

            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            cart.clear()

            return JsonResponse({'session': session, 'order': payment_intent})
    else:
        form = OrderForm()

    return render(request, 'store/checkout.html', {
        'cart': cart,
        'form': form,
        'pub_key': settings.STRIPE_PUB_KEY,
    })


from django.db.models import Q

def search(request):
    query = request.GET.get('query', '')
    sort_by = request.GET.get('sort_by', 'newest')

    products = Product.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query),
        status=Product.ACTIVE,
    )

    if sort_by == 'newest':
        products = products.order_by('-created_at')
    elif sort_by == 'lowest_price':
        products = products.order_by('price')
    elif sort_by == 'highest_price':
        products = products.order_by('-price')
    elif sort_by == 'alphabetical':
        products = products.order_by('title')

    return render(request, 'store/search.html', {
        'query': query,
        'products': products,
        'selected_sort': sort_by,  # Pass the selected sorting option to the template
    })
    
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status = Product.ACTIVE)

    return render(request, 'store/category_detail.html',{
        'category':category,
        'products': products,
        })
    

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)

    return render(request, 'store/product_detail.html', {
        'product': product,
        "reviews": product.reviews.all().order_by('-id')[:3],
        "form": ReviewForm()
    })

@login_required
def create_review(request, product_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['stars']
            comment = form.cleaned_data['comment']
            Review.objects.create(
                product_id=product_id,
                user=request.user,
                rating=rating,
                comment=comment,
            )
    return redirect(request.META['HTTP_REFERER'])

@login_required
def my_orders(request):
    # Get all order items related to the user
    order_items = OrderItem.objects.filter(order__created_by=request.user).order_by('-order__created_at')

    # Group order items by order ID
    grouped_order_items = {key: list(group) for key, group in groupby(order_items, key=lambda x: x.order.id)}

    return render(request, 'mystore.html', {'grouped_order_items': grouped_order_items})



from .forms import OrderStatusUpdateForm

def update_order_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        new_status = request.POST.get('order_status')

        # Update the order status
        order.status = new_status
        order.save()

        # Redirect back to the order detail page
        return redirect('my_store_order_detail', pk=order_id)

    return redirect('my_store_order_detail', pk=order.id)

def my_store_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    context = {
        'order': order,
        'order_status': order.status,  # Include the order status in the context
    }

    return render(request, 'your_template_path/my_store_order_detail.html', context)