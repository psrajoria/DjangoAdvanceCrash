from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Flights

def index(request):
    return render(request,"flights/index.html",{
        "flights": Flights.objects.all()
    })

def flight(request, flight_id):
    flight = Flights.objects.get(pk=flight_id)
    return render(request,"flights/flight.html",{
        "flight":flight,
        "passengers": flight.passengers.all()
    })
