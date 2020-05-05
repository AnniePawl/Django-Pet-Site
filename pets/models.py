from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Pet(models.Model):
    pet_name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    weight_in_pounds = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Appointment(models.Model):
    date_of_appointment = models.DateField(blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    special_instructions = models.CharField(max_length=5000)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True)
