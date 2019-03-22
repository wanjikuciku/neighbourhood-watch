from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length=40)

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()
        
    @classmethod
    def find_neighbourhood(cls,neighbourhood_id):
        neighbourhood = cls.objects.get(id=neighbourhood_id)
        return neighbourhood

    def update_neighbourhood(self,name):
        self.name = name
        self.save()

    def __str__(self):
        return self.neighbourhood_name

class UserProfile(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey('Neighbourhood',on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=40)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username

class Business(models.Model):
    name = models.CharField(max_length=40)
    owner = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    business_location = models.CharField(max_length=40)
    email = models.EmailField()
    business_neighbourhood = models.ForeignKey('neighbourhood',on_delete=models.CASCADE,null=True)

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()
    
    def __str__(self):
        return self.name




