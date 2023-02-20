from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


# defines a vehicle available for rental
class Vehicle(models.Model):

    class VehicleType(models.TextChoices):
        SEDAN = 'SEDAN', "Sedan"
        HATCHBACK = 'HATCHBACK', "Hatchback"
        SUV = 'SUV', "SUV"

    class FuelType(models.TextChoices):
        GAS = 'GAS', "Gas"
        ELECTRIC = 'ELECTRIC', "Electric"

    class TransmissionType(models.TextChoices):
        MANUAL = 'MANUAL', "Manual"
        AUTOMATIC = 'AUTOMATIC', "Automatic"

    name=models.CharField(max_length=50)
    price_per_day = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    has_air_conditioning = models.BooleanField(default=True)

    vehicle_type = models.CharField(
        max_length=10,
        choices=VehicleType.choices,
        default=VehicleType.SEDAN        
    )
    fuel_type = models.CharField(
        max_length=10,
        choices=FuelType.choices,
        default=FuelType.GAS
    )
    transmission_type = models.CharField(
        max_length=10,
        choices=TransmissionType.choices,
        default=TransmissionType.MANUAL
    )


class Location(models.Model):
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.city + ", " + self.address


# defines a rating of a given rental
class Rating(models.Model):
    MAX_VALUE = 5
    value = models.IntegerField(default=0)
    comment = models.TextField(max_length=300, default="No comment for this rental. Sorry!")


# defines a relationship between a user and a vehicle
class Rental(models.Model):
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_id = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    pickup_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="pickup_location")
    dropoff_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="dropoff_location", null=True)

    active = models.BooleanField(default=True)

    user_comments = models.TextField(max_length=500, null=True)




