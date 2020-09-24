from django.db import models
from accounts.models import Admin

# Create your models here.
class Restaurant(models.Model):
    id_admin = models.ForeignKey(Admin, null=False, blank=False, on_delete=models.CASCADE)
    nit = models.IntegerField(null=False, blank=False, unique=True)
    name = models.CharField(max_length=20, null=False, blank=False)
    address_location = models.CharField(max_length=40, null=False, blank=False)
    phone_num = models.IntegerField(null=False, blank=False, unique=True)
    web_page = models.URLField(max_length=100, null=True, blank=True)
    hours = models.CharField(max_length=25, null=True, blank=True)
    image = models.ImageField(upload_to='img_restaurants', null=False, blank=False)
    date_creation = models.DateField(auto_now=True, auto_now_add=False)
    state_delete = models.BooleanField(default=False)
    state_disponibility = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        #return str(self.id)
        return self.name

