from django.contrib import admin

# Register your models here.
from .models import Flights,Airport,Passengers

admin.site.register(Flights)
admin.site.register(Airport)
admin.site.register(Passengers)