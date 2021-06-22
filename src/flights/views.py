from django.http.response import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
from .models import Flights, Passengers

def index(request):
    return render(request,"flights/index.html",{
        "flights": Flights.objects.all()
    })

def flight(request, flight_id):
    flight = Flights.objects.get(pk=flight_id)
    return render(request,"flights/flight.html",{
        "flight":flight,
        "passengers": flight.passengers.all(),
        ####to get non passengers
        "non_passengers": Passengers.objects.exclude(flights=flight).all(),
    })

def book(request,flight_id):
    if request.method=="POST":
        flight = Flights.objects.get(pk=flight_id)
        passenger = Passengers.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flights:flight', args=(flight.id,)))
