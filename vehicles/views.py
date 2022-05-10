from ssl import VERIFY_CRL_CHECK_CHAIN
from .models import Vehicle
from blog.models import Post
from vehicles import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,

)
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from vehicles.forms import VehicleAddForm

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

class AddVehicleView(LoginRequiredMixin, CreateView):
    
    model = Vehicle
    form_class = VehicleAddForm

    def get_form_kwargs(self):
           
            kwargs = super().get_form_kwargs()
            kwargs['user'] = self.request.user
            return kwargs

    def form_valid(self, form):
            
            form.instance.owner = self.request.user
            return super().form_valid(form)
