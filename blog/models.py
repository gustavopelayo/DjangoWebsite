from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile
from vehicles.models import Vehicle

class Post(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE,  null=True)

    
    def get_absolute_url(self):

        return reverse('post-detail', kwargs ={'pk': self.pk} )
