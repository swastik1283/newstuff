from django.contrib import admin
from django.urls import path
from new import views 
from django.conf import settings
from django.conf.urls.static import static
import os 

urlpatterns = [
    path("",views.index,name="new"),
    path("about",views.about,name="about"),
    path("services",views.service,name="services"),
    path("contact",views.contact,name="contact"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
