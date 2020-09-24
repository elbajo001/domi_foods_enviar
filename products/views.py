from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to products\' views</h1>")

class ProductView(ListView):
    model = Product
    template_name = 'product_list.html'