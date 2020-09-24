from rest_framework import serializers
from restaurants.models import Restaurant
from products.models import Category

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'id_admin', 'nit', 'name', 'address_location', 'phone_num', 'web_page', 'hours', 'image', 'date_creation', 'state_delete', 'state_disponibility')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image', 'date_creation', 'state_delete')
