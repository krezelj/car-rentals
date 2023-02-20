from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.core.validators import RegexValidator

User = get_user_model()
driving_licence_validator = RegexValidator(r"^\d{5}\/\d{2}\/\d{4}$", "Invalid driving licence format")

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label="First Name")
    last_name = forms.CharField(max_length=50, label="Last Name")
    email = forms.EmailField()
    driving_licence = forms.CharField(
        label="Driving Licence Number",
        required=True,
        validators=[driving_licence_validator],
        help_text="Driving licence must follow the format XXXXX/YY/ZZZZ"
    )

    class Meta():
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2", "driving_licence"]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # self.fields.pop('username')

        self.fields['password1'].widget.attrs.update({'class': 'field-common'})
        self.fields['password2'].widget.attrs.update({'class': 'field-common'})
        self.fields['email'].widget.attrs.update({'class': 'field-common'})
        self.fields['first_name'].widget.attrs.update({'class': 'field-common'})
        self.fields['last_name'].widget.attrs.update({'class': 'field-common'})
        self.fields['driving_licence'].widget.attrs.update({'class': 'field-common'})
