from django.shortcuts import render
from apps.base.models import InfoUser

# Create your views here.

def index(request):     #request - запросы
    infouser = InfoUser.objects.latest("id")    #all()
    return render(request, "index.html", locals())      #locals() - translater from py to html