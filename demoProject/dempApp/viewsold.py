from msilib.schema import SelfReg
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import catalog
from .models import detail
# Create your views here.
image_name = "boom.JPG"
sw1=False
modelSelected="" 

def index(request):
    global sw1
    context = {
    "sw1":False,
    "cList_path":"index",
    "image_name":image_name
    }
    return render(request,"index.html",context)

def cList(request):
    global sw1
    global modelSelected
    selection = request.GET.get('mybtn',None)
    print("clist-1",selection)
    if selection ==  None :
         context  = {
            "sw1": True,
            "modelSelected":"catalog",
            "cList_path":"cList",
            "catalogs":catalog.objects.all(),
                 }
        # return render(request,"index.html",context)       
    else :   
       print("clist-2",selection)    
       context  = {
           "sw1": True,
           "dList_path":"dList",
           "modelSelected":"detail",
           "details":detail.objects.all().filter(catalog=selection),
               }
    return render(request,"index.html",context)

def image(request):
    global image_name
    
    context = {
        "image_name":image_name
    }
    return render(request,"index.html",context)

def dList(request):
    global sw1
    selection = request.POST.get('mybtn',None)
    print("dlist----------")
    print("dlist-1",selection)
    order(selection)
    context = {
        "clist_path":"order",
    #    "image_name":image_name
            }
    return  redirect("order.html",context)

def order(selection):
    #selection = request.GET.get('mybtn',None)       
    print("order********")
    print("order-1",selection)
    return 