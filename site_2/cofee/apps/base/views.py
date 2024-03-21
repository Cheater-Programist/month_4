from django.shortcuts import render
from apps.base.models import *

# Create your views here.
def index(request):
    return render(request, 'base/index-2.html', locals())

def about(request):
    return render(request, 'base/about-us.html', locals())

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        result = Contact.objects.create(name = name, email = email, message = message)
    return render(request, 'base/contact.html', locals())