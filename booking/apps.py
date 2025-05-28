from django.apps import AppConfig

"""
This file is used to configure the Booking app in Django.
It sets the default auto field type and the name of the app.
"""


class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
