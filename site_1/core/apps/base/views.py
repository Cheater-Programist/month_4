from django.shortcuts import render
from apps.base.models import InfoUser, Numbers, Service, Experience, Educations, Skills

# Create your views here.

def index(request):     #request - запросы
    infouser = InfoUser.objects.latest("id")    #all()
    numbers = Numbers.objects.latest("id")
    service = Service.objects.all()
    experience = Experience.objects.all()
    educations = Educations.objects.all()
    skills = Skills.objects.all()
    return render(request, "index.html", locals())      #locals() - translater from py to html