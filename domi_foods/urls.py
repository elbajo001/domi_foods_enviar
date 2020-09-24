"""domi_foods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'), name='products'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('restaurants/', include('restaurants.urls'), name='restaurants'),
    path('api_products/', include('api_products.urls'), name='api_restaurants'),
    path('api_products/v1/', include('api_products.urls')),
    path('api_restaurants/', include('api_restaurants.urls'), name='api_restaurants'),
    path('api_restaurants/v1/', include('api_restaurants.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   