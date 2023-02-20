from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import VehicleFilterForm, RentalForm
from .models import Vehicle, Rental
from django.utils import timezone
from .src import get_rating

# Create your views here.

def index(response):
    if response.method == "POST":
        form = VehicleFilterForm(response.POST)
        vehicles = Vehicle.objects.\
            filter(vehicle_type__in=form['vehicle_type'].value()).\
            filter(fuel_type__in=form['fuel_type'].value()).\
            filter(transmission_type__in=form['transmission_type'].value()).\
            filter(has_air_conditioning__in=form['has_air_conditioning'].value()).\
            order_by(form['sort_by'].value())
            
    else:
        vehicles = Vehicle.objects.all()
        form = VehicleFilterForm()
    return render(response, "main/home.html", {"form": form, "vehicles": vehicles})

def about(response):
    return render(response, "main/about.html", {})

def user_profile(response):
    past_rentals = None
    current_rental = None
    if response.user.is_authenticated:
        past_rentals = Rental.objects.filter(user_id=response.user).filter(active=False).filter(end_date__lte=timezone.now().date())
        current_rental = Rental.objects.filter(user_id=response.user).filter(active=True).filter(end_date__gte=timezone.now().date())

    return render(response, "main/user_profile.html", {"past_rentals": past_rentals, "current_rentals": current_rental})

def rent(response, vehicle_id):
    if response.method == "POST":
        form = RentalForm(response.POST)
        if form.is_valid():
            new_rental = form.save(commit=False)
            new_rental.vehicle_id = Vehicle.objects.get(id=vehicle_id)
            new_rental.user_id = response.user
            new_rental.save()
            return HttpResponseRedirect("/user_profile")

        vehicle = Vehicle.objects.get(id=vehicle_id)
    else:
        form = RentalForm()
        vehicle = Vehicle.objects.get(id=vehicle_id)
    
    return render(response, "main/rent.html", {"vehicle": vehicle, "form": form})

def end_rental(response, rental_id):
    rental = Rental.objects.get(id=rental_id)
    if response.user.id != rental.user_id.id:
        return HttpResponse(status=403)

    if rental.start_date > timezone.now().date():
        rental.start_date = timezone.now().date()
    rental.end_date = timezone.now().date()

    get_rating(rental)
    rental.active = False
    rental.save()
    
    return HttpResponseRedirect("/user_profile")