from django.db import models

# Create your models here.
class User_Restaurant(models.Model):
    DOCUMENTS_TYPE = [
        ('C.C', 'Cédula de ciudadanía'),
        ('T.I', 'Tarjeta de identificación'),
        ('Passport', 'Pasaporte'),
    ]
    #login_id = models.ForeignKey()
    document_type = models.CharField(choices=DOCUMENTS_TYPE, max_length=8)
    document = models.IntegerField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    phone_num = models.IntegerField(null=False, blank=False, unique=True)
    email_address = models.EmailField(max_length=30, null=False, blank=False, unique=True)
    address_location = models.CharField(max_length=50, null=False, blank=False)
    state_delete = models.BooleanField(default=False)
    state_disponibility = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Admin(models.Model):
    id_user_restaurant = models.ForeignKey(User_Restaurant, on_delete=models.CASCADE)
    position_staff = models.CharField(max_length=20, default='Admin', null=False, blank=False)

    def __str__(self):
        return self.id_user_restaurant.first_name

class Client(models.Model):
    id_user_restaurant = models.ForeignKey(User_Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_user_restaurant.first_name

class Delivery_man(models.Model):
    VEHICLE_TYPE = [
        ('bicyle', 'bicycle / monocycle'),
        ('motorcycle', 'motorcycle'),
    ]
    image = models.ImageField(upload_to='img_accounts', null=False, blank=False)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type_of_vehicle = models.CharField(choices=VEHICLE_TYPE, max_length=10)
    vehicle_document = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.id_client.id_user_restaurant.first_name