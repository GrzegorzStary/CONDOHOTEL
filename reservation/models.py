from django.db import models
from django.contrib.auth.models import User
# Create your models here.

ROOM_TYPE = (
    ('single', 'Single'),
    ('double', 'Double'),
    ('suite', 'Suite'),
    ('deluxe', 'Deluxe'),
    ('family', 'Family'),
)

class Reservation(models.Model):
    """
    Model representing a reservation.
    """
    user = models.ForeignKey('auth.User', related_name='guest', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    details = models.CharField(max_length=1000, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    room_type = models.CharField(max_length=100, choices=ROOM_TYPE, default='single', null=False, blank=False)

    def __str__(self):
        return str(self.title)