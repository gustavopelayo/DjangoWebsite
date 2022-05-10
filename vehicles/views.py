from ssl import VERIFY_CRL_CHECK_CHAIN
from django.shortcuts import render
from .models import Vehicle
from django.contrib.auth.models import User
from users.models import Profile
from blog.models import Post
from django.views.generic import (
    ListView,
    DetailView,

)
from django.shortcuts import render, get_object_or_404

class UserVehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicles/vehicles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'vehicles'
    
    def get_queryset(self):
        print(Vehicle.objects.filter(owner_id= self.request.user.id))
        return Vehicle.objects.filter(owner_id= self.request.user.id)
class UserVehicleDetailView(ListView):
    model = Post
    template_name = 'vehicles/vehicle_detail.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'


    def get_queryset(self):

        vehicle = get_object_or_404(Vehicle, id =self.kwargs.get('pk'))
        
        print(Post.objects.filter(vehicle= vehicle))
        return Post.objects.filter(vehicle= vehicle)


