from django import forms
from .models import Reservation
"""
This file contains the form for the Reservation model.
It uses Django's ModelForm to create a form based on the Reservation model.
The form includes fields for full name, check-in date, check-out date,
number of guests, room type, and additional information.
"""
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['full_name', 'check_in', 'check_out', 'guests', 'room_type', 'additional_info']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }
