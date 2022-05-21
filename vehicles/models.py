from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Vehicle(models.Model):

     

    owner =  models.ForeignKey(User, on_delete=models.CASCADE) 
    brand = models.CharField(max_length=150)
    battery = models.CharField(max_length=150)

    model = models.CharField(max_length=150)

    def __str__(self):
            return self.model
    
    def get_absolute_url(self):

        return reverse('vehicle-list')
    class Meta:
        db_table = "vehicles"