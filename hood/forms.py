from django import forms
from .models import UserProfile,Business,Neighbourhood
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core import validators

class NeighbourhoodForm(ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('neighbourhood_name',)

class AddBusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ('name','business_location','email')

class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','location')