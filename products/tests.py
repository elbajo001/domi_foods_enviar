from django.test import TestCase
from .models import Product
# Create your tests here.


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='carne', price=15000, description='carne asada')

    def test_name_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.name}'
        self.assertEquals(expected_object_name, 'carne')

    def test_price_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.price}'
        self.assertEquals(expected_object_name, 15000)

    def test_description_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.description}'
        self.assertEquals(expected_object_name, 'carne asada')