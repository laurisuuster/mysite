

from django.shortcuts import render

from product.models import Product

from django.shortcuts import render, redirect, HttpResponse
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import EmailMessage


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            EmailMessage(
               'Contact Form Submission from {}'.format(name),
               message,
               'form-response@example.com', # Send from (your website)
               ['JohnDoe@gmail.com'], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to
                
            ).send()
            
            return redirect('success')

    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def success(request):
    return render(request, 'core/success.html')


def success(request):
   return HttpResponse('Success!')

def index(request):
    # Filter to display only active products
    products = Product.objects.filter(status = Product.ACTIVE)[0:6]

    return render(request, 'core/index.html', {
        'products': products
    })




def faq_view(request):
    return render(request, 'core/faq.html')


def privacy_policy_view(request):
    return render(request, 'core/privacy_policy.html')


def terms_and_conditions_view(request):
    return render(request, 'core/terms.html')