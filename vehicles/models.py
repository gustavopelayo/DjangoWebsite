from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):

     
    TESLA = 'Tesla'
    MAZDA = 'Mazda'
    VOLVO = 'Volvo'
    VEHICLE_CHOICES = (
        (TESLA, "Tesla"),
        (MAZDA, "Mazda"),
        (VOLVO, "Volvo"),
        )

    owner =  models.ForeignKey(User, on_delete=models.CASCADE) 
    brand = models.CharField(max_length=150)
    battery = models.CharField(max_length=150)

    model = models.CharField(max_length=150,
       
                    choices=VEHICLE_CHOICES,
                    default=TESLA)

    def __str__(self):
            return self.model

    class Meta:
        db_table = "vehicles"