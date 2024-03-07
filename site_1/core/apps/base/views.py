from django.shortcuts import render

# Create your views here.

def index(request):     #request - запросы
    return render(request, "index.html", locals())      #locals() - translater