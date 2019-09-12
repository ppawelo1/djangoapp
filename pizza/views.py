from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   # return HttpResponse("witaj w zakładzie pogrzebowym "Dobry koniec")
    return render(request, 'pizza/index.html')

def news(request):
    return HttpResponse("<h1>Trendy 2019 ;)))</h1>")

def menu(request):
    return HttpResponse("<h2>Szeroki wybór trumien i karawanów.</h2>")

# Create your views here.
