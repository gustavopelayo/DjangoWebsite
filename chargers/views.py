from django.shortcuts import render
from .models import chargers
from django.contrib.auth.models import User
from users.models import Profile

from django.views.generic import (
    ListView,
    DetailView,

)
class UserChargersListView(ListView):
    model = chargers
    template_name = 'chargers/chargers.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'chargers'
    
    def get_queryset(self):
        print(chargers.objects.filter(self.request.user.id))
        return chargers.objects.filter(self.request.user.id)

class UserchargersDetailView(ListView):
    model = chargers