import os
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import catalog
from .models import detail
# Create your views here.
image_name = "boom.JPG"
modelSelected="" 

def index(request):
    context = {
        "modelSelected":"catalog",
        "cList_path":"cList",
        "catalogs":catalog.objects.all(),
            }    
    return render(request,"index.html",context)

def cList(request):
    global modelSelected
    context  = {
            "modelSelected":"catalog",
            "cList_path":"cList",
            "catalogs":catalog.objects.all(),
                 }
    return render(request,"index.html",context)
       
def dList(request):
    global modelSelected
    selection = request.POST.get("submit",None)
    context  = {
       "dList_path":"dList",
       "modelSelected":"detail",
       "catalogs":catalog.objects.all().filter(id=selection),
       "details":detail.objects.all().filter(catalog=selection),
        }
    return render(request,"index.html",context)                                 
def image(request):
    global image_name
    
    context = {
        "image_name":image_name
    }
    return render(request,"index.html",context)

def order(request):
       next = request.POST.get('next', '/')
       selection = request.POST.get("submit",None)

       print("next",next)
       print("selection",selection)
       if (next=="cList"):
             print("next",next)
             context  = {
                 "modelSelected":"catalog",
                 "cList_path":"cList",
                 "catalogs":catalog.objects.all(),
               }
             return render(request,"index.html",context)
    #   print(request.path)
    #   print(next)
    #   return HttpResponseRedirect(next)
       context  = {
          "dList_path":"order",
            }
       return render(request,"order.html",context)
             
def contactMe(request):
      global modelSelected
      with open(os.path.join(settings.BASE_DIR, 'contact.txt'),'r') as file_:
              fileContent = file_.read()
      context  = {
        "dList_path":"contactMe",
        "modelSelected":"contactMe",
       "catalogs":catalog.objects.all(),
        "myContact" : fileContent,
          }
      return render(request,"index.html",context)         
    

def aboutMe(request):
      global modelSelected
      with open(os.path.join(settings.BASE_DIR, 'ramtin.txt'),'r') as file_:
              fileContent = file_.read()
      context  = {
        "dList_path":"aboutMe",
        "modelSelected":"aboutMe",
        "catalogs":catalog.objects.all(),
        "myProfile" : fileContent,
          }
      return render(request,"index.html",context)         
    