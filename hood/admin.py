from django.contrib import admin
from .models import UserProfile,Business,Post,Neighborhood
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Neighborhood)
