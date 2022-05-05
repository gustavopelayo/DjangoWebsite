from django.shortcuts import render
from .models import Vehicle
from django.contrib.auth.models import User
from users.models import Profile

from django.views.generic import (
    ListView,
    DetailView,

)
class UserVehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicles/vehicles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'vehicles'
    
    def get_queryset(self):
        print(Vehicle.objects.filter(owner_id= self.request.user.id))
        return Vehicle.objects.filter(owner_id= self.request.user.id)

class UserVehicleDetailView(DetailView):
    model = Vehicle