from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image, Category, Location

# Create your views here.

def index(request):
    '''
    Index function loads the start up page 
    '''
    
    return render(request,'index.html')

def gallery(request):
    '''
    gallery function returns the list of photos in the database
    '''
    gallery = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'gallery':gallery})

