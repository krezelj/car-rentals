# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from .models import Vehicle, Rental
from django.utils import timezone
# from django.core.validators import RegexValidator

User = get_user_model()
# driving_licence_validator = RegexValidator(r"^\d{5}\/\d{2}\/\d{4}$", "Invalid driving licence format")


class VehicleFilterForm(forms.Form):
    vehicle_type = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=Vehicle.VehicleType.choices,
        initial=[c[0] for c in Vehicle.VehicleType.choices])

    fuel_type = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=Vehicle.FuelType.choices,
        initial=[c[0] for c in Vehicle.FuelType.choices])

    transmission_type = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=Vehicle.TransmissionType.choices,
        initial=[c[0] for c in Vehicle.TransmissionType.choices])

    ac_choices = [(True, 'Yes'), (False, 'No')]
    has_air_conditioning = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=ac_choices, 
        initial=[c[0] for c in ac_choices], label="Air conditioning"
    )

    sort_choices = [('price_per_day', "price (ascending)"), ('-price_per_day', "price (descending)")]
    sort_by= forms.ChoiceField(
        widget=forms.Select, choices=sort_choices, label="Sort by"
    )

    def __init__(self, *args, **kwargs):
        super(VehicleFilterForm, self).__init__(*args, **kwargs)

        self.fields['vehicle_type'].widget.attrs.update({'class': 'field-select-multiple'})
        self.fields['fuel_type'].widget.attrs.update({'class': 'field-select-multiple'})
        self.fields['transmission_type'].widget.attrs.update({'class': 'field-select-multiple'})
        self.fields['has_air_conditioning'].widget.attrs.update({'class': 'field-select-multiple'})


class RentalForm(ModelForm):

    different_location = forms.BooleanField(widget=forms.CheckboxInput, label="Different drop off location")

    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)

        self.fields['start_date'].widget = forms.DateInput(attrs={'type':'date', 'class':'datetime-input'})
        self.fields['end_date'].widget = forms.DateInput(attrs={'type':'date', 'class': 'datetime-input'})
        self.fields['pickup_location'].widget.attrs.update({'class': 'select-input'})
        self.fields['dropoff_location'].widget.attrs.update({'class': 'select-input'})
        self.fields['user_comments'].widget.attrs.update({'class': 'text-input'})
        self.fields['user_comments'].label = "Any special wishes?"

        self.fields['different_location'].required = False
        self.fields['dropoff_location'].required = False
        self.fields['user_comments'].required = False


    class Meta():
        model = Rental
        exclude = ('vehicle_id', 'user_id', 'rating_id', 'active')
        fields = ['start_date', 'end_date', 'pickup_location', 'dropoff_location', 'different_location', 'user_comments']

    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        different_location = cleaned_data.get("different_location")
        pickup_location = cleaned_data.get("pickup_location")
        dropoff_location = cleaned_data.get("dropoff_location")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")
        if start_date < timezone.now().date():
            raise forms.ValidationError("Rental cannot start in the past.")
        if different_location and dropoff_location is None:
            raise forms.ValidationError("You must specify drop off location")
        if not different_location:
            dropoff_location = pickup_location
