from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index-2.html', locals())

def about(request):
    return render(request, 'base/about-us.html', locals())