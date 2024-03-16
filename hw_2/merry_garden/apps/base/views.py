from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index.html', locals())

def about_us(request):
    return render(request, 'about.html', locals())

def team(request):
    return render(request, 'team.html', locals())

def post(request):
    return render(request, 'post.html', locals())

def news(request):
    return render(request, 'news.html', locals())

def gallery(request):
    return render(request, 'gallery.html', locals())

def contact(request):
    return render(request, 'contact.html', locals())