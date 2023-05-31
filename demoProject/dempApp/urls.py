from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name="index"),
    path('index', views.index,name="index"),
    path('clist/',views.cList,name="cList"),
    path('dlist/',views.dList,name="dList"),
    path('image/',views.image,name="image"),
    path('order/',views.order,name="order"),
    path('getQuote/',views.getQuote,name="getQuote"),
    path('contactMe/',views.contactMe,name="contactMe"),
    path('aboutMe/',views.aboutMe,name="aboutMe"),
]