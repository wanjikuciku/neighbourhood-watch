from django import forms
from .models import UserProfile,Business,Neighborhood,Post
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core import validators

class NeighborhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('neighborhood_name',)

class AddBusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ('name','business_location','email')

class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','neighborhood_name',)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','post_description',)