from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Flights

def index(request):
    return render(request,"flights/index.html",{
        "flights": Flights.objects.all()
    })