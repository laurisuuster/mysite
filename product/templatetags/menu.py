from django import template

from product.models import Category

register = template.Library()

# Retrive all the categories 

@register.inclusion_tag('core/menu.html')
def menu():
     categories = Category.objects.all()
     return {'categories': categories}