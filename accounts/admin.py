from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User_Restaurant)
class UserRestaurantAdmin(admin.ModelAdmin):
    list_display = ['document_type', 'document', 'first_name', 'last_name', 'phone_num', 'email_address', 'address_location', 'state_delete', 'state_disponibility']

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['id_user_restaurant', 'position_staff']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id_user_restaurant']

@admin.register(Delivery_man)
class DeliveyManAdmin(admin.ModelAdmin):
    list_display = ['image', 'id_client', 'vehicle_document']

'''
admin.site.register(Client)
admin.site.register(Admin)
admin.site.register(User_Restaurant)
admin.site.register(Delivey_man)
'''