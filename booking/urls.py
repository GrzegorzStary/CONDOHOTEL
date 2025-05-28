from django.urls import path
from .views import Index, About, ContactView

"""
This file contains the URL patterns for the Booking app.
It maps URLs to views for the index, about, and contact pages.
"""


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]