from django import forms
from .models import Reservation
from django.utils import timezone
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
    """
    Custom clean method to validate check-in and check-out dates.
    PREVENTS users from selecting past dates for check-in and ensures that check-out is after check-in.
    """
    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        today = timezone.now().date()

        if check_in and check_in < today:
            self.add_error('check_in', 'Check-in date cannot be in the past.')

        if check_in and check_out and check_out <= check_in:
            self.add_error('check_out', 'Check-out date must be after check-in date.')
