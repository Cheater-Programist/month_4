from django.shortcuts import render
from apps.base.models import UserInfo

# Create your views here.

def index(requests):
    userinfo = UserInfo.objects.latest("id")
    return render(requests, 'index.html', locals())