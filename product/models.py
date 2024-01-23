from statistics import mode
from django.contrib.auth.models import User
from django.db import models
#Thumbnail
from django.core.files import File
from io import BytesIO
from PIL import Image

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    # Fix mispelled category in admin panel
    class Meta:
        verbose_name_plural = 'Categories'
    
    # String representation of class 
    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    DELETED = 'deleted'
    INACTIVE = 'inactive'  # Instead of 'deleted'
    OUT_OF_STOCK = 'outofstock'
    SOLD_OUT = 'soldout'

    STATUS_CHOICES = (
        (DRAFT,'Draft'),
        (WAITING_APPROVAL, 'Waiting approval'),
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted- Product listing has been removed'),
        (DRAFT, 'Draft - Product is in the draft stage and not yet ready for publishing.'),
        (WAITING_APPROVAL, 'Waiting Approval - Product is submitted and waiting for approval.'),
        (ACTIVE, 'Active - Product is live and available for purchase.'),
        (INACTIVE, 'Inactive - Product is not currently available for purchase.'),
        (OUT_OF_STOCK, 'Out of Stock - Product is temporarily unavailable but will be restocked.'),
        (SOLD_OUT, 'Sold Out - Product is completely sold out and not available for purchase.'),

    )
      # New field for region
    REGION_CHOICES = [
        ('Auckland', 'Auckland'),
        ('Hamilton', 'Hamilton'),
        ('Tauranga', 'Tauranga'),
        ('Napier', 'Napier'),
        ('Palmerston North', 'Palmerston North'),
        ('Porirua', 'Porirua'),
        ('Upper Hutt', 'Upper Hutt'),
        ('Lower Hutt', 'Lower Hutt'),
        ('Wellington', 'Wellington'),
        ('Nelson', 'Nelson'),
        ('Christchurch', 'Christchurch'),
        ('Dunedin', 'Dunedin'),
        ('Invercargill', 'Invercargill'),
        ('North Island', 'North Island'),
        ('South Island', 'South Island'),
        ('Far North', 'Far North (Kaitaia)'),
        ('Kaipara', 'Kaipara (Dargaville)'),
        ('Whangarei', 'Whangarei (Whangarei)'),
        ('Hauraki', 'Hauraki (Paeroa)'),
        ('Matamata-Piako', 'Matamata-Piako (Matamata)'),
        ('Ōtorohanga', 'Ōtorohanga (Ōtorohanga)'),
        ('South Waikato', 'South Waikato (Tokoroa)'),
        ('Thames-Coromandel', 'Thames-Coromandel (Whitianga)'),
        ('Waikato', 'Waikato (Hamilton)'),
        ('Waipa', 'Waipa (Te Awamutu)'),
        ('Kawerau', 'Kawerau (Kawerau)'),
        ('Ōpōtiki', 'Ōpōtiki (Ōpōtiki)'),
        ('Western Bay of Plenty', 'Western Bay of Plenty (Tauranga)'),
        ('Whakatāne', 'Whakatāne (Whakatāne)'),
        ('Central Hawke\'s Bay', 'Central Hawke\'s Bay (Waipawa)'),
        ('Hastings', 'Hastings (Hastings)'),
        ('Wairoa', 'Wairoa (Wairoa)'),
        ('New Plymouth', 'New Plymouth (New Plymouth)'),
        ('South Taranaki', 'South Taranaki (Hawera)'),
        ('Horowhenua', 'Horowhenua (Levin)'),
        ('Manawatū', 'Manawatū (Palmerston North)'),
        ('Ruapehu', 'Ruapehu (Ohakune)'),
        ('Whanganui', 'Whanganui (Whanganui)'),
        ('Carterton', 'Carterton (Carterton)'),
        ('Kāpiti Coast', 'Kāpiti Coast (Paraparaumu)'),
        ('Masterton', 'Masterton (Masterton)'),
        ('South Wairarapa', 'South Wairarapa (Martinborough)'),
        ('Rangitikei', 'Rangitikei (Marton)'),
        ('Rotorua Lakes', 'Rotorua Lakes (Rotorua)'),
        ('Stratford', 'Stratford (Stratford)'),
        ('Tararua', 'Tararua (Dannevirke)'),
        ('Taupō', 'Taupō (Taupō)'),
        ('Waitomo', 'Waitomo (Te Kuiti)'),
        ('Gisborne', 'Gisborne (Gisborne)'),
        ('Buller', 'Buller (Westport)'),
        ('Grey', 'Grey (Greymouth)'),
        ('Westland', 'Westland (Hokitika)'),
        ('Ashburton', 'Ashburton (Ashburton)'),
        ('Hurunui', 'Hurunui (Amberley)'),
        ('Kaikōura', 'Kaikōura (Kaikōura)'),
        ('Mackenzie', 'Mackenzie (Fairlie)'),
        ('Selwyn', 'Selwyn (Rolleston)'),
        ('Timaru', 'Timaru (Timaru)'),
        ('Waimakariri', 'Waimakariri (Rangiora)'),
        ('Waimate', 'Waimate (Waimate)'),
        ('Central Otago', 'Central Otago (Alexandra)'),
        ('Clutha', 'Clutha (Balclutha)'),
        ('Queenstown-Lakes', 'Queenstown-Lakes (Queenstown)'),
        ('Gore', 'Gore (Gore)'),
        ('Southland', 'Southland (Invercargill)'),
        ('Waitaki', 'Waitaki (Oamaru)'),
        ('Marlborough', 'Marlborough (Blenheim)'),
        ('Tasman', 'Tasman (Richmond)'),
    ]
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    # Image uploader
    image = models.ImageField(upload_to='uploads/product_images', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/product_images/thumbnail', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)
    region = models.CharField(max_length=50, choices=REGION_CHOICES, blank=True, null=True)

   
    # Display newest products first
    class Meta:
        ordering = ('-created_at',)

    # String representation of class 
    def __str__(self) -> str:
        return self.title
    
    # Function to display product prices in dollars instead of cents
    def get_display_price(self):
        return self.price /100
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'
    
    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        name = image.name.replace('uploads/product_images/', '')
        thumbnail = File(thumb_io, name=name)

        return thumbnail
    
    
class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    paid_amount = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    # For payment gateway
    payment_intent = models.CharField(max_length=255,blank=True, null=True)
    # Refrence to the user object 
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    # When was the order created
    created_at = models.DateTimeField(auto_now_add=True)

    #Order Statuses 

    STATUS_CHOICES = [
        ('received', 'Received'),
        ('processed', 'Processed'),
        ('shipped', 'Shipped'),
        ('declined', 'Declined'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='received',
    )

    # Modified checkout 
    SHIPPING_CHOICES = [
        ('postage', 'Postage'),
        ('home_delivery', 'Home Delivery'),
        ('self_pickup', 'Self Pickup'),
    ]

    shipping_option = models.CharField(
        max_length=20,
        choices=SHIPPING_CHOICES,
        default='postage',
    )

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_display_price(self):
        return self.price / 100
    
# not sure whether this is required
from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"
    


# Product review model 
class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review on {self.product.title}"