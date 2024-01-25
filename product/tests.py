from django.test import TestCase
from .models import Product

# Create your tests here.
from django.db import models


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(
            category='Berries',
            title='Apple',
            description='This is a test product.',
            price=100.00,
            image='media/uploads/kumara.jpg',
            region='nelson'
        )

    def test_category_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('category').max_length
        self.assertEquals(max_length, 50)

    def test_title_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_description_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('description').max_length
        self.assertEquals(max_length, 1000)

    def test_price_max_digits(self):
        product = Product.objects.get(id=1)
        max_digits = product._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 8)

    def test_price_decimal_places(self):
        product = Product.objects.get(id=1)
        decimal_places = product._meta.get_field('price').decimal_places
        self.assertEquals(decimal_places, 2)


class ProductTestCase(TestCase):
    def test_something(self):
        # Your test code here
        self.assertEqual(1 + 1, 2)