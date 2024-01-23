# This class handle cart crud operations 

# Ability to use variables from setting file 
from django.conf import settings

from .models import Product

# Cart class
class Cart(object):
    # Initilize cart class 
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        # Check if cart exist 
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart

    #Iterate through the cart, get product information and store it in product variable
    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
        
        # Convert cents to dollars 
        for item in self.cart.values():
            item['total_price'] = int(item['product'].price * item['quantity']) / 100

            yield item
    # Set the value for whole cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    # Notify the server about the change 
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': int(quantity), 'id': product_id}
        
        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id] ['quantity'] == 0:
                self.remove(product_id)

        
        self.save()

    #Remove items from the cart 
    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]

            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
        
        return int(sum(item['product'].price * item['quantity'] for item in self.cart.values())) / 100
