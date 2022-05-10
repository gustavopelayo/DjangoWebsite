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

    nickname = models.CharField(max_length=350,
       
                    choices=CHARGERS_CHOICES,
                    default=MAIA)

    def __str__(self):
            return self.nickname
    chargepower = models.IntegerField()    
    shelly = models.CharField(max_length = 100, default= None)
    class Meta:
        db_table = "chargers"