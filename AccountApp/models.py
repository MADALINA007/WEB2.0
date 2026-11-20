from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

number_validator=RegexValidator(
     regex=r'\d{8}$'
     message=" doit contenir exactement 8 chiffres"
)
def birth_date_validator(date):
    if date>= timezone.localdate()
    raise ValidationError=" la date doit etre enterieure de la date d'aujourd'hui"
class User (AbstractUser):
    pass

class Doctor (User):
    license_number = models.CharField(max_length=6, unique=True,blank=False, validators=[MinlengthValidator(6)])
    phone=models.CharField(max_length=8, unique=True, validators=[number_validator])

class Patient(User):
    phone=models.CharField(max_length=8, unique=True, validators=[number_validator])
    birth_date=models.DateField(validators=birth_date_validator)

class Speciality (models.Model):
    name=models.CharField(max_length=50, blank=False)
    doctors=models.ManyToManyField(Doctor, related_name='Doctors')