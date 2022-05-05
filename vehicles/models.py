from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):

     
    TESLA = 'TESLA'
    MAZDA = 'MAZDA'
    VOLVO = 'VOLVO'
    VEHICLE_CHOICES = (
        (TESLA, "Tesla"),
        (MAZDA, "Mazda"),
        (VOLVO, "Volvo"),
        )

    owner =  models.ForeignKey(User, on_delete=models.CASCADE) 
    
    model = models.CharField(max_length=9,
       
                    choices=VEHICLE_CHOICES,
                    default=TESLA)

    def __str__(self):
            return self.model