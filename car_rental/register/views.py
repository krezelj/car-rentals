from django.shortcuts import render, HttpResponseRedirect
from .forms import RegisterForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login

# Create your views here.


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Car Rental Registration Confirmation',
                'Your registration is successful!',
                'car.rentals.paw@gmail.com',
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            new_user = authenticate(driving_licence=form.cleaned_data['driving_licence'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(response, new_user)
            return HttpResponseRedirect('/user_profile')

    else:
        form = RegisterForm()

    return render(response, 'register/register.html', {"form":form})


def login_redirect(response):
    return HttpResponseRedirect('/login')