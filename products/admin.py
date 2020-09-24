from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image', 'date_creation', 'state_delete', 'state_disponibility']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date_creation', 'state_delete']


'''
admin.site.register(Category)
admin.site.register(Product)
'''

