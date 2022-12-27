from email import message
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
   return render(request, "index.html")
def about(request):
       return render(request, "about.html")


def Services(request):
      return render(request, "Services.html")

  
def contact(request):
       if request.method=="POST":
              name=request.POST.get('name')
              contact=Contact(name=name , date=datetime.today())
              contact.save()
              messages.success(request, 'The Message Has Been ubmitteed.')
       return render(request, "contact.html")
