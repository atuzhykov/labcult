from django.shortcuts import render
from .models import Subscriber
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        subscriber = Subscriber()
        subscriber.email=email
        subscriber.save()
        return HttpResponse("<h3>Your email {0} was added to subscibers database. Thank you!</h3>".format(email))
       
    return render(request, 'index.html')



def enversion(request):
    if request.method == "POST":
        email = request.POST.get("email")
        subscriber = Subscriber()
        subscriber.email=email
        subscriber.save()
        return HttpResponse("<h3>Your email {0} was added to subscibers database. Thank you!</h3>".format(email))
    return render(request,'index_en.html')

 