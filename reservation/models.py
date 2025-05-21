from django.db import models
from django.contrib.auth.models import User

ROOM_CHOICES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
        ('deluxe', 'Deluxe'),
        ('family', 'Family'),
    )

class RoomType(models.Model):

    name = models.CharField(max_length=50, choices=ROOM_CHOICES, unique=True)

    def __str__(self):
        return dict(self.ROOM_CHOICES).get(self.name, self.name)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    room_type = models.ForeignKey(RoomType,choices=ROOM_CHOICES, on_delete=models.CASCADE, null=False, blank=False)
    additional_info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Reservation by {self.full_name} from {self.check_in} to {self.check_out}"

