from django.db import models

class Reservation(models.Model):
    ROOM_CHOICES = [
        ('DELUXE', 'Deluxe'),
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
        ('FAMILY', 'Family'),
        ('SUITE', 'Suite'),
    ]

    full_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    room_type = models.CharField(choices=ROOM_CHOICES)
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.check_in} to {self.check_out})"
