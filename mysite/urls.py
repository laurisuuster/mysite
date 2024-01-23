"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Imports for helper function 
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include

#My views
from core.views import index, contact, faq_view, terms_and_conditions_view, privacy_policy_view, success

urlpatterns = [

    #Hardcoded urls must be on top
    path('contact/', contact, name='contact'),
    path('terms/', terms_and_conditions_view, name='terms_and_conditions'),
    path('success/', success, name='success'),

 
    path('faq/', faq_view, name='faq'),
    path('privacy-policy/', privacy_policy_view, name='privacy_policy'),

    
    
    path('admin/', admin.site.urls),
    path('', include('userprofile.urls')),

    # Frontpage
    path('', include('product.urls')),
    path('', index, name='index'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
