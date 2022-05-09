from django.db import models
from django.contrib.auth.models import User

class chargers(models.Model):
    MAIA='Maia'
    CHAVES='Chaves'
    PORTO ='Porto'
    CHARGERS_CHOICES = (
        (MAIA, "Maia"),
        (CHAVES, "Chaves"),
        (PORTO, "Porto"),
        )

    owner =  models.ForeignKey(User, on_delete=models.CASCADE) 
    
    brand = models.CharField
    model = models.CharField(max_length=9,
       
                    choices=CHARGERS_CHOICES,
                    default=MAIA)

    battery = models.CharField
    def __str__(self):
            return self.model

    class Meta:
        db_table = "chargers"