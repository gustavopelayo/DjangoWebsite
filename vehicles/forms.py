
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from vehicles.models import Vehicle
from chargers.models import chargers

class VehicleAddForm(forms.ModelForm):
	
    class Meta:
        model = Vehicle
        fields = ('brand','model', 'battery')
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['brand']
        self.fields['model']
        self.fields['battery']