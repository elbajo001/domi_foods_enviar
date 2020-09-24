from django.db import models
from restaurants.models import Restaurant

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='img_categories', null=False, blank=False)
    date_creation = models.DateField(auto_now=True, auto_now_add=False)
    state_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img_products', null=False, blank=False)
    category = models.ManyToManyField(Category)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date_creation = models.DateField(auto_now=True, auto_now_add=False)
    state_delete = models.BooleanField(default=False)
    state_disponibility = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        #ordering = ['nombre']

    def __str__(self):
        return self.name

