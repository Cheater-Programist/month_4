from django.shortcuts import render
from apps.base.models import *

# Create your views here.

def index(requests):
    userinfo = UserInfo.objects.latest("id")
    service = Service.objects.all()
    testimonials = Testimonials.objects.all()
    experience = Experience.objects.all()
    educations = Educations.objects.all()
    skills = Skills.objects.all()
    office = Office.objects.latest("id")
    portfolio = Portfolio.objects.all()
    blog = Blog.objects.all()
    return render(requests, 'index.html', locals())