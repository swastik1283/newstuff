from django.shortcuts import render,HttpResponse
from datetime import datetime
from new.models import Contact
from django.contrib.messages import constants as messages
from django.contrib.messages.constants import SUCCESS

# Create your views here.


def index(request):  
    return render(request, 'index.html')



def about (request):
    #return HttpResponse('About site  ')
    return render(request, 'about.html')


def service (request):
    return render(request, 'services.html', )


def contact (request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        Query=request.POST.get('Query')
        if not Query:
            return render(request, 'contact.html', {'error': 'Query field is required'})
        contact_instance=Contact(name=name,email=email,phone=phone,Query=Query,date=datetime.today())
        contact_instance.save()
        messages.SUCCESS(request,'Your message has been  sent')
        
    return render(request, 'contact.html')

