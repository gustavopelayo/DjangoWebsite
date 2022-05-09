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

    
    model = models.CharField(max_length=9,
       
                    choices=CHARGERS_CHOICES,
                    default=MAIA)

    def __str__(self):
            return self.model

    class Meta:
        db_table = "chargers"