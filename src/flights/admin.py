from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Flights,Airport,Passengers

class FlightAdmin(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)

admin.site.register(Flights, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passengers, PassengerAdmin)
