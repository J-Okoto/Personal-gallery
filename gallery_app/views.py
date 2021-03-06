from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image, Category, Location

# Create your views here.

def index(request):
    '''
    Index function loads the start up page 
    '''
    gallery = Image.objects.all()[:6]
    return render(request,'index.html',{'gallery':gallery})

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

def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term  =  request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message  = f"{search_term}"
        
        return render(request, 'search.html', {"message":message, "images":searched_images})
    else:
        message = "You have not searched for any category"
        
        return render(request, 'search.html', {"message":message})


def portrait(request):
    portrait_category=Category.objects.get(pk=1)
    portrait = Image.objects.all().filter(category=portrait_category)
    return render(request,'category/portrait.html', {'portrait':portrait})

def nature(request):
    nature_category=Category.objects.get(pk=4)
    nature = Image.objects.filter(category=nature_category)
    return render(request,'category/nature.html', {'nature':nature})

def wedding(request):
    wedding_category = Category.objects.get(pk=3)
    wedding = Image.objects.filter(category=wedding_category)
    return render(request,'category/wedding.html', {'wedding':wedding}) 

def wildlife(request):
    wildlife_category = Category.objects.get(pk=2)
    wildlife = Image.objects.filter(category=wildlife_category)
    return render(request,'category/wildlife.html', {'wildlife':wildlife})      