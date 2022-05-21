from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Vehicle
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,

)
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404
from vehicles.forms import VehicleAddForm
import plotly.express as px
import plotly.offline as plot
import plotly.graph_objects as go
from datetime import datetime
import plotly.express as px



class UserVehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicles/vehicles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'vehicles'
    
    def get_queryset(self):
        print(Vehicle.objects.filter(owner_id= self.request.user.id))
        return Vehicle.objects.filter(owner_id= self.request.user.id)

def UserVehicleDetailView(request, pk):
    
    
    posts = Post.objects.filter(vehicle=pk)
    dates = []
    powers = []
    times = []
    chargers = []
    for post in posts:
        dates.append(post.hourin)
        powers.append(post.power)
        chargers.append(post.chargers.nickname)
    for date in dates:
        date = date.strftime('%H:%M:%S')
        times.append(date)

    context_object_name = 'posts'
    print(times)
    print(powers)
    print(chargers)
    template = loader.get_template('vehicles/vehicle_detail.html')
    data = [go.Scatter(x = times, y = powers,name='Net Worth')]
    graph = plot.plot(data, auto_open=False, output_type='div')
    data2=[go.Pie(labels=chargers)]
    fig = plot.plot(data2, auto_open=False, output_type='div')

    context = {'graph': graph, 'posts': posts, 'fig': fig}
    print(posts)
    return render(request, 'vehicles/vehicle_detail.html', context = {'graph': graph, 'posts': posts, 'fig':fig })

    

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
