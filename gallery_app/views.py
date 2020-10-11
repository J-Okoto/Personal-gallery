from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    Index function loads the start up page 
    '''
    
    return render(request,'index.html')

