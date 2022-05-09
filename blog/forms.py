
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from vehicles.models import Vehicle
from chargers.models import chargers

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('vehicle','chargers')
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['vehicle'].queryset = Vehicle.objects.filter(owner=user)
        self.fields['chargers'].queryset = chargers.objects
