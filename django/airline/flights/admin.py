from django.contrib import admin
from .models import Flight, Airport

# Register your models here.
admin.site.register(Airport)

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

admin.site.register(Flight, FlightAdmin)
