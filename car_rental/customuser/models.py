from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_superuser(self, email, driving_licence, first_name, last_name, password):
        user = self.model(
            email=email, 
            driving_licence=driving_licence, 
            first_name=first_name, 
            last_name=last_name)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    
class User(AbstractUser):
    objects = UserManager()

    username = None

    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    driving_licence = models.CharField(max_length=13, unique=True)

    USERNAME_FIELD = 'driving_licence'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.driving_licence
