from django.apps import AppConfig

"""
This file is used to configure the Reviews app in Django.
It sets the default auto field type and the name of the app.
"""
class ReviewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
