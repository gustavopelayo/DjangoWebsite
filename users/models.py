
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    middlename = models.CharField(max_length = 300, default= "middle_name")
    nif = models.IntegerField(unique  =True, default= 000000000)
    address = models.CharField(max_length = 400, default= "address")
    city = models.CharField(max_length = 50, default= "city")
    postalcode = models.CharField(max_length = 150, default= "0000-000")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):

        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:

            output_size = (300,300)

            img.thumbnail(output_size)
            img.save(self.image.path)


    class Meta:
        db_table = "profile"