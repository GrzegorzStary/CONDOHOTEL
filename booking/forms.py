from django import forms
from .models import ContactMessage


"""
This file contains the form for the ContactMessage model.
It uses Django's ModelForm to create a form based on the ContactMessage model.
The form includes fields for name, email, and message.
"""


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']