from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model
from django.core.validators import MinValueValidator, MaxValueValidator

"""
This file contains the Reservation model for the hotel booking system.
"""


class Reservation(models.Model):
    ROOM_CHOICES = [
        ('DELUXE', 'Deluxe'),
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
        ('FAMILY', 'Family'),
        ('SUITE', 'Suite'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations', null=True)
    full_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES)
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.check_in} to {self.check_out})"
