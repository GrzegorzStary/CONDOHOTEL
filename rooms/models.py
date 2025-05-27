from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from djrichtextfield.models import RichTextField
from django.core.validators import MinValueValidator
# Create your models here.
"""
Model representing a room.
This model is used to create a room with various attributes such as title, details, price, image, and room type.
"""

ROOM_TYPE = (
    ('single', 'Single'),
    ('double', 'Double'),
    ('suite', 'Suite'),
    ('deluxe', 'Deluxe'),
    ('family', 'Family'),
)

class Room(models.Model):
    """
    Model representing a room creation.
    """
    user = models.ForeignKey('auth.User', related_name='owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    details = RichTextField(max_length=10000, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)], null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = ResizedImageField(
        size=[400, None], quality=75, 
        upload_to='rooms/', 
        force_format='WEBP',
        null=True, 
        blank=True,
        )
    image_alt = models.CharField(max_length=200, null=True, blank=True)
    room_type = models.CharField(max_length=100, choices=ROOM_TYPE, default='single', null=False, blank=False)
    def __str__(self):
        return self.title