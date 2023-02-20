from django.contrib import admin
from .models import Vehicle, Rental, Location, Rating

# Register your models here.

admin.site.register(Vehicle)
admin.site.register(Rental)
admin.site.register(Location)
admin.site.register(Rating)