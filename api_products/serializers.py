from rest_framework import serializers
from products.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image', 'category', 'restaurant', 'date_creation', 'state_delete', 'state_disponibility')