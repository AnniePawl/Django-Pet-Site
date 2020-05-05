from django.shortcuts import render
from .models import Pet
from .models import Appointment


# HOME VIEW
def home(request):
    context = {

    }
    return render(request, 'pets/home.html', context)


# PETS LIST PAGE VIEW
  # Lists all user's pets (bullet points)
  # Pets names must link to detail pages uses {% url%} template tag
  # must include form to create new pet or link to seperate creation page
  # should not be vieable by non-logged-in users


# PETS DETAIL VIEW
  # Must show all relevant details about pet
  # must list all appointments associated with pet
  # Should not be viewable by non-logged-in users


# CALENDAR PAGE
  # Must show all upcoming appointments w/ all pets, earliest first
  # Should not show appointments that have already occured
  # Must include form to create new appointment of link to seperate appointment creation page
  # should not be viewable by non logged in users

# LOGIN PAGE

# SIGNUP PAGE
