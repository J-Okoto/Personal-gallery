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
    Function returns the list of photos in the database
    '''
    gallery = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'gallery':gallery})

def single_image_details(request,image_id):
    '''
    Function that returns details of a single image. 
    '''
    image_detail = get_object_or_404(Image, pk=image_id)
    return render(request,'gallery/details.html', {'image_detail':image_detail})

