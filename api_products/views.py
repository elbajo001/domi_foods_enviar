from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from .serializers import ProductSerializer


# Create your views here.
class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class GETDetailProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class GETListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class POSTListProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class POSTDetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer