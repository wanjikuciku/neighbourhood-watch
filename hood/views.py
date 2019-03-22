from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse,Http404
from .models import Neighbourhood,Business,UserProfile


# Create your views here.
def index(request):
    return render(request,'index.html')
