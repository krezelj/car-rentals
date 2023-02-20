from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("user_profile/", views.user_profile, name="user_profile"),
    path("rent/<int:vehicle_id>", views.rent, name="rent"),
    path("end_rental/<int:rental_id>", views.end_rental, name="end_rental"),
]