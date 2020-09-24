from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from restaurants.models import Restaurant
from products.models import Category, Product
from .serializers import RestaurantSerializer, CategorySerializer


# Create your views here.
class ProductAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

#listar un restaurante con id X
class GETDetailRestaurant(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
'''
#listar todas las categorías de un restaurante X
class GETDetailCategoryRestaurant(generics.ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        products = Product.objects.filter(restaurant=1)
        print("query: ", products[1])
        print("query: ", products[2].category.name)
         #= products.category.all()
        #print("query: ", queryset)
'''

#Listar todos los restaurantes
class GETListRestaurant(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

#crear un restaurante
class POSTListRestaurant(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

#Modificar un restaurante con id X
class POSTDetailRestaurant(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer